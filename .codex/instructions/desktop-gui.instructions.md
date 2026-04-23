# Desktop GUI Instructions

Use these rules when work touches the desktop interface.

## Required Practices

- Keep GUI code thin; delegate business logic to services.
- Use view or view-model state only to represent user interaction and display state.
- Call solver, validation, import, comparison, calibration, and reporting behavior through explicit contracts.
- Keep long-running work responsive with progress, cancellation where appropriate, and clear errors.
- Surface shared preflight and validation results without duplicating their logic.
- Keep GUI tests focused on interaction, state mapping, and error presentation.

## Acceptance Checks

- The same core workflow can run without the GUI.
- GUI state maps to service inputs and outputs predictably.
- Heavy computation, import, calibration, validation, and report generation do not live in views.
- User-facing errors preserve useful service detail.

## Do-Not Rules

- Do not place heavy business logic in GUI modules.
- Do not create GUI-dependent execution paths for core behavior.
- Do not duplicate validation, comparison, calibration, or reporting logic in the desktop layer.
