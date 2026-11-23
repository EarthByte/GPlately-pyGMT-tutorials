# GPlates in fifteen minutes

This is the demonstration shown at the start of the course, written as steps you can repeat on your own laptop afterwards. It uses GPlates 2.5 and the files of the Zahirovic et al. (2022) plate model that ship with this tutorial suite, so the model you see in GPlates is the same one the notebooks load in Python. Menu names are those of the [GPlates user manual](https://www.gplates.org/docs/user-manual/).

## 0. Install GPlates

Download GPlates 2.5 for your system from <https://www.gplates.org/download/> (macOS Apple silicon or Intel, Windows, Ubuntu) and install it like any other application. GPlates needs no Python.

## 1. Load a plate model

The model files are in the tutorial folder under `data/pmm_cache/zahirovic2022/`. Drag these files into the GPlates main window, or open them with **File > Open Feature Collection** (Ctrl+O; you can select several files at once):

| File | What it is |
|---|---|
| `Rotations/CombinedRotations.rot` | The rotation model: how every plate has moved, as a sequence of finite rotations |
| `Topologies/Plate_Boundaries.gpml` | Plate boundaries that close into plate polygons at every time |
| `Topologies/Feature_Geometries.gpml` | The boundary segments those polygons are built from |
| `Topologies/Deforming_Networks_Active.gpml` | Regions that deform, such as the Andes and Tibet |
| `Coastlines/Global_coastlines_low_res.shp` | Present-day coastlines, cut into pieces that each belong to one plate |
| `ContinentalPolygons/Global_EarthByte_GPlates_PresentDay_ContinentalPolygons.shp` | Continental crust |

The globe now shows today's coastlines, continents and plate boundaries. **Window > Show Layers** (Ctrl+L) lists one layer per file; tick and untick them to see what each one contains.

## 2. Go back in time

- **Reconstruction > Reconstruct to Time…** (Ctrl+T): type `100` and press Enter. Coastlines, continents and plate boundaries move to where the model puts them 100 million years ago.
- Use the time slider and the play button in the main window, or **Reconstruction > Play Animation**, to run the model through time. **Reconstruction > Configure Animation…** sets the time range, step and frames per second.

Watch the Atlantic close, India travel north, Australia separate from Antarctica, and the plate boundaries reorganise.

## 3. Colour by plate and change the frame of reference

- **Features > Manage Colouring** opens the draw-style dialog. Choose **Colour by plate ID**: each plate gets its own colour, which shows how the coastline fragments are assigned to plates.
- **Reconstruction > Specify Anchored Plate ID…** (Ctrl+D) fixes one plate in place. Enter `701` (Africa) or `801` (Australia) and play the animation again: the relative motions are the same, only the viewpoint changes. Enter `0` to return to the mantle reference frame, or `701701` for the model's paleomagnetic frame. Tutorial 4 shows how much the choice of frame matters for paleolatitude.

## 4. Put your own data on the plates

Load `course/sample_sites.geojson` from the tutorial folder: six Australian localities (Hobart, Sydney, Broken Hill, Mount Isa, Kalgoorlie, Ediacara Hills). At first they do not move, because they have no plate ID.

1. Also load `StaticPolygons/Global_EarthByte_GPlates_PresentDay_StaticPlatePolygons.shp` from the model folder.
2. **Features > Assign Plate IDs**: choose the static polygons as the partitioning features and the sample sites as the features to be partitioned, keep **Present day**, and copy the **Reconstruction plate ID**.
3. Reconstruct to 100 Ma again. The sites now travel with Australia.

The same works for your own samples saved as GeoJSON, shapefile or GMT files.

## 5. Export the result

**Reconstruction > Export…** (Ctrl+Shift+E):

1. Choose **Export Time Sequence of Snapshots**, for example from 200 to 0 Ma in steps of 10 Myr.
2. **Add Export**: pick **Reconstructed Geometries** (as Shapefiles or GeoJSON) for the data, and **Image (screenshot)** for a picture of each frame.
3. Choose an output folder and click **Begin Export**.

You now have your sites, the coastlines and the plate boundaries at every time step, ready for a GIS or a map.

**File > Save Project** saves the loaded files, layers and settings so you can reopen the whole session later.

## Why go beyond GPlates?

GPlates is the best way to look at a plate model, check it and edit it. But a figure made by clicking is hard to reproduce: which files were loaded, which anchor plate, which time steps, which colours? The rest of the course does the same things in Python. The Plate Model Manager fetches a published model by name, GPlately reconstructs data with it, and pyGMT draws the map, all recorded in a notebook that anyone can run again and get the same figure.

Further reading: the [GPlates user manual](https://www.gplates.org/docs/user-manual/) and the [GPlates tutorials](https://www.gplates.org/docs/).
