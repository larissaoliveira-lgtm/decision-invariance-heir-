# Methodology

This document is a navigation layer over the frozen machine-readable protocol in `../protocol/`.
The machine-readable files are authoritative when an exact value is required.

## Primary design

- Dataset: scikit-learn Wisconsin Breast Cancer benchmark.
- Fixed allocation: 60% training, 20% calibration, 20% locked test.
- Split seeds: 42 and 43, with provenance hashes recorded in `protocol/split_provenance.json`.
- Primary operational policy: three actions separated by two frozen thresholds.
- Primary probability thresholds: 0.30 and 0.70, represented in the affine/logit space by the frozen thresholds in `protocol/frozen_operational_policy.json`.
- Primary near-boundary definition: calibration-derived q=0.10; q=0.05 and q=0.20 are sensitivity analyses.
- HE configurations: `ckks_reference_f55_s45` and `ckks_reduced_f50_s40`.

## Numerical decomposition

The analysis separates float64-to-float32 export deviation, incremental HE deviation relative to float32 export, and total float64-to-HE deviation.

## Statistical roles

- H1: pre-specified composite empirical criterion.
- H2: one-sided Fisher exact tests at the primary boundary cutoff, Holm-adjusted across the two CKKS configurations.
- H3: diagnostic comparison of margin-normalized versus raw numerical error; no independent reject/accept claim.
- H4: paired bootstrap and sign-flip randomization on incremental HE error.

Exact settings, estimands, bootstrap counts, and multiplicity scope are frozen in `protocol/protocol.json` and `protocol/confirmatory_freeze.json`.
