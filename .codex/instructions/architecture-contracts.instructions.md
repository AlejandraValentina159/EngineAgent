# Architecture Contracts Instructions

Use these rules when work touches service boundaries, schemas, artifact formats, data flow, compatibility, or module ownership.

## Required Practices

- Define important inputs, outputs, errors, reports, and artifacts explicitly.
- Prefer headless-first services that the GUI can call instead of GUI-owned workflows.
- Keep schemas and data models close to the services that own them.
- Record defaults, optional fields, units, and compatibility behavior.
- Name reproducible artifact paths or structures when workflows create files.
- Add migration notes for breaking changes.
- Keep validation and preflight contracts reusable outside the GUI.
- Record meaningful boundary, contract, or compatibility decisions for `.process/DECISIONS.md`.

## Acceptance Checks

- A caller can understand how to run the workflow without reading GUI code.
- The GUI-facing contract is a projection of service behavior, not a second implementation.
- Artifacts and reports have stable shapes that validation can assert.
- Backward compatibility or migration behavior is explicit.
- The `contracts ready` gate can be closed with explicit boundaries and contract shapes.
- `.process/STATUS.md` and `.process/NEXT-STEPS.md` can be updated from the contract outcome.

## Do-Not Rules

- Do not hide important schemas or artifact shapes in prose only.
- Do not define contracts that require GUI state for core behavior.
- Do not leave compatibility behavior ambiguous when defaults change.
