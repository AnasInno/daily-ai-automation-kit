# Agentic Build Loop

The loop is built for speed without sloppiness.

The goal is not to make an agent "do everything." The goal is to use agents like an engineering team: conversation first, smallest useful slice, one orchestrator when needed, narrow worker lanes, evals where quality matters, autoreview for minimality and proof claims, local or Crabbox execution, hard proof gates, and a merge candidate that can be inspected by a human.

For actual agent work, start at `codex/how-i-engineer/LOAD-FIRST.md`, then load the smallest matching skill under `.agents/skills/`.

## Phase 0: Problem Conversation

Before orchestration, clarify the job in plain English:

- who is actually stuck
- what they open, copy, paste, compare, rewrite, or check
- where the work becomes expensive or trust-sensitive
- what output would change the next action
- what a false positive would cost
- what the automation must never do

The conversation is where the useful slice appears.

## Phase 1: Brief

Start with a concrete workflow:

- who has the pain
- what they do manually today
- what input they already have
- what output would save time
- what the tool must never do automatically

The brief is the handoff into orchestration. If the brief is still vague, the orchestrator should reject the work before code exists.

Use `.agents/skills/how-i-engineer-conversation-brief/SKILL.md` when the brief is not buildable yet.

## Phase 2: Worker Split

Each worker gets a narrow job.

- research worker: workflow reality, public data shape, rejection risks
- builder worker: CLI/local app, deterministic core, optional AI layer
- eval worker: scenario pack, rubric, scorecard, and routing verdict
- autoreview worker: brief fit, minimality, overengineering, proof claims, safety
- QA worker: smoke tests, fixtures, docs, failure modes
- browser worker: real owner-facing flow when there is a UI
- computer worker: desktop, file-picker, PDF, download, or OS-level visible flow
- Crabbox worker: hydrated isolated run with tool-readiness checks
- PR/ship worker: safety scan, clean tree, CI/CD-ready shape

This keeps the system from becoming a single giant prompt with no accountability.

Use `.agents/skills/how-i-engineer-orchestrator/SKILL.md` only when the work genuinely benefits from multiple lanes.

## Phase 3: Eval When Quality Matters

Use evals when the change affects generated quality, model routing, confidence,
fallback behavior, or claims about usefulness.

The public shape is:

```text
scenario pack -> candidate outputs -> rubric -> deterministic scorer -> scorecard
```

Use `.agents/skills/how-i-engineer-eval-framework/SKILL.md` for eval-shaped work.

## Phase 4: Local Or Crabbox Execution

The automation is run in the smallest context that proves the claim. Sometimes that is a disposable local pass; sometimes it is a Crabbox run.

Either way, the rules are the same:

- no hidden local state
- no real secrets for sample mode
- fake public-safe inputs in public examples
- outputs recreated from commands
- proof artifacts separated from normal workspace noise
- ignored runtime junk cleaned before release

If it only works on the builder's machine, it does not count.

Use `.agents/skills/how-i-engineer-crabbox-proof/SKILL.md` when isolated proof is required.

## Phase 5: Proof Chain

Every example needs a proof chain:

```text
sample input -> command -> generated output -> tests -> eval when relevant -> safety scan
```

If there is a UI:

```text
verify Browser Use -> open local app -> enter realistic input -> run -> inspect output -> download file
```

If the flow leaves the browser:

```text
verify Computer Use -> open desktop/file/PDF path -> complete visible user action -> inspect artifact
```

Only call that browser E2E proof after a browser run has actually been recorded.
Only call Computer Use proof after the OS-level visible path has actually been
recorded. Do not claim either proof from hidden API calls, local-storage edits,
or console shortcuts.

## Phase 6: Autoreview

Before release, run an independent review against the brief.

The review asks:

- did the build stay inside the agreed slice?
- is there code, structure, AI, or integration work that should be removed?
- do docs and sample outputs match the command path?
- do proof claims match actual evidence?
- did public-safety boundaries hold?

Use `.agents/skills/how-i-engineer-autoreview/SKILL.md`.

## Phase 7: PR / Ship Gate

Before submit or merge:

- current tree passes safety scan
- CI/CD runs the proof chain on push or pull request
- git history is clean
- no generated archives are accidentally tracked
- no local paths or secrets exist
- docs match commands
- limitations are honest

The output should feel like a calm release, not a lucky terminal transcript.

Use `.agents/skills/how-i-engineer-pr-ship-safety/SKILL.md` before submitting,
merging, shipping, or presenting PR-shaped work.
