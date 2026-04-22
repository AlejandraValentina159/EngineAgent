# Copilot Instructions — EngineAgent

## Repository intent

This repository provides a multi-agent orchestration layout for PyWaveDyn engine simulation development.

## Hard constraints

- Use Python for simulation and tooling.
- No Docker, no databases, no web frameworks.
- Focus domain: 0D thermo, 1D gas dynamics, coupling, CLI, GUI, schemas, pytest.
- Preferred models available to this project: Claude Sonnet 4.6 and Claude Haiku 4.5.

## Expected quality gates

- Preserve deterministic numerical behavior.
- Keep schemas explicit and versioned.
- Validate with pytest for unit/integration/physics/gui slices.
