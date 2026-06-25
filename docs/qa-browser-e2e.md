# QA And Browser E2E Proof

The QA standard is simple: if a real user would touch it, the visible path needs proof.

For agent procedure, use `.agents/skills/how-i-engineer-real-user-qa/SKILL.md`.

## Proof Levels

### Level 1: CLI Proof

The command runs against fake sample data and produces an output file.

Example:

```bash
make smoke
```

### Level 2: Test Proof

Automated tests verify the main behavior and important failure modes.

Example:

```bash
python3 -m pytest -q
```

### Level 3: Browser E2E Proof

For local apps, a Browser Use-style worker checks the real interaction:

- open the app
- inspect the first screen
- enter realistic inputs
- run the automation
- inspect the resulting table/output
- download the CSV
- confirm the output file shape

Do not claim this level unless the browser path was actually run and recorded.

Before claiming Browser E2E proof, verify that:

- the app starts from a documented command
- the target URL opens in a controllable browser session
- fake fixtures and sample files are available
- downloads go to a known location
- screenshots or artifact notes can be captured safely
- the UI path uses the same logic as the CLI or documented command

The test should follow the path a real owner would take: start from the first
screen, read the visible labels, type or upload realistic fake input, click the
visible action, wait for the result, inspect the output, and download or copy the
artifact if that is part of the workflow.

Do not cheat by calling hidden APIs directly, changing local storage, injecting
state through the console, or skipping validation that a real user would hit.

### Level 3b: Computer Use Proof

Use Computer Use-style proof when browser automation is not enough:

- desktop app flows
- OS dialogs or file pickers
- drag/drop paths
- PDFs or generated files opened visually
- browser flows that need visual confirmation outside normal DOM control

Computer Use proof must still use fake data, public-safe screenshots, and a
clear note about the visible path completed. Do not use private browser
profiles, cookies, inboxes, real accounts, or logged-in private systems.

### Level 4: Eval Proof

For behavior or quality changes, an eval worker checks:

- scenario pack
- rubric
- strategy comparison
- scorecard
- quality verdict
- proof source of truth

Fixture evals prove the harness mechanics. They do not prove live model quality.

### Level 5: PR / Ship Proof

The merge candidate passes a public safety scan and CI/CD check:

- no secrets
- no local absolute paths
- no generated archives by accident
- no private workspace markers
- no hidden runtime state
- CI/CD runs the same proof chain

## What QA Should Catch

- the README command does not work
- the app needs an API key even for sample mode
- generated output is ignored but not reproducible
- the UI wraps a different path from the CLI
- Browser Use or Computer Use was needed but not available
- the visible flow only works through hidden state or a console shortcut
- downloads are created but never inspected
- screenshots contain private data
- a zip file or `.env` slipped into git
- the tool claims more than it proves

## Browser Proof Language

Be precise:

- "CLI smoke tested" means the command ran.
- "Browser E2E tested" means the visible local app path ran.
- "Computer Use tested" means an OS-level or desktop visual path ran.
- "Eval scored" means a named scenario pack, rubric, and scorecard exist.
- "Safety scanned" means the PR/ship artifact passed the public scanner.
- "CI/CD checked" means the proof chain ran on push or pull request.

Do not flatten these into one vague "tested" claim.
