# cgenie_kpg_ying2026 — cGENIE K-Pg boundary ocean biogeochemistry + plankton ecosystem (Ying et al. 2026)

**Provenance:** derived from Ying, R. (2026). *cGENIE model outputs for KPG study* [Data set]. Zenodo. https://doi.org/10.5281/zenodo.17742290 — supplementary model output for Ying, R., Monteiro, F. M., Witts, J. D. & Schmidt, D. N. (2026), "Darkness and body size shaped end-Cretaceous marine extinction patterns," *Nature* 655, 957-962, https://doi.org/10.1038/s41586-026-10541-4. (An earlier round of this suite's documentation cited DOI 10.5281/zenodo.18700674 for this dataset; that was an error — 10.5281/zenodo.17742290 is the DOI the published paper's own Data Availability statement gives, and is used throughout this repository as of 2026-08-11.)

The full archive (~927 MB across 9 experiment directories) is a set of cGENIE Earth System Model (`derpycode/cgenie.muffin`) transient simulations of the Cretaceous-Paleogene (K-Pg, ~66 Ma) boundary mass extinction: a 10 kyr late-Maastrichtian spinup, a 100-year "impact winter" crisis experiment (combined solar dimming + CO2 forcing + dust/iron deposition), a 5 kyr Danian recovery continuation, and several single-mechanism sensitivity experiments (solar-only, CO2-only, no size-dependent export, no extinction).

This folder bundles a **small, derived subset** of that archive — global-mean time series, a handful of full-grid spatial snapshots at key moments (pre-impact baseline, immediately post-impact, end of the 100-yr crisis, Danian recovery), and per-plankton-functional-type (PFT) biomass summaries — computed by aggregating/subsetting the original NetCDF output. Consumers: T69, T70, T71.

## Contents

```
cgenie_kpg_ying2026/  (1.1 MB)
kpg_biogeochem_snapshots.nc (700 KB) — ocean biogeochemistry (BioGeM) spatial snapshots: ocn_sur_temp,
    misc_pH, carb_sur_ohm_cal, carb_sur_ohm_arg, bio_fexport_POC, phys_fxsw, ocn_sur_PO4, plus
    grid_mask/grid_area/grid_topo, on the model's native 36x36 late-Maastrichtian paleogeography grid.
    Dim `exp` indexes 34 (experiment, time) combinations: SPIN_baseline, main_t*.* (18 slices spanning
    the 100-yr crisis), danian_t*.* (12 slices spanning the 5 kyr recovery), and one peak-crisis snapshot
    each from the solar-only / CO2-only / no-extinction sensitivity runs.
kpg_ecogem_size_maps.nc (49 KB) — plankton ecosystem (EcoGeM) mean-cell-size + total biomass/chlorophyll
    fields at "baseline" (pre-impact) vs "post_impact" (end of crisis), main experiment.
kpg_global_timeseries.csv (320 KB) — global-mean time series (ocean temperature, surface pH, POC export,
    O2, alkalinity) for all 7 downloaded experiments, at native model output cadence.
kpg_pft_biomass_baseline_vs_post.csv (22 KB) — area-weighted global-mean biomass for each of 112 plankton
    functional types (PFTs), baseline vs post-impact, for the `main` and `size_effect` experiments.
kpg_pft_traits.csv (18 KB) — the 112-PFT trait table (cell diameter, cell volume, phytoplankton/zooplankton
    type, nutrient half-saturation constants, etc.) from `ecogem/Plankton_params.txt`.
```

## How this was derived

Downloaded 7 of the 9 experiment zips from the Zenodo record above (`SPIN`, `main`, `Danian`, `solar`, `CO2`, `size_effect`, `noextinction` — omitted `forcePAR` and `forceSST`, which decouple light/temperature effects on plankton but aren't used by any of T69-T71). For each, loaded `biogem/fields_biogem_2d.nc` and `ecogem/fields_ecogem_2d.nc` with `xarray`, selected the variables and time slices listed above, and wrote the result back out as compact NetCDF (zlib-compressed). Global-mean time series were parsed directly from the archive's `biogem/biogem_series_*.res` ASCII files. PFT biomass was computed as the grid-area-weighted mean of each `eco2D_Plankton_C_NNN` field. No values were altered — this is a subsetting/repackaging of the original model output, not a reanalysis.

**Why subset rather than bundle the full archive**: the full 927 MB (9 experiments x full 3-D fields at every saved time step) is far more than T69-T71 need — each notebook uses a handful of full-grid 2-D snapshots plus global-mean time series. Subsetting keeps this small enough to git-track directly, the same convention used for `data/plasim_genie_permian/` (T66) and `data/evenick_2021_basins/` (T53-T55). For the full archive (3-D fields, restart files, sediment/weathering output, per-experiment config namelists), see the Zenodo DOI above.

## Consumer notebooks

**T69**, **T70**, **T71**

## References

Ying, R., Monteiro, F. M., Witts, J. D. & Schmidt, D. N. (2026). Darkness and body size shaped end-Cretaceous marine extinction patterns. *Nature* 655, 957-962. https://doi.org/10.1038/s41586-026-10541-4 (Open Access, CC BY 4.0). Data: https://doi.org/10.5281/zenodo.17742290

Ying, R. (2024). cgeniepy: A Python package for analysing cGENIE Earth System Model output. *Journal of Open Source Software* 9(101), 6762. https://doi.org/10.21105/joss.06762

Ward, B.A., Wilson, J.D., Death, R.M., Monteiro, F.M., Yool, A. & Ridgwell, A. (2018). EcoGEnIE 1.0: plankton ecology in the cGEnIE Earth system model. *Geoscientific Model Development* 11, 4241-4267. https://doi.org/10.5194/gmd-11-4241-2018 — the EcoGeM plankton ecosystem module used to generate the `ecogem/` output.

Ridgwell, A., et al. cGENIE.muffin Earth system model. https://github.com/derpycode/cgenie.muffin. Model configuration branch for this study: https://github.com/ruiying-ocean/cgenie.muffin/tree/rui_kpg

Analysis code repository (for full reproducibility of the original study): https://github.com/ruiying-ocean/kpg_selectivity

## License

**CC BY 4.0** (per the Zenodo record). Derived/subsetted here from the original NetCDF and ASCII output; attribution to Ying et al. (2026) as above.
