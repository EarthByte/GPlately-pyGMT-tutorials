# zenodo_data/ — the suite's external-data folder (manifest)

This folder does not ship on GitHub (it's gitignored — see `.gitignore`,
except for this README). It is the **one** place every not-bundled
dataset lands. Download the suite's companion Zenodo archive and extract
it here, so you end up with:

```
GPlately-pyGMT_tutorials/
├── Notebooks/
├── data/              (small, git-tracked datasets)
└── zenodo_data/        <- this folder, sibling of Notebooks/ and data/
    ├── README.md        (this file)
    ├── wu2023_zircons/
    ├── reveal_full_grid/
    ├── paleodem_scotese_wright_2018/
    ├── pySCION/
    ├── santosh_dynamic_topography/
    ├── young2022_dynamic_topo/
    ├── gmcm9/
    ├── paleo_elevation_zhou/
    ├── thermochronology_central_asia/   (precomputed caches only)
    ├── thermochronology_boone/
    ├── thermochronology_north_america/
    ├── basins_icons_heine/
    ├── sediment_thickness_bird_mooney/
    └── crustal_thickness_afonso/
```

Every notebook that needs one of these looks for it at
`zenodo_data/<slug>/` by default (resolved relative to the repo root —
notebooks already `chdir` there if launched from `Notebooks/`). Each
dataset also has a `ZENODO_<NAME>_DIR` environment-variable override for
users who keep the data somewhere else — see the notebook's own
configuration cell for the exact variable name.

**Note for the maintainer (Dietmar):** the "Currently at" column below
is where each dataset already sits on your machine as of this redesign.
For most of these, populating `zenodo_data/` is a `mv`/`cp`, not a
re-download — only two datasets (`wu2023_zircons` and the
`Reconstructions/For_gld504/*` files under `santosh_dynamic_topography`)
could not be located anywhere reachable from this session and genuinely
need sourcing before the archive can be assembled.

## Datasets

### wu2023_zircons
- **Used by:** T21, T22, T23, T24
- **Contents:** `zircons_sedimentary_Wu2023.gpmlz`,
  `zircons_igneous_Wu2023.gpmlz`, `zircons_metamorphic_Wu2023.gpmlz`
- **Source:** Wu et al. 2023 zircon compilation,
  https://zenodo.org/records/8303076 — **note:** T24's markdown citation
  cites a different DOI (`10.5281/zenodo.7795705`) for what appears to be
  the same dataset; this discrepancy hasn't been resolved, check both
  before assuming which is authoritative.
- **Currently at:** not found anywhere reachable from this session —
  needs sourcing from the Zenodo record above.
- **Env var:** none yet (T21-24 raise a clear `FileNotFoundError` naming
  the expected path if missing).

### reveal_full_grid
- **Used by:** T27
- **Contents:** `REVEAL.nc` (~394 MB, full-resolution 3-D tomography grid)
- **Source:** REVEAL global mantle tomography model.
- **Currently at:** `external/REVEAL_plume_tutorial/Models/REVEAL.nc` on
  your machine (a real file, not a symlink).
- **Env var:** `ZENODO_REVEAL_DIR` (default `zenodo_data/reveal_full_grid`)
- **Distinct from:** `data/reveal_tomography/` (already bundled, 7.8 MB,
  pre-sliced horizontal depth grids used by T26 — do not confuse the two).

### paleodem_scotese_wright_2018
- **Used by:** T47, T67, T51 (T51 uses the already-bundled 1-degree
  `data/paleotopo_scotese/` copy directly, not this one — see below)
- **Contents:** Scotese & Wright (2018) PaleoDEM grids, 1-degree
  resolution (no 6-arcmin version found locally).
- **Currently at:** `external/PaleoDEMs_Scotese_Wright_2018` and
  `external/PaleoDEMs_Scotese_Wright_2018_1deg` — both are symlinks to
  the same target, `~/Documents/Software/Paleotopo_data_assimilation/
  data/Scotese_Wright_2018_Maps_1-88_1degX1deg_PaleoDEMS_nc_v2`.
- **Env var:** `ZENODO_PALEODEM_DIR` (default
  `zenodo_data/paleodem_scotese_wright_2018`)
- **Note:** T51 instead reads the smaller, already git-bundled
  `data/paleotopo_scotese/corrected_SW/` (geochemistry-corrected variant,
  fully tracked in git) — that one needs no Zenodo download.

### pySCION
- **Used by:** T67
- **Contents:** pySCION standalone source.
- **Source:** Zenodo record 7940113 (upstream, third-party).
- **Currently at:** `external/pySCION` — a symlink to
  `~/Documents/Software/NeuroLEM/src/pySCION`.
- **Env var:** `ZENODO_PYSCION_DIR` (default `zenodo_data/pySCION`)

### santosh_dynamic_topography
- **Used by:** T28, T29, T30
- **Contents:** per-(continent, age) dynamic-topography `.nc` files
  (`DTvsSediment/<gld_id>/PlateFrameGrid_<CODE>/`), per-(age, depth)
  mantle-temperature `.grd` files (`Temperature_and_Velocity/
  Temperature/`), and 8 gld504 reconstruction files
  (`Reconstructions/For_gld504/*` + `Reconstructions/
  shapes_static_polygons_Merdith_et_al.gpml`).
- **Source:** Santosh Dhungana, *Dynamic Topography and Great
  Unconformity* — DOI `10.5281/zenodo.17773494` (upstream, third-party;
  the full repo is ~19 GB, we only need the ~570 MB subset above).
- **Currently at:** MOSTLY already at `data/mantle/` on your machine —
  `DTvsSediment/` (65 MB — note it has a confusing double-nested
  `DTvsSediment/DTvsSediment/{gld421,gld486,gld504}/` artifact that
  should be flattened before copying) and `Temperature_and_Velocity/
  Temperature/` (481 MB). The 8 `Reconstructions/For_gld504/*` files are
  NOT at `data/mantle/` — they're only in the full clone at
  `external/Dynamic-Topography-and-Great-Unconformity/Reconstructions/`.
- **Env var:** `ZENODO_SANTOSH_DIR` (default
  `zenodo_data/santosh_dynamic_topography`)

### young2022_dynamic_topo
- **Used by:** T31, T32, T51
- **Contents:** `plate_frame/20my_0-960Ma/`, `plate_frame/
  5my_0-250Ma/` (gld428), `plate_model/` (M21 NNR rotation + topology
  files).
- **Source:** Young et al. (2022, *EPSL* 584, 117451) — EarthByte webdav:
  https://www.earthbyte.org/webdav/ftp/Dynamic_Topography/gld428_m21/
- **Currently at:** already fully present at `data/Young2022_dynamic_topo/`
  on your machine (982 MB) — this one is a straight `mv`.
- **Env var:** `ZENODO_YOUNG2022_DIR` (default
  `zenodo_data/young2022_dynamic_topo`)

### gmcm9
- **Used by:** T48, T50
- **Contents:** `MantleFrame/`, `PlateFrame/` (31 NetCDFs each, 0-150 Ma,
  ~5-Myr cadence).
- **Source:** Braz et al. (2021) — EarthByte webdav:
  https://www.earthbyte.org/webdav/ftp/Dynamic_Topography/gmcm9/
- **Currently at:** already fully present at `data/gmcm9/` (124 MB) —
  straight `mv`.
- **Env var:** `ZENODO_GMCM9_DIR` (default `zenodo_data/gmcm9`)

### paleo_elevation_zhou
- **Used by:** T46
- **Contents:** `global_crustal_thickness_with_paleo_coords.csv` +
  supporting age-temperature CSVs.
- **Source:** Zhou et al. — geochemistry-corrected paleo-elevation.
- **Currently at:** already fully present at `data/paleo_elevation_zhou/`
  (24 MB) — straight `mv`.
- **Env var:** `ZENODO_PALEO_ELEV_ZHOU_DIR` (default
  `zenodo_data/paleo_elevation_zhou`)

### thermochronology_central_asia (Zenodo subfolder — caches only)
- **Used by:** T48 (writes), T49 (writes), T50 (reads); T47 reads the
  *bundled* CSVs at `data/thermochronology_central_asia/` directly (git
  -tracked, no Zenodo needed for T47).
- **Contents:** `thermochron_master/*.parquet` (written by T48),
  `kinematics_master/*.parquet` (written by T49) — precomputed per-age
  cache tables so T50 doesn't require re-running T48/T49 first.
- **Currently at:** already present at `data/thermochronology_central_asia/
  {thermochron_master,kinematics_master}/` (832 KB total) from a prior
  local run — straight `mv` of just those two subfolders (leave
  `central_asia_regions.csv` / `central_asia_thermal_histories.csv`
  where they are, in git).
- **Env var:** `ZENODO_THERMOCHRON_CA_DIR` (default
  `zenodo_data/thermochronology_central_asia`)
- **If missing:** T48/T49 rebuild these caches automatically on first run
  (a few minutes); they aren't a hard dependency, just a time-saver.

### thermochronology_boone
- **Used by:** T49
- **Contents:** `Southern_Margin_Polygons_V4/` (231 `.xy` files),
  `Faults/` (GEM Global Active Faults, pre-reconstructed), `AFEAD_Faults/
  AFEAD_v2022/` (regional supplement) — a subset of Sam Boone's larger
  ThermoPlates auxiliary bundle.
- **Source:** Boone, S.C., re-processed from AFEAD / GEM Foundation public
  sources.
- **Currently at:** the full ~10 GB collection is at `data/thermochronology/`
  on your machine (also has `HadCM3_paleoprecip/`, not used by any
  current notebook) — only copy the 3 subfolders above into
  `zenodo_data/thermochronology_boone/`, no need to ship the rest.
- **Env var:** `ZENODO_THERMOCHRON_BOONE_DIR` (default
  `zenodo_data/thermochronology_boone`)

### thermochronology_north_america
- **Used by:** T51
- **Contents:** `usgs_geochron_v4/` (raw USGS Geochron v4.0 CSVs),
  `na_thermal_histories.csv` (flat reduction), `dyntopo_master/`
  (precomputed per-age cache, same pattern as thermochronology_central_asia).
- **Source:** Hillenbrand et al. (2023, rev. 2025), USGS Geochron v4.0 —
  DOI 10.5066/P9RZNPIF (public domain).
- **Currently at:** already fully present at
  `data/thermochronology_north_america/` (37 MB) — straight `mv`.
- **Env var:** `ZENODO_THERMOCHRON_NA_DIR` (default
  `zenodo_data/thermochronology_north_america`)

### basins_icons_heine
- **Used by:** T53, T54, T55
- **Contents:** `BasinsMay2012.shp` (+ sidecar files), Heine (2007) ICONS
  Atlas, 870 basins.
- **Currently at:** already fully present at `data/basins_icons_heine/`
  (14 MB) — straight `mv`.
- **Env var:** `ZENODO_BASINS_ICONS_DIR` (default
  `zenodo_data/basins_icons_heine`)

### sediment_thickness_bird_mooney
- **Used by:** T53, T55
- **Contents:** `Bird_Mooney_GST14_WGS84.nc` (0.125° global sediment
  thickness).
- **Source:** Bird & Mooney (2026) GST-1.
- **Currently at:** already fully present at
  `data/sediment_thickness_bird_mooney/` (8.4 MB) — straight `mv`.
- **Env var:** `ZENODO_SEDTHICK_DIR` (default
  `zenodo_data/sediment_thickness_bird_mooney`)

### crustal_thickness_afonso
- **Used by:** T53, T54, T55
- **Contents:** `crustal-thickness-gmt-surface.nc` (0.25° global crustal
  thickness).
- **Source:** Afonso et al. (2019).
- **Currently at:** already fully present at
  `data/crustal_thickness_afonso/` (4.0 MB) — straight `mv`.
- **Env var:** `ZENODO_CRUSTTHICK_DIR` (default
  `zenodo_data/crustal_thickness_afonso`)

## Not part of this redesign

- **`data/pmm_cache/`** — `plate_model_manager`'s own download cache
  (rotation files, topologies, coastlines auto-fetched from EarthByte
  servers on first run of many notebooks). It's gitignored, but it's
  self-populating, not a Zenodo dependency — nothing to do here.
- **`data/Zahirovic2022_with_gpmdb_frame.rot`** (used by T33, T34, T42,
  T62) — only 2.8 MB. Recommendation: un-gitignore it (`.gitignore` line
  currently excludes `**/Zahirovic2022_with_gpmdb_frame.rot`) and commit
  it directly to the repo instead of routing it through Zenodo — small
  enough that git is simpler for everyone.

## Present locally but not read by any current notebook (orphaned)

These have READMEs under `data/` and real content on disk, but no
notebook in the suite currently references them. Flagging so they aren't
silently forgotten (or silently included) when the Zenodo archive is
assembled — decide per-dataset whether to include them for a future
notebook or drop them from the archive:

- `data/thermochronology_afro_arabia/` (22.5 MB) — Afro-Arabia
  thermochronology compilation, structured like the Boone Central Asia
  set.
- `data/thermochronology_andes_frontal/` (688.8 MB, its own README says
  "Zenodo-only") — Howlett (2025) + broader Andes-margin compilation.
- `data/paleogeography/` (`M2020-merge.gpml`) — not referenced by any
  notebook; every "paleogeography" hit in the codebase turned out to be
  prose, not a path.
- `data/paleobiogeography/` (`Version5p1_Cambrian_Ordovician_Cryptospores.xlsx`)
  — likewise, no notebook actually reads this file yet.
