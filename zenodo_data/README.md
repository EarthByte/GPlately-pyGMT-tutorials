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
    └── crustal_thickness_Afonso/
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
| `paleoDEM_ScoteseWright2018.zip` | `paleoDEM_ScoteseWright2018/` | 4.1 MB | T47, T67 |
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
- **Used by:** T47, T67 (T51 instead uses the smaller, already
  git-bundled `data/paleotopo_scotese/corrected_SW/` — no download
  needed for T51)
- **Contents:** all 109 Scotese & Wright (2018) PaleoDEM `.nc` grids,
  1-degree resolution, full 0–540 Ma.
- **Source:** Scotese, C.R. & Wright, N.M. (2018). PaleoDEM resource.
  https://www.earthbyte.org/paleodem-resource-scotese-and-wright-2018/

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

**Note on basin polygons (T53/T54/T55):** these three notebooks also load
a global basin-polygon shapefile, but it is NOT part of this Zenodo
archive — it's `data/evenick_2021_basins/` (Evenick 2021, CC BY-NC-ND
4.0), small enough to ship directly in the git repo. See
`data/evenick_2021_basins/README.md`. (An earlier version of this
archive staged a Heine/ICONS Atlas basin shapefile here; it was dropped
because its redistribution rights could not be verified — see
`CHANGELOG.md` in the main repo.)
