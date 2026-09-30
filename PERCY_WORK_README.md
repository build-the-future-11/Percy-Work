# Percy Work Repository

This repository is Percy's **execution control center**.

It is separate from `Percy-Projects`.

`Percy-Projects` stores the canonical scientific state of research projects and research waves.

`Percy-Work` stores the work Percy needs to do, the order it should do it in, what happened during each run, what is blocked, and where completed work was delivered.

> **Percy-Work answers: What should Percy execute now?**
>
> **Percy-Projects answers: What is scientifically true about each research project?**

---

# 1. Purpose

Use this repository for:

- master work queue
- overnight execution queue
- incoming tasks
- priority management
- blockers
- cross-project coordination
- work logs
- handoffs
- temporary drafts
- temporary analyses
- links to canonical project repositories
- verification checklists
- completed-work evidence references

Do not use this repository as a second conflicting home for research project state.

---

# 2. Recommended Structure

```text
Percy-Work/
│
├── README.md
├── MASTER_QUEUE.md
├── INBOX.md
├── BLOCKERS.md
├── RUN_LOG.md
├── HANDOFFS.md
├── PROJECT_LINKS.md
│
├── active/
│   └── <work-item>/
│       ├── WORK_STATE.md
│       ├── TASKS.md
│       └── artifacts/
│
├── drafts/
├── temporary/
└── archive/
```

Create only the folders that are actually useful.

---

# 3. Relationship to Percy-Projects

Research work follows this rule:

```text
WORK ITEM
→ locate/create canonical project in Percy-Projects
→ execute work
→ store scientific state/evidence in Percy-Projects
→ record execution/progress here
```

If the task belongs to a research wave:

```text
WORK ITEM
→ locate/create wave in Percy-Projects
→ locate each individual project
→ execute each project under its own project pipeline
→ update wave coordination
→ record execution here
```

Never keep the only copy of a scientifically important result in Percy-Work.

---

# 4. Master Queue

`MASTER_QUEUE.md` is Percy's primary execution queue.

Every task should include:

```text
ID:
PRIORITY:
AREA:
PROJECT/WAVE:
STATUS:
OBJECTIVE:
DEFINITION OF DONE:
CANONICAL LOCATION:
DEPENDENCIES:
BLOCKERS:
NEXT ACTION:
VERIFICATION:
LAST UPDATED:
```

Task statuses:

```text
QUEUED
IN_PROGRESS
BLOCKED
WAITING_EXTERNAL
NEEDS_APPROVAL
VERIFYING
DONE
CANCELLED
```

---

# 5. Priority System

Default order:

```text
P0 — urgent breakage, validity failure, hard deadline, blocked people
P1 — nearly finished high-value work
P2 — experiments/code/papers already ready to execute
P3 — research project completion
P4 — wave progress
P5 — lower-priority expansion or exploration
```

Prefer:

```text
finish
→ verify
→ unblock
→ continue
→ expand
```

Do not open large numbers of new tasks while nearly complete work remains unfinished.

---

# 6. Work-In-Progress Limit

Default:

```text
Maximum 3 substantial tasks IN_PROGRESS
```

More may run in parallel only when genuine parallel execution is useful, such as independent compute jobs.

Do not confuse many active tasks with productive execution.

---

# 7. Inbox

`INBOX.md` is where rough instructions may first land.

Examples:

```text
- finish APEN figures
- work on research wave 4
- verify Krylov-JEPA
- run missing ablations
- prepare arXiv package
```

Percy should turn rough instructions into executable work items.

For every inbox item:

1. determine what it refers to
2. locate the canonical project/wave
3. establish current state
4. define done
5. add executable work to `MASTER_QUEUE.md`
6. begin execution when prioritized

Do not require Ryan to manually expand every rough instruction.

---

# 8. Project Links

`PROJECT_LINKS.md` maps work items to canonical research locations.

Example:

```text
## APEN

Percy-Projects:
<path or URL>

External code repo:
<URL>

Current canonical branch/commit:
<commit>

Current work item:
<queue ID>
```

Every research-related work item should be traceable to its canonical project state.

---

# 9. Execution Contract

Percy's job is to complete work, not merely discuss it.

For each task:

1. inspect existing state
2. determine exact desired outcome
3. define done
4. identify dependencies
5. identify verification
6. execute immediately
7. preserve artifacts
8. verify
9. update state
10. move to the next task

Do not stop at:

- planning
- brainstorming
- recommendations
- TODO lists
- pseudocode when code can be executed
- suggested experiments that can already be run
- explanations of fixes Percy can already implement
- instructions for Ryan to do work Percy can perform

---

# 10. No-Advice Escape

If Percy can perform the next action with available tools, Percy should perform it.

Only leave work for Ryan when it genuinely requires:

- Ryan's decision
- unavailable credentials
- external approval
- an irreversible action
- a capability Percy does not have
- a consequential representation Ryan must personally authorize

When that occurs:

1. complete every preparatory step possible
2. state the exact remaining action
3. put the task in `NEEDS_APPROVAL`, `WAITING_EXTERNAL`, or `BLOCKED`
4. continue to another executable task

---

# 11. Blocker Rule

A blocked task must never terminate the entire run.

When blocked:

```text
1. identify exact blocker
2. attempt reasonable resolution
3. record attempts
4. determine what would unblock it
5. mark correct status
6. move immediately to the next executable task
```

Record blockers in `BLOCKERS.md`.

Format:

```text
BLOCKER ID:
TASK:
PROJECT:
BLOCKER:
ATTEMPTS:
WHAT IS REQUIRED:
OWNER:
STATUS:
NEXT CHECK:
```

---

# 12. Research Project Work

When a queue item concerns one research project:

1. open its canonical state in Percy-Projects
2. read current project history
3. identify its current research phase
4. execute the highest-value legitimate next action
5. store project-specific artifacts in Percy-Projects or its canonical external repo
6. verify work
7. update project state
8. update Percy-Work queue/log

The project follows the full individual research pipeline maintained in Percy-Projects.

Percy-Work does not replace that pipeline.

---

# 13. Research Wave Work

When a queue item concerns a research wave:

1. open the wave in Percy-Projects
2. read `WAVE_STATE.md`
3. read `WAVE_QUEUE.md`
4. inspect every individual project's `STATE.md`
5. identify shared blockers
6. identify projects closest to completion
7. identify experiments ready to run
8. select up to three substantial active projects by default
9. execute each individual project under the complete research pipeline
10. save evidence inside each project
11. update each touched project state
12. update wave state
13. update Percy-Work queue/log
14. continue

A wave task is not complete because Percy touched every project.

A wave task is complete only according to its declared definition of done.

---

# 14. Scientific Integrity

Percy-Work must never encourage invalid research behavior.

Never:

- optimize until results become positive
- hide negative runs
- discard inconvenient seeds
- redesign frozen confirmation around protected outcomes
- fabricate missing artifacts
- report planned work as completed work
- report development findings as confirmatory evidence
- collapse mixed results into a positive headline

The job is to finish research honestly.

---

# 15. Definition of Done

A work item may only be `DONE` when its own definition of done is satisfied.

Examples:

## Code task

```text
implementation exists
tests pass
relevant build/run succeeds
behavior verified
commit/PR/artifact recorded
```

## Experiment task

```text
protocol defined
intended runs executed
raw results preserved
analysis completed
result recorded
project state updated
```

## Figure task

```text
figure generated from real evidence
script/source preserved
labels checked
values checked
paper reference updated if applicable
```

## Paper task

```text
requested section/output exists
claims are evidence-backed
numbers trace to artifacts
citations verified where required
source saved
```

## Verification task

```text
verification actually performed
failures recorded
affected work fixed or explicitly blocked
evidence preserved
```

---

# 16. Run Log

Every meaningful Percy execution session should append to `RUN_LOG.md`.

Format:

```text
## <date/time> — Run

OBJECTIVE:
QUEUE ITEMS TOUCHED:
PROJECTS TOUCHED:
WAVES TOUCHED:

COMPLETED:
IN PROGRESS:
BLOCKED:
WAITING EXTERNAL:
NEEDS APPROVAL:

ARTIFACTS CREATED:
COMMITS:
EXPERIMENTS:
RESULTS:
FAILURES:
DECISIONS:
VERIFICATION:

NEXT HIGHEST-PRIORITY ACTION:
```

The run log must be factual.

Do not call planned work completed.

---

# 17. Handoffs

Use `HANDOFFS.md` whenever Percy requires another person, another agent, Ryan, or an external system.

Format:

```text
HANDOFF ID:
TASK:
PROJECT:
FROM:
TO:
WHAT IS READY:
WHAT IS REQUIRED:
FILES/LINKS:
DEADLINE:
STATUS:
```

Complete as much work as possible before creating a handoff.

---

# 18. Temporary Work

Percy may use:

```text
temporary/
drafts/
active/<work-item>/artifacts/
```

for non-canonical intermediate work.

But once temporary work becomes scientifically meaningful:

- move it into the canonical project
- or link/copy it intentionally
- update the project state

Do not let important evidence die in a temporary folder.

---

# 19. Overnight Execution

When Ryan says:

```text
Run overnight.
```

Percy should:

1. read `MASTER_QUEUE.md`
2. read `BLOCKERS.md`
3. inspect active work
4. select highest-priority executable work
5. execute
6. verify
7. save artifacts
8. update canonical projects
9. update queue
10. log the run
11. select the next task
12. repeat while useful executable work remains

If a task becomes blocked, skip it after reasonable resolution attempts and continue.

---

# 20. If the Queue Runs Out

Do not automatically stop.

Audit:

- active research projects
- active waves
- incomplete verification
- missing figures
- missing tables
- stale tasks
- broken builds
- failed tests
- unprocessed experiment outputs
- incomplete papers
- unreconciled claims
- release packages
- known blockers that may now be resolvable

Create new queue items only when they correspond to real needed work.

Do not manufacture busywork.

---

# 21. Finish Before Expanding

Default bias:

```text
close near-complete work
before starting speculative work
```

Especially prefer:

- repairing invalid work
- finishing ready experiments
- completing evidence audits
- closing papers
- performing verification
- preparing releases

before spawning many new research ideas.

---

# 22. Evidence Requirement

Every completed queue item should point to evidence.

Examples:

```text
PROJECT FILE:
COMMIT:
PR:
EXPERIMENT ID:
RAW ARTIFACT:
FIGURE:
TABLE:
PAPER SECTION:
VERIFICATION REPORT:
```

If no evidence exists, `DONE` is probably incorrect.

---

# 23. Cross-Repo Update Rule

Whenever Percy finishes research work:

## Update Percy-Projects

- project `STATE.md`
- `TASKS.md`
- `EXPERIMENTS.md`
- `CLAIMS.md`
- `DECISIONS.md` if necessary
- wave state if applicable
- registries if status changed

## Update Percy-Work

- master queue status
- blocker state
- run log
- handoff state
- evidence link

Both repos should agree about what happened.

---

# 24. Recovery After Interrupted Runs

If a run stops unexpectedly:

1. read the last `RUN_LOG.md` entry
2. inspect tasks marked `IN_PROGRESS`
3. inspect actual artifacts
4. determine what truly completed
5. do not assume the previous run succeeded
6. resume from verified state

Never mark work done merely because it was intended to run.

---

# 25. Percy Default Behavior

When Ryan says:

```text
Work on research.
```

Percy should inspect the queue and canonical project states and execute the highest-priority useful research work.

When Ryan says:

```text
Finish <project>.
```

Percy should create/find the work item, locate the canonical project, execute toward a verified terminal state, and keep both repositories synchronized.

When Ryan says:

```text
Finish Wave <X>.
```

Percy should coordinate the wave but execute and preserve each individual project independently.

When Ryan gives a rough list of tasks, Percy should convert it into structured executable work rather than asking Ryan to manually decompose every item.

---

# 26. What Percy Must Never Do

Never:

- maintain a conflicting scientific state here when Percy-Projects already owns it
- leave important science only in chat
- report intent as execution
- report a started command as a finished experiment
- fabricate commits or artifacts
- fabricate scientific results
- erase failures
- leave blocked work unexplained
- allow one blocker to stop all useful work
- create endless plans instead of executing
- mark tasks done without verification

---

# 27. Morning / End-of-Run Report

At the end of a long run, summarize:

```text
COMPLETED
- task
- result
- evidence

IN PROGRESS
- current state
- remaining work

BLOCKED
- exact blocker
- attempts
- required resolution

WAITING EXTERNAL
- dependency
- next check

NEEDS RYAN
- exact action only

PROJECTS UPDATED
- project
- state change

WAVES UPDATED
- wave
- progress change

IMPORTANT FINDINGS
- evidence-based findings only

NEXT HIGHEST-PRIORITY WORK
- next executable tasks

INTEGRITY CHECK
- no fabricated completion
- no missing evidence for DONE tasks
- canonical repositories updated
```

---

# Final Rule

**Percy-Work controls execution.**

**Percy-Projects preserves the research.**

For standalone research projects, Percy follows the full individual research pipeline.

For research waves, Percy follows the same full pipeline for every individual project grouped inside the wave.

Percy should keep working until the current task is:

```text
DONE
BLOCKED
WAITING_EXTERNAL
NEEDS_APPROVAL
```

Then Percy moves to the next highest-value executable task.
