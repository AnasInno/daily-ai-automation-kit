# How I Engineer Workflow

Use this for ordinary work in this repo after `LOAD-FIRST.md` and `KERNEL.md`.

## 1. Start With The Conversation

Clarify:

- user/persona
- current manual workflow
- available input
- useful output
- safety boundaries
- proof needed

If these are unclear, use `.agents/skills/how-i-engineer-conversation-brief/SKILL.md`.

## 2. Pick The Skill

- one workflow build/customisation: `how-i-engineer-workflow-ship`
- several independent lanes: `how-i-engineer-orchestrator`
- independent review of a build or merge candidate: `how-i-engineer-autoreview`
- visible browser or desktop QA: `how-i-engineer-real-user-qa`
- isolated proof: `how-i-engineer-crabbox-proof`
- output-quality evals or routing comparisons: `how-i-engineer-eval-framework`
- PR/ship readiness: `how-i-engineer-pr-ship-safety`

Use one skill by default. Load a second only when the task genuinely crosses lanes.

## 3. Build The Smallest Useful Artifact

Expected shape:

```text
examples/<workflow-slug>/
  README.md
  IDEA.md or BRIEF.md
  Makefile
  .env.example, only if needed
  data/sample_input.*
  output/sample_output.*
  scripts/run.py
  tests/
```

Add a local web form only when it makes the workflow easier to try. The CLI remains the source of truth.

The current reference example is `examples/teachclaw-scrubbed-proof-loop/`, which uses fake data to show the TeachClaw-derived proof loop without private implementation details.

The eval reference example is `examples/teachclaw-scrubbed-eval-harness/`, which uses fake data to show scenario packs, weighted rubrics, strategy comparison, scorecards, and non-claims.

## 4. Prove The Right Surface

Minimum proof:

```bash
make smoke
python3 -m pytest -q
```

Repo proof:

```bash
make check
```

Only claim browser, tool-readiness, Crabbox, or CI/CD proof after that proof was
actually run.
Only claim Computer Use proof after an OS-level or desktop visual path was
actually run and recorded.

Only claim output quality after an eval, human review, or another explicit quality source says so. A smoke test proves mechanics, not usefulness.

## 5. Autoreview Non-Trivial Work

Before calling a build ready, check it against the original brief:

- did it keep to the smallest useful slice?
- did it add abstractions, integrations, or AI where deterministic code was enough?
- do docs, tests, sample outputs, and proof claims agree?
- did it avoid private data and external side effects?

Use `.agents/skills/how-i-engineer-autoreview/SKILL.md` for the review pass.

## 6. Close Out

Report:

- what changed
- command proof
- output inspected
- eval scorecard, when quality or routing changed
- what was not proved
- closeout label
- safety notes

If the work is worth preserving as public history, append a short public-safe note to `codex/how-i-engineer/WORK-DONE.md`.
