# What Not To Publish

This repo is designed to show how I engineer without exposing private operating detail.

The public artifact should make the system look powerful. It should not show the raw private machinery.

Avoid publishing:

- exact private workspace paths
- raw model keys or provider account details
- real customer data or sensitive user data
- private planning notes
- personal inbox exports
- browser profiles
- screenshots, recordings, HAR files, traces, logs, PDFs, or downloads that have not been scrubbed
- unreleased product strategy
- internal agent memory, hidden prompts, or scratchpad logs
- private eval traces, live model outputs, or production routing evidence
- generated artifacts that have not been inspected

Safe alternatives:

- describe the workflow at a high level
- include fake fixtures
- include a redacted brief
- include a reproducible test
- include a public safety scanner
- include fake scenario packs, rubrics, and fixture scorecards
- describe the orchestrator/worker pattern without publishing private prompts
- show browser proof categories without exposing private sessions
