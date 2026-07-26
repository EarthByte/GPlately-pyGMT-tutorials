"""Plate-motion velocity-arrow helper.

Ported from T11 (Paleo-strain-rate maps) so all four T15-T18 debug notebooks
can overlay a consistent plate-motion vector field on their maps. The
returned east/north components are in cm/yr in the topological snapshot's
anchor-plate frame (usually anchor 0 = hotspot / spin-axis reference).

Usage:

    from plate_model_debug import calculate_plate_motion_arrows
    snap = topological_model.topological_snapshot(time)
    glons, glats, ge, gn = calculate_plate_motion_arrows(
        snap, region=[W, E, S, N], spacing_deg=15.0)
    speed   = np.sqrt(ge**2 + gn**2)
    azimuth = np.rad2deg(np.arctan2(ge, gn))
    m = speed >= 0.1
    if m.any():
        fig.plot(x=glons[m], y=glats[m], style='V0.15c+e+a35',
                 direction=[azimuth[m], VEL_SCALE * speed[m]],
                 fill='gray30', pen='0.3p,gray30')
"""

from __future__ import annotations

import numpy as np
import pygplates


def calculate_plate_motion_arrows(topological_snapshot, region,
                                    spacing_deg: float = 15.0):
    """Sample plate-motion velocities on a regular lat/lon grid.

    Parameters
    ----------
    topological_snapshot : pygplates.TopologicalSnapshot
        Snapshot at the desired reconstruction time. Obtain via
        `pygplates.TopologicalModel(topology_features, rotation_model).topological_snapshot(time)`.
    region : (W, E, S, N)
        Bounding box of the map, in degrees.
    spacing_deg : float
        Grid spacing in degrees. 15° gives a readable arrow density on a
        global map; drop to 3-5° for a regional zoom.

    Returns
    -------
    (lons, lats, east, north) : four 1-D numpy arrays
        Positions and velocity components in the snapshot's anchor-plate
        frame. Velocity components are in cm/yr, with east positive
        eastward and north positive northward. Points that fall outside
        any resolved topology are silently dropped.
    """
    W, E, S, N = region
    lon_arr = np.arange(W + spacing_deg / 2, E, spacing_deg)
    lat_arr = np.arange(S + spacing_deg / 2, N, spacing_deg)
    glon, glat = np.meshgrid(lon_arr, lat_arr)
    flat_lons = glon.flatten()
    flat_lats = glat.flatten()
    points = [pygplates.PointOnSphere(lat, lon)
              for lat, lon in zip(flat_lats, flat_lons)]

    velocities = topological_snapshot.get_point_velocities(
        points,
        velocity_delta_time=1.0,
        velocity_units=pygplates.VelocityUnits.cms_per_yr,
    )

    # Some grid points may fall in gaps between resolved topologies — drop them
    keep = [i for i, v in enumerate(velocities) if v is not None]
    if not keep:
        z = np.empty(0)
        return z, z, z, z

    pts_valid = [points[i] for i in keep]
    vecs_valid = [velocities[i] for i in keep]
    ned = pygplates.LocalCartesian.convert_from_geocentric_to_north_east_down(
        pts_valid, vecs_valid)

    lons = np.array([flat_lons[i] for i in keep])
    lats = np.array([flat_lats[i] for i in keep])
    east = np.array([n.get_y() for n in ned])
    north = np.array([n.get_x() for n in ned])
    return lons, lats, east, north
