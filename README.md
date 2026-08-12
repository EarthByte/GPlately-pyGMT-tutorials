<p align="center">
  <img src="docs/images/GPlately%2BpyGMT.png" alt="GPlately + pyGMT" width="360">
</p>

# Extending pyGMT into Deep Time via GPlately

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.21895853.svg)](https://doi.org/10.5281/zenodo.21895853)

An open, reproducible tutorial suite of **Jupyter notebooks** that couples
[GPlately](https://github.com/GPlates/gplately) (plate-tectonic reconstructions)
with [pyGMT](https://www.pygmt.org/) (publication-quality maps, charts, and
scientific plots).

The suite is sequenced as a teaching ladder, starting with first-paleo-map and
projection-cookbook primers for undergraduates and building through to
research-grade workflows in plate kinematics, mantle dynamics and dynamic
topography, paleomagnetism, paleo-geography and -topography, paleo-biogeography,
paleo-climate, and reconstruction-driven exploration for Earth resources. See
[`Notebooks/README.md`](Notebooks/README.md) for the per-cluster description and
the GitHub directory listing for the always-current notebook inventory — each
notebook's first markdown cell names its cluster and runs you through what it
produces.

## Quick start

```bash
# 1. Clone
git clone https://github.com/EarthByte/GPlately-pyGMT-tutorials.git
cd GPlately-pyGMT-tutorials

# 2. Get the large-data companion archive (~12 GB) from Zenodo
#    (only needed for 9 of the 80 notebooks — see below)
wget https://zenodo.org/records/21836196/files/GPlately-pyGMT-tutorial-data-v1.zip
unzip GPlately-pyGMT-tutorial-data-v1.zip
rsync -av GPlately-pyGMT-tutorial-data/zenodo_data/ ./zenodo_data/

# 3. Install the environment
conda env create -f environment.yml
conda activate gplately-pygmt
jupyter lab
```

Or use the official [`gplates/gplately` Docker image](https://hub.docker.com/r/gplates/gplately).

### About the Zenodo companion archive

**71 of the 80 notebooks** run purely from what's in this repo — everything
they need is either bundled in `data/` (small paleo-DEM subsets, published
tabular datasets, palette files) or auto-fetched at runtime via
`plate_model_manager` (Cao 2024, Zahirovic 2022, Merdith 2021, Müller 2022).

**9 notebooks** — the thermochronology + mantle-dynamics group (T28, T46,
T48–T51) and the Devonian / PhanSST / Cenozoic-gateway paleoclimate trio
(T69–T71) — lean on larger datasets that would push the repo past 100 MB per
file / into the multi-GB range on disk. Those datasets ship in a single
**Zenodo companion archive** at DOI
[10.5281/zenodo.21836196](https://doi.org/10.5281/zenodo.21836196)
(~12 GB compressed): AFEAD + GEM fault databases, gmcm9 dynamic topography,
Dhungana + Flament mantle temperature/velocity fields, per-continent
thermochronology compilations, and the FOAM / PhanSST / gateway-bathymetry
datasets behind T69–T71. Extract it as `zenodo_data/` at the repo root (see
[`Notebooks/README.md`](Notebooks/README.md) for the exact layout). See the
archive's own `README.md` and `DATA_INVENTORY.md` for the full manifest,
provenance, and per-dataset citations.

A handful of other notebooks (T34, T41, T62) need only a small, single-file
rotation model (`data/Zahirovic2022_with_gpmdb_frame.rot`, 2.8 MB) that's
committed straight to the repo — no Zenodo download required for those.

If you skip step 2, the notebooks that depend on the Zenodo archive raise
`FileNotFoundError` on their first cell with a pointer to the Zenodo DOI —
nothing runs silently against missing inputs. The other 71 notebooks work
regardless.

## Layout

```
GPlately-pyGMT-tutorials/
├── Notebooks/               # T01_*.ipynb … + README.md
├── data/                    # bundled non-PMM datasets — see each notebook's
│                            # Data Availability cell for what it relies on
├── external/                # gitignored — symlinks to larger companion
│                            # datasets some notebooks need (see Notebooks/README.md)
├── environment.yml
└── LICENSE
```

The `plate_model_manager` cache (Cao 2024, Zahirovic 2022, Merdith 2021,
Müller 2022) is downloaded automatically by the notebooks on first run; it is
not stored in the repository.

## Contributing

Contributions welcome via pull request. See [`Notebooks/README.md`](Notebooks/README.md)
for the conventions every notebook follows (executed outputs preserved,
three-section header, `# === USER CONFIGURATION ===` block, in-frame age stamp,
closing *Extend this* section).

Author-contributed notebooks from co-authors building on their own published or
in-preparation workflows are explicitly welcome — the contributor goes in a
`*Contributed by:*` provenance line in the notebook header. See **Attribution**
below for the full, current list of notebooks built on a co-author's own
published methodology or dataset.

## License

BSD 3-Clause — see [`LICENSE`](LICENSE). Matches the license of
[pyGMT](https://github.com/GenericMappingTools/pygmt). The tutorials also
import [GPlately](https://github.com/GPlates/gplately) (GPL 2.0); because the
EarthByte Group is both the GPlately copyright holder and the publisher of
this tutorial suite, the same group controls the licensing of both.

## Attribution

Several notebooks build on previously published methodologies or datasets and
cite the original authors in their own References section. The authoritative
attribution is therefore inside each notebook (visible on GitHub by opening
the file). The suite has grown into a genuine community-contribution
platform — the list below is a systematic, per-notebook account of every
external methodology or dataset it currently leans on, organised by cluster.

**Cluster B — Plate kinematics + tectonics**
- **T14** rift-obliquity framework of Brune, Williams, Butterworth & Müller
  (2016, *Nature Comms* 7, 11409), Brune, Williams & Müller (2017, *Nature
  Geoscience* 10, 941–946) and Brune, Williams & Müller (2018, *Solid Earth*
  9, 1187–1206).
- **T15** reimplements Ehsan Farahbakhsh's own kinematic-feature-extraction
  workflow (Farahbakhsh et al. 2025), ported from his
  [GPlates_Workflows](https://github.com/e-farahbakhsh/GPlates_Workflows) repo.

**Cluster D — Zircons + tectonic-setting predictors**
- **T24** paleo-distance-to-subduction predictor is inspired by Jian,
  Williams, Yu & Zhao (2022, *JGR Solid Earth*, doi:10.1029/2022JB024606) —
  the implementation here is independent; no code is recycled (their
  repository is GPL-3.0).
- **T25** Hf-Nd terrane-mapping tradition of Bennett & DePaolo (1987,
  *GSA Bulletin* 99, 674–685) and Roberts & Spencer (2015).

**Cluster E — Mantle dynamics + dynamic topography**
- **T26–T27** REVEAL global full-waveform tomography (Thrastarson, van
  Herwaarden, Noe, Schiller & Fichtner 2024, *BSSA* 114, 1392–1406).
- **T29–T30** and **T48, T50** (see cluster G) use **gmcm9** dynamic
  topography (Braz, Zahirovic, Salles, Flament, Harrington & Müller 2021,
  *Basin Research* 33(6), 3378–3405).

**Cluster F — Paleomagnetism**
- Rooted throughout in **PmagPy** (Tauxe, Shaar, Jonestrask et al. 2016,
  *G-cubed* 17(6), 2450–2463).
- **T42** paleolatitude-via-reverse-reconstruction follows the approach of
  Kocsis, Raja, Williams & Dowding (2024) and their
  [`rgplates`](https://github.com/GPlates/rgplates) R package.

**Cluster G — Paleo-geography + paleo-topography + thermochronology**
- **T43** geochemistry-corrected paleo-elevation (Zhou, Farahbakhsh,
  Williams, Li, Liu, Li & Müller 2025, *JGR Solid Earth* 130(5),
  e2024JB030404; Zhou et al. 2026, *Geology*).
- **T44** Macrostrat lithology-styled paleogeologic maps — author-contributed
  by **Daven Quinn** and **Shanan E. Peters** (University of Wisconsin-Madison),
  creators of Macrostrat — adapted from their own
  [UW-Macrostrat / GPlately + pyGMT demo](https://github.com/UW-Macrostrat/gplately-pygmt-demo),
  following Peters, Husson & Czaplewski (2018, *G-cubed* 19, 1393-1409) and
  Quinn, Czaplewski, Husson & Peters (2024, *Geoscience Data Journal* 11,
  597-608).
- **T46** highland-footprint DBSCAN analysis — author-contributed by
  **Jianping Zhou**, reproducing Fig. 4 of Zhou et al. (2026, *Geology*).
- **T47, T48–T51** — the ThermoPlates thermochronology-on-paleo-Earth suite,
  following Boone, Glorie, Zahirovic, Nixon, Meeuws, Kohlmann et al. (2025,
  *Communications Earth & Environment* 6, 1015); **T48, T50** additionally
  use **gmcm9** dynamic topography (Braz et al. 2021, above).

**Cluster H — Sedimentary basins**
- **T53–T55** draw on the global sedimentary-basin compilation of Evenick
  (2021, *Earth-Science Reviews* 215, 103564).

**Cluster I — Paleo-biogeography**
- **T58** Kimmeridgian-dinosaurs notebook is a Python re-implementation of
  the Kocsis et al. (2024) `rgplates` worked example.
- **T59** uses the ForCenS planktonic-foraminifera database (Siccha & Kucera
  2017, *Scientific Data* 4, 170109; Jonkers et al. 2025).
- **T61** H3 hexagonal-grid paleo-bioregionalisation adapts the approach of
  Kocsis et al. (2024).

**Cluster J — Paleoclimate**
- **T62** Phanerozoic climate-sensitive lithologies of Boucot, Xu, Scotese &
  Morley (2013).
- **T63** plant-fossil / Early Triassic super-greenhouse notebook —
  author-contributed by **Zhen Xu** and **Benjamin J.W. Mills**, following
  Xu et al. (2025a, 2025b).
- **T64–T67** SCION + pySCION Earth-evolution model (Mills, Donnadieu &
  Goddéris 2021, *Gondwana Research* 100, 73–86; Merdith, Gernon, Maffre,
  Donnadieu, Goddéris, Longman, Müller & Mills 2025, *Science Advances*
  11(7), eadm9798; Mills & Gurung 2025).
- **T68** reference-frame paleoclimate mines the Leonard, Zahirovic, Salles,
  Dimitrijević, Merdith et al. (2025) archive.
- **T69** Devonian paleoclimatology drapes the Pohl et al. (2022) FOAM GCM
  climatology on its own published plate model.
- **T70** deep-time SST-proxy reconstruction is verified against the Judd
  et al. (2022) PhanSST database's own published paleo-coordinate method.
- **T71** Cenozoic ocean-gateway bathymetry (Straume et al. 2020) is
  cross-checked against independently reconstructed plate boundaries
  (Seton et al. 2012).
- **T72** continental-arc CO₂-degassing modelling follows Mather, Müller,
  Dutkiewicz & Zahirovic (2026).

**Cluster K — Mineral exploration**
- **T73–T78** porphyry-Cu paleo-prospectivity workflows draw on Farahbakhsh
  et al. (2025), Mather et al. (2025), and the Norbisrath, Singh, Singh &
  Müller (submitted, *Geology*) plate-reorganisation / carbonate-subduction
  fertility-window study, built on Satyam Singh's Geonome archive.
- **T80** craton-boundary framework (REVEAL VSH vs mineral deposits) follows
  Shirmard et al. (2025).
- Underlying reference datasets credited throughout the cluster: **PALEOMAP
  / Scotese & Wright** paleo-DEMs, **GPMDB** paleomagnetic database,
  **Paleobiology Database**, **Macrostrat**, **WSM** stress map, **GEM** +
  **AFEAD** fault databases, and others — fully credited in the relevant
  notebooks.

Full bibliographic references with verified DOIs are at the end of every
notebook.
