# Next Steps

1. Initialize or refresh `.process/STATUS.md` for the next multi-step workstream.
   Owner: `orchestrator`
   Dependencies: incoming task context; choose `new` or `resume`

2. Route the next workstream to `analysis-spec` and close the `spec ready` gate.
   Owner: `orchestrator`
   Dependencies: `.process/STATUS.md` initialized; current request understood

3. Open the next required upstream gates only for touched ownership areas and record resulting decisions.
   Owner: `orchestrator`
   Dependencies: `spec ready`; affected agents may include `architecture-contracts`, `physics-numerics-rigor`, `data-import-benchmark-calibration`, and `desktop-gui`
