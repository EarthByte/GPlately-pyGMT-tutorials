# GPlately × pyGMT tutorials

A collection of Jupyter notebooks that demonstrate how to combine
[GPlately](https://github.com/GPlates/gplately) (plate reconstructions) with
[pyGMT](https://www.pygmt.org/) (publication-quality maps, charts, and
scientific plots).

> **Live repository versus archived snapshot.** This GitHub repository is the
> living version of the suite: notebooks are added, corrected and renumbered
> over time. The Zenodo record
> ([10.5281/zenodo.21977669](https://doi.org/10.5281/zenodo.21977669)) is a
> frozen snapshot of the suite as it stood at the time the companion paper
> (Müller et al., *Geochemistry, Geophysics, Geosystems*) was published; it is
> not updated afterwards. If notebook numbers, contents or environments here
> differ from what the paper describes, the Zenodo snapshot is the version the
> paper refers to.

## How to find what you want

Notebooks are filename-prefixed with an ID (`A01_…`, `A02_…`, …, `K08_…`): a
cluster letter (A-K) followed by the notebook's index within that cluster, then
a short topical slug. The full, always-current list is just the directory
listing — browse it on
[GitHub](https://github.com/EarthByte/GPlately-pyGMT-tutorials/tree/main/Notebooks)
or in JupyterLab's file sidebar. Each filename's slug is descriptive enough to
hint at the topic without a separate index.

IDs are grouped by theme — see *Themes* below. Numbering restarts within each
cluster, so a new notebook is appended to the end of the cluster it belongs to.
The cluster header in each notebook's *first markdown cell* is the
authoritative source for its cluster assignment.

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

## Working without the plate-model server

`plate_model_manager` contacts `repo.gplates.org` every time `PlateModelManager()` is created, even when a model is already cached, so cells can hang or fail when the server is down or blocked (VPN, firewall). All notebooks therefore use `LocalFirstPMM` from `Notebooks/pmm_local.py` instead. It checks once per session (5 s timeout) whether the server answers. If it does, it behaves exactly like `PlateModelManager`; if it does not, it loads the model from the local cache folder (`gplately_data/<model name in lower case>/`) in read-only mode and prints a message. A model that has never been downloaded cannot be loaded offline; the error names the missing folder. Set `PMM_OFFLINE=1` to skip the server check and always use the cache.

If a corporate VPN does the TLS inspection and Python reports certificate errors, point `SSL_CERT_FILE` and `REQUESTS_CA_BUNDLE` to a CA bundle that contains the organisation's root certificate.

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

- **A01 — Hello, deep time.** Your first pyGMT paleo-map; introduces the
  GPlately + pyGMT plumbing.
- **A02 — GPlates Web Service from Python.** Pure HTTP-REST workflow: reconstruct
  modern-city paleo-positions through deep time using nothing more than
  `requests` + `pygmt`. Doesn't require a local `pygplates` install, which makes
  it the lowest-barrier entry point in the suite — excellent for a teaching lab
  where install friction is the bottleneck.
- **A03 — Projection cookbook.** The cartographic foundation the rest of the
  suite leans on.
- **A04 — Plate model comparison** and **A05 — Comparing rotation models**, once
  A01-A03 are comfortable — these show how to reason about model choice
  rather than treat any one model as ground truth.
- **B03 — Paleobathymetry profile across the Atlantic at 50 Ma** as the first
  application notebook that turns the workflow into a concrete cross-section.

## Themes

The suite is organised into **11 thematic clusters, A-K**, containing 80
notebooks in total. Every notebook has an ID made of its cluster letter and its
index within the cluster (for example **F03**), and the notebook file names
start with that ID. Numbering is contiguous within each cluster, so adding a
notebook extends one cluster without disturbing the others. Re-read the cluster
header inside each notebook for the authoritative cluster assignment. Notebooks
that were numbered `T01`-`T80` in earlier versions of the suite (and in the
review-stage manuscript) are listed in
[`docs/NOTEBOOK_IDS.md`](../docs/NOTEBOOK_IDS.md).

- **Cluster A — Getting started + core workflows (A01-A07).** First paleo-maps,
  projection choices, model-comparison patterns, animations, interactive Panel
  views.
- **Cluster B — Plate kinematics + tectonics (B01-B09).** Plate-tectonic
  diagnostics, age-of-subducting-crust, paleo-bathymetry profiles, strain-rate
  maps, lithospheric-thickness retrodeformation, paleo-stress along
  subduction zones, rift obliquity, kinematic feature extraction at
  subduction zones through time (B08) — convergence rate/obliquity, trench
  velocity, and derived slab-flux proxies on an interactive map — and (B09)
  subducted-slab flux inventory: a deep-time budget of subducted slab volume,
  sediment, carbonate, and water mass.
- **Cluster C — Plate-model debugging (C01-C04).** Divergence/convergence sign
  anomalies at plate boundaries, MOR velocity-magnitude anomalies, topology
  construction anomalies (gaps/overlaps/non-unique sections), subduction-zone
  feature-extractability diagnostics.
- **Cluster D — Zircons + tectonic-setting predictors (D01-D05).** Detrital /
  igneous / metamorphic zircons reconstructed through deep time, paleo-distance
  to the nearest subduction zone as a tectonic-setting predictor, Hf-Nd
  isotope terrane mapping.
- **Cluster E — Mantle dynamics + dynamic topography (E01-E07).** REVEAL
  tomography overlain with reconstructed plate boundaries, deep-time mantle
  transects, clustering of plate-frame dynamic-topography histories,
  dynamic-topography vs sediment flux, dynamic-topography change rate through
  deep time, and the mantle-to-plate frame conversion walkthrough.
- **Cluster F — Paleomagnetism (F01-F10).** Building a paleomagnetic reference
  frame from GPMDB, comparing alternative reference frames, plate-mantle
  reference-frame uncertainty, continent rotation with GPlately, predicted vs
  observed paleomagnetic directions, single-key-pole case studies, full
  Phanerozoic apparent polar wander, inclination-shallowing corrections, pole
  rotation utilities, true polar wander decomposition, paleolatitude via
  reverse reconstruction.
- **Cluster G — Paleo-geography + paleo-topography (G01-G10).**
  Geochemistry-corrected paleo-elevation, Macrostrat stratigraphic columns
  progressively styled by lithology (flat API colour, mixed-lithology colour
  blending, GMT pattern fills — adapted from the UW-Macrostrat / GPlately +
  pyGMT demo), Macrostrat sedimentary units in paleo-position, highland-footprint
  detection in deep time, ophiolite emplacement, and the full ThermoPlates
  suite of thermochronology-on-paleo-Earth workflows (cooling rates on
  Earth-system overlays, against plate kinematics and fault databases, and
  as correlation/time-series analyses).
- **Cluster H — Sedimentary basins (H01-H03).** Evenick (2021) global
  sedimentary-basin compilation: basin inventory + thickness + paleogeographic
  reconstruction, crustal stretching factor (β), individual rift-basin
  syn-rift/post-rift analysis.
- **Cluster I — Paleo-biogeography (I01-I06).** Paleobiology Database ×
  Macrostrat joins in paleo-coordinates, fossil corals through deep time, Late
  Jurassic dinosaur distributions on a reconstructed climate, Cenozoic
  planktonic foraminifera on reconstructed paleo-latitude, PBDB
  paleobiogeography live-API workflow, H3 hexagonal-grid bioregionalisation.
- **Cluster J — Paleoclimate (J01-J11).** Phanerozoic climate-sensitive
  lithologies on reconstructed plates, (J02) plant-fossil occurrences
  reconstructed onto Early Triassic super-greenhouse climate fields (Xu & Mills
  community contribution), deep-time paleoclimate model snapshots
  regridded onto reconstructed coastlines, model-vs-proxy SST comparisons,
  end-Permian CO2-sensitivity ensembles, full-Phanerozoic biogeochemistry,
  reference-frame uncertainty in reconstructed paleoclimate, Devonian
  paleogeography and climatology (FOAM GCM on Scotese & Wright 2018),
  deep-time SST proxy reconstruction (PhanSST, verified against the
  database's own published paleo-coordinate method), Cenozoic ocean-gateway
  bathymetry cross-checked against independently reconstructed plate
  boundaries (Fram Strait, Greenland-Scotland Ridge, Central American
  Seaway, Tethyan Seaway) -- and (J11) continental-arc CO2 degassing driven
  by subducted carbonate-platform decarbonation.
- **Cluster K — Mineral exploration (K01-K08).** SW-Pacific porphyry-Cu-Au
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
