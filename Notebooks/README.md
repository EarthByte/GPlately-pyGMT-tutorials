# GPlately × pyGMT tutorials

A growing collection of Jupyter notebooks that demonstrate how to combine
[GPlately](https://github.com/GPlates/gplately) (plate reconstructions) with
[pyGMT](https://www.pygmt.org/) (publication-quality maps, charts, and
scientific plots).

## Conventions

Every notebook in this folder follows the same conventions:

1. **Executed outputs preserved.** Re-run each notebook before commit so that
   the embedded figures are visible when the file is opened on GitHub. A
   newcomer should be able to see what each notebook produces without
   installing anything. *(Changed from the original "stripped outputs"
   convention on 2026-06-16 to lower the barrier to discovery; see
   `CHANGELOG.md`.)* Animation cells that embed HTML5 video previews may
   still be stripped — the saved MP4 lives on disk under `videos/` (which
   is gitignored). If an individual notebook grows past ~5 MB consider
   moving it onto Git LFS via `.gitattributes`.
2. **Self-contained.** Each notebook prints library versions in cell 1, downloads
   any required data via `plate_model_manager` (so no manual setup), and
   produces at least one figure.
3. **Three-section header.** Title + one-paragraph motivation, learning
   objectives, prerequisites/runtime.
4. **CONFIGURATION block.** A `# === USER CONFIGURATION ===` cell immediately
   after the imports surfaces model name, snapshot time, region, anchor
   plate, and any other user-tunable knob as named constants.
5. **In-frame `{time} Ma` stamp.** Every pyGMT figure draws a
   `fig.text(... position="TL" ...)` stamp as the *last* layer so it
   sits on top of all coast/grdimage layers.
6. **Closing "Extend this" section.** Suggestions for follow-up modifications.

## Recommended environment

```bash
conda create -n gplately-pygmt -c conda-forge gplately pygmt jupyter
conda activate gplately-pygmt
jupyter lab
```

(GPlately's docker image works too: `gplates/gplately`.)

## External data dependencies

Most notebooks fetch what they need on the fly — plate models via `plate_model_manager`, fossil occurrences via the Paleobiology Database / Macrostrat APIs, plate-tectonic information via the GPlates Web Service, etc. — so cloning this repo and `conda`-installing the environment above is enough to run them.

A small number of notebooks rely on companion data clones that are too large (or licensed separately) to bundle into this repository. The notebooks look for them under `./external/<dataset>` first, then fall back to an environment variable. Provide them as either symlinks or env-var overrides — whichever fits your machine:

| Used by | Dataset | Default location |
|---|---|---|
| T19 - T22 | [Dynamic-Topography-and-Great-Unconformity (Santosh Dhungana)](https://github.com/santoshdhungana/Dynamic-Topography-and-Great-Unconformity) — gld504 plate model + mantle-convection NetCDFs | `./external/Dynamic-Topography-and-Great-Unconformity/` or `SANTOSH_REPO=...` |
| T23 | [Scotese & Wright 2018 PaleoDEMs](https://www.earthbyte.org/paleodem-resource-scotese-and-wright-2018/) — 88 NetCDFs (1°) | `./external/PaleoDEMs_Scotese_Wright_2018_1deg/` or `PALEODEM_DIR=...` |
| T32 | Geochemistry-corrected paleotopography (NetCDFs from Zhou, Müller & Farahbakhsh, in review) | `./external/Paleotopo_data_assimilation/` or `PALEOTOPO_REPO=...` |
| T44 | [pySCION (Mills & Gurung 2025)](https://github.com/bjwmills/pySCION) — Python source for the SCION Earth-evolution model | `./external/pySCION/` or `PYSCION_REPO=...` |

Set up once with symlinks:

```bash
cd <path-to-this-repo>
mkdir -p external
ln -sfn ~/path/to/Dynamic-Topography-and-Great-Unconformity \
    external/Dynamic-Topography-and-Great-Unconformity
ln -sfn ~/path/to/Scotese_Wright_2018_PaleoDEMs \
    external/PaleoDEMs_Scotese_Wright_2018_1deg
ln -sfn ~/path/to/Paleotopo_data_assimilation \
    external/Paleotopo_data_assimilation
ln -sfn ~/path/to/pySCION \
    external/pySCION
```

`external/` is gitignored and never pushed.

## Recommended starting points for newcomers / undergraduates

For users new to plate reconstructions in Python, a good entry sequence is:

- **T01 — Hello, deep time.** First pyGMT paleo-map; introduces the GPlately + pyGMT plumbing.
- **T02 — GPlates Web Service from Python.** Pure HTTP-REST workflow: reconstruct modern-city paleo-positions through deep time using nothing more than `requests` + `pygmt`. Doesn't require a local `pygplates` install, which makes it the lowest-barrier entry point in the suite — excellent for a teaching lab where install friction is the bottleneck.
- **T03 — Projection cookbook.** The cartographic foundation the rest of the suite leans on.
- **T04 — Multi-model diff maps** and **T05 — Comparing rotation models**, once T01-T03 are comfortable — these show how to reason about model choice rather than treat any one model as ground truth.
- **T10 — Paleobathymetry profile across the Atlantic at 50 Ma** as the first application notebook that turns the workflow into a concrete cross-section.

## Index

### Cluster A — Getting started / core workflows
| # | Notebook | Audience | Difficulty |
|---|----------|----------|------------|
| T01 | [Hello, deep time](T01_Hello_Deep_Time.ipynb) | undergrad | ★☆☆ |
| T02 | [GPlates Web Service from Python: paleo-trajectories of modern cities](T02_GPlates_Web_Service_Python.ipynb) | undergrad | ★☆☆ |
| T03 | [Projection cookbook](T03_Projection_Cookbook.ipynb) | undergrad | ★☆☆ |
| T04 | [Multi-model diff maps](T04_Multi_Model_Diff_Maps.ipynb) | undergrad | ★☆☆ |
| T05 | [Comparing rotation models: how the choice of plate reconstruction redraws paleo-geography](T05_Rotation_Model_Comparison.ipynb) | undergrad | ★☆☆ |
| T06 | [Animations](T06_Plate_Motion_Animation.ipynb) | undergrad | ★☆☆ |
| T07 | [Interactive paleo-Earth with Panel + pyGMT](T07_Interactive_Paleo_Earth.ipynb) | undergrad | ★☆☆ |

### Cluster B — Plate kinematics + tectonics
| # | Notebook | Audience | Difficulty |
|---|----------|----------|------------|
| T08 | [Plate-tectonic diagnostics through deep time](T08_Plate_Tectonic_Diagnostics.ipynb) | both | ★★☆ |
| T09 | [Age of subducting crust](T09_Age_of_Subducting_Crust.ipynb) | both | ★★☆ |
| T10 | [Paleobathymetry profile across the Atlantic at 50 Ma](T10_Paleobathymetry_Profile.ipynb) | both | ★★☆ |
| T11 | [Paleo-strain rate maps](T11_Paleo_Strain_Rate_Maps.ipynb) | both | ★★☆ |
| T12 | [Retrodeforming a global lithospheric-thickness grid through deep time](T12_Paleo_Lithospheric_Thickness_Retrodeformed.ipynb) | postgrad | ★★★ |
| T13 | [Paleo-σHmax along the Andean subduction zone](T13_Paleo_SHmax_Subduction.ipynb) | both | ★★☆ |

### Cluster C — Zircons + tectonic-setting predictors
| # | Notebook | Audience | Difficulty |
|---|----------|----------|------------|
| T14 | [Detrital zircons through deep time](T14_Detrital_Zircons_Reconstructed.ipynb) | postgrad | ★★★ |
| T15 | [Igneous zircons through deep time](T15_Igneous_Zircons_Reconstructed.ipynb) | postgrad | ★★★ |
| T16 | [Metamorphic zircons through deep time](T16_Metamorphic_Zircons_Reconstructed.ipynb) | postgrad | ★★★ |
| T17 | [Detrital-zircon paleo-distance to the nearest subduction zone](T17_Detrital_Zircon_Distance_to_Subduction.ipynb) | postgrad | ★★★ |

### Cluster D — Mantle dynamics + dynamic topography
| # | Notebook | Audience | Difficulty |
|---|----------|----------|------------|
| T18 | [REVEAL tomography slices with reconstructed plate boundaries](T18_REVEAL_Tomography_Slices.ipynb) | postgrad | ★★★ |
| T19 | [Paleo-mantle structure beneath a moving plate: a great-circle transect through deep time](T19_Paleo_Mantle_Transect_DeepTime.ipynb) | postgrad | ★★★ |
| T20 | [Clustering plate-frame dynamic-topography histories with k-means](T20_DT_History_Clustering.ipynb) | postgrad | ★★★ |
| T21 | [Coupling dynamic topography to preserved sediment flux on every continent](T21_DT_vs_Sediment_Flux.ipynb) | postgrad | ★★★ |
| T22 | [Dynamic topography change in deep time — Young 2022 plate-frame Δz over 20-Myr intervals at 10 snapshot ages 900-0 Ma](T22_dynamic_topo_change_in_deep_time.ipynb) | postgrad | ★★★ |

### Cluster E — Paleomagnetism
| # | Notebook | Audience | Difficulty |
|---|----------|----------|------------|
| T24 | [Building a Paleomagnetic Reference Frame from the Global Paleomagnetic Database](T24_Paleomagnetic_Reference_Frame.ipynb) | postgrad | ★★★ |
| T25 | [Comparing Alternative Paleomagnetic Reference Frames in Reconstructions](T25_Comparing_Reference_Frames.ipynb) | postgrad | ★★★ |
| T26 | [Beyond `pt_rot`: continent reconstruction with `gplately` instead of hard-coded Euler poles](T26_Continent_Rotation_gplately.ipynb) | postgrad | ★★★ |
| T27 | [Predicted paleolatitude from an APWP vs a `gplately` paleo-site](T27_APWP_vs_Reconstructed_Site.ipynb) | postgrad | ★★★ |
| T28 | [Round-trip consistency: a Laurentia paleomagnetic pole at 1.1 Ga, on reconstructed Laurentia](T28_Osler_VGP_Laurentia_1100Ma.ipynb) | postgrad | ★★★ |
| T29 | [A Phanerozoic apparent polar wander path draped on reconstructed Laurentia](T29_Phanerozoic_APWP_on_Reconstructed_Laurentia.ipynb) | postgrad | ★★★ |
| T30 | [Inclination shallowing meets plate reconstruction: a corrected sedimentary paleolatitude on a reconstructed site](T30_SVEI_Inclination_Shallowing_Reconstructed.ipynb) | postgrad | ★★★ |
| T31 | [Rotating paleomagnetic poles into reconstructed plate frames](T31_Rotated_Paleo_Poles.ipynb) | postgrad | ★★★ |

### Cluster F — Paleo-geography + paleo-topography (incl. Central Asia thermochronology)
| # | Notebook | Audience | Difficulty |
|---|----------|----------|------------|
| T32 | [Geochemistry-corrected paleo-elevation: from samples to comparison](T32_Geochem_Corrected_Paleo_Elevation.ipynb) | postgrad | ★★☆ |
| T33 | [Macrostrat sedimentary units in paleo-position: mapping the Great Unconformity](T33_Macrostrat_Paleo_Position.ipynb) | postgrad | ★★☆ |
| T49 | [Highland footprints in deep time: probabilistic elevation thresholds + bias-aware DBSCAN](T49_Highland_Footprints_DBSCAN.ipynb) (author-contributed by J. Zhou — reproduces Fig. 4 of Zhou et al. 2026 *Geology*) | postgrad | ★★★ |
| T50 | [Cooling rates × Earth-system overlays: multi-layer paleo-Earth maps](T50_Cooling_Earth_System_Overlays.ipynb) (Central Asian thermochronology after Boone et al. 2025 *Comm. Earth Env.*; cooling-rate dots over seafloor age, dynamic topography, paleotopography) | postgrad | ★★☆ |
| T51 | [Cooling rates × plate kinematics × fault analysis](T51_Cooling_Kinematics_Faults.ipynb) (after Boone et al. 2025; convergence rate + trench migration maps + fault proximity + rose diagrams) | postgrad | ★★★ |
| T52 | [Cooling-rate correlations + time-series analysis](T52_Cooling_Rate_Correlations.ipynb) (cross-variable scatter, Pearson r per age, per-age means ± SD) | postgrad | ★★★ |

### Cluster G — Paleo-biogeography
| # | Notebook | Audience | Difficulty |
|---|----------|----------|------------|
| T34 | [Joining PBDB occurrences with Macrostrat lithology in paleo-coordinates](T34_PBDB_Macrostrat_Paleo_Litho.ipynb) | undergrad+ | ★★☆ |
| T35 | [Reconstructing fossil corals: paleolatitude and reef habitat through time](T35_Reef_Builders_Paleolatitude.ipynb) | undergrad+ | ★★☆ |
| T36 | [Kimmeridgian dinosaurs on a Late Jurassic paleoclimate reconstruction](T36_Kimmeridgian_Dinosaurs.ipynb) | undergrad+ | ★★☆ |
| T37 | [Cenozoic planktonic foraminifera on reconstructed paleo-latitude](T37_Cenozoic_Foraminifera_Paleo_Latitude.ipynb) | undergrad+ | ★★☆ |

### Cluster H — Paleo-climate
| # | Notebook | Audience | Difficulty |
|---|----------|----------|------------|
| T38 | [Phanerozoic Köppen-Geiger climate belts on reconstructed plates](T38_Koppen_Geiger_Paleo_Belts.ipynb) | postgrad | ★★★ |
| T39 | [HadCM3 paleoclimate snapshots regridded onto reconstructed coastlines](T39_HadCM3_Paleoclimate_Snapshots.ipynb) | postgrad | ★★★ |
| T40 | [Model-data comparison: cGENIE paleo-SST against proxy sites reconstructed with GPlately](T39_cGENIE_SST_vs_Proxies.ipynb) | postgrad | ★★★ |
| T41 | [Bayesian SST from δ18O at paleo-sites with `bayfox` and GPlately](T41_Bayfox_SST_at_Paleo_Sites.ipynb) | postgrad | ★★★ |
| T42 | [SCION end-Permian SAT on a reconstructed paleo-Earth](T42_SCION_SAT_On_Permian_Reconstruction.ipynb) | postgrad | ★★★ |
| T43 | [End-Permian CO₂-sensitivity ensemble (end-Permian CO₂-sensitivity ensemble; pySCION (Mills & Gurung 2025); ensemble computed by A.M. for this study)](T43_SCION_CO2_Sensitivity_252Ma.ipynb) | postgrad | ★★★ |
| T44 | [pySCION Phanerozoic biogeochemistry on a reconstructed paleo-Earth](T43_pySCION_Phanerozoic_Biogeochemistry.ipynb) | postgrad | ★★★ |

### Cluster I — Mineral exploration
| # | Notebook | Audience | Difficulty |
|---|----------|----------|------------|
| T45 | [Paleo-prospectivity of porphyry Cu-Au in the SW-Pacific arc system](T45_SW_Pacific_Porphyry_Prospectivity.ipynb) | postgrad | ★★★ |
| T46 | [Global porphyry-Cu paleo-prospectivity through subduction kinematics](T46_Global_Porphyry_Kinematic_Envelope.ipynb) | postgrad | ★★★ |
| T47 | [Seafloor age-grid anomalies as porphyry-Cu predictors through time (Mather et al. 2025)](T47_Seafloor_Anomalies_Porphyry_Cu.ipynb) | postgrad | ★★★ |
| T48 | [Sediment-hosted Cu deposits on reconstructed paleo-Earth](T48_Sediment_Hosted_Cu_Reconstructed.ipynb) | postgrad | ★★★ |

## See also: rgplates (R-language equivalent)

Kocsis, Raja, Williams & Dowding's [`rgplates`](https://github.com/GPlates/rgplates) R package covers a subset of this Python tutorial suite's scope — point/polygon reconstruction via the GPlates Web Service or local GPlates Desktop install. T21 (continent rotation) and T31 (PBDB×Macrostrat) include explicit cross-references to the corresponding rgplates vignettes. The two tools are designed to complement, not compete with, each other: choose the one that fits your downstream stack (R/`sf`/`chronosphere` → `rgplates`; Python/`xarray`/`pygmt` → this suite).

