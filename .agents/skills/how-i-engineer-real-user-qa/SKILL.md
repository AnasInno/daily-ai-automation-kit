---
name: how-i-engineer-real-user-qa
description: "Use when QA needs Browser Use, Computer Use, or another visible-session check that proves the workflow like a real user."
---

# Real User QA

Use this skill when a workflow has a visible browser, desktop, download, upload,
or file-picker path that a real user would touch.

This is for:

- Browser Use checks for local web apps and owner-facing forms
- Computer Use checks for desktop, OS-level, file-picker, PDF, or visual flows
- verifying that the UI calls the same path as the CLI or documented command
- screenshots, downloads, and output inspection
- finding confusing first-run states, broken buttons, layout issues, and
  proof claims that outrun recorded evidence

This is not for:

- replacing unit tests or evals
- using private browser profiles, cookies, inboxes, or real accounts
- clicking through logged-in private systems
- claiming browser or computer proof from CLI-only evidence

## Tool Readiness

Before the run, verify the tools needed for the proof:

- local app or server starts from a documented command
- Browser Use or browser-control tooling can open the target URL
- Computer Use is available if the flow leaves the browser or needs OS-level
  interaction
- fake fixtures and sample files are ready
- download/output directory is known and clean
- screenshot or artifact capture works without exposing private data

If a required tool is missing, stop and report:

```text
Real-user QA not run; missing tool: <tool or capability>.
```

## Real-User Script

Test the path a non-technical owner would take:

1. Open from a blank or first-run state.
2. Inspect the first screen before interacting.
3. Enter realistic fake input by typing, selecting, uploading, or pasting.
4. Click the visible run/action button.
5. Wait for the UI state a user would see.
6. Inspect the rendered result for usefulness, not just presence.
7. Download, export, print, or open the output when that is part of the flow.
8. Compare the visible output to the CLI/sample-output contract.
9. Capture only public-safe screenshots or artifact notes.
10. Record what was not proved.

Avoid shortcuts that a real user cannot take, such as calling hidden APIs
directly, editing local storage, bypassing validation, or injecting fixture
state through the console.

## Browser Use Standard

Use Browser Use-style proof for web flows:

- page loads at the documented local URL
- visible labels, buttons, and inputs are understandable
- form validation handles missing or bad input
- realistic fake input can be submitted
- progress, loading, and error states do not trap the user
- rendered output is readable
- downloads or copied outputs are inspectable
- mobile or narrow viewport is checked when the user would expect it

## Computer Use Standard

Use Computer Use-style proof only when browser automation is not enough:

- desktop dialogs
- native app flows
- file pickers
- PDFs or generated files opened visually
- drag/drop or OS-level interactions
- browser paths that require visual confirmation outside normal DOM control

Computer Use proof should still use fake data, public-safe screenshots, and a
clear note about the exact visible path completed.

## Output Standard

Return:

- tool readiness checked
- visible path tested
- screenshots/artifacts captured, using public-safe descriptions
- output inspected
- mismatch between UI, CLI, docs, or sample output
- accessibility or layout blockers
- proof label: `browser-recorded`, `computer-recorded`, or `not-run`
- what was not proved
