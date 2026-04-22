# Core Solver Instructions

## Domain focus

Implement and maintain engine simulation core capabilities:

- 0D thermodynamic cycle elements
- 1D gas dynamics transport elements
- Stable coupling interfaces between 0D and 1D models

## Engineering rules

- Prioritize numerical stability and conservation consistency.
- Use explicit units and clear variable naming.
- Keep coupling interfaces schema-driven and testable.
- Provide pytest coverage for physical sanity checks.
