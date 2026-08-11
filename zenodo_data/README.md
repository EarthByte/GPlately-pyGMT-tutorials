# zenodo_data/ — companion data archive for the GPlately × pyGMT tutorial suite

This folder holds every dataset used by the tutorial suite (80 Jupyter
notebooks in `Notebooks/`) that's too large, or licensed separately, to
bundle on GitHub. It does not ship in the git repo (gitignored except
this README) — download it from Zenodo instead:

**Zenodo DOI: [10.5281/zenodo.21836196](https://doi.org/10.5281/zenodo.21836196)**

## How to use this archive

Download the file(s) you need (see the table below — most notebooks only
need one dataset) and extract each into `zenodo_data/` at the repo root,
a sibling of `Notebooks/` and `data/`:

```
GPlately-pyGMT_tutorials/
├── Notebooks/
├── data/              (small, git-tracked datasets — no download needed)
└── zenodo_data/        <- extract each zip here
    ├── README.md
    ├── zircon_geochronology_Wu2023/
    ├── REVEAL_mantle_tomography/
    ├── paleoDEM_ScoteseWright2018/
    ├── pySCION_biogeochemistry_model/
    ├── dynamic_topography_Dhungana/
    ├── dynamic_topography_Young2022/
    ├── gmcm9_dynamic_topography_Braz/
    ├── paleo_elevation_Zhou/
    ├── thermochronology_precomputed_cache_CentralAsia/
    ├── thermochronology_faults_Boone/
    ├── thermochronology_geochronology_USGS_NorthAmerica/
    ├── sediment_thickness_BirdMooney/
    ├── crustal_thickness_Afonso/
    ├── foam_devonian_climatology_Pohl/
    ├── phansst_proxy_database_Judd2022/
    └── gateway_reconstruction_Straume2020/
```

Every folder name follows the same pattern — `<what it is>_<who made
it>` — so you can tell what a folder contains without opening this file.
Every notebook that needs one of these datasets looks for it at
`zenodo_data/<folder-name>/` by default, and also accepts a
`ZENODO_<NAME>_DIR` environment-variable override if you'd rather keep
the data somewhere else — see the notebook's own "Data availability"
cell and configuration cell for the exact variable name. If a notebook's
data isn't found, it fails fast with a clear `FileNotFoundError` naming
the expected path.

## Reference: every file in this archive

| Zip file | Extracts to | Size | Used by |
|---|---|---|---|
| `zircon_geochronology_Wu2023.zip` | `zircon_geochronology_Wu2023/` | 2.1 MB | T21, T22, T23, T24 |
| `REVEAL_mantle_tomography.zip` | `REVEAL_mantle_tomography/` | 225 MB | T27 |
| `paleoDEM_ScoteseWright2018.zip` | `paleoDEM_ScoteseWright2018/` | 4.1 MB | T47, T67, T69 |
| `pySCION_biogeochemistry_model.zip` | `pySCION_biogeochemistry_model/` | 12 MB | T67 |
| `dynamic_topography_Dhungana.zip` | `dynamic_topography_Dhungana/` | 449 MB | T28, T29, T30 |
| `dynamic_topography_Young2022.zip` | `dynamic_topography_Young2022/` | 193 MB | T31, T32, T51 |
| `gmcm9_dynamic_topography_Braz.zip` | `gmcm9_dynamic_topography_Braz/` | 129 MB | T48, T50 |
| `paleo_elevation_Zhou.zip` | `paleo_elevation_Zhou/` | 6.1 MB | T46 |
| `thermochronology_precomputed_cache_CentralAsia.zip` | `thermochronology_precomputed_cache_CentralAsia/` | 576 KB | T48, T49, T50 (optional time-saver) |
| `thermochronology_faults_Boone_core.zip` | `thermochronology_faults_Boone/` | 145 MB | T49 |
| `AFEAD_faults_Boone.zip` | `thermochronology_faults_Boone/` (same folder as above) | 1.8 GB | T49 |
| `thermochronology_geochronology_USGS_NorthAmerica.zip` | `thermochronology_geochronology_USGS_NorthAmerica/` | 192 KB | T51 |
| `sediment_thickness_BirdMooney.zip` | `sediment_thickness_BirdMooney/` | 9.1 MB | T53, T55 |
| `crustal_thickness_Afonso.zip` | `crustal_thickness_Afonso/` | 3.1 MB | T53, T54, T55 |
| `foam_devonian_climatology_Pohl.zip` | `foam_devonian_climatology_Pohl/` | 578 MB | T69 |
| `phansst_proxy_database_Judd2022.zip` | `phansst_proxy_database_Judd2022/` | 41 MB | T70 |
| `gateway_reconstruction_Straume2020.zip` | `gateway_reconstruction_Straume2020/` | 241 MB | T71 |

`thermochronology_faults_Boone` is the one dataset split across two zip
files (both required by T49) — extract both into the same
`zenodo_data/thermochronology_faults_Boone/` folder.

## Dataset details

### zircon_geochronology_Wu2023
- **Used by:** T21, T22, T23, T24
- **Contents:** `zircons_sedimentary_Wu2023.gpmlz`,
  `zircons_igneous_Wu2023.gpmlz`, `zircons_metamorphic_Wu2023.gpmlz`
- **Source:** Wu, Y., Fang, X. & Ji, J. (2023). A global zircon U–Th–Pb
  geochronological database. *Earth System Science Data* 15(11),
  5171–5181. https://doi.org/10.5194/essd-15-5171-2023 — data archived
  at https://doi.org/10.5281/zenodo.7387566

### REVEAL_mantle_tomography
- **Used by:** T27
- **Contents:** `REVEAL.nc` — full-resolution 3-D global mantle
  tomography grid.
- **Source:** REVEAL global mantle tomography model.
- **Distinct from:** `data/reveal_tomography/` (already bundled in git,
  7.8 MB, pre-sliced horizontal depth grids used by T26 — a different,
  smaller product from the same model; do not confuse the two).

### paleoDEM_ScoteseWright2018
- **Used by:** T47, T67, T69 (T51 instead uses the smaller, already
  git-bundled `data/paleotopo_scotese/corrected_SW/` — no download
  needed for T51)
- **Contents:** all 109 Scotese & Wright (2018) PaleoDEM `.nc` grids,
  1-degree resolution, full 0–540 Ma, single `z` variable (elevation, m;
  negative = submerged), already in the paleo (reconstructed) reference
  frame. T69 uses just the two grids at 420 Ma and 360 Ma.
- **Source:** Scotese, C.R. & Wright, N.M. (2018). PaleoDEM resource.
  https://www.earthbyte.org/paleodem-resource-scotese-and-wright-2018/.
  Archived at https://doi.org/10.5281/zenodo.5460860

### pySCION_biogeochemistry_model
- **Used by:** T67
- **Contents:** a minimal runnable subset of Mills & Gurung's pySCION
  Earth-evolution model — the 5 Python modules T67 actually imports and
  runs, plus the forcing-data files they read (21 MB total, vs. ~103 MB
  for the full upstream checkout, which also includes an unused
  reconstruction-model cache and unused data files).
- **Source:** Mills, B.J.W. & Gurung, K. — pySCION.
  https://doi.org/10.5281/zenodo.7940113 · https://github.com/bjwmills/pySCION

### dynamic_topography_Dhungana
- **Used by:** T28, T29, T30
- **Contents:** per-(continent, age) dynamic-topography grids
  (`DTvsSediment/`), per-(age, depth) mantle-temperature grids
  (`Temperature_and_Velocity/`), and supporting reconstruction files
  (`Reconstructions/`).
- **Source:** Dhungana, S. & Flament, N. — *Dynamic Topography and
  Great Unconformity*. https://doi.org/10.5281/zenodo.17773494

### dynamic_topography_Young2022
- **Used by:** T31, T32, T51
- **Contents:** `plate_frame/` dynamic-topography grids (two age
  cadences) and `plate_model/` (M21 NNR rotation + topology files).
- **Source:** Young, A. et al. (2022). *Earth and Planetary Science
  Letters* 584, 117451.

### gmcm9_dynamic_topography_Braz
- **Used by:** T48, T50
- **Contents:** `MantleFrame/`, `PlateFrame/` mantle-flow
  dynamic-topography grids, 0–150 Ma at ~5-Myr cadence.
- **Source:** Braz, C. et al. (2021) — EarthByte dynamic-topography
  archive ("gmcm9" model run).

### paleo_elevation_Zhou
- **Used by:** T46
- **Contents:** geochemistry-corrected paleo-elevation compilation
  (`global_crustal_thickness_with_paleo_coords.csv` + supporting
  age-temperature CSVs).
- **Source:** Zhou et al. — geochemistry-corrected paleo-elevation.

### thermochronology_precomputed_cache_CentralAsia
- **Used by:** T48 (writes), T49 (writes), T50 (reads) — an optional
  time-saver, not a hard dependency: T48/T49 rebuild these caches
  automatically on first run (a few minutes) if this folder is absent.
  T47 does not need this download; it reads the smaller, already
  git-bundled CSVs at `data/thermochronology_central_asia/` directly.
- **Contents:** `thermochron_master/*.parquet` (written by T48),
  `kinematics_master/*.parquet` (written by T49) — precomputed per-age
  cache tables.

### thermochronology_faults_Boone (two zips, one folder)
- **Used by:** T49
- **Contents:** `Southern_Margin_Polygons_V4/` (Boone's per-age Eurasian
  margin polygon), `Faults/` (GEM Global Active Faults Database,
  pre-reconstructed), `AFEAD_Faults/AFEAD_v2022/` (Active Faults of
  Eurasia Database, a regional supplement, pre-reconstructed).
- **Source:** Boone, S.C. et al. (2025). *Communications Earth &
  Environment* 6, 1015. https://doi.org/10.1038/s43247-025-03005-6 —
  re-processed from AFEAD / GEM Foundation public sources.

### thermochronology_geochronology_USGS_NorthAmerica
- **Used by:** T51
- **Contents:** `dyntopo_master/` — precomputed per-age
  dynamic-topography cache (same pattern as the Central Asia cache
  above). The raw USGS Geochron CSVs and flat thermal-history reduction
  this dataset is named for are small enough to ship directly in the
  git repo at `data/thermochronology_north_america/` — no download
  needed for those.
- **Source:** Hillenbrand et al. (2023, rev. 2025), USGS Geochron v4.0
  — DOI 10.5066/P9RZNPIF (public domain).

### sediment_thickness_BirdMooney
- **Used by:** T53, T55
- **Contents:** `Bird_Mooney_GST14_WGS84.nc` — 0.125° global sediment
  thickness.
- **Source:** Bird & Mooney (2026) GST-1.

### crustal_thickness_Afonso
- **Used by:** T53, T54, T55
- **Contents:** `crustal-thickness-gmt-surface.nc` — 0.25° global
  crustal thickness.
- **Source:** Afonso et al. (2019).

### foam_devonian_climatology_Pohl
- **Used by:** T69
- **Contents:** 8 NetCDF files, `{360,380,400,420}rd_1368W_EccN_{atmos,ocean}_2240ppm.nc`
  — FOAM GCM Devonian climatology at 420 Ma and 360 Ma. Atmosphere files
  include `TS1` (K, surface air temperature), `T`/`U`/`V`/`Z3`
  (time=12, lev=18, lat=40, lon=48). Ocean files include `TEMP` (°C, sea
  surface temperature), `S`/`U`/`V`/`W` (time=12, lev=24, lat=128, lon=128;
  `lev` is depth in metres, index -1 = shallowest). Subset of a much larger
  archive (102 files, 4.9 GB, full 0-540 Ma coverage at 20 Myr steps) — only
  the 8 files at 360/380/400/420 Ma are bundled here.
- **Source:** Pohl, A. (2021). *Phanerozoic global climatic fields simulated
  using the FOAM ocean-atmosphere general circulation model* [Data set].
  Zenodo. https://doi.org/10.5281/zenodo.5780097, CC BY 4.0. This is the
  literal upstream boundary-condition input to the cGENIE Devonian/
  Carboniferous ocean-oxygenation config family (Pohl et al. 2022, *Nature*
  608, 523-527, https://doi.org/10.1038/s41586-022-05018-z).
- **To obtain locally:** download the 8 files named above from
  https://zenodo.org/records/5780097 and place them directly in this
  folder — each individual file is available for direct download from the
  record page (no need to fetch the full 4.9 GB archive). Too large to
  transfer via the device bridge's per-file cap (files up to 124 MB each).

### phansst_proxy_database_Judd2022
- **Used by:** T70
- **Contents:** `PhanSST_v001.csv` (150,691 rows, 55 columns, 1,241 unique
  site names, full Phanerozoic 540 Ma-present) + `PhanSST_ReadMe.md`.
- **Source:** Judd, E.J., Tierney, J.E. et al. (2022). The PhanSST global
  database of Phanerozoic sea surface temperature proxy data. *Scientific
  Data* 9, 753. https://doi.org/10.1038/s41597-022-01826-0. The exact
  `PhanSST_v001.csv` used here ships inside the author's GitHub repo
  (https://github.com/EJJudd/PhanSST) and its Zenodo snapshot, v0.0.1-beta,
  https://doi.org/10.5281/zenodo.7275402 (concept DOI, always resolves to
  the latest archived version: https://doi.org/10.5281/zenodo.7049233), CC
  BY 4.0.

### gateway_reconstruction_Straume2020
- **Used by:** T71
- **Contents:** 15 NetCDF files, `paleobathy-topo_{1,5,10,15,20,25,30,34,
  35,40,45,50,55,60,65}.00Ma_Straume_et_al.nc`, each a single `z` variable
  (paleobathymetry/topography, m; negative = below sea level) on a 0.1°
  global grid (lat: 1801, lon: 3601), already expressed in the paleo
  (reconstructed) reference frame.
- **Source:** Straume, E.O., Gaina, C., Medvedev, S. et al. (2020). Global
  Cenozoic paleobathymetry with a focus on the Northern Hemisphere oceanic
  gateways. *Global and Planetary Change* 194, 103297.
  https://doi.org/10.1016/j.gloplacha.2020.103297. Data (v2.0) archived at
  https://doi.org/10.5281/zenodo.4193576, CC BY 4.0.

**Note on basin polygons (T53/T54/T55):** these three notebooks also load
a global basin-polygon shapefile, but it is NOT part of this Zenodo
archive — it's `data/evenick_2021_basins/` (Evenick 2021, CC BY-NC-ND
4.0), small enough to ship directly in the git repo. See
`data/evenick_2021_basins/README.md`. (An earlier version of this
archive staged a Heine/ICONS Atlas basin shapefile here; it was dropped
because its redistribution rights could not be verified — see
`CHANGELOG.md` in the main repo.)
