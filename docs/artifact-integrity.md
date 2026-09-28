# Artifact integrity

The repository separates human-readable documentation from machine-verifiable frozen state.

Primary integrity records include:

- `protocol/confirmatory_freeze.sha256`
- `protocol/confirmatory_freeze.json`
- `protocol/split_provenance.json`
- `MANIFEST.pilot.sha256.json`
- `MANIFEST.confirmatory.sha256.json`
- environment and compatibility records under `environment/`

The preserved main-study freeze digest is:

`3b0347b70e8df2979b4371ee1fecd273d79f197c498d42afea526a0b2c11e45e`

During repository preparation, all 74 artifact hashes directly referenced by the frozen confirmatory record were recomputed successfully, and all 249 entries in the confirmatory bundle manifest matched their recorded SHA-256 values.

Large frozen bundles are intended to be attached to a tagged GitHub Release. Their SHA-256 sidecar files should be distributed alongside the archives and rechecked after upload.

See `docs/confirmatory-audit.md` for the audit scope, conclusions, and limitations.
