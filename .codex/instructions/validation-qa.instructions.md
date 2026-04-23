# Validation QA Instructions

Use these rules when planning or reviewing validation for a change.

## Required Practices

- Cover changed behavior with the smallest sufficient mix of unit, integration, regression, and workflow tests.
- Verify contracts, schemas, preflight behavior, and artifact/report shapes.
- Include headless execution checks for core workflows.
- Include GUI checks only for GUI responsibilities.
- Represent physical and numerical criteria from `physics-numerics-rigor` in tests or documented evidence.
- Record commands run, results, skipped checks, known gaps, and residual risk.
- Treat missing fixtures, non-determinism, and unchecked artifacts as validation gaps.

## Acceptance Checks

- Validation evidence maps back to acceptance criteria.
- Contract and artifact checks are explicit.
- Physical and numerical criteria are not replaced by generic test passing.
- Skipped checks and residual risks are visible to reviewers.
- The `validation report ready` gate can be closed with explicit evidence and residual risk.

## Do-Not Rules

- Do not replace scientific acceptance criteria with generic QA checks.
- Do not ignore skipped checks, missing fixtures, or unchecked artifacts.
- Do not mark validation complete without a usable report.
