# Work Done

Public-safe history only.

Use this for durable repo-level notes that help a future agent understand public examples, proof decisions, or release boundaries.

Do not record private customer details, exact local paths, secrets, browser sessions, private prompts, Crabbox lease IDs, broker URLs, screenshots, logs, or live run metadata.

Current truth still comes from the checkout, tests, sample outputs, and recorded proof artifacts.

## Public Reference Examples

- Added `examples/teachclaw-scrubbed-eval-harness/` as the public-safe eval reference: fake scenarios, weighted rubric, candidate strategy fixtures, deterministic scorecards, and non-claims for live model/runtime proof.

## 2026-06-25

- Added an explicit autoreview skill and routing references so non-trivial work
  gets checked against the brief, minimality, proof claims, and public safety
  before being called ready.
- Clarified Crabbox proof as lease, hydrate tools, sync, verify toolchain, run,
  collect evidence, and release, including public-safe MCP/tool readiness checks.
- Added real-user QA guidance for Browser Use and Computer Use proof, including
  tool readiness, visible-path testing, downloads, screenshots, and non-claims.
- Synced lane names, proof labels, PR/ship safety, example non-claims, and
  scanner rules so newer proof surfaces are not only described in the README.
- Reframed the final boundary as submit PR, CI/CD checks, and merge/ship rather
  than public-repo release ceremony.
