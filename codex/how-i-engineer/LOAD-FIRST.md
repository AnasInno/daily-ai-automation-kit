# How I Engineer - Load First

This file is the public agent router. Keep startup light.

## Startup

For non-trivial work:

1. Read `codex/how-i-engineer/KERNEL.md`.
2. Pick one task skill from `.agents/skills/`.
3. Load topic docs only when the skill routes you there.
4. Inspect the current files, tests, examples, generated outputs, or public proof artifacts that matter for the task.
5. Use `codex/how-i-engineer/WORK-DONE.md` only for public-safe history, never as current truth.

Do not load private memories, private project repos, hidden scratchpads, local browser profiles, inboxes, or unredacted run logs into this public repo.

## Skill Router

- Conversation still unclear: `.agents/skills/how-i-engineer-conversation-brief/SKILL.md`
- Build or customise one workflow: `.agents/skills/how-i-engineer-workflow-ship/SKILL.md`
- Coordinate several worker lanes: `.agents/skills/how-i-engineer-orchestrator/SKILL.md`
- Autoreview a build or merge candidate: `.agents/skills/how-i-engineer-autoreview/SKILL.md`
- Visible browser or desktop QA: `.agents/skills/how-i-engineer-real-user-qa/SKILL.md`
- Isolated execution or browser/desktop proof: `.agents/skills/how-i-engineer-crabbox-proof/SKILL.md`
- Eval harness or quality routing: `.agents/skills/how-i-engineer-eval-framework/SKILL.md`
- PR/ship readiness: `.agents/skills/how-i-engineer-pr-ship-safety/SKILL.md`

## Topic Docs

Load only at point of use:

- Build loop: `docs/agentic-build-loop.md`
- Orchestrator and workers: `docs/orchestrator-worker-system.md`
- Crabbox runs: `docs/crabbox-runs.md`
- Eval framework: `docs/eval-framework.md`
- Browser proof: `docs/qa-browser-e2e.md`
- PR/ship safety: `docs/pr-ship-safety.md`
- Scrub boundaries: `docs/what-not-to-publish.md`
- Eval contracts: `ops/evals/README.md`
- Validation gates: `ops/contracts/validation-gates/README.md`
- Worker brief template: `ops/contracts/worker-briefs/worker-brief-template.md`
- Workflow brief template: `templates/automation-brief.md`

## Default Flow

```text
conversation -> brief -> skill -> build/customise -> eval/proof -> PR -> CI/CD -> merge/ship
```

Start with the smallest useful workflow. Do not create a platform when a script, local app, and CSV/Markdown output would solve the problem.
