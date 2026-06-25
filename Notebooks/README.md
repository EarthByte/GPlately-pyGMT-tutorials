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
that are too large or licensed separately to bundle here. Each such notebook
spells out its requirements in its first markdown cell ("Data availability")
and its `# === USER CONFIGURATION ===` cell, which carries a default path
under `./external/<dataset-name>/` plus an environment-variable fallback. To
set them up once, drop symlinks under `external/` pointing at your local
clones — `external/` is gitignored and never pushed.

If a notebook's data isn't found, it fails fast with a clear `FileNotFoundError`
that names the expected path and env-var override.

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
- **T04 — Multi-model diff maps** and **T05 — Comparing rotation models**, once
  T01-T03 are comfortable — these show how to reason about model choice
  rather than treat any one model as ground truth.
- **T10 — Paleobathymetry profile across the Atlantic at 50 Ma** as the first
  application notebook that turns the workflow into a concrete cross-section.

## Themes

The suite is loosely organised into nine thematic clusters. Each cluster has
its own opening sentence below; the T-number range listed alongside is current
at the time of writing and will grow as the suite is extended. Re-read the
cluster header inside each notebook for the authoritative cluster assignment.

- **Cluster A — Getting started + core workflows.** First paleo-maps, projection
  choices, model-comparison patterns, animations, interactive Panel views.
- **Cluster B — Plate kinematics + tectonics.** Plate-tectonic diagnostics,
  age-of-subducting-crust, paleo-bathymetry profiles, strain-rate maps,
  lithospheric-thickness retrodeformation, paleo-stress along subduction zones.
- **Cluster C — Zircons + tectonic-setting predictors.** Detrital / igneous /
  metamorphic zircons reconstructed through deep time, paleo-distance to the
  nearest subduction zone as a tectonic-setting predictor.
- **Cluster D — Mantle dynamics + dynamic topography.** REVEAL tomography
  overlain with reconstructed plate boundaries, deep-time mantle transects,
  clustering of plate-frame dynamic-topography histories, dynamic-topography
  change rate through deep time.
- **Cluster E — Paleomagnetism.** Building a paleomagnetic reference frame from
  GPMDB, comparing alternative reference frames, continent rotation with
  GPlately, predicted vs observed paleomagnetic directions, single-key-pole
  case studies, full Phanerozoic apparent polar wander, inclination-shallowing
  corrections, pole rotation utilities.
- **Cluster F — Paleo-geography + paleo-topography.** Geochemistry-corrected
  paleo-elevation, Macrostrat sedimentary units in paleo-position, highland-
  footprint detection in deep time, and the full ThermoPlates suite of
  thermochronology-on-paleo-Earth workflows (cooling rates on Earth-system
  overlays, against plate kinematics and fault databases, and as
  correlation/time-series analyses).
- **Cluster G — Paleo-biogeography.** Paleobiology Database × Macrostrat joins
  in paleo-coordinates, fossil corals through deep time, Late Jurassic
  dinosaur distributions on a reconstructed climate, Cenozoic planktonic
  foraminifera on reconstructed paleo-latitude.
- **Cluster H — Paleo-climate.** Phanerozoic climate-sensitive lithologies on
  reconstructed plates, deep-time paleoclimate model snapshots regridded onto
  reconstructed coastlines, model-vs-proxy SST comparisons, Bayesian SST
  inference from δ¹⁸O, end-Permian SAT scenarios, CO₂-sensitivity ensembles,
  full-Phanerozoic biogeochemistry on a reconstructed paleo-Earth.
- **Cluster I — Mineral exploration.** SW-Pacific porphyry-Cu-Au paleo-
  prospectivity, global porphyry kinematics envelope, seafloor age-grid
  anomalies as porphyry-Cu predictors, sediment-hosted Cu deposits on a
  reconstructed paleo-Earth.

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
