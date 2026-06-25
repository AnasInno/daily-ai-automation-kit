---
name: how-i-engineer-orchestrator
description: "Use when coordinating several bounded worker lanes for one workflow or release."
---

# Orchestrator

Use this skill when a task naturally splits into independent lanes.

This is for:

- one implementation lane plus one QA/review lane
- parallel research and build lanes
- separate workflow variants
- coordinating browser, computer, Crabbox, eval, or release proof
- integrating worker output into a single release verdict

This is not for:

- tiny edits where coordination costs more than the work
- vague repo-wide improvement
- overlapping file edits that need one continuous judgement
- pretending internal subagents are real independent worker owners

## Required Context

Load:

- `codex/how-i-engineer/WORKFLOW.md`
- `ops/contracts/worker-briefs/worker-brief-template.md`
- relevant task skill for each worker lane

## Coordinator Loop

1. Discuss the problem, options, and risks with the user first.
2. Decide whether multi-lane work is worth it.
3. Split by user-impact lane, not by random file ownership.
4. Give each worker one objective, one allowed scope, and one proof expectation.
5. Require each worker to report changed files, commands, evidence, risks, and what was not proved.
6. Read worker output critically; do not accept "looks good" without proof.
7. Integrate in an intentional order.
8. Run coordinator-level validation after integration.
9. Run PR/ship safety before public claims.

## Worker Prompt Shape

```text
Use the How I Engineer workflow.

Task: [one concrete thing]
Lane: [conversation | research | build | eval | autoreview | QA | browser | computer | Crabbox | release]
Allowed files:
Forbidden files:
Proof required:

Constraints:
- follow AGENTS.md and LOAD-FIRST.md
- keep the slice scoped
- do not publish private details
- do not mutate external systems
- close out with changed files, commands, evidence, risks, and unproved claims
```

## Evidence Rules

- CLI proof means the command ran and output exists.
- Test proof means focused tests passed.
- Browser proof means the visible path was actually completed and recorded.
- Computer proof means the desktop or OS-level visible path was actually completed and recorded.
- Crabbox proof means a Crabbox run actually executed and produced evidence.
- Tool-readiness proof means required tools were hydrated or checked before the proof run.
- Autoreview proof means an independent brief-fit, minimality, claim, and safety review was recorded.
- Safety proof means the public safety scanner passed.

Do not flatten these into "tested".
