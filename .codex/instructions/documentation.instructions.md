# Documentation Instructions

Use these rules when updating user-facing or developer-facing documentation.

## Required Practices

- Document implemented behavior, approved contracts, assumptions, limits, validation behavior, and artifact outputs.
- Keep documentation aligned with service contracts and validation evidence.
- Document headless workflows without implying GUI-only execution.
- Include import, benchmark, comparison, calibration, and report behavior when touched.
- Record documentation gaps instead of inventing behavior.
- Tell the orchestrator when documentation creates or closes follow-up work so `.process/NEXT-STEPS.md` can be updated.

## Acceptance Checks

- Docs describe current behavior without stale runtime or model assumptions.
- Contract and artifact descriptions match implementation.
- Known limits, assumptions, and validation gaps are visible.
- The `documentation aligned` gate can be closed when docs match delivered behavior and artifacts.
- Documentation status can be reflected in `.process/STATUS.md`.

## Do-Not Rules

- Do not invent behavior that is not implemented or explicitly approved.
- Do not imply GUI-only execution for headless services.
- Do not hide assumptions, limits, or validation gaps.
