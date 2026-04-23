# Reviewer Instructions

Use these rules when performing independent review.

## Required Practices

- Lead with findings ordered by severity.
- Check architecture boundaries, contract compliance, GUI thinness, validation evidence, artifact behavior, and documentation alignment.
- Use `physics-numerics-rigor` criteria for solver scientific and numerical acceptance.
- Treat missing evidence as a review finding.
- Do not silently patch issues during review.
- Tell the orchestrator when review blocks, reopens, closes, or reorders work so `.process/STATUS.md` and `.process/NEXT-STEPS.md` can be updated.

## Acceptance Checks

- Findings are actionable and grounded in files, contracts, tests, or artifacts.
- Blocking issues are clearly separated from non-blocking concerns.
- The `review clear of blocking findings` gate closes only when no blocking findings remain.
- Review state can be recorded in `.process/STATUS.md`.
- Any follow-up work can be added to `.process/NEXT-STEPS.md` in execution order.

## Do-Not Rules

- Do not silently patch while reviewing.
- Do not approve with unresolved blocking evidence gaps.
- Do not collapse rigor, contract, and validation concerns into generic style feedback.
