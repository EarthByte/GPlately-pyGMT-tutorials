# Tutorial notes

These notes go with the short course [GPlates and Beyond](README.md). Each tutorial tells you which notebook to open, what to look at in its figures, and which single line to change to make the notebook your own. You do not need to write code. If you fall behind, skip ahead to where the group is; every notebook runs on its own.

## Working with a notebook

Start JupyterLab as described in [SETUP.md](SETUP.md) ("On the day"). In the file panel on the left, open the `Notebooks/` folder and double-click a notebook to open it.

- A notebook is a column of **cells**. Text cells explain; code cells (grey, with `[ ]:` on the left) do the work.
- **Shift+Enter** runs the selected cell and moves to the next one. **Run > Run All Cells** runs the whole notebook from the top. While a cell runs, its label shows `[*]`; when it has finished, it shows a number.
- Every notebook has a **Configuration** cell near the top, framed by `=== USER CONFIGURATION ===`. This is the only cell you need to edit. Change a value, then choose **Run > Run All Cells** again so every figure is redrawn with the new setting.
- If something seems stuck, choose **Kernel > Interrupt Kernel**. If a notebook behaves strangely, **Kernel > Restart Kernel and Run All Cells** starts it afresh.
- To keep the original intact, save your edited version under a new name first: **File > Save Notebook As…**

Ages are in Ma (millions of years ago). Plate models are named as in the Plate Model Manager, for example `"Zahirovic2022"` or `"Cao2024"`; text values keep their quotation marks.

---

## Tutorial 1 — A01 Hello, deep time (12 minutes)

**Notebook:** `A01_Hello_Deep_Time.ipynb`

**What it does.** Downloads (or, after the setup check, reads) the Zahirovic et al. (2022) plate model by name, reconstructs coastlines, continents and plate boundaries to 50 Ma, and draws them with pyGMT: mid-ocean ridges in red, subduction zones in blue with teeth on the overriding plate.

**Do this**

1. Open the notebook and choose **Run > Run All Cells**. The map appears after about half a minute.
2. Find India south of Asia, the narrow gap between Australia and Antarctica, and the North Atlantic, open only south of Greenland.

**Make it yours.** In the Configuration cell, change

```python
RECONSTRUCTION_TIME  = 50.0
```

to `150.0`, then to `250.0`, and run all cells after each change. The model covers 0–410 Ma.

**Think about.** At 250 Ma the continents form Pangea. Where are the subduction zones, and what happened to the ocean floor that existed then?

---

## Tutorial 2 — B04 How Asia deforms (10 minutes)

**Notebook:** `B04_Paleo_Strain_Rate_Maps.ipynb`

**What it does.** The Zahirovic et al. (2022) model includes deforming networks: regions such as Tibet and Indonesia where the crust does not move as a rigid plate. The notebook maps how fast that crust is stretching or shortening (the dilatation rate), with plate motions shown as arrows, for today, 10 Ma and 30 Ma, with Eurasia held fixed.

**Do this**

1. **Run > Run All Cells** (about half a minute).
2. Blue means shortening and thickening (collision, fold-and-thrust belts), red means extension (rifts, back-arc basins). Follow the blue band along the Himalaya and the extension in eastern China and the South China Sea.

**Make it yours.** In the Configuration cell, change the snapshot times, for example

```python
SNAPSHOT_TIMES = (0, 20, 40)
```

or move the map to the Mediterranean with `INDO_AUS_REGION = (-10, 45, 25, 50)`.

**Think about.** How does the pattern of shortening change as India moves north? When does the collision zone first appear in the model?

---

## Tutorial 3 — E01 Seismic tomography through time (10 minutes)

**Notebook:** `E01_REVEAL_Tomography_Slices.ipynb`

**What it does.** Seismic tomography images cold, fast slabs (blue) deep in the mantle. If slabs sink at a known speed, each depth corresponds to an age at which that slab was at the surface. The notebook converts depth to age with a sinking speed of 5 cm/yr in the upper mantle and 1.3 cm/yr in the lower mantle, and draws the subduction zones of that age on top of a slice through the REVEAL tomography model.

**Do this**

1. **Run > Run All Cells** (about a minute, because it prepares frames for the slider at the end).
2. On the 1500 km map (≈78 Ma), look for subduction-zone teeth sitting on blue patches, for example under the Americas and the western Pacific.
3. Scroll to the end and drag the **depth slider** from 500 to 2500 km.

**Make it yours.** In the Configuration cell, try another depth or a slower lower mantle:

```python
DEPTH_KM             = 2000
V_LOWER_CMYR         = 1.1
```

Bundled depths are 500, 650, 850, 1000, 1250, 1500, 1750, 2000, 2250 and 2500 km.

**Think about.** Where do the teeth fall on blue anomalies, and where not? What would make the match fail: the sinking speed, the plate model, or slabs that do not sink vertically?

---

## Themed tracks (30 minutes)

Choose one track. Run the first two notebooks; the third is for those who finish early. Each takes about a minute to run.

### Track S — Paleo-sedimentology and climate

**J01 Climate-sensitive lithologies** (`J01_Boucot_Climate_Sensitive_Lithologies.ipynb`). Coals, evaporites, bauxites, tillites and other climate-indicative rocks and fossils compiled by Boucot et al. (2013), reconstructed with the plates and coloured by climate zone, at six ages from 410 to 15 Ma, followed by a slider through all ages.

- Look for evaporites in the subtropical arid belts and tillites near the poles, and how both belts move as continents drift.
- Change `SNAPSHOT_TIMES = (410.0, 320.0, 250.0, 145.0, 65.0, 15.0)` to ages of your choice (up to 410 Ma).

**G03 Macrostrat sedimentary units** (`G03_Macrostrat_Paleo_Position.ipynb`). Queries the Macrostrat database live for sedimentary units of the Sauk and Tippecanoe transgressions (635–472 Ma) and plots them at their positions at 540 Ma on the Cao et al. (2024) model: the record above the Great Unconformity of Laurentia. Needs internet.

- Look at where Laurentia lay at 540 Ma, and at the gaps where no sediment of this age survives.
- Change `AGE_RANGE_MA` and `TARGET_TIME`, for example `AGE_RANGE_MA = (252.0, 300.0)` and `TARGET_TIME = 280.0` for the Permian.

**Extra: I01 Fossils and lithology** (`I01_PBDB_Macrostrat_Paleo_Litho.ipynb`). Ordovician brachiopods from the Paleobiology Database, joined to the lithology of the nearest Macrostrat unit and mapped at 470 Ma. Change `TAXON_NAME = "Brachiopoda"` to `"Trilobita"` or `"Bryozoa"`. Needs internet.

### Track O — Oceans and climate

**J04 Model sea-surface temperatures against proxies** (`J04_GENIE_SST_vs_DeepMIP_Proxies.ipynb`). Early Eocene (≈50 Ma) sea-surface temperatures from a PLASIM-GENIE climate simulation (Leonard et al., 2025), compared with the DeepMIP proxy compilation (Hollis et al., 2019) after the proxy sites have been reconstructed with the same plate model and reference frame as the simulation.

- Find the high-latitude sites in the southwest Pacific where the proxies are much warmer than the model, and the flatter pole-to-equator gradient of the proxies.
- Change `DEEPMIP_SUBSET = "v1"` to `"v2"` to include all proxy estimates, and see how the misfit changes.

**B03 Paleobathymetry across the Atlantic** (`B03_Paleobathymetry_Profile.ipynb`). Converts the seafloor age grid of 50 Ma to basement depth with the half-space cooling relation (depth = 2500 + 350√age) and draws a depth profile along the great circle between the reconstructed positions of New York and Lisbon.

- Find the mid-Atlantic ridge (shallowest point) and the oldest, deepest crust next to North America.
- Change `RECONSTRUCTION_TIME` to `100.0` or `20.0`, or draw a South Atlantic profile with `PROFILE_START = (-43.2, -22.9)` and `PROFILE_END = (13.2, -8.8)` (Rio de Janeiro to Luanda).

**Extra: J03 Deep-time climate snapshots** (`J03_Deep_Time_Paleoclimate_Snapshots.ipynb`). Surface air temperature of the end-Permian hothouse (252 Ma, 8960 ppm CO₂) on its reconstructed coastlines, next to the modern climate and the difference between the two.

### Track M — Mineral deposits

**K04 Sediment-hosted copper** (`K04_Sediment_Hosted_Cu_Reconstructed.ipynb`). The 785 deposits of the USGS sediment-hosted copper database (Cox et al., 2003), reconstructed to the ages of their host rocks on the Cao et al. (2024) model, at six ages from 50 to 1450 Ma. Symbol size shows contained copper.

- Note that these deposits sit inside continents and on basin margins, away from subduction zones: the Central African Copperbelt at 900 Ma, the Kupferschiefer at 260 Ma.
- Change `SNAPSHOT_TIMES` and `TIME_WINDOW_MA` (how far in age a deposit may be from the map age).

**K01 Porphyry copper–gold in the SW Pacific** (`K01_SW_Pacific_Porphyry_Prospectivity.ipynb`). Cenozoic porphyry deposits of New Guinea and the Solomon Islands (Singer et al., 2008), each reconstructed to its own mineralisation age and measured against the nearest subduction zone at that time: a first-order prospectivity score.

- Compare the deposits' distances from the trench; porphyries form above subduction zones.
- Change `TARGET_TIME = 10.0` to `5.0` or `20.0`, or `REGION` to another arc.

**Extra: K05 Porphyry trajectories in the North American Cordillera** (`K05_Deep_Time_Porphyry_Trajectories.ipynb`). Follows porphyry deposits back through time on the Alfonso et al. (2024) model and relates their formation to the carbonate sediments being subducted beneath the margin.

---

## Tutorial 4 — F02 How certain is a paleolatitude? (12 minutes)

**Notebook:** `F02_Comparing_Reference_Frames.ipynb`

**What it does.** A plate model's absolute positions come from a reference frame. A paleomagnetic frame places the continents relative to the Earth's spin axis, which fixes paleolatitude, the quantity that matters for climate, sedimentation and life. F02 compares two paleomagnetic frames for the same model: the frame built into Zahirovic et al. (2022), and an alternative built from the Global Paleomagnetic Database by notebook F01 (the setup check ran F01 for you).

**Do this.** F02 also renders an animation that takes several minutes, so run only its first two sections:

1. Click into the heading **"3. Animate the difference"**.
2. Choose **Run > Run All Above Selected Cell** (about a minute).
3. In section 1, compare the grey continents (built-in frame) with the blue outlines (alternative frame) at 50, 150, 250 and 350 Ma.
4. In section 2, read the paleolatitude histories of Africa, North America and Australia under both frames.

**Make it yours.** Change `KEY_TIMES = [50, 150, 250, 350]` in the Configuration cell, or change the reference points in section 2 (`REF_POINTS`, given as plate ID, latitude, longitude). Skip section 3; if time allows, click into the heading **"4. Approach 2"** and choose **Run > Run Selected Cell and All Below** for an uncertainty envelope of the paleolatitude of central Australia.

**Think about.** By how many degrees do the two frames differ, and when? Would that difference move a sample from one climate belt into another?

---

## Wrap-up: making your own work reproducible

A deep-time result can be reproduced when someone else can recover every choice behind it. Record these for every figure:

1. **The plate model**, by its Plate Model Manager name and the DOI of the model version (each model folder in `gplately_data/` has a `readme.txt` with it).
2. **The reference frame**: the anchor plate ID (0 for the mantle frame; for Zahirovic et al. 2022, 701701 for its paleomagnetic frame).
3. **The reconstruction age or ages**, and for each data point the age at which it was reconstructed.
4. **The data**, with their DOIs, including the version or download date of databases queried live.
5. **The software**: the `environment.yml` you installed from, and the package versions each notebook prints in its first code cell.
6. **The code**: keep your edited notebooks in a git repository or archive them with your paper, for example on Zenodo.

When you publish work based on the suite, cite the companion paper and the DOI of the suite version you used, which is on the [front page](../README.md) of this repository, together with the plate models and data sets named in each notebook's References section.

## Quick glossary

| Term | Meaning |
|---|---|
| Plate model | A set of files describing how the plates have moved and how their boundaries have changed through time |
| Rotation file | The part of a plate model that gives each plate's position through time as rotations about Euler poles |
| Plate ID | The number that identifies each plate (701 = Africa, 801 = Australia, 101 = North America) |
| Anchor plate | The plate or frame held fixed while everything else moves; 0 is the mantle reference frame |
| Mantle reference frame | Plate positions relative to the deep mantle, based on hotspot tracks and other geodynamic constraints |
| Paleomagnetic reference frame | Plate positions relative to the Earth's spin axis, from paleomagnetic poles; it fixes paleolatitude but not paleolongitude |
| Topologies | Plate boundaries that close into plate polygons at every time step |
| Static polygons | Present-day polygons used to assign a plate ID to any point, such as a sample site |
| Deforming network | A region modelled as continuously deforming rather than as a rigid plate |
| Age grid | A map of the age of the ocean floor at a given time |
| Plate Model Manager | The part of GPlately that downloads published plate models by name |
