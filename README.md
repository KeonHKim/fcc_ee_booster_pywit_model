# FCC-ee High Energy Booster impedance and wake model

| Data | Location |
| --- | --- |
| V26.2.1 ExtK20 full-wake RF update | [Fits, ring impedance and tracking wake](docs/v26_2_1_full_wake_rf.md) |
| V26.2.1 transverse IDDEFIX budget and tracking wake | [Total impedance and wakes](fcc_ee_booster_pywit_model/data/total/v26_2_HOMonly_Damper_N2_RF_IDDEFIXdipoles) |
| Earlier V26.2.1 longitudinal HOM-only RF and damper budget | [Original V26.2.1](fcc_ee_booster_pywit_model/data/total/v26_2_HOMonly_Damper_N2) |
| Six-component V26.2 baseline | [V26.2 totals](fcc_ee_booster_pywit_model/data/total/v26_2) · [Model assumptions](docs/v26_2_model.md) |
| RF cavity sources, fitted impedance and 0.4 mm RF wakes | [RF cavities](fcc_ee_booster_pywit_model/data/rf_cavities) |
| Extraction and damper kickers | [Kickers](fcc_ee_booster_pywit_model/data/kickers) |
| BPMs, bellows, resistive-wall data and optics | [Package data](fcc_ee_booster_pywit_model/data) |
| V26.2 plots and verification | [Plots](figures/v26_2) · [Plot example](Example/plot_v26_2_budget.py) · [Verification script](Example/verify_v26_2_release.py) |

Use the `Z_total_*` and `W_total_*` files for full-ring values. The component CSVs in the same folder contain the ring contributions of the individual families, including wiggler, RF, BPM and bellows. The signed impedance tables use GHz for frequency, Ω longitudinally and Ω/m transversely. The 0.4 mm wake tables use mm for distance, V/pC longitudinally and V/(pC mm) transversely. The V26.2.1 tracking ECSV uses ns for time. Transverse ring totals already include the lattice beta weighting.

The `4p18m` extraction files already include the HEB length scaling. The model separately accepts the original 20 m `Z_*_optimizedKicker.txt` files or `kicker_z_w.zip` and applies `4.18 / 20` when it loads them. The `stripkickers26` files are collider reference data. The case-tagged `Damper` files are the scaled HEB exports.

## Reproduce the V26.2.1 export

1. Run the [RF fit notebook](fcc_ee_booster_pywit_model/FCC_ee_HEB_RF_IDDEFIX_Option1_BUDGET_EXPORT_Transverse.ipynb) in the package directory with the editable PyWIT environment. It saves the longitudinal HOM-only and transverse RF inputs and their matched wakes.
2. Run the [budget notebook](Example/HEB_V26_2_IDDEFIX_HOMonly_Damper_PyWIT_Transverse.ipynb) in the same environment. `RF_TRANSVERSE_MODE = 'iddefix_fit'` selects the transverse fit. `cst_native` selects the original signed CST spectra and their native-grid wakes. Use the fit manifest for the residuals and fitted-mode provenance.

The PyWIT calculation also uses the local machine-layout helpers, the 20 m extraction input and an IW2D wiggler cache or executable. The precomputed totals can be read directly from this repository.

The [previous collider-style publication snapshot](https://github.com/KeonHKim/fcc_ee_booster_pywit_model/tree/ae9ba3c09c5c592ff5f33cbc06ad950cd55d8612/HEB_IW_2026/HEB_IW_2026_V26_2) records the original mirror layout and its checksums.
