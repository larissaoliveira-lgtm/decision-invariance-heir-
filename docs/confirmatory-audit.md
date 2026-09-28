# Confirmatory artifact audit

## Scope

This record audits the main-workload confirmatory artifact

`decision-invariance-heir-v1-3_1.3.0_20260917T195635259936Z.zip`

against the preserved v1.3 PILOT freeze currently distributed with this repository.

The purpose of this audit is to determine whether the confirmatory artifact is structurally compatible with the frozen pre-confirmatory state. It is not an external replication or independent third-party certification.

## Conclusion

The confirmatory artifact is **compatible with the preserved v1.3 frozen PILOT protocol** and may be treated as the main-study `HEIR_REAL_HE_CONFIRMATORY` execution for this repository.

The evidence supporting that conclusion is:

1. the confirmatory artifact contains freeze SHA-256
   `3b0347b70e8df2979b4371ee1fecd273d79f197c498d42afea526a0b2c11e45e`;
2. that digest is identical to the currently preserved `protocol/confirmatory_freeze.sha256`;
3. the two `confirmatory_freeze.json` files are byte-identical;
4. the frozen `protocol.json`, operational policy, split provenance, rare-event plan, boundary-stress plausibility record, HE configuration specifications, and both configuration JSON files are byte-identical between the preserved PILOT repository state and the confirmatory artifact;
5. all 74 files referenced directly by the frozen confirmatory record match their expected SHA-256 values in the confirmatory artifact;
6. all 249 entries in the confirmatory artifact's `MANIFEST.sha256.json` were independently recomputed during this audit and matched their recorded SHA-256 values;
7. the confirmatory runtime record reports `locked_test_access_granted: true` and `locked_test_materialized: true`;
8. the confirmatory environment matches the frozen compatibility contract: CPython 3.13, Linux, x86_64, with the same recorded HEIR and OpenFHE revisions;
9. the final dependency consistency check reports no broken requirements;
10. the confirmatory run evaluates both frozen CKKS configurations and labels its transformation type `HEIR_REAL_HE_CONFIRMATORY`.

## Temporal ordering

The frozen record was created before the confirmatory run:

- confirmatory freeze created: `2026-09-17T19:40:23.891287+00:00`;
- confirmatory run ID: `20260917T195635259936Z`.

This ordering is consistent with the intended PILOT -> freeze -> CONFIRMATORY workflow.

## Main confirmatory outcome

The locked test contains 114 observations.

For both frozen CKKS configurations:

- binary-classification disagreement count: 0;
- operational-action disagreement count: 0;
- transformed binary accuracy: 0.9824561403508771;
- absolute binary-accuracy difference vs plaintext: 0.

Consequently:

- H1 strict coexistence criterion: not met, because no operational-action disagreement occurred;
- H2: not estimable because no operational disagreements occurred;
- H3: not estimable because disagreement labels contain only one class;
- H4: no primary configuration difference detected under the frozen paired analysis.

For H4, the paired difference in incremental HE MAE (`reduced - reference`) is
`3.80208356338635e-08`, with 95% bootstrap CI
`[-8.731925239165619e-08, 1.6862044535708006e-07]` and two-sided paired sign-flip randomization p-value `0.5717214139293035`.

For zero observed operational disagreements with `n = 114`, the frozen analysis reports an exact one-sided 95% upper bound of `0.02593608201362844`. Therefore the correct interpretation is finite-sample preservation in this locked test, not universal decision invariance.

## Environment evidence

The PILOT and CONFIRMATORY runtime provenance records both report:

- CPython 3.13.15;
- Linux 6.6.122+;
- x86_64;
- glibc 2.39;
- `heir_py==2026.9.1`;
- HEIR source commit `5eaf0be77f9c07428e37d21cf4d7313d1295872e`;
- OpenFHE ref `v1.4.2`;
- OpenFHE resolved commit `aa391988d354d4360f390f223a90e0d1b98839d7`.

A dependency inconsistency present at the baseline stage (`jedi` missing for IPython) was repaired during setup; the final dependency consistency check returned success with no broken requirements.

## Bundle hashes

Main PILOT bundle:

`90c54b1f1a5d89e94db94d444eb4fdd3afe14596fa2dd554ac911d0be69572fb`

Main CONFIRMATORY bundle:

`997d189ff9bac0cf7bba87d689fc90a31791df2debb7b0cad26704f79b5d67bf`

These should be rechecked after upload to the public GitHub Release.

## Limitations of this audit

This audit verifies the supplied digital artifacts and their internal consistency. It cannot, from the artifact bytes alone, prove organizational facts outside those artifacts, such as whether the freeze digest was stored in a physically independent location before the run or whether no unrecorded human observation of locked-test outcomes occurred. The artifacts are consistent with the claimed fail-closed workflow, but those process facts remain provenance claims rather than independently observable cryptographic facts.

The locked test is an internal provenance-preserving held-out subset and is not an external validation cohort. External replication remains a separate validity objective.
