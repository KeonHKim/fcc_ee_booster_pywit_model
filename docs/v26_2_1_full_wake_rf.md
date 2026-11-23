# FCC-ee HEB V26.2.1 ExtK20 full-wake RF budget

This update uses the complete transverse 3 mm CST bunch wake with four IDDEFIX resonators and no frequency taper. The finite model uses the 200.039 mm CST endpoint for comparison. The ring budget uses the fully decayed impedance and the fitted 0.4 mm bunch wake. The extrapolated transverse RF peak depends on the modeled tail beyond the CST record.

The longitudinal model uses HOM 1–3 from the corrected 100 m CST fit. The existing ExtK20 component tables supply the other impedance and wake terms, with the 150 nm NEG/Cu wall and 0.3 µm roughness, 20 extraction kicker modules, two damper striplines, wigglers, BPMs, and bellows.

## Run the notebooks

Open both notebooks from the repository and run all cells in this order.

1. [RF fits and per-cavity exports](../Example/FCC_ee_HEB_RF_IDDEFIX_Both_Planes_Full_Wake.ipynb). The longitudinal CST source and both 3 mm transverse CST files are in the package data. The normal CST wake supplies the budget. The filtered CST wake supplies a cross-check. The RF notebook uses IDDEFIX 0.3.0.
2. [Ring impedance budget and tracking wake](../Example/HEB_V26_2_ExtK20_Full_Wake_RF_Budget_and_Wake.ipynb). The notebook combines the generated RF files with the ExtK20 tables. It generates the component CSVs, signed ring totals, plots, and tracking ECSV.

## Read the budget and tracking input

The [case directory](../fcc_ee_booster_pywit_model/data/total/v26_2_HOMonly_Damper_N2_RF_IDDEFIXfullwakeCST_ExtK20) contains the signed 0–50 GHz ring spectra as gzip-compressed text, the 0.4 mm ring wakes, the loss and kick factors, and the tracking files. NumPy can read the spectra with numpy.loadtxt on the compressed paths. The spectra use GHz and Ω for the longitudinal plane or Ω/m for the dipole planes.

Use the [positive-loss ECSV](../fcc_ee_booster_pywit_model/data/total/v26_2_HOMonly_Damper_N2_RF_IDDEFIXfullwakeCST_ExtK20/HEB_v26_2_HOMonly_Damper_N2_RF_IDDEFIXfullwakeCST_ExtK20_sigma0p4mm_ds_cell_exp235_positive_loss.ecsv) as the Xwakes input at ds_cell_exp.235. The time column uses ns, the longitudinal column uses V/pC, and the dipole columns use V/(pC·mm). The workshop wake-only check gave a mean energy change of −6.02 MeV for 20 GeV, a 4 mm bunch, and a population of 1.2 × 10¹¹. The [export manifest](../fcc_ee_booster_pywit_model/data/total/v26_2_HOMonly_Damper_N2_RF_IDDEFIXfullwakeCST_ExtK20/HEB_v26_2_HOMonly_Damper_N2_RF_IDDEFIXfullwakeCST_ExtK20_EXPORT_MANIFEST.json) records the normalization and file checksums.

## Compare with the earlier budgets

At a 4 mm bunch length, the full-ring loss factor is 300.56 V/pC. The horizontal and vertical kick factors are 13.1047 and 13.0188 V/(pC·mm). The previous unfiltered-CST calculation used the same longitudinal RF fit. The new transverse model shifts the first RF-band peak to 1.227 GHz.

[Signed impedance comparison](../figures/v26_2_HOMonly_Damper_N2_RF_IDDEFIXfullwakeCST_ExtK20/FCCee_HEB_ExtK20_Total_Impedance_Comparison.png)
