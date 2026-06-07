# GPlately × pyGMT tutorials

A growing collection of Jupyter notebooks that demonstrate how to combine
[GPlately](https://github.com/GPlates/gplately) (plate reconstructions) with
[pyGMT](https://www.pygmt.org/) (publication-quality maps, charts, and
scientific plots).

## Conventions

Every notebook in this folder follows the same conventions:

1. **Stripped outputs.** Run cells locally to generate figures; do not commit
   notebook outputs. (Same convention as the GPlately upstream `Notebooks/`.)
2. **Self-contained.** Each notebook prints library versions in cell 1, downloads
   any required data via `plate_model_manager` (so no manual setup), and
   produces at least one figure.
3. **Three-section header.** Title + one-paragraph motivation, learning
   objectives, prerequisites/runtime.
4. **Closing "Extend this" section.** Suggestions for follow-up modifications.

## Recommended environment

```bash
conda create -n gplately-pygmt -c conda-forge gplately pygmt jupyter
conda activate gplately-pygmt
jupyter lab
```

(GPlately's docker image works too: `gplates/gplately`.)

## Index

| # | Notebook | Audience | Difficulty | Status |
|---|----------|----------|------------|--------|
| T01 | [Hello, deep time](T01_Hello_Deep_Time.ipynb) | undergrad | ★☆☆ | drafted |
| T02 | [Projection cookbook](T02_Projection_Cookbook.ipynb) | undergrad | ★☆☆ | drafted |
| T03 | [Animations](T03_Plate_Motion_Animation.ipynb) | both | ★★☆ | drafted |
| T04 | [Interactive paleo-Earth with Panel + pyGMT](T04_Interactive_Paleo_Earth.ipynb) | both | ★★☆ | drafted |
| T05 | [Multi-model diff maps](T05_Multi_Model_Diff_Maps.ipynb) | undergrad | ★★☆ | drafted |
| T06 | [Paleobathymetry profile across the Atlantic at 50 Ma](T06_Paleobathymetry_Profile.ipynb) | undergrad | ★★☆ | drafted |
| T07 | [Plate-tectonic diagnostics through deep time](T07_Plate_Tectonic_Diagnostics.ipynb) | postgrad | ★★★ | drafted |
| T08 | [Age of subducting crust](T08_Age_of_Subducting_Crust.ipynb) | undergrad+ | ★★☆ | drafted |
| T09 | [Detrital zircons through deep time](T09_Detrital_Zircons_Reconstructed.ipynb) | postgrad | ★★★ | drafted |
| T10 | [Igneous zircons through deep time](T10_Igneous_Zircons_Reconstructed.ipynb) | postgrad | ★★★ | drafted |
| T11 | [Metamorphic zircons through deep time](T11_Metamorphic_Zircons_Reconstructed.ipynb) | postgrad | ★★★ | drafted |
| T12 | [Detrital-zircon paleo-distance to the nearest subduction zone](T12_Detrital_Zircon_Distance_to_Subduction.ipynb) | postgrad | ★★★ | drafted |
| T13 | [REVEAL tomography slices with reconstructed plate boundaries](T13_REVEAL_Tomography_Slices.ipynb) | postgrad | ★★★ | drafted |
| T14 | [Plate-boundary convergence + deforming-region strain rates](T14_Plate_Convergence_Strain_Rates.ipynb) | postgrad | ★★★ | drafted |
| T15 | [Paleo-σHmax along the Andean subduction zone](T15_Paleo_SHmax_Subduction.ipynb) | postgrad | ★★★ | drafted |

All 15 are currently "drafted" — they parse as valid Jupyter notebooks with
no committed outputs, but **none have been executed end-to-end yet**. Running
them locally in the `gplately-pygmt` environment is the next step. Expect
small API tweaks (column names, layer accessors, projection strings) when
each one first runs. T-numbers are provisional and will be renumbered in a
single sweep when the suite is finalised.

The **zircon trio** (T09 detrital, T10 igneous, T11 metamorphic) are
structurally identical — same loader, same Cao 2024 reconstruction logic,
same per-polygon shapely continental filter, same individual large pyGMT
maps + Panel slider — differing only in which Wu 2023 `.gpmlz` file they
ingest. T09 + T12 are inspired by Jian, Williams, Yu & Zhao (2022,
[doi:10.1029/2022JB024606](https://doi.org/10.1029/2022JB024606)). The
implementation in this suite is independent — no code is recycled from
the Jian et al. GPL-licensed repository
(<https://github.com/JIANDONGCHUAN/2022_DetritalZircon_TectonicSetting_Public>);
we use only the Wu 2023 database, the Cao 2024 plate model via
`plate_model_manager`, and stock `gplately` + `pyGMT` workflows.

