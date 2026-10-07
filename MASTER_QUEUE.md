# Master queue

Updated: 2026-10-07. The [execution contract](PERCY_WORK_README.md) defines statuses and priorities. Keep at most three substantial tasks IN_PROGRESS unless independent work justifies more.

Continue authorized drafting, venue-fit research and code review whenever useful work is available. WAITING_EXTERNAL applies to the specifically named unavailable input or outside decision; it adds no approval requirement to routine project work.

| ID | Priority | Status | Work |
|---|---|---|---|
| CW-001 | P1 | DONE | Deliver the bounded project packages |
| CW-002 | P1 | DONE | Map conference and journal routes to evidence |
| CW-003 | P1 | BLOCKED | Recover authentic source and original evidence |
| CW-004 | P3 | WAITING_EXTERNAL | Obtain the data and study prerequisites for research completion |
| CW-005 | P1 | WAITING_EXTERNAL | Complete independent review and author/venue decisions |
| CW-006 | P2 | WAITING_EXTERNAL | Resolve official-call, eligibility and existing-submission dependencies |

## CW-001 — Bounded project delivery

- **ID:** CW-001
- **PRIORITY:** P1
- **AREA:** Verification and delivery
- **PROJECT/WAVE:** Conference portfolio; bounded packages only
- **STATUS:** DONE
- **OBJECTIVE:** Deliver useful implementation, verification, presentation or recovery work to canonical repositories.
- **DEFINITION OF DONE:** Each of the eleven bounded packages has a published commit, its own completed scope, verification evidence and an explicit research-readiness boundary.
- **CANONICAL LOCATION:** [Restricted project evidence index](https://github.com/THE-BU1LD/org-infra-/blob/79fd04222c341a21aa7f924427097e5f8ef88d88/conferences/index.json); follow each project's canonical link.
- **DEPENDENCIES:** Completed repository work and verified publication receipts.
- **BLOCKERS:** None for this bounded delivery. Research-completion dependencies remain in CW-003 through CW-006.
- **NEXT ACTION:** Resume the highest-priority dependency task when its required input becomes available; review canonical updates before claiming broader completion.
- **VERIFICATION:** The pinned index records eleven published bounded packages with exact evidence commits and remaining requirements.
- **LAST UPDATED:** 2026-10-07

## CW-002 — Route mapping

- **ID:** CW-002
- **PRIORITY:** P1
- **AREA:** Conference coordination
- **PROJECT/WAVE:** Conference portfolio
- **STATUS:** DONE
- **OBJECTIVE:** Connect the reviewed venue and track routes to actual project work and actionable requirements.
- **DEFINITION OF DONE:** All forty-two routes have a project mapping, official-source context, deadline state and a remaining action; journals, future calls and existing submissions are identified.
- **CANONICAL LOCATION:** [Restricted route index](https://github.com/THE-BU1LD/org-infra-/blob/79fd04222c341a21aa7f924427097e5f8ef88d88/conferences/index.json) and its linked official sources.
- **DEPENDENCIES:** Reviewed route snapshot and project evidence records.
- **BLOCKERS:** None for route mapping. Mapping is not a scientific-completion or submission decision.
- **NEXT ACTION:** Recheck the official source when a route is selected or its call changes; update the index before acting on a revised deadline.
- **VERIFICATION:** All forty-two route identities are unique and retain a next requirement. Submission readiness and authorization remain separate from package delivery.
- **LAST UPDATED:** 2026-10-07

## CW-003 — Authentic source and evidence recovery

- **ID:** CW-003
- **PRIORITY:** P1
- **AREA:** Research completion
- **PROJECT/WAVE:** Source-dependent streams in the restricted conference index
- **STATUS:** BLOCKED
- **OBJECTIVE:** Recover the authentic implementation and original evidence required by the affected research routes.
- **DEFINITION OF DONE:** Each affected stream has an accessible, complete source/evidence package admitted against its canonical identity and preserved in its designated repository.
- **CANONICAL LOCATION:** [Restricted source dependencies](https://github.com/THE-BU1LD/org-infra-/blob/79fd04222c341a21aa7f924427097e5f8ef88d88/conferences/index.json); scientific coordination is in [Percy-Projects](https://github.com/build-the-future-11/Percy-Projects).
- **DEPENDENCIES:** Accessible authentic archives or repositories; exact source-version binding; original inputs, outputs and provenance where required.
- **BLOCKERS:** B-001: some original artifacts remain inaccessible, incomplete or unbound; some project identities lack a designated authentic implementation.
- **NEXT ACTION:** On receipt of a distinct accessible artifact or routing decision, validate identity and integrity, reconcile its lineage, and perform the permitted intake in the canonical repository.
- **VERIFICATION:** Verify archive/file integrity, source binding and agreement with preserved evidence. Do not substitute another study or rerun closed work to fill a provenance gap.
- **LAST UPDATED:** 2026-10-07

## CW-004 — Data and study prerequisites

- **ID:** CW-004
- **PRIORITY:** P3
- **AREA:** Research completion
- **PROJECT/WAVE:** Routes requiring evidence beyond the completed bounded packages
- **STATUS:** WAITING_EXTERNAL
- **OBJECTIVE:** Obtain legitimate study inputs and a frozen evaluation suitable for each selected research claim.
- **DEFINITION OF DONE:** Required data permissions, cohorts, labels, controls, evaluation protocol and resource admission are resolved in the canonical project before a permitted study executes.
- **CANONICAL LOCATION:** [Restricted project requirements](https://github.com/THE-BU1LD/org-infra-/blob/79fd04222c341a21aa7f924427097e5f8ef88d88/conferences/index.json); follow the designated implementation and scientific-state records.
- **DEPENDENCIES:** Appropriate data owners and study leads; lawful data access or participant permission where applicable.
- **BLOCKERS:** B-002: prospective or representative data, consent where needed, reference labels, comparator definitions and approved study resources are not all available.
- **NEXT ACTION:** Continue available protocol preparation. When the responsible owner supplies the required inputs, bind their provenance, freeze the protocol and complete the applicable admission checks before outcome work.
- **VERIFICATION:** Project-specific checks must establish permission, input identity, data splits, controls and protocol completeness; constructed examples alone do not establish external validation.
- **LAST UPDATED:** 2026-10-07

## CW-005 — Scientific review and author decisions

- **ID:** CW-005
- **PRIORITY:** P1
- **AREA:** Research completion and publication preparation
- **PROJECT/WAVE:** Candidate presentations and manuscripts
- **STATUS:** WAITING_EXTERNAL
- **OBJECTIVE:** Obtain the independent domain review and presenter/coauthor decisions that remain beyond the completed verification.
- **DEFINITION OF DONE:** Required independent domain or proof review, presenter/coauthor representation and any unresolved existing-venue policy decisions are recorded in canonical project state.
- **CANONICAL LOCATION:** [Restricted project and route requirements](https://github.com/THE-BU1LD/org-infra-/blob/79fd04222c341a21aa7f924427097e5f8ef88d88/conferences/index.json) and the corresponding canonical manuscripts.
- **DEPENDENCIES:** Qualified independent review beyond existing verification; presenter/coauthor decisions; responses needed from an existing venue process.
- **BLOCKERS:** B-003: the required outside domain review or personal/venue decision has not arrived.
- **NEXT ACTION:** Continue authorized draft refinement, venue-fit research and code review using the completed assets. Incorporate external feedback when received, preserve frozen or submitted artifacts, and keep the final submission within its recorded authorization.
- **VERIFICATION:** Confirm that every proposed claim traces to admissible evidence and that required presenter, reviewer and venue decisions are recorded. A draft PR is not publication acceptance.
- **LAST UPDATED:** 2026-10-07

## CW-006 — External venue dependencies

- **ID:** CW-006
- **PRIORITY:** P2
- **AREA:** Conference coordination
- **PROJECT/WAVE:** Selected future calls and existing submission routes
- **STATUS:** WAITING_EXTERNAL
- **OBJECTIVE:** Resolve the external rules and decisions needed to act on a selected route.
- **DEFINITION OF DONE:** The relevant official call, actual cutoff and timezone, presenter eligibility, sponsorship or membership conditions, and any existing-submission decision are resolved for that route.
- **CANONICAL LOCATION:** [Restricted route index](https://github.com/THE-BU1LD/org-infra-/blob/79fd04222c341a21aa7f924427097e5f8ef88d88/conferences/index.json); use each route's official source and existing submission record.
- **DEPENDENCIES:** Venue publication of calls and rules; organizer or sponsor decisions where required; existing editorial or review processes.
- **BLOCKERS:** B-004: some calls are unannounced, some deadline wording needs resolution, and some eligibility or existing-process conditions remain external.
- **NEXT ACTION:** Recheck the authoritative source when it changes or before acting on the route; update canonical coordination without inventing dates or duplicate submissions.
- **VERIFICATION:** Preserve the source, original deadline wording and verified conversion, eligibility resolution and overlap decision before final submission preparation.
- **LAST UPDATED:** 2026-10-07
