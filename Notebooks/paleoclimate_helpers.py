"""Shared display helpers for the paleoclimate-cluster notebooks (T40–T45).

These functions clean up how a coarse climate-model field on a lat/lon grid is
drawn with ``pygmt.grdimage`` in a Mollweide projection. They are display-only:
they wrap/clamp/resample a field for *plotting* and never change the underlying
data used for analysis.

Used by T40 (deep-time SAT snapshots) and T41 (cGENIE SST vs proxies); import
with, e.g.::

    from paleoclimate_helpers import close_lon_seam, clamp_lat_poles, refine_for_plot

Requires ``numpy`` and ``xarray``.
"""

import numpy as np
import xarray as xr


def close_lon_seam(da):
    """Pad a −180→180 grid cyclically so grdimage reaches the ±180 seam.

    Climate-model SAT/SST grids typically stop short of the +180 meridian (a
    3.75° grid's last column is at +176.25°), so grdimage leaves an unpainted
    wedge at the antimeridian where the Mollweide boundary curves past the last
    data column (GMT fills it grey). Wrapping one column round each seam lets the
    raster reach the edge; the extra half-cells fall outside ``region="d"`` and
    are clipped by the projection boundary.
    """
    lon = da.lon.values
    dlon = float(lon[1] - lon[0])
    west = da.isel(lon=-1).assign_coords(lon=lon[0] - dlon)   # +180 side → west edge
    east = da.isel(lon=0).assign_coords(lon=lon[-1] + dlon)   # −180 side → east edge
    return xr.concat([west, da, east], dim="lon").sortby("lon")


def clamp_lat_poles(da):
    """Extend the outermost lat rows out to ±90 (latitude can't wrap, so clamp).

    A grid that stops short of the poles would leave NaN slivers there when
    interpolated onto a finer grid. Repeating the edge rows out to ±90 keeps the
    interpolation in-range. Only adds a pole row when the grid actually stops
    short — a grid that already reaches −90 would get a duplicated row, making
    the latitude index non-unique (which breaks ``interp``).
    """
    lat = da.lat.values
    parts = [da]
    if float(lat[0]) > -90.0:
        parts.insert(0, da.isel(lat=0).assign_coords(lat=-90.0))
    if float(lat[-1]) < 90.0:
        parts.append(da.isel(lat=-1).assign_coords(lat=90.0))
    return xr.concat(parts, dim="lat").sortby("lat") if len(parts) > 1 else da


def refine_for_plot(da, step=0.5):
    """Resample a coarse field onto a fine regular grid for display.

    grdimage draws each native model cell as a quadrilateral, which staircases
    along the curved Mollweide rim at high latitudes (and aliases into stray
    cells right at the ±180 seam). Wrapping the seam, clamping the poles, and
    bilinearly resampling onto a fine (default 0.5°) grid before plotting gives a
    smooth rim. Display-only: it linearly interpolates a continuous field and
    changes no analysis.

    The final ``.transpose("lat", "lon")`` is essential: the concat/sortby steps
    can silently reorder the dims to (lon, lat), and pygmt infers the plot region
    from dim order — a transposed grid renders with lon/lat swapped (the data
    collapses to a central blob). Forcing (lat, lon) keeps grdimage correct.
    """
    src = clamp_lat_poles(close_lon_seam(da))
    lon = np.arange(-180.0, 180.0 + step / 2, step)
    lat = np.arange(-90.0, 90.0 + step / 2, step)
    return src.interp(lon=lon, lat=lat, method="linear").transpose("lat", "lon")
