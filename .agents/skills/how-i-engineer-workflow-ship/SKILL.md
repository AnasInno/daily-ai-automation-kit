---
name: how-i-engineer-workflow-ship
description: "Use when building or customising one small workflow automation from a clear brief."
---

# Workflow Ship

Use this skill when the user has a clear workflow or has accepted a brief.

Assume `codex/how-i-engineer/KERNEL.md` is already loaded.

This is for:

- customising the example for a new persona
- adding a new small automation under `examples/`
- making a CLI/local app produce a useful output
- adding focused tests and sample outputs
- documenting limits honestly

This is not for:

- live external writes
- scraping private systems
- broad SaaS/platform work
- publishing real customer data

## Brief Shape

```text
Use the How I Engineer workflow.

Task: [one concrete workflow]
User: [persona]
Input: [file/text/CSV/PDF/public page]
Output: [CSV/Markdown/HTML/report]
Validation: [smoke | tests | eval | browser | computer | Crabbox | autoreview | safety]
Goal: [what useful result exists after the run]

Constraints:
- deterministic core first
- optional AI only where judgement helps
- sample mode works without secrets
- no external writes by default
- proof claims must match recorded proof
```

## Loop

1. Inspect current repo state with `git status --short`.
2. Read the accepted brief or create one from `templates/automation-brief.md`.
3. Pick the smallest coherent artifact shape.
4. Reuse the existing example patterns before inventing new structure.
5. Build deterministic parsing/filtering/scoring/transformation first.
6. Add optional AI only behind config or fixture mode.
7. Add fake or public-safe sample input.
8. Generate intentional sample output.
9. Add `make smoke`.
10. Add tests for the happy path and at least one failure or rejection path.
11. Update README/OWNER_README/VERIFY-style docs for the workflow.
12. Run focused checks, then `make check` from repo root.

## Expected Files

For a new workflow, prefer:

```text
examples/<workflow-slug>/
  README.md
  IDEA.md or BRIEF.md
  Makefile
  .env.example
  data/
  output/
  scripts/run.py
  tests/
```

Add a local web wrapper only if it helps the user enter inputs or download outputs. The CLI remains the source of truth.

## Closeout

Report:

- changed files
- commands run
- output produced
- what was inspected
- what was not proved
- closeout label: `fail`, `needs repair`, `needs judgement`, or `merge candidate`
