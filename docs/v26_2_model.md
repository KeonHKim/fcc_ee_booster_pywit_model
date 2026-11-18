# Model scope and normalization — HEB V26.2

| Component | Model treatment |
|---|---|
| RW | Circular Cu/150 nm NEG pipe, b=30 mm, Rq=0.3 µm; fitted Gold/TL q=-2.1043; total physical RW length 89,080.356 m. |
| RF | 112 cavities; local-beta weighting for transverse spectra. |
| BPM | 2740 devices; local-beta weighting. |
| Bellows | 10000 units of 0.15 m; original source already integrated around ring — **do not multiply again**. |
| Damping wigglers | 10 × 6.03 m; provisional S4 scenario, beta matching not finalized. |
| Extraction kicker | 10 × 0.418 m = 4.18 m; provisional length-scaled main-ring injection kicker reference, factor 0.209; local location/beta pending. |

The v26_2 inventory, source_provenance CSV and export manifest document the current source files and numerical assumptions.

**Limitations:** NEG use in booster is not finalized; a bare-copper alternative is not part of this release. Wiggler input `wiggler_config_A_budget_e-1_to_e11_ppd60.npz` is an external source, not present in the original repository. Its published contribution is in the component CSVs. Source impedance data are not the original CST projects. The kicker model has a sharp effective cutoff near 10.239 GHz. The RW high-frequency input was extended to 10 THz for 0.4 mm wake calculation, but the total published impedance files only run to 50 GHz. Quadrupolar wakes are omitted.

All source data are preserved exactly, without interpolation or smoothing. The q calibration is a reference-plane convention, not a universal physical constant.

Codes: [IW2D](https://gitlab.cern.ch/IRIS/IW2D), [TLWallNew](https://github.com/ImpedanCEI/TLWallNew).
