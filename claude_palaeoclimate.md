# Palaeoclimate cluster (T40–T45) — change summary

Notes on a tidy/fix pass over the paleoclimate-cluster notebooks (**T40–T45**),
done with Claude. Everything below is committed on `main`. T42 was deliberately
left untouched (see *Known issues*).

## Shared infrastructure

- **`Notebooks/paleoclimate_helpers.py`** — new module with three display-only
  helpers used across the raster-map notebooks:
  - `close_lon_seam` — cyclically pads a −180→180 grid so `grdimage` reaches the
    ±180° seam (kills the grey wedge at the antimeridian).
  - `clamp_lat_poles` — extends the outermost latitude rows to ±90° before
    interpolation (no NaN slivers at the poles).
  - `refine_for_plot` — wraps the seam, clamps the poles, and bilinearly
    resamples a coarse GCM field onto a fine (0.5°) grid so the Mollweide rim is
    smooth instead of a staircase. **Display-only** — analysis still uses the
    native grids. It ends with `.transpose("lat","lon")` because pyGMT infers the
    plot region from dim order, and the intermediate steps can silently transpose.
  T40, T41, T43, T44 import from it (via a `sys.path` insert of `Notebooks/`).

- **Data rename** — `data/scion_permian/` → `data/plasim_genie_permian/`, and the
  three bundled files `scion_252Ma_*` → `plasim_genie_252Ma_*`. The bundle README
  was rewritten (correct model name, Holden 2016 citation, T43/T44 cross-refs, and
  a leaked local path removed).

- **`environment.yml`** — added `cmcrameri` + `openpyxl` (conda-forge) and
  `cgeniepy` (pip). `bayfox` (T42) omitted; pySCION (T45) is a separate clone, not
  a package.

## Model-naming correction (T40, T43, T44)

The bundled end-Permian climate fields were variously labelled "cGENIE-PLASIM"
and "SCION". They are **PLASIM-GENIE** runs (PLASIM atmosphere + GOLDSTEIN ocean;
the cGENIE biogeochemistry module was off), cited as Holden et al. (2016). All
three notebooks were renamed/relabelled accordingly, and their SCION references
were replaced. (T45 is genuinely pySCION-based, so SCION naming stays there.)

## Per-notebook changes

- **T40 — Deep-time snapshots.** Fixed the Mollweide rim/gridding artefacts
  (seam + high-latitude staircase); a transposed Gaussian-lat grid that had
  collapsed the deep-time map to a central blob; prose/code mismatches (palette
  clamps); `cGENIE`→`GENIE`→`PLASIM-GENIE`; `jet`→`vik` anomaly palette; removed
  SCION framing; reference fixes. Data caveat below.

- **T41 — cGENIE SST vs proxies.** Removed the unused/advertised `cgeniepy`
  dependency (loads the bundled netCDF with xarray); fixed the rim artefact via
  `refine_for_plot`; switched both panels to reconstructed 50 Ma coastlines
  (were modern); corrected a `viridis`→`thermal` mismatch; fixed a wrong bundled
  filename; stripped inline-URL clutter.

- **T43 — PLASIM-GENIE Permian SAT** *(renamed from `..._SCION_...`)*. SCION →
  PLASIM-GENIE throughout; fixed wrong plate-model labels (prose said
  Müller2022 / Zahirovic2022 for coastlines that are actually Merdith2021);
  `refine_for_plot` on the SAT + land-sea-mask panels.

- **T44 — CO₂-sensitivity ensemble** *(renamed from `..._SCION_...`)*. Fixed the
  SAT-map coastlines (were **modern** GSHHG on a 252 Ma map → now the model's own
  land-sea-mask contour); fixed a mangled "CO₂" title (Unicode subscript doesn't
  render in GMT); `refine_for_plot` rim fix; moved the spin-up / equilibrium
  check up to §2 (validate before analysing); **fixed a 64× normalization bug** —
  the bundled spin-up scalars were area-weighted but never divided by the number
  of longitudes, so GAST and |TOA thermal| were 64× too large. SCION →
  PLASIM-GENIE; broken version probe fixed.

- **T45 — pySCION Phanerozoic biogeochemistry.** Fixed a **years→Ma bug**:
  `age` came from `state.time` (in years), so every time-series x-axis read
  0–6×10⁸ "Ma" and, worse, SET 5's inflection lookup compared Ma against years —
  all three paleo-Earth maps stamped the same ~349 ppmv. After `/1e6` the run
  window reads "0–600 Ma" and the maps show age-correct pCO₂ (250 Ma → 8690,
  30 Ma → 336 ppmv). Also adapted to the current `amer7632/pySCION` API
  (`pySCION_initialise` now returns a `(run, interpstack, lipstack)` tuple), and
  set the reference to Merdith et al. (2025, *Science Advances*).

## Known issues / follow-ups

- **T42 (bayfox SST)** — left untouched. It won't run with `bayfox` installed:
  the code calls a non-existent `bayfox.predict_sst` (real API is
  `predict_seatemp`, returning a `Prediction`); `SPECIES="G_ruber"` is invalid
  and unused (valid code is `"G. ruber"` via `foram=`). The bundled CSV is now a
  planktonic WPWP (ODP 806) record, but the prose/Data-availability still describe
  the old LR04 benthic stack and `CORE_LON_LAT` points at the North Atlantic.

- **`data/paleoclimate/hadcm3_modern_mat.nc`** (T40 modern panel) is nearly
  zonal — no land-sea contrast and far too warm at the poles — i.e. not a
  faithful HadCM3 field. Left as-is; worth replacing at source.

- **`plasim_genie_252Ma_spinup.nc`** still stores the 64×-inflated GAST/thermal
  values at source; T44 divides by `n_lon` as a workaround.

- **pySCION** is not bundled: T45 needs a clone at `external/pySCION`
  (`https://github.com/amer7632/pySCION`, gitignored) plus `openpyxl`.
