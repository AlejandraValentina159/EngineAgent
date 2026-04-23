# Data Import Benchmark Calibration Instructions

Use these rules when work touches measured data, canonical import, benchmarks, comparison, calibration, or reports.

## Required Practices

- Define canonical dataset fields and accepted source formats.
- Record source units, normalized units, provenance, and rejected-data behavior.
- Keep mapping and normalization reusable outside the GUI.
- Package benchmarks with enough metadata to reproduce results.
- Define simulation-versus-measurement metrics and report artifacts.
- Define calibration workflow inputs, outputs, stopping conditions, and result artifacts.
- Ensure reports are deterministic and validation can assert their structure.

## Acceptance Checks

- Imported data can be traced back to source fields and units.
- Benchmark packages can be rerun reproducibly.
- Comparison and calibration reports have explicit shapes.
- Calibration does not depend on GUI state.
- Data workflow tests cover mapping, normalization, provenance, and artifact creation.
- The `data/report contract ready` gate can be closed when relevant workflow contracts and report artifacts are explicit.

## Do-Not Rules

- Do not hide provenance or unit normalization.
- Do not make comparison, calibration, or reporting GUI-only.
- Do not treat data workflow artifacts as informal outputs.
