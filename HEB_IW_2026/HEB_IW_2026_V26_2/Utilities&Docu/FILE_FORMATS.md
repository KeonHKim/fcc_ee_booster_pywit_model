# V26.2 file formats and use

- `Impedances/Total/*.txt`: whitespace-separated **GHz, signed Re(Z), signed Im(Z)**; Ω longitudinal and Ω/m transverse. The transverse totals are already beta-weighted.
- `Impedances/Devices/HEB_V26_2_all_component_budget_{long,dipx,dipy}.csv`: frequency_GHz followed by Re/Im for RW, Wiggler, Kicker, RF, BPM, Bellows, Total. These contributions are already ring normalized.
- `Wakes/Total/*.txt`: s [mm], finite 0.4 mm Gaussian bunch wake potential [V/pC] longitudinal or [V/pC/mm] transverse.
- `Wakes/Devices/HEB_V26_2_all_component_wakes_{long,dipx,dipy}_sigma0p4mm.csv`: s_mm, RW, Wiggler, Kicker, RF, BPM, Bellows, Total.
- `Wakes/Total/HEB_V26_2_sigma0p4mm_PyHEADTAIL.ecsv`: fields time, longitudinal, dipole_x, dipole_y. The time-axis physical unit is not explicitly declared in the archived header: verify separately.
- `Impedances/Devices/ResistiveWall`: original 50 GHz and high-frequency (to 10 THz) RW sources; `ExtractionKicker`: already length-scaled to 4.18 m.
- `Simulation_files/SourceImpedances`: unweighted RF/BPM source spectra and already integrated bellows source; consult the provenance file before any normalization.

Only plot displays may mask negative values on log scales. Data signs are never clipped or changed.
