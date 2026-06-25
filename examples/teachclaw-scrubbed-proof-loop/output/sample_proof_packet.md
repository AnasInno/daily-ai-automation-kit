# TeachClaw Scrubbed Proof Packet

Status: needs_judgement
Validation source of truth: local-cli, sample-output

## Conversation Brief

- Workflow: TeachClaw teacher artifact proof loop
- Persona: secondary school teacher
- Manual workflow: Turn a rough teaching request and fake class evidence into a useful artifact plan, then verify the result before handing it back.
- Teacher request: Create a short reteach activity for a fictional Year 10 class on factorising quadratics.
- Desired artifact: A concise reteach plan with a worked example, two checks for understanding, and an exit question.

## Fake Evidence

- misconception: Some pupils expand brackets correctly but miss common factors before factorising.
- misconception: Some pupils choose factor pairs that multiply correctly but do not add to the middle coefficient.

## Deterministic Artifact Plan

1. Anchor the artifact on the request: Create a short reteach activity for a fictional Year 10 class on factorising quadratics.
2. Use the class context only at the safe level provided: Fictional mixed-attainment group; no real pupil data.
3. Address each fake misconception explicitly before adding extension work.
4. Produce the requested artifact shape: A concise reteach plan with a worked example, two checks for understanding, and an exit question.
5. End with a human review checkpoint before claiming quality.

## Validation Gates

| Gate | Result | Evidence |
| --- | --- | --- |
| local code validated | pass | script validates required fields |
| workflow mechanically validated | pass | sample JSON produces Markdown output |
| output quality validated | needs_judgement | teacher-quality usefulness still needs human review |
| pr/ship safety validated | needs_judgement | repo-level safety scan is separate from this example command |

## Required Proof

- local-cli
- unit-tests
- sample-output
- human-output-review

## Safety Boundaries

- Do not use real pupil data
- Do not claim live classroom validation
- Do not publish private prompts
- Do not send external messages
- Do not include private runtime or deployment details

## What This Public Example Does Not Claim

- live TeachClaw runtime behavior
- real teacher approval
- real pupil-data handling
- private prompt quality
- browser proof
- Computer Use proof
- Crabbox hydration/tool-readiness proof
- Crabbox proof
- autoreview/minimality verdict
- CI/CD verification
