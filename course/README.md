# GPlates and Beyond: Reproducible Workflows to Investigate Deep Time Earth Evolution

Short course at the meeting of the Geological Society of Australia Specialist Group in Earth Systems Science (SGESS), Hobart, February 2027. Two hours, hands-on, on your own laptop.

The course starts with a brief demonstration of GPlates, the desktop application for plate reconstructions, and then moves to Python, where GPlately and pyGMT turn the same plate models into scripted, repeatable workflows. You run ready-made notebooks from the GPlately-pyGMT tutorial suite, change a few settings in each, and see how geological, climate, ocean and mineral-deposit data look when they are carried back in time with the plates. No Python experience beyond the basics is assumed: every notebook runs from top to bottom as it is, and each step below tells you which single line to edit.

## Before the course

Please set up your laptop at home, a few days before the course. It takes about 30 minutes, most of it downloading.

1. Follow [SETUP.md](SETUP.md): install Miniforge, download this tutorial suite, create the `gplately-pygmt` environment.
2. Run the setup check: `python course/setup_check.py`. It tests the installation, draws a test map, downloads the plate models used in the course and prepares notebook F02. It finishes with `READY` when your laptop is set.

The venue Wi-Fi cannot handle thirty people downloading plate models at once, so the setup check matters. If it reports a problem you cannot fix, email its output to the course organiser before the course.

## Programme (120 minutes)

| Time | Session | What you do |
|---|---|---|
| 0:00 | **Welcome and aims** | Check that JupyterLab opens; three minutes on running a notebook |
| 0:08 | **GPlates in fifteen minutes** (demonstration) | Watch a plate model being loaded, reconstructed, animated and exported. The steps are in [GPLATES_DEMO.md](GPLATES_DEMO.md) so you can repeat them later |
| 0:23 | **From GPlates to Python** | How pyGPlates, GPlately, the Plate Model Manager and pyGMT fit together; mantle and paleomagnetic reference frames; the anatomy of a tutorial notebook |
| 0:33 | **Tutorial 1: A01 Hello, deep time** | Reconstruct the world at any age between 0 and 410 Ma |
| 0:45 | **Tutorial 2: B04 How Asia deforms** | Strain rates in the India–Asia collision zone through the Cenozoic |
| 0:55 | **Tutorial 3: E01 Seismic tomography through time** | Match slabs in the mantle with the trenches that fed them |
| 1:05 | *Break and catch-up* | |
| 1:10 | **Themed track** (choose one) | Paleo-sedimentology and climate, Oceans and climate, or Mineral deposits: two notebooks each, a third for the quick |
| 1:40 | **Tutorial 4: F02 How certain is a paleolatitude?** | Compare the paleolatitudes of continents in two paleomagnetic reference frames |
| 1:52 | **Wrap-up** | A checklist for reproducible deep-time work, how to cite, where to go next |

Step-by-step instructions for every tutorial are in [TUTORIALS.md](TUTORIALS.md).

## The notebooks

All notebooks below run from files bundled with the suite or downloaded by the setup check. None needs the separate Zenodo data archive.

| Session | Notebook | Plate model | Runtime |
|---|---|---|---|
| Tutorial 1 | [A01 Hello, deep time](../Notebooks/A01_Hello_Deep_Time.ipynb) | Zahirovic et al. (2022) | < 1 min |
| Tutorial 2 | [B04 Paleo-strain rate maps](../Notebooks/B04_Paleo_Strain_Rate_Maps.ipynb) | Zahirovic et al. (2022) | < 1 min |
| Tutorial 3 | [E01 REVEAL tomography slices](../Notebooks/E01_REVEAL_Tomography_Slices.ipynb) | Zahirovic et al. (2022) | < 1 min |
| Tutorial 4 | [F02 Comparing paleomagnetic reference frames](../Notebooks/F02_Comparing_Reference_Frames.ipynb) (sections 1–2) | Zahirovic et al. (2022) | ≈ 1 min |
| Track S | [J01 Climate-sensitive lithologies](../Notebooks/J01_Boucot_Climate_Sensitive_Lithologies.ipynb) | Zahirovic et al. (2022) | < 1 min |
| Track S | [G03 Macrostrat units in paleo-position](../Notebooks/G03_Macrostrat_Paleo_Position.ipynb) | Cao et al. (2024) | < 1 min (online) |
| Track S, extra | [I01 PBDB fossils joined with Macrostrat](../Notebooks/I01_PBDB_Macrostrat_Paleo_Litho.ipynb) | Merdith et al. (2021) | ≈ 1 min (online) |
| Track O | [J04 Model sea-surface temperatures against proxies](../Notebooks/J04_GENIE_SST_vs_DeepMIP_Proxies.ipynb) | Zahirovic et al. (2022) | < 1 min |
| Track O | [B03 Paleobathymetry profile across the Atlantic](../Notebooks/B03_Paleobathymetry_Profile.ipynb) | Zahirovic et al. (2022) | ≈ 1 min |
| Track O, extra | [J03 Deep-time climate model snapshots](../Notebooks/J03_Deep_Time_Paleoclimate_Snapshots.ipynb) | Zahirovic et al. (2022) | < 1 min |
| Track M | [K04 Sediment-hosted copper deposits](../Notebooks/K04_Sediment_Hosted_Cu_Reconstructed.ipynb) | Cao et al. (2024) | ≈ 1 min |
| Track M | [K01 Porphyry Cu-Au in the SW Pacific](../Notebooks/K01_SW_Pacific_Porphyry_Prospectivity.ipynb) | Zahirovic et al. (2022) | < 1 min |
| Track M, extra | [K05 Porphyry trajectories in the North American Cordillera](../Notebooks/K05_Deep_Time_Porphyry_Trajectories.ipynb) | Alfonso et al. (2024) | ≈ 1 min |
| Any time | [A02 GPlates Web Service](../Notebooks/A02_GPlates_Web_Service_Python.ipynb) | Merdith et al. (2021) | ≈ 1 min (online) |

A02 reconstructs points through the GPlates Web Service, so it also works on a laptop where the full installation failed.

## After the course

The suite has 80 notebooks in 11 themes; the full list is in [Notebooks/README.md](../Notebooks/README.md). The companion paper is Müller et al., *Extending pyGMT into Deep Time with GPlately*, Geochemistry, Geophysics, Geosystems (2026). To cite the version of the suite you used, use the DOI on the [front page](../README.md) of this repository.

## Course materials in this folder

| File | Contents |
|---|---|
| [SETUP.md](SETUP.md) | Installation, step by step, for macOS, Windows and Linux |
| [setup_check.py](setup_check.py) | Tests the installation and downloads the plate models |
| [GPLATES_DEMO.md](GPLATES_DEMO.md) | The GPlates demonstration, as steps you can repeat |
| [TUTORIALS.md](TUTORIALS.md) | What to run, what to change and what to look for in every notebook of the course |
