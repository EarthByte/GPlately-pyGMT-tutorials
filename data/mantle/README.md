# Mantle / dynamic-topography data — required by T24, T25, T27, T28

Time-dependent mantle netCDF cubes from Dhungana & Flament's
*Deep Earth Origin of the Great Unconformity* online supplement.
Each cube is typically 100+ MB, so they are **not bundled** here.

## How to get them

Santosh's source repo uses Git LFS, so cloning needs LFS support:

    # one-time install (if you don't already have it)
    brew install git-lfs        # macOS — or apt install git-lfs on Linux
    git lfs install             # global hook

    # then clone normally — LFS pull is automatic
    git clone https://github.com/santosh-dhungana/Dynamic-Topography-and-Great-Unconformity

## Files referenced by the notebooks in this folder

After cloning, copy these out of his repo and into this directory:

    muller2019_T_anomaly_subsampled.nc     used by T24
    muller2019_DT_cube.nc                  used by T25, T27, T28

The notebooks' Configuration cell uses `MANTLE_NCFILE` / `DT_NCFILE`
constants — point those at the local path of whichever cube you want
to run. The notebooks make no assumption about which simulation
produced the field; any `(time, depth, lat, lon)` or `(time, lat, lon)`
raster is fine.
