# Reproducibility

## PILOT

Use `notebooks/OpenScience_HEIR_Decision_Invariance_PILOT_v1_3.ipynb` in a fresh compatible Linux/Colab runtime.

The complete frozen PILOT bundle is distributed as a release asset rather than committed as a git blob. It contains the protocol, model, split provenance, environment records, generated HE artifacts, runtime libraries, logs, figures, results, and integrity manifest required to reconstruct the frozen state.

The preserved confirmatory-freeze SHA-256 is:

`3b0347b70e8df2979b4371ee1fecd273d79f197c498d42afea526a0b2c11e45e`

## CONFIRMATORY

Use `notebooks/OpenScience_HEIR_Decision_Invariance_CONFIRMATORY_v1_3.ipynb` only with the complete frozen PILOT bundle and the preserved freeze digest.

The execution gate verifies the frozen scientific and integrity state before locked-test outputs are materialized. The main confirmatory execution was completed as run `20260917T195635259936Z` and is preserved as a separate release asset.

Compact outputs are available in `results/confirmatory/`. The full bundle retains detailed execution logs, per-sample and per-repeat results, binaries, runtime libraries, and its complete SHA-256 manifest.

## Environment

See `environment/requirements.lock.txt`, `environment/confirmatory_requirements.txt`, `environment/heir_openfhe_compatibility.json`, the recorded HEIR/OpenFHE revisions, and runtime provenance records. Confirmatory-specific runtime snapshots are under `environment/confirmatory/`.

## Verification

`docs/confirmatory-audit.md` records the artifact-level audit used to reconcile the main confirmatory package with the frozen v1.3 PILOT state.

The scripts under `scripts/` are publication/repository utility scripts. They were added after the scientific freeze and are not part of the frozen analysis code.
