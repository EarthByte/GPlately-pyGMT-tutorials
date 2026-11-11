# plasim_genie_permian — End-Permian (252 Ma) PLASIM-GENIE CO2-sensitivity ensemble

**Provenance:** model runs by Andrew Merdith with the SCION-coupled PLASIM-GENIE climate model (run MER25rev6, 1 August 2025), computed for the GPlately-pyGMT tutorials

Ten PLASIM-GENIE simulations at the 252 Ma paleogeography, one per atmospheric CO2 level (140, 280, 560, 1120, 2240, 3360, 4480, 8960, 17920 and 35840 ppm). PLASIM-GENIE couples the PLASIM atmosphere (T21, 64 × 32 grid) to the GOLDSTEIN ocean (Holden et al., 2016). The files keep the last model year (year 3000) of each run, the spin-up time series and the input bathymetry; the full model output (about 1.5 GB) is held by the model author.

## Contents

```
plasim_genie_permian/  (0.4 MB)
├── README.md
├── plasim_genie_252Ma_equilibrium.nc   year-3000 fields per CO2 level (co2_ppm 10 × latitude 32 × longitude 64):
│                                       SAT, surface_T, sea_ice_cover, sea_ice_thickness, snow_depth,
│                                       surface_albedo, landsea_mask, orography, top_thermal, top_solar
├── plasim_genie_252Ma_spinup.nc        energy-balance time series per CO2 level, years 100–3000 in 100-yr steps:
│                                       GAST, top_thermal_abs, top_solar_abs, min_seaice_lat
└── plasim_genie_252Ma_bathymetry.nc    GOLDSTEIN input bathymetry (identical for all CO2 levels)
```

## Consumer notebooks

**J05**

## References

Holden, P.B. et al. (2016). PLASIM-GENIE v1.0: a new intermediate complexity AOGCM. *Geoscientific Model Development* 9, 3347-3361. https://doi.org/10.5194/gmd-9-3347-2016

Mills, B.J.W., Donnadieu, Y. & Goddéris, Y. (2021). Spatial continuous integration of Phanerozoic global biogeochemistry and climate. *Gondwana Research* 100, 73-86. https://doi.org/10.1016/j.gr.2021.02.011 — the SCION model.

## License

CC BY 4.0.
