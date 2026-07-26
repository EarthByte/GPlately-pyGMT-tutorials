"""Display-only helpers for the paleoclimate cluster (cluster J: T61-T69).

Three functions that fix the Mollweide/global-map rendering artefacts common
to coarse GCM outputs — grey seam at the antimeridian, NaN slivers at the
poles, and staircase artefacts along the map rim.

Adopted from Andrew Merdith's paleoclimate-cluster-fixes PR (GitHub PR #1,
branch palaeoclimate-cluster-fixes on the amer7632 fork).

**Display-only** — the actual quantitative analysis in each notebook still
uses the native GCM grids. Only the grdimage-facing raster is passed through
`refine_for_plot`.

Usage:

    sys.path.insert(0, str(Path("Notebooks").resolve()))
    from paleoclimate_helpers import refine_for_plot

    da = xr.open_dataarray("data/paleoclimate/some_field.nc")
    da_plot = refine_for_plot(da)   # padded, pole-clamped, resampled to 0.5°
    fig.grdimage(da_plot, cmap=True)
"""

from __future__ import annotations

import numpy as np
import xarray as xr


# ---------------------------------------------------------------------------
# Building blocks
# ---------------------------------------------------------------------------

def close_lon_seam(da: xr.DataArray, lon_name: str = "lon") -> xr.DataArray:
    """Cyclically pad a -180 → +180 grid so grdimage reaches the ±180° seam.

    GCM outputs typically store longitudes as cell centres from ~-180 to
    ~+180 - dlon. When pyGMT infers grid extent from coord min/max, the
    raster stops one half-cell short of the dateline, leaving a grey wedge
    along the antimeridian on Mollweide/Winkel-Tripel maps. This function
    appends a copy of the first column at lon[0]+360 so the grid is cyclic
    from -180 all the way to +180.

    Parameters
    ----------
    da : xr.DataArray
        Global DataArray with a `lon` coordinate (or as named by `lon_name`).
    lon_name : str
        Coordinate name for longitude.

    Returns
    -------
    xr.DataArray
        Cyclically-padded copy.
    """
    lon = da[lon_name].values
    dlon = float(np.diff(lon).mean())
    east_edge = lon[0] + 360.0
    # If the grid already reaches +180 within half a cell, no padding needed
    if abs(lon[-1] + dlon - east_edge) > 1e-6:
        return da
    east_col = da.isel({lon_name: 0}).assign_coords({lon_name: east_edge})
    return xr.concat([da, east_col], dim=lon_name)


def clamp_lat_poles(da: xr.DataArray, lat_name: str = "lat") -> xr.DataArray:
    """Extend the outermost latitude rows to exactly ±90° before plotting.

    Coarse GCM latitudes often stop one cell short of the poles (e.g.
    HadCM3 top row at +87.5°). On a Mollweide projection this leaves a
    NaN sliver at each pole where grdimage has no data to draw. This
    function duplicates the outermost rows and reassigns their latitude to
    ±90°, extending the coverage without changing the interior values.

    Parameters
    ----------
    da : xr.DataArray
        DataArray with a `lat` coordinate.
    lat_name : str
        Coordinate name for latitude.

    Returns
    -------
    xr.DataArray
        Pole-clamped copy.
    """
    lat = da[lat_name].values
    # Determine if latitudes are ascending or descending
    ascending = lat[-1] > lat[0]
    if ascending:
        bottom, top = -90.0, +90.0
    else:
        bottom, top = +90.0, -90.0
    pieces = []
    if not np.isclose(lat[0], bottom):
        first_row = da.isel({lat_name: 0}).assign_coords({lat_name: bottom})
        pieces.append(first_row.expand_dims({lat_name: 1}))
    pieces.append(da)
    if not np.isclose(lat[-1], top):
        last_row = da.isel({lat_name: -1}).assign_coords({lat_name: top})
        pieces.append(last_row.expand_dims({lat_name: 1}))
    if len(pieces) == 1:
        return da
    return xr.concat(pieces, dim=lat_name)


def refine_for_plot(
    da: xr.DataArray,
    lon_name: str = "lon",
    lat_name: str = "lat",
    target_res_deg: float = 0.5,
) -> xr.DataArray:
    """Wrap the longitude seam, clamp the poles, and bilinearly resample onto
    a regular fine grid so pyGMT's grdimage draws a smooth Mollweide rim
    instead of a coarse staircase.

    **Display-only** — do not use the returned DataArray for quantitative
    analysis. Sample the native grid for that.

    Parameters
    ----------
    da : xr.DataArray
        GCM output with (lat, lon) or (lon, lat) coords.
    lon_name, lat_name : str
        Coordinate names.
    target_res_deg : float
        Output grid step in degrees. 0.5° gives a smooth Mollweide rim at
        map widths up to ~22 cm.

    Returns
    -------
    xr.DataArray
        Resampled DataArray with regular lat/lon grid and (lat, lon) dim order.
    """
    # Step 1: pad longitude seam + latitude poles
    da_p = close_lon_seam(da, lon_name=lon_name)
    da_p = clamp_lat_poles(da_p, lat_name=lat_name)

    # Step 2: regular target grid
    lon_min, lon_max = float(da_p[lon_name].min()), float(da_p[lon_name].max())
    target_lon = np.arange(lon_min, lon_max + target_res_deg / 2, target_res_deg)
    target_lat = np.arange(-90.0, 90.0 + target_res_deg / 2, target_res_deg)

    # Step 3: bilinear interpolation onto the target grid
    da_i = da_p.interp(
        {lon_name: target_lon, lat_name: target_lat},
        method="linear",
    )

    # Step 4: enforce (lat, lon) dim order — pyGMT infers plot region from
    # dim order, and intermediate xarray operations can silently transpose.
    if lat_name in da_i.dims and lon_name in da_i.dims:
        da_i = da_i.transpose(lat_name, lon_name)
    return da_i
