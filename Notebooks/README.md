# GPlately × pyGMT tutorials

A growing collection of Jupyter notebooks that demonstrate how to combine
[GPlately](https://github.com/GPlates/gplately) (plate reconstructions) with
[pyGMT](https://www.pygmt.org/) (publication-quality maps, charts, and
scientific plots).

## How to find what you want

Notebooks are filename-prefixed with a stable T-number (`T01_…`, `T02_…`, …) and
a short topical slug. The full, always-current list is just the directory
listing — browse it on
[GitHub](https://github.com/EarthByte/GPlately-pyGMT-tutorials/tree/main/Notebooks)
or in JupyterLab's file sidebar. Each filename's slug is descriptive enough to
hint at the topic without a separate index.

T-numbers are clustered by theme — see *Themes* below — but they don't reset
between clusters: as the suite grows, new notebooks pick up the next free
T-number rather than slotting into the middle of an existing cluster. A
follow-up paragraph in the relevant cluster description below tells you which
T-number ranges sit in which cluster at the time of writing; if you need exact
mapping, the cluster header in each notebook's *first markdown cell* is the
authoritative source (it says e.g. *"Cluster F: paleo-geography + paleo-
topography"*).

## Conventions

Every notebook in this folder follows the same conventions:

1. **Executed outputs preserved.** Notebooks are re-run before commit so the
   embedded figures are visible when the file is opened on GitHub. A newcomer
   should be able to see what each notebook produces without installing
   anything. Animation cells that embed HTML5 video previews may still be
   stripped — the saved MP4 lives on disk under `videos/` (gitignored). If an
   individual notebook grows past ~5 MB it goes onto Git LFS via
   `.gitattributes`.
2. **Self-contained.** Each notebook prints library versions in cell 1,
   downloads any required plate-model data on first run via
   `plate_model_manager`, and produces at least one figure.
3. **Three-section header.** Title + one-paragraph motivation, learning
   objectives, prerequisites/runtime.
4. **CONFIGURATION block.** A `# === USER CONFIGURATION ===` cell immediately
   after the imports surfaces model name, snapshot time, region, anchor plate,
   and any other user-tunable knob as named constants. **This is where you
   look first if you want to change behaviour without editing the rest of the
   notebook.**
5. **In-frame `{time} Ma` stamp.** Every pyGMT figure draws a
   `fig.text(... position="TL" ...)` stamp as the *last* layer so it sits on
   top of all coast/grdimage layers.
6. **Closing "Extend this" section.** Suggestions for follow-up
   modifications.

## Recommended environment

```bash
conda create -n gplately-pygmt -c conda-forge gplately pygmt jupyter
conda activate gplately-pygmt
jupyter lab
```

(GPlately's docker image works too: `gplates/gplately`.)

## External data dependencies

Most notebooks fetch everything they need at run-time — plate models via
`plate_model_manager`, fossil occurrences via the Paleobiology Database /
Macrostrat APIs, plate-tectonic information via the GPlates Web Service,
etc. — so cloning this repo and `conda`-installing the environment above is
enough to run them.

A small number of notebooks pull in larger companion datasets (mantle-
convection NetCDFs, paleotopography assimilations, the pySCION repository, …)
that are too large or licensed separately to bundle here. These all live in
**one place**: download the suite's companion Zenodo archive and extract it
as `zenodo_data/` at the repo root, a sibling of `Notebooks/` and `data/`:

```
GPlately-pyGMT_tutorials/
├── Notebooks/
├── data/          (small, git-tracked datasets — nothing to do here)
└── zenodo_data/    (download + extract the Zenodo archive here)
    ├── README.md    (manifest: every dataset, what's in it, which
    │                 notebooks need it, and source citation)
    ├── gmcm9_dynamic_topography_Braz/
    ├── dynamic_topography_Dhungana/
    └── ...
```

Every dataset folder is named `<content-type>_<source>` so it's clear
what it is without opening the manifest. See **`zenodo_data/README.md`**
for the full reference table (every dataset, exact expected layout, and
source citation). Each such notebook also spells out its requirements
in its first markdown cell ("Data availability") and its
`# === USER CONFIGURATION ===` cell, which carries a default path under
`zenodo_data/<dataset-name>/` plus a `ZENODO_<NAME>_DIR`
environment-variable override for anyone who keeps the data somewhere
else. `zenodo_data/` is gitignored (except its own README) and never
pushed — download the archive once, extract it there, and every
notebook that needs external data finds it automatically.

If a notebook's data isn't found, it fails fast with a clear `FileNotFoundError`
that names the expected path and env-var override.

(A handful of small, single-file datasets — e.g. `Zahirovic2022_with_gpmdb_frame.rot`,
2.8 MB — are committed straight to the repo under `data/` instead of going
through Zenodo, since they're small enough that git is simpler for everyone.)

## Recommended starting points for newcomers / undergraduates

If you're new to plate reconstructions in Python, a good entry sequence is:

- **T01 — Hello, deep time.** Your first pyGMT paleo-map; introduces the
  GPlately + pyGMT plumbing.
- **T02 — GPlates Web Service from Python.** Pure HTTP-REST workflow: reconstruct
  modern-city paleo-positions through deep time using nothing more than
  `requests` + `pygmt`. Doesn't require a local `pygplates` install, which makes
  it the lowest-barrier entry point in the suite — excellent for a teaching lab
  where install friction is the bottleneck.
- **T03 — Projection cookbook.** The cartographic foundation the rest of the
  suite leans on.
- **T04 — Plate model comparison** and **T05 — Comparing rotation models**, once
  T01-T03 are comfortable — these show how to reason about model choice
  rather than treat any one model as ground truth.
- **T10 — Paleobathymetry profile across the Atlantic at 50 Ma** as the first
  application notebook that turns the workflow into a concrete cross-section.

## Themes

The suite is organised into **11 thematic clusters, A-K**, fully contiguous as
of the **2026-07-30 T63 addition** (which folded in Ehsan Farahbakhsh's kinematic-
feature-extraction notebook as T15, cluster B, on 2026-07-27; moved T72
"Carbonate-platform arc degassing" from cluster K into cluster J on 2026-07-28,
since it is a paleoclimate-forcing notebook rather than a mineral-prospectivity
one; moved T16 "Subducted-slab flux inventory" from cluster E into cluster
B on 2026-07-29, directly after T15, since it is a per-trench kinematic-flux
notebook rather than a mantle-dynamics one; then added T63 "Reconstructing
plant-fossil occurrences and Early Triassic super-greenhouse climate" -- a
community contribution from Zhen Xu and Benjamin J.W. Mills -- to cluster J
directly after T62 on 2026-07-30, the last notebook added before paper
submission). Each cluster has its own opening
sentence below with its current T-number range. Re-read the cluster header
inside each notebook for the authoritative cluster assignment.

- **Cluster A — Getting started + core workflows (T01-T07).** First paleo-maps,
  projection choices, model-comparison patterns, animations, interactive Panel
  views.
- **Cluster B — Plate kinematics + tectonics (T08-T16).** Plate-tectonic
  diagnostics, age-of-subducting-crust, paleo-bathymetry profiles, strain-rate
  maps, lithospheric-thickness retrodeformation, paleo-stress along
  subduction zones, rift obliquity, kinematic feature extraction at
  subduction zones through time (T15) — convergence rate/obliquity, trench
  velocity, and derived slab-flux proxies on an interactive map — and (T16)
  subducted-slab flux inventory: a deep-time budget of subducted slab volume,
  sediment, carbonate, and water mass.
- **Cluster C — Plate-model debugging (T17-T20).** Divergence/convergence sign
  anomalies at plate boundaries, MOR velocity-magnitude anomalies, topology
  construction anomalies (gaps/overlaps/non-unique sections), subduction-zone
  feature-extractability diagnostics.
- **Cluster D — Zircons + tectonic-setting predictors (T21-T25).** Detrital /
  igneous / metamorphic zircons reconstructed through deep time, paleo-distance
  to the nearest subduction zone as a tectonic-setting predictor, Hf-Nd
  isotope terrane mapping.
- **Cluster E — Mantle dynamics + dynamic topography (T26-T32).** REVEAL
  tomography overlain with reconstructed plate boundaries, deep-time mantle
  transects, clustering of plate-frame dynamic-topography histories,
  dynamic-topography vs sediment flux, dynamic-topography change rate through
  deep time, and the mantle-to-plate frame conversion walkthrough.
- **Cluster F — Paleomagnetism (T33-T43).** Building a paleomagnetic reference
  frame from GPMDB, comparing alternative reference frames, plate-mantle
  reference-frame uncertainty, continent rotation with GPlately, predicted vs
  observed paleomagnetic directions, single-key-pole case studies, full
  Phanerozoic apparent polar wander, inclination-shallowing corrections, pole
  rotation utilities, true polar wander decomposition, paleolatitude via
  reverse reconstruction.
- **Cluster G — Paleo-geography + paleo-topography (T44-T52).**
  Geochemistry-corrected paleo-elevation, Macrostrat sedimentary units in
  paleo-position, highland-footprint detection in deep time, ophiolite
  emplacement, and the full ThermoPlates suite of thermochronology-on-paleo-Earth
  workflows (cooling rates on Earth-system overlays, against plate kinematics
  and fault databases, and as correlation/time-series analyses).
- **Cluster H — Sedimentary basins (T53-T55).** Evenick (2021) global
  sedimentary-basin compilation: basin inventory + thickness + paleogeographic
  reconstruction, crustal stretching factor (β), individual rift-basin
  syn-rift/post-rift analysis.
- **Cluster I — Paleo-biogeography (T56-T61).** Paleobiology Database ×
  Macrostrat joins in paleo-coordinates, fossil corals through deep time, Late
  Jurassic dinosaur distributions on a reconstructed climate, Cenozoic
  planktonic foraminifera on reconstructed paleo-latitude, PBDB
  paleobiogeography live-API workflow, H3 hexagonal-grid bioregionalisation.
- **Cluster J — Paleoclimate (T62-T72).** Phanerozoic climate-sensitive
  lithologies on reconstructed plates, (T63) plant-fossil occurrences
  reconstructed onto Early Triassic super-greenhouse climate fields (Xu & Mills
  community contribution), deep-time paleoclimate model snapshots
  regridded onto reconstructed coastlines, model-vs-proxy SST comparisons,
  end-Permian CO2-sensitivity ensembles, full-Phanerozoic biogeochemistry,
  reference-frame uncertainty in reconstructed paleoclimate, a K-Pg
  (Chicxulub impact) cGENIE trio -- ocean biogeochemistry collapse, plankton
  trait-based extinction selectivity, and fossil-record extinction
  selectivity tested against the model -- and (T72) continental-arc CO2
  degassing driven by subducted carbonate-platform decarbonation.
- **Cluster K — Mineral exploration (T73-T80).** SW-Pacific porphyry-Cu-Au
  paleo-prospectivity, global porphyry kinematics envelope, seafloor age-grid
  anomalies as porphyry-Cu predictors, sediment-hosted Cu deposits, deep-time
  porphyry-Cu deposit trajectories, continent-scale prospectivity maps,
  manganese-deposit paleogeography, craton boundary framework.

For the exact list of notebooks under each cluster at any moment, the
authoritative source is the directory listing alongside this README; the
opening markdown cell of each notebook always names its cluster.

## See also: rgplates (R-language equivalent)

Kocsis, Raja, Williams & Dowding's
[`rgplates`](https://github.com/GPlates/rgplates) R package covers a subset of
this Python tutorial suite's scope — point/polygon reconstruction via the
GPlates Web Service or local GPlates Desktop install. Several notebooks in this
suite include explicit cross-references to the corresponding rgplates
vignettes; the two tools are designed to complement, not compete with, each
other. Choose the one that fits your downstream stack (R / `sf` /
`chronosphere` → `rgplates`; Python / `xarray` / `pygmt` → this suite).
