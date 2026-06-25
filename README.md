<p align="center">
  <img src="docs/images/GPlately%2BpyGMT.png" alt="GPlately + pyGMT" width="360">
</p>

# Extending pyGMT into Deep Time via GPlately

An open, reproducible tutorial suite of **Jupyter notebooks** that couples
[GPlately](https://github.com/GPlates/gplately) (plate-tectonic reconstructions)
with [pyGMT](https://www.pygmt.org/) (publication-quality maps, charts, and
scientific plots).

The suite is sequenced as a teaching ladder, starting with first-paleo-map and
projection-cookbook primers for undergraduates and building through to
research-grade workflows in plate kinematics, mantle dynamics and dynamic
topography, paleomagnetism, paleo-geography and -topography, paleo-biogeography,
paleo-climate, and reconstruction-driven mineral exploration. See
[`Notebooks/README.md`](Notebooks/README.md) for the per-cluster description and
the GitHub directory listing for the always-current notebook inventory — each
notebook's first markdown cell names its cluster and runs you through what it
produces.

## Quick start

```bash
git clone https://github.com/EarthByte/GPlately-pyGMT-tutorials.git
cd GPlately-pyGMT-tutorials
conda env create -f environment.yml
conda activate gplately-pygmt
jupyter lab
```

Or use the official [`gplates/gplately` Docker image](https://hub.docker.com/r/gplates/gplately).

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
`*Contributed by:*` provenance line in the notebook header. The current author-
contributed notebook is by **Jianping Zhou** (highland-footprint DBSCAN
analysis reproducing Fig. 4 of Zhou et al. 2026 *Geology*).

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
the file). Among the major external dependencies the suite leans on:

- **REVEAL** global full-waveform tomography (Thrastarson, van Herwaarden, Noe,
  Schiller & Fichtner 2024, *BSSA* 114, 1392–1406).
- **gmcm9** dynamic topography (Braz, Zahirovic, Salles, Flament, Harrington &
  Müller 2021, *Basin Research* 33(6), 3378–3405).
- **ThermoPlates** thermochronology-on-paleo-Earth workflow (Boone, Glorie,
  Zahirovic, Nixon, Meeuws, Kohlmann et al. 2025, *Communications Earth &
  Environment* 6, 1015).
- **SCION + pySCION** Earth-evolution model (Mills, Donnadieu & Goddéris 2021
  *Gondwana Research* 100, 73–86; Merdith, Gernon, Maffre, Donnadieu,
  Goddéris, Longman, Müller & Mills 2025, *Science Advances* 11(7), eadm9798).
- **Geochemistry-corrected paleo-elevation** (Zhou, Farahbakhsh, Williams, Li,
  Liu, Li & Müller 2025, *JGR Solid Earth* 130(5), e2024JB030404; Zhou et al.
  2026, *Geology*, in press).
- **Tomography-zircon paleo-distance to subduction** (Jian, Williams, Yu &
  Zhao 2022, *JGR Solid Earth*, doi:10.1029/2022JB024606). The implementation
  in this suite is independent — no code is recycled.
- **PALEOMAP / Scotese & Wright** paleo-DEMs, **GPMDB** paleomagnetic
  database, **Paleobiology Database**, **Macrostrat**, **WSM** stress map,
  **GEM** + **AFEAD** fault databases, and others — fully credited in the
  relevant notebooks.

Full bibliographic references with verified DOIs are at the end of every
notebook.
