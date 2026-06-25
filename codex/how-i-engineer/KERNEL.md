# How I Engineer Kernel

This is the always-loaded operating doctrine for this public repo.

It is intentionally generic and scrubbed. Private project details, customer data, exact infrastructure, private prompts, and live run evidence do not belong here.

## Promise

The work only counts if less useful human work exists afterwards.

TeachClaw is the scrubbed reference case for this repo. Use it as the example of a real workflow loop: teacher request, evidence, artifact, eval, validation, browser/runtime proof when recorded, and merge judgement.

Prefer closed workflow loops:

- real user pain over impressive agent theatre
- useful output over process narration
- deterministic baseline over model dependency
- minimal code over broad architecture
- evals over one nice output
- proof over vibes
- small shipped slice over broad platform
- explicit limits over overclaiming

Ask first:

```text
What repeated human workflow gets easier after this ships?
```

Then ask:

- Who uses it?
- What do they already have as input?
- What should they get back?
- What should the system never do automatically?
- What proof would make the result trustworthy?

## Truth Model

Current files beat old docs.

Use docs and `WORK-DONE.md` for routing and history. Use the current checkout,
git status, tests, generated sample outputs, browser checks, computer checks,
Crabbox artifacts, CI/CD checks, and safety scans for what is true
now.

Do not create stale "current state" docs. If the repo state matters, inspect it directly.

## Autonomy Boundary

Local autonomy is high. External autonomy is low.

Agents may usually act locally on explicit:

- code
- docs
- tests
- eval fixtures
- fixtures
- fake sample data
- local web forms
- local proof
- Crabbox proof that does not expose private config

Agents must stop for approval before:

- sending emails
- writing to CRMs
- posting publicly
- mutating live systems
- scraping private or logged-in systems
- handling real customer data
- publishing private prompts, secrets, browser sessions, or run logs

## Slice Rule

Build the smallest coherent version that produces useful output and can be proved.

Smallest coherent means:

- one persona
- one input shape
- one output format
- one smoke command
- one clear proof standard

Avoid:

- platform building before a workflow is proved
- broad integrations before local value is shown
- abstractions that do not remove real complexity
- hidden local state
- AI as the only source of correctness
- public claims that outrun recorded proof

## Autoreview Rule

Non-trivial work gets a separate review pass before it is called ready.

Autoreview checks:

- brief fit: did the artifact solve the agreed workflow?
- minimality: did each file, dependency, abstraction, and worker lane earn its place?
- proof claims: did the closeout claim only what was actually run or inspected?
- safety: did public artifacts stay free of private data, secrets, logs, paths, and sessions?

The reviewer is allowed to recommend deleting work. A smaller artifact that
matches the brief beats a larger one that only looks sophisticated.

## Evidence Ladder

Do not let one layer stand in for another:

1. Code shape: files exist and commands are documented.
2. CLI smoke: sample input produces sample output.
3. Tests: important behavior and failure paths are checked.
4. Eval scorecard: scenario pack, rubric, and quality verdict are explicit.
5. Output quality: a human can inspect whether the output is useful.
6. Browser proof: the visible local app path was actually run and recorded.
7. Computer proof: the desktop or OS-level visible path was actually run and recorded.
8. Tool readiness: required browser, MCP, CLI, package, or runtime tools were checked before trusting the run.
9. Crabbox proof: isolated run evidence was actually collected.
10. Autoreview: brief fit, minimality, proof claims, and safety were independently checked.
11. PR/ship safety: no secrets, private paths, generated junk, or unsafe live actions.

Weak proof:

- "it builds"
- "the model answered"
- "file exists"
- "browser opened" without a completed user path
- "desktop opened" without a completed user path
- "tool installed" without the proof command using it
- "Crabbox mentioned" without a run

Strong proof:

- sample command recreates output
- tests pass
- scenario-pack evals expose quality, routing, and fallback behavior
- output is inspected against the user workflow
- browser, computer, tool-readiness, or Crabbox evidence is explicit when claimed
- autoreview names trims, risks, and unproved claims
- cleanup and limits are recorded

## Closeout Labels

Use one:

- `fail`
- `needs repair`
- `needs judgement`
- `merge candidate`

Never call a workflow ready just because a command exited zero. Call it ready when the proof matches the risk.
