# FCC-ee High Energy Booster impedance and wake model — V26.2

This is a **collider-style publication layout** of precomputed V26.2 model outputs, not a new impedance calculation.

| Need | Folder |
|---|---|
| **Recommended full-ring impedances** | `Impedances/Total/` |
| **Precomputed per-device contributions** | `Impedances/Devices/` |
| **Recommended Gaussian 0.4 mm bunch wakes** | `Wakes/Total/` |
| **Component-resolved 0.4 mm wake potentials** | `Wakes/Devices/` |
| Original plots | `Plots/` |
| Optics and source impedance inputs | `Simulation_files/` |
| Assumptions, provenance and examples | `Utilities&Docu/` |

## Recommended total impedance files

* `Impedances/Total/Z_total_long_v26_2.txt` — longitudinal Ω.
* `Impedances/Total/Z_total_dipx_beta_weighted_v26_2.txt` — horizontal dipolar Ω/m.
* `Impedances/Total/Z_total_dipy_beta_weighted_v26_2.txt` — vertical dipolar Ω/m.

Three columns: frequency **GHz**, **signed** Re(Z), **signed** Im(Z). Transverse impedances are already beta weighted. Source range: **0–50 GHz**. Never multiply ring totals by number of devices a second time.

## Recommended Gaussian-bunch wake potentials

* `Wakes/Total/W_total_long_sigma0p4mm_v26_2.txt` — s (mm), potential (V/pC).
* `Wakes/Total/W_total_dipx_beta_weighted_sigma0p4mm_v26_2.txt` — s (mm), potential (V/pC/mm).
* `Wakes/Total/W_total_dipy_beta_weighted_sigma0p4mm_v26_2.txt` — s (mm), potential (V/pC/mm).
* `Wakes/Total/HEB_V26_2_sigma0p4mm_PyHEADTAIL.ecsv` — tracking-oriented combined export; verify the unit of its time coordinate in the consuming tracking code, since its ECSV header does not explicitly declare it.

**These are finite 0.4 mm Gaussian-bunch wake potentials, not point-charge wakes.**

## Model inventory

Six existing sources: resistive wall (Cu / 150 nm NEG, Rq = 0.3 µm), 112 RF cavities, 2740 BPMs, 10000 bellows, 10 damping wigglers, and 10 extraction magnetic kicker modules. RW radius 30 mm; length ≈ 89,080.356 m; the extraction kicker is provisionally modeled as 4.18 m scaled once from the main-ring reference (0.209). NEG presence, wiggler position/beta matching, and kicker installation remain design assumptions.

For the 0.4 mm wakes, the resistive-wall source was computed to **10 THz**, whereas the displayed total spectra stop at 50 GHz. The kicker source becomes zero beyond approximately **10.239 GHz** in the released input and should not be extrapolated as a physical high-frequency prediction.

The external wiggler source NPZ is not in the original published repository, but its calculated ring contribution is contained in the per-device tables. Original CST project files are not published in this repository. The source model omits quadrupolar wakes and some planned HEB devices.

## Quick validation and plotting

From the repository root, with NumPy installed:

```bash
python 'HEB_IW_2026/HEB_IW_2026_V26_2/Utilities&Docu/verify_release.py'
```

With Matplotlib installed:

```bash
python 'HEB_IW_2026/HEB_IW_2026_V26_2/Utilities&Docu/plot_example.py'
```

See the documentation in `Utilities&Docu/`. All copied numerical files have SHA-256 checksums in `Utilities&Docu/COPY_CHECKSUMS.json`. No source values are altered or reprocessed.
