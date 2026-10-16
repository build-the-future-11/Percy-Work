#!/usr/bin/env python3
"""Audit saved PR/check receipts without accessing any network or changing a repo.

Python 3.10+, standard library only.
  python receipt_audit.py --self-test
  python receipt_audit.py snapshot.json

Input: {repository, observed_at, pr, required_checks, checks}.
`pr` uses the normalized get_pr_info shape. Each check must contain name,
head_sha, status, conclusion, completed_at, and a positive integer attempt.
The caller must supply the actual required-check names, not infer them from
successful runs. Check names must identify unique workflow/job contexts.

Outputs are classifications of SUPPLIED receipts, not authenticated evidence,
branch-protection discovery, deployment approval, or scientific validation.
For a merged PR, head checks describe its pre-merge candidate, not the merge
commit or the deployed website. This script never authorizes either.
"""
from __future__ import annotations
import argparse
import copy
import json
import re
import sys
import unittest
from datetime import datetime
from pathlib import Path
from typing import Any

SHA = re.compile(r"[0-9a-f]{40}\Z")
REPOSITORY = re.compile(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+\Z")
ALLOWED_OWNERS = {"build-the-future-11", "the-bu1ld", "finance-meta-research", "vertex-studyai"}
BLOCKED_NAMES = {"worldcastr", "yel", "young-entrepreneurs-league", "young-entrepreneurship-league"}
FAILURES = {"failure", "cancelled", "timed_out", "action_required", "startup_failure", "stale"}


def instant(value: Any) -> datetime:
    if not isinstance(value, str):
        raise ValueError("timestamp must be a timezone-aware ISO string")
    try:
        result = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as exc:
        raise ValueError("invalid ISO timestamp") from exc
    if result.tzinfo is None or result.utcoffset() is None:
        raise ValueError("timestamp must include a timezone")
    return result


def audit(snapshot: dict[str, Any]) -> dict[str, Any]:
    """Fail closed on malformed/ambiguous receipts; never modify the input."""
    if not isinstance(snapshot, dict):
        raise ValueError("snapshot must be an object")
    repo = snapshot.get("repository")
    if not isinstance(repo, str) or not REPOSITORY.fullmatch(repo):
        raise ValueError("repository must be an exact owner/name")
    owner, name = repo.lower().split("/")
    if owner not in ALLOWED_OWNERS or name in BLOCKED_NAMES or "worldcastr" in name:
        raise ValueError("repository is outside the permitted audit scope")
    observed = instant(snapshot.get("observed_at"))
    pr = snapshot.get("pr")
    if not isinstance(pr, dict):
        raise ValueError("pr must be an object")
    for field in ("merged", "draft"):
        if type(pr.get(field)) is not bool:
            raise ValueError(f"pr.{field} must be an explicit boolean")
    if pr.get("state") not in {"open", "closed"}:
        raise ValueError("pr.state must be open or closed")
    if pr["merged"] and (pr["state"] != "closed" or pr["draft"]):
        raise ValueError("contradictory merged/state/draft receipt")
    head = pr.get("head_sha")
    if not isinstance(head, str) or not SHA.fullmatch(head):
        raise ValueError("pr.head_sha must be an exact lowercase 40-hex SHA")
    if pr["merged"]:
        merge_sha = pr.get("merge_commit_sha")
        if not isinstance(merge_sha, str) or not SHA.fullmatch(merge_sha):
            raise ValueError("merged receipt requires exact merge_commit_sha")
        if instant(pr.get("merged_at")) > observed:
            raise ValueError("merge timestamp is later than observation")
    required = snapshot.get("required_checks")
    if not isinstance(required, list) or any(not isinstance(x, str) or not x.strip() for x in required):
        raise ValueError("required_checks must be a list of nonempty context names")
    if len(set(required)) != len(required):
        raise ValueError("duplicate required-check context")
    checks = snapshot.get("checks")
    if not isinstance(checks, list):
        raise ValueError("checks must be a list")
    exact: dict[str, list[dict[str, Any]]] = {x: [] for x in required}
    stale_count = 0
    for check in checks:
        if not isinstance(check, dict):
            raise ValueError("check must be an object")
        sha = check.get("head_sha")
        if not isinstance(sha, str) or not SHA.fullmatch(sha):
            raise ValueError("check requires exact head_sha")
        if sha != head:
            stale_count += 1
            continue
        context = check.get("name")
        if context not in exact:
            continue
        if type(check.get("attempt")) is not int or check["attempt"] < 1:
            raise ValueError("check attempt must be a positive integer")
        if check.get("status") not in {"queued", "in_progress", "completed"}:
            raise ValueError("unrecognized check status")
        if check["status"] == "completed":
            if instant(check.get("completed_at")) > observed:
                raise ValueError("check completed after observation")
        exact[context].append(check)
    states: dict[str, str] = {}
    for context, candidates in exact.items():
        if not candidates:
            states[context] = "MISSING"
            continue
        attempt = max(x["attempt"] for x in candidates)
        latest = [x for x in candidates if x["attempt"] == attempt]
        signatures = {(x["status"], x.get("conclusion"), x.get("completed_at")) for x in latest}
        if len(signatures) != 1:
            states[context] = "AMBIGUOUS"
            continue
        check = latest[0]
        if check["status"] != "completed":
            states[context] = "PENDING"
        elif check.get("conclusion") == "success":
            states[context] = "PASSED"
        elif check.get("conclusion") in FAILURES:
            states[context] = "FAILED"
        else:
            states[context] = "NOT_PROVEN"  # skipped/neutral/missing never become a pass
    values = set(states.values())
    if "FAILED" in values:
        ci = "FAILED_AT_HEAD"
    elif not required or values & {"MISSING", "AMBIGUOUS", "NOT_PROVEN"}:
        ci = "UNVERIFIED"
    elif "PENDING" in values:
        ci = "PENDING_AT_HEAD"
    else:
        ci = "PASSED_AT_HEAD"
    warnings = []
    body = pr.get("body", "")
    if not isinstance(body, str):
        raise ValueError("pr.body must be text when present")
    if pr["merged"] and re.search(r"\b(?:not (?:been )?merged|remains a draft)\b", body, re.I):
        warnings.append("DESCRIPTION_MAY_BE_STALE: advisory only; inspect historical context")
    if not required:
        warnings.append("REQUIRED_CHECK_POLICY_MISSING")
    if pr["merged"]:
        warnings.append("HEAD_CHECKS_ARE_NOT_MERGE_COMMIT_OR_DEPLOYMENT_CHECKS")
    return {
        "repository": repo, "observed_at": snapshot["observed_at"],
        "review_state": "MERGED" if pr["merged"] else ("CLOSED_UNMERGED" if pr["state"] == "closed" else "DRAFT" if pr["draft"] else "OPEN"),
        "head_sha": head, "ci": ci, "required_contexts": states,
        "ignored_other_sha_receipts": stale_count, "warnings": warnings,
        "verification_scope": "supplied_receipts_only", "deployment_verified": False,
        "scientific_validation": False, "actions_executed": [],
    }


def fixture() -> dict[str, Any]:
    return {"repository": "THE-BU1LD/example", "observed_at": "2026-10-16T04:00:00Z",
            "pr": {"state": "open", "merged": False, "draft": True, "head_sha": "a" * 40},
            "required_checks": ["CI / tests"],
            "checks": [{"name": "CI / tests", "head_sha": "a" * 40, "status": "completed", "conclusion": "success", "completed_at": "2026-10-16T03:59:00Z", "attempt": 1}]}


class AuditTests(unittest.TestCase):
    def setUp(self): self.s = fixture()
    def result(self): return audit(self.s)
    def test_exact_success(self): self.assertEqual(self.result()["ci"], "PASSED_AT_HEAD")
    def test_input_immutable(self):
        before = copy.deepcopy(self.s); self.result(); self.assertEqual(self.s, before)
    def test_old_success_not_pass(self):
        self.s["checks"][0]["head_sha"] = "b" * 40
        self.assertEqual(self.result()["ci"], "UNVERIFIED")
    def test_old_failure_not_fail(self):
        self.s["checks"].append(dict(self.s["checks"][0], head_sha="b" * 40, conclusion="failure"))
        self.assertEqual(self.result()["ci"], "PASSED_AT_HEAD")
    def test_current_failure(self):
        self.s["checks"][0]["conclusion"] = "failure"
        self.assertEqual(self.result()["ci"], "FAILED_AT_HEAD")
    def test_new_retry_success(self):
        self.s["checks"][0]["conclusion"] = "failure"
        self.s["checks"].append(dict(self.s["checks"][0], attempt=2, conclusion="success"))
        self.assertEqual(self.result()["ci"], "PASSED_AT_HEAD")
    def test_new_retry_pending(self):
        self.s["checks"].append(dict(self.s["checks"][0], attempt=2, status="in_progress", conclusion=None, completed_at=None))
        self.assertEqual(self.result()["ci"], "PENDING_AT_HEAD")
    def test_conflicting_attempt(self):
        self.s["checks"].append(dict(self.s["checks"][0], conclusion="failure"))
        self.assertEqual(self.result()["ci"], "UNVERIFIED")
    def test_duplicate_identical_receipts(self):
        self.s["checks"].append(copy.deepcopy(self.s["checks"][0]))
        self.assertEqual(self.result()["ci"], "PASSED_AT_HEAD")
    def test_missing_context(self):
        self.s["required_checks"].append("CI / database")
        self.assertEqual(self.result()["ci"], "UNVERIFIED")
    def test_no_policy(self):
        self.s["required_checks"] = []
        self.assertEqual(self.result()["ci"], "UNVERIFIED")
    def test_skipped_not_success(self):
        self.s["checks"][0]["conclusion"] = "skipped"
        self.assertEqual(self.result()["ci"], "UNVERIFIED")
    def test_neutral_not_success(self):
        self.s["checks"][0]["conclusion"] = "neutral"
        self.assertEqual(self.result()["ci"], "UNVERIFIED")
    def test_cancelled(self):
        self.s["checks"][0]["conclusion"] = "cancelled"
        self.assertEqual(self.result()["ci"], "FAILED_AT_HEAD")
    def test_blocked_repository(self):
        self.s["repository"] = "build-the-future-11/WorldCastr"
        with self.assertRaises(ValueError): self.result()
    def test_unknown_owner(self):
        self.s["repository"] = "unrelated/example"
        with self.assertRaises(ValueError): self.result()
    def test_malformed_repository(self):
        self.s["repository"] = "THE-BU1LD/example/../WorldCastr"
        with self.assertRaises(ValueError): self.result()
    def test_short_sha(self):
        self.s["pr"]["head_sha"] = "abc123"
        with self.assertRaises(ValueError): self.result()
    def test_boolean_string(self):
        self.s["pr"]["merged"] = "false"
        with self.assertRaises(ValueError): self.result()
    def test_naive_time(self):
        self.s["observed_at"] = "2026-10-16T04:00:00"
        with self.assertRaises(ValueError): self.result()
    def test_future_check(self):
        self.s["checks"][0]["completed_at"] = "2026-10-17T00:00:00Z"
        with self.assertRaises(ValueError): self.result()
    def test_merged_open_contradiction(self):
        self.s["pr"]["merged"] = True
        with self.assertRaises(ValueError): self.result()
    def test_merged_scope_and_stale_description(self):
        self.s["pr"].update(state="closed", merged=True, draft=False, merge_commit_sha="c"*40, merged_at="2026-10-16T03:58:00Z", body="This remains a draft and has not been merged.")
        r = self.result()
        self.assertEqual(r["review_state"], "MERGED")
        self.assertTrue(any("DESCRIPTION_MAY_BE_STALE" in w for w in r["warnings"]))
        self.assertFalse(r["deployment_verified"]); self.assertFalse(r["scientific_validation"])
    def test_closed_unmerged(self):
        self.s["pr"].update(state="closed", draft=False)
        self.assertEqual(self.result()["review_state"], "CLOSED_UNMERGED")
    def test_duplicate_required_context(self):
        self.s["required_checks"] *= 2
        with self.assertRaises(ValueError): self.result()
    def test_bool_attempt_rejected(self):
        self.s["checks"][0]["attempt"] = True
        with self.assertRaises(ValueError): self.result()
    def test_no_actions(self): self.assertEqual(self.result()["actions_executed"], [])
    def test_invalid_top_level(self):
        with self.assertRaises(ValueError): audit([])


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", nargs="?", type=Path)
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(AuditTests)
        return 0 if unittest.TextTestRunner(verbosity=2).run(suite).wasSuccessful() else 1
    if args.input is None: parser.error("provide snapshot.json or --self-test")
    try:
        if args.input.stat().st_size > 5_000_000: raise ValueError("snapshot exceeds 5 MB limit")
        snapshot = json.loads(args.input.read_text(encoding="utf-8"))
        result = audit(snapshot)
    except (OSError, ValueError, TypeError) as exc:
        print(json.dumps({"error": str(exc)}), file=sys.stderr)
        return 2
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result["ci"] == "PASSED_AT_HEAD" else 1


if __name__ == "__main__":
    raise SystemExit(main())
