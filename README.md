<p align="center">
  <img src="docs/images/GPlately%2BpyGMT.png" alt="GPlately + pyGMT" width="360">
</p>

<p align="center">
  <img src="docs/images/AuScope_NCRIS_logos.png" alt="AuScope and NCRIS logos" width="360">
</p>

# Extending pyGMT into Deep Time via GPlately

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.21977669.svg)](https://doi.org/10.5281/zenodo.21977669)

*This research was supported by AuScope and the Australian Government's
National Collaborative Research Infrastructure Strategy (NCRIS).*

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

This suite is the companion repository to *Extending pyGMT into Deep Time
with GPlately* (Müller et al.), currently in review at *Geochemistry,
Geophysics, Geosystems* (G3).

**Live repository versus archived snapshot.** This GitHub repository is the
living version of the suite and will keep changing (new notebooks, fixes,
renumbering). The Zenodo record
[10.5281/zenodo.21977669](https://doi.org/10.5281/zenodo.21977669) is a frozen
snapshot of the suite as it stood when the companion paper was published and is
not updated afterwards; if something here differs from what the paper describes,
the Zenodo snapshot is the version the paper refers to. Cite the Zenodo DOI to
refer to the exact version described in the paper.

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

**9 notebooks** — the thermochronology + mantle-dynamics group (E03, G04,
G06–G09) and the Devonian / PhanSST / Cenozoic-gateway paleoclimate trio
(J08–J10) — lean on larger datasets that would push the repo past 100 MB per
file / into the multi-GB range on disk. Those datasets ship in a single
**Zenodo companion archive** at DOI
[10.5281/zenodo.21836196](https://doi.org/10.5281/zenodo.21836196)
(~12 GB compressed): AFEAD + GEM fault databases, gmcm9 dynamic topography,
Dhungana + Flament mantle temperature/velocity fields, per-continent
thermochronology compilations, and the FOAM / PhanSST / gateway-bathymetry
datasets behind J08–J10. Extract it as `zenodo_data/` at the repo root (see
[`Notebooks/README.md`](Notebooks/README.md) for the exact layout). See the
archive's own `README.md` and `DATA_INVENTORY.md` for the full manifest,
provenance, and per-dataset citations.

A handful of other notebooks (F02, F09, J01) need only a small, single-file
rotation model (`data/Zahirovic2022_with_gpmdb_frame.rot`, 2.8 MB) that's
committed straight to the repo — no Zenodo download required for those.

If you skip step 2, the notebooks that depend on the Zenodo archive raise
`FileNotFoundError` on their first cell with a pointer to the Zenodo DOI —
nothing runs silently against missing inputs. The other 71 notebooks work
regardless.

## Working without the plate-model server

`plate_model_manager` contacts `repo.gplates.org` every time `PlateModelManager()` is created, even when a model is already cached, so cells can hang or fail when the server is down or blocked (VPN, firewall). All notebooks therefore use `LocalFirstPMM` from `Notebooks/pmm_local.py` instead. It checks once per session (5 s timeout) whether the server answers. If it does, it behaves exactly like `PlateModelManager`; if it does not, it loads the model from the local cache folder (`gplately_data/<model name in lower case>/`) in read-only mode and prints a message. A model that has never been downloaded cannot be loaded offline; the error names the missing folder. Set `PMM_OFFLINE=1` to skip the server check and always use the cache.

If a corporate VPN does the TLS inspection and Python reports certificate errors, point `SSL_CERT_FILE` and `REQUESTS_CA_BUNDLE` to a CA bundle that contains the organisation's root certificate.

## Layout

```
GPlately-pyGMT-tutorials/
├── Notebooks/               # A01_*.ipynb … + README.md
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

**How contributions are reviewed.** Every pull request is reviewed by the
maintainers (EarthByte Group) against the checklist in
[`.github/PULL_REQUEST_TEMPLATE.md`](.github/PULL_REQUEST_TEMPLATE.md) before it
is merged: the notebook follows the structure above; it runs top-to-bottom in
the `environment.yml` environment (any new dependency is added there); any data
beyond the plate models is either bundled in `data/` or declared as a Zenodo
dependency with a clear error message when it is missing; every method and
dataset is cited with a DOI that has been checked to resolve to the cited work;
contributed methodology is credited in the notebook header, in
[`CONTRIBUTORS.md`](CONTRIBUTORS.md) and in the Attribution section below; and
the change is recorded in [`CHANGELOG.md`](CHANGELOG.md). The maintainers
re-execute contributed notebooks before merging so that the preserved outputs
match the committed code. Tagged releases are archived on Zenodo.

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
- **B07** rift-obliquity framework of Brune, Williams, Butterworth & Müller
  (2016, *Nature Comms* 7, 11409), Brune, Williams & Müller (2017, *Nature
  Geoscience* 10, 941–946) and Brune, Williams & Müller (2018, *Solid Earth*
  9, 1187–1206).
- **B08** reimplements Ehsan Farahbakhsh's own kinematic-feature-extraction
  workflow (Farahbakhsh et al. 2025), ported from his
  [GPlates_Workflows](https://github.com/e-farahbakhsh/GPlates_Workflows) repo.

**Cluster D — Zircons + tectonic-setting predictors**
- **D04** paleo-distance-to-subduction predictor is inspired by Jian,
  Williams, Yu & Zhao (2022, *JGR Solid Earth*, doi:10.1029/2022JB024606) —
  the implementation here is independent; no code is recycled (their
  repository is GPL-3.0).
- **D05** Hf-Nd terrane-mapping tradition of Bennett & DePaolo (1987,
  *GSA Bulletin* 99, 674–685) and Roberts & Spencer (2015).

**Cluster E — Mantle dynamics + dynamic topography**
- **E01–E02** REVEAL global full-waveform tomography (Thrastarson, van
  Herwaarden, Noe, Schiller & Fichtner 2024, *BSSA* 114, 1392–1406).
- **G06, G08** (see cluster G) use **gmcm9** dynamic
  topography (Braz, Zahirovic, Salles, Flament, Harrington & Müller 2021,
  *Basin Research* 33(6), 3378–3405).

**Cluster F — Paleomagnetism**
- Rooted throughout in **PmagPy** (Tauxe, Shaar, Jonestrask et al. 2016,
  *G-cubed* 17(6), 2450–2463).
- **F10** paleolatitude-via-reverse-reconstruction follows the approach of
  Kocsis, Raja, Williams & Dowding (2024) and their
  [`rgplates`](https://github.com/GPlates/rgplates) R package.

**Cluster G — Paleo-geography + paleo-topography + thermochronology**
- **G01** geochemistry-corrected paleo-elevation (Zhou, Farahbakhsh,
  Williams, Li, Liu, Li & Müller 2025, *JGR Solid Earth* 130(5),
  e2024JB030404; Zhou et al. 2026, *Geology*).
- **G02** Macrostrat lithology-styled paleogeologic maps — author-contributed
  by **Daven Quinn** and **Shanan E. Peters** (University of Wisconsin-Madison),
  creators of Macrostrat — adapted from their own
  [UW-Macrostrat / GPlately + pyGMT demo](https://github.com/UW-Macrostrat/gplately-pygmt-demo),
  following Peters, Husson & Czaplewski (2018, *G-cubed* 19, 1393-1409) and
  Quinn, Czaplewski, Husson & Peters (2024, *Geoscience Data Journal* 11,
  597-608).
- **G04** highland-footprint DBSCAN analysis — author-contributed by
  **Jianping Zhou**, reproducing Fig. 4 of Zhou et al. (2026, *Geology*).
- **G05, G06–G09** — the ThermoPlates thermochronology-on-paleo-Earth suite,
  following Boone, Glorie, Zahirovic, Nixon, Meeuws, Kohlmann et al. (2025,
  *Communications Earth & Environment* 6, 1015); **G06, G08** additionally
  use **gmcm9** dynamic topography (Braz et al. 2021, above).

**Cluster H — Sedimentary basins**
- **H01–H03** draw on the global sedimentary-basin compilation of Evenick
  (2021, *Earth-Science Reviews* 215, 103564).

**Cluster I — Paleo-biogeography**
- **I03** Kimmeridgian-dinosaurs notebook is a Python re-implementation of
  the Kocsis et al. (2024) `rgplates` worked example.
- **I04** uses the ForCenS planktonic-foraminifera database (Siccha & Kucera
  2017, *Scientific Data* 4, 170109; Jonkers et al. 2025).
- **I06** H3 hexagonal-grid paleo-bioregionalisation adapts the approach of
  Kocsis et al. (2024).

**Cluster J — Paleoclimate**
- **J01** Phanerozoic climate-sensitive lithologies of Boucot, Xu, Scotese &
  Morley (2013).
- **J02** plant-fossil / Early Triassic super-greenhouse notebook —
  author-contributed by **Zhen Xu** and **Benjamin J.W. Mills**, following
  Xu et al. (2025a, 2025b).
- **J03–J06** SCION + pySCION Earth-evolution model (Mills, Donnadieu &
  Goddéris 2021, *Gondwana Research* 100, 73–86; Merdith, Gernon, Maffre,
  Donnadieu, Goddéris, Longman, Müller & Mills 2025, *Science Advances*
  11(7), eadm9798; Mills & Gurung 2025).
- **J07** reference-frame paleoclimate mines the Leonard, Zahirovic, Salles,
  Dimitrijević, Merdith et al. (2025) archive.
- **J08** Devonian paleoclimatology drapes the Pohl et al. (2022) FOAM GCM
  climatology on its own published plate model.
- **J09** deep-time SST-proxy reconstruction is verified against the Judd
  et al. (2022) PhanSST database's own published paleo-coordinate method.
- **J10** Cenozoic ocean-gateway bathymetry (Straume et al. 2020) is
  cross-checked against independently reconstructed plate boundaries
  (Seton et al. 2012).
- **J11** continental-arc CO₂-degassing modelling follows Mather, Müller,
  Dutkiewicz & Zahirovic (2026).

**Cluster K — Mineral exploration**
- **K01–K06** porphyry-Cu paleo-prospectivity workflows draw on Farahbakhsh
  et al. (2025), Mather et al. (2025), and the Norbisrath, Singh, Singh &
  Müller (submitted, *Geology*) plate-reorganisation / carbonate-subduction
  fertility-window study, built on Satyam Singh's Geonome archive.
- **K08** craton-boundary framework (REVEAL VSH vs mineral deposits) follows
  Shirmard et al. (2025).
- Underlying reference datasets credited throughout the cluster: **PALEOMAP
  / Scotese & Wright** paleo-DEMs, **GPMDB** paleomagnetic database,
  **Paleobiology Database**, **Macrostrat**, **WSM** stress map, **GEM** +
  **AFEAD** fault databases, and others — fully credited in the relevant
  notebooks.

Full bibliographic references with verified DOIs are at the end of every
notebook.
