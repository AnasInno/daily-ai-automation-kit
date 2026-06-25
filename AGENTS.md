# AGENTS.md - How I Engineer

This repo is a public-safe operating kit for shipping small, useful AI-assisted workflows.

## Load First

For any non-trivial task, read:

1. `codex/how-i-engineer/LOAD-FIRST.md`
2. `codex/how-i-engineer/KERNEL.md`
3. The smallest relevant skill under `.agents/skills/`

Do not load the whole repo as startup context. Use the router, pick a skill, then inspect the current files and example code that matter for the task.

## Scope

This repo is for:

- turning a user conversation into a tight workflow brief
- building or customising one small automation at a time
- evaluating output quality, routing strategy, and behavior change
- splitting substantial work into bounded orchestrator/worker lanes
- autoreviewing changes against the brief, minimality, proof, and safety
- running local, visible-session, or Crabbox proof
- preparing public-safe PR/ship artifacts

It is not for publishing private project internals, customer data, private prompts, browser sessions, inboxes, API keys, Crabbox broker details, live run logs, or exact production runbooks.

## Common Entry Points

- Unclear workflow or early scoping: `.agents/skills/how-i-engineer-conversation-brief/SKILL.md`
- Build or customise one workflow: `.agents/skills/how-i-engineer-workflow-ship/SKILL.md`
- Coordinate several worker lanes: `.agents/skills/how-i-engineer-orchestrator/SKILL.md`
- Autoreview a build or merge candidate: `.agents/skills/how-i-engineer-autoreview/SKILL.md`
- Test a visible browser or desktop path like a real user: `.agents/skills/how-i-engineer-real-user-qa/SKILL.md`
- Run isolated proof with Crabbox: `.agents/skills/how-i-engineer-crabbox-proof/SKILL.md`
- Build or review an eval harness: `.agents/skills/how-i-engineer-eval-framework/SKILL.md`
- PR/ship readiness: `.agents/skills/how-i-engineer-pr-ship-safety/SKILL.md`

## Development Rules

- Start from the user problem, not the tool.
- Keep the first useful slice small enough to run locally in minutes.
- Prefer deterministic logic before AI.
- Add AI only for judgement, extraction, ranking, summarisation, or rewriting where it improves the output.
- Keep sample mode working without secrets.
- Autoreview non-trivial changes for brief fit, minimality, overengineering,
  proof claims, and public safety.
- Include a smoke command, tests where useful, sample input/output, and honest limits.
- Use evals for behavior-shaping or quality-routing changes; do not treat a green smoke test as output-quality proof.
- Use real-user QA for visible flows: verify Browser Use or Computer Use tooling, then click/type/upload/download through the same path a user would.
- Use browser proof only when a browser run was actually recorded.
- Use Computer Use proof only when an OS-level or desktop visible run was actually recorded.
- Use tool-readiness proof only when required tools were checked before the proof run.
- Use Crabbox proof only when a Crabbox run was actually performed.
- Do not wire examples to send email, write to CRMs, post online, scrape private systems, or mutate external state by default.

## Validation

Run this before PR-shaped or ship-shaped changes:

```bash
make check
```

For structure checks only:

```bash
make doctor
```

Public claims should name their proof surface: CLI, tests, eval scorecard,
browser, computer, tool-readiness, Crabbox, autoreview, safety scan, CI/CD check,
or human judgement.
