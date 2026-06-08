<p align="center">
  <img src="docs/images/GPlately%2BpyGMT.png" alt="GPlately + pyGMT" width="360">
</p>

# Extending pyGMT into Deep Time via GPlately

An open, reproducible tutorial suite of **15 Jupyter notebooks** that couples
[GPlately](https://github.com/GPlates/gplately) (plate-tectonic reconstructions)
with [pyGMT](https://www.pygmt.org/) (publication-quality maps, charts, and
scientific plots).

The suite is sequenced as a teaching ladder from undergraduate primer (T01) to
three research-grade flagship workflows:

- **T13** — REVEAL tomography slices with reconstructed plate boundaries
  overlaid at sinking-rate-derived ages, exposing the slab-graveyard signal
  in the deep mantle.
- **T14** — Plate-boundary convergence statistics combined with deforming-
  region strain rates inside topological networks.
- **T15** — Paleo-σHmax computation along subduction zones, a Python port of
  the Stephan et al. (2023) `tectonicr` method applied to deep time.

See [`Notebooks/README.md`](Notebooks/README.md) for the full index and per-
notebook descriptions.

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
├── Notebooks/               # T01..T15 + README.md
├── data/                    # bundled non-PMM data (REVEAL slices, sea-level XLSX,
│                            # WSM stress map, Afonso 2019 lithospheric thickness)
├── environment.yml
└── LICENSE
```

The `plate_model_manager` cache (Cao 2024, Zahirovic 2022, Merdith 2021,
Müller 2022) is downloaded automatically by the notebooks on first run; it is
not stored in the repository.

## Contributing

Contributions welcome via pull request. See `Notebooks/README.md` for the
conventions every notebook follows.

## License

BSD 3-Clause — see [`LICENSE`](LICENSE). Matches the license of
[pyGMT](https://github.com/GenericMappingTools/pygmt). The tutorials also
import [GPlately](https://github.com/GPlates/gplately) (GPL 2.0); because the
EarthByte Group is both the GPlately copyright holder and the publisher of
this tutorial suite, the same group controls the licensing of both.

## Attribution

Several notebooks build on prior published methodologies and cite the original
authors:

- **T06** (Paleobathymetry profile) uses the Müller et al. (2022) paleobathymetry
  grids and the GDH plate-cooling reference curve (Stein & Stein 1992).
- **T07** (Plate-tectonic diagnostics) is a modern Python re-implementation of
  the metric panel from Seton et al. (2023, *Nature Reviews Earth & Environment*).
- **T09–T12** (zircon notebooks) are inspired by Jian, Williams, Yu & Zhao
  (2022, *J. Geophys. Res. Solid Earth*, doi:10.1029/2022JB024606). The
  implementation in this suite is independent — no code is recycled from the
  Jian et al. repository.
- **T13** (REVEAL tomography slices) uses the REVEAL global tomography model
  of Thrastarson et al. (2024).
- **T15** (paleo-σHmax along subduction zones) is a Python port of the
  Stephan et al. (2023) `tectonicr` method applied to deep time.

Full bibliographic references are at the end of every notebook.
