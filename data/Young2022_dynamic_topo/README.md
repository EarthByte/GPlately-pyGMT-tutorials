# Young 2022 dynamic topography (gld428) + M21 NNR plate model

This folder contains the mantle-flow-derived dynamic topography (DT) grids of **Young, Flament, Williams, Merdith, Cao, Müller & Zahirovic (2022)** in their two production cadences and both reference frames, plus the **M21 NNR** (Merdith 2021 no-net-rotation) plate model that the geodynamic simulation ran in. It is the input substrate for tutorial **T78** (mantle → plate → difference walkthrough) and is the same product referenced by **T29** (deep-time DT change) and **T48** (North America thermochronology). Total footprint ≈ 1 GB.

## Layout

```
Young2022_dynamic_topo/
├── README.md                          this file
├── plate_model/                       M21 NNR — Merdith 2021 no-net-rotation
│   ├── *.rot                          rotation files (0-1000 Ma)
│   ├── *.gpml                         topologies, continents, cratons
│   └── M21NNR.gproj                   GPlates project file
├── mantle_frame/                      DT in the mantle (absolute) frame
│   ├── 5my_0-250Ma/                   51 grids at 5-Myr cadence (.nc)
│   └── 20my_0-960Ma/                  49 grids at 20-Myr cadence (.grd)
└── plate_frame/                       DT in the plate frame (present-day positions)
    ├── 5my_0-250Ma/                   51 grids + 51 ocean-masked siblings (.nc)
    └── 20my_0-960Ma/                  51 grids at 20-Myr cadence (.nc)
```

## What the two reference frames mean

- **Mantle frame** — DT at a fixed position in the mantle. This is what the convection model outputs directly. Differencing two mantle-frame grids at the same (lon, lat) compares *different crustal columns* at the two times, because the plate slides over the mantle. Correct use: single-snapshot maps only.

- **Plate frame** — DT rotated so that each plate's DT is attached to its present-day position. Now the (lon, lat) of a cell is a fixed piece of continental crust across time. Differencing two plate-frame grids gives the actual DT change *each crustal column* experienced. Correct use: differencing, per-column history, tectonic-substrate reasoning. T78 walks through the mantle → plate rotation step-by-step.

## Filename conventions

| Folder | Example file | Age extraction regex |
|---|---|---|
| mantle_frame/5my_0-250Ma/  | `gld428DT_MFgrid100_corrected.nc`      | `MFgrid(\d+)_corrected` |
| mantle_frame/20my_0-960Ma/ | `gld428DT_MantleFrameGrid100.grd`       | `MantleFrameGrid(\d+)` |
| plate_frame/5my_0-250Ma/   | `100.00.nc`, `Masked_100.00.nc`         | `^(?:Masked_)?(\d+)\.\d+` |
| plate_frame/20my_0-960Ma/  | `gld428_PlateFrameGrid100.nc`           | `PlateFrameGrid(\d+)` |

`Masked_*` files in `plate_frame/5my_0-250Ma/` are ocean-masked siblings of the canonical `<age>.00.nc` files — skip them when scanning by age unless you specifically want the ocean-masked field.

## Loading recipes

```python
import xarray as xr
from glob import glob

# 20-Myr plate-frame grid at 500 Ma
da = xr.open_dataset("data/Young2022_dynamic_topo/plate_frame/20my_0-960Ma/"
                     "gld428_PlateFrameGrid500.nc")["z"]

# 5-Myr mantle-frame grid at 100 Ma
da = xr.open_dataset("data/Young2022_dynamic_topo/mantle_frame/5my_0-250Ma/"
                     "gld428DT_MFgrid100_corrected.nc")["z"]

# Load the plate model
import pygplates
rot_files = sorted(glob("data/Young2022_dynamic_topo/plate_model/*.rot"))
rot = pygplates.RotationModel(rot_files)
topo = [pygplates.FeatureCollection(f)
        for f in glob("data/Young2022_dynamic_topo/plate_model/*Topologies*.gpml")]
```

## References

- **Young, A., Flament, N., Williams, S.E., Merdith, A., Cao, X., Müller, R.D. & Zahirovic, S. (2022)**. Long-term Phanerozoic sea level change from solid Earth processes. *Earth and Planetary Science Letters* 584, 117451. [doi:10.1016/j.epsl.2022.117451](https://doi.org/10.1016/j.epsl.2022.117451) — the geodynamic model that produced `gld428`.
- **Merdith, A.S., Williams, S.E., Collins, A.S., Tetley, M.G., Mulder, J.A., Blades, M.L., Young, A., Armistead, S.E., Cannon, J., Zahirovic, S. & Müller, R.D. (2021)**. Extending full-plate tectonic models into deep time: Linking the Neoproterozoic and the Phanerozoic. *Earth-Science Reviews* 214, 103477. [doi:10.1016/j.earscirev.2020.103477](https://doi.org/10.1016/j.earscirev.2020.103477) — the M21 plate model; the NNR variant here is the same kinematics rotated into a no-net-rotation absolute frame used to drive the geodynamic simulation.
- **Mather, B.R., Müller, R.D., Zahirovic, S., et al. (2024)**. Deep time spatio-temporal data analysis using GPlately. *Geoscience Data Journal* 11, 3-10. [doi:10.1002/gdj3.185](https://doi.org/10.1002/gdj3.185) — the toolkit used by all consumer notebooks.

## Consumer notebooks

- **T29** — Dynamic-topography change through deep time (differencing in plate frame).
- **T48** — North America thermochronology with DT overlay.
- **T78** — Mantle → plate → difference reference-frame walkthrough (this tutorial explains, step-by-step, the rotation the other two apply silently).

## License

The gld428 grids and the M21 NNR plate model are redistributed under **CC BY 4.0** with attribution to Young et al. (2022) and Merdith et al. (2021). See the parent CHANGELOG for the Zenodo companion-archive DOI once published.
