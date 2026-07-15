"""Topology construction anomaly detectors — refactored into per-time functions.

Originally standalone scripts by Ben Sculley + John Cannon (EarthByte):
- Topology-Construction-Anomalies/detect_topology_gaps_and_overlaps.py
- Topology-Construction-Anomalies/detect_topology_non_unique_sections.py

Refactored here so a notebook can call them at a single geological time and
get lists of anomalous features back (instead of writing GPML files to disk).
Used by tutorial notebook T61.

Three detectors, one per anomaly type:

- `detect_gaps_and_overlaps_at_time` — finds shared boundary sub-segments that
  are NOT shared by exactly two resolved topologies (i.e. gap = shared by 1,
  overlap = shared by >= 3).
- `detect_missing_polarity_at_time` — finds subduction-zone features used in
  a resolved topology that have no `gpml_subduction_polarity` property
  (or have it set to "Unknown", if `unknown_is_anomalous=True`).
- `detect_non_unique_sections_at_time` — finds topologies that use the same
  topological section more than once and where the duplicate sub-segments
  actually touch (touching is the signal that it's a real duplication rather
  than the valid head/tail-of-A + B + tail-of-A pattern).
"""

from __future__ import annotations

import pygplates


# ---------------------------------------------------------------------------
# Gaps and overlaps
# ---------------------------------------------------------------------------

def detect_gaps_and_overlaps_at_time(rotation_model, topology_features, time):
    """Find sub-segments that are NOT shared by exactly two resolved topologies.

    Parameters
    ----------
    rotation_model : pygplates.RotationModel
    topology_features : list of pygplates.FeatureCollection (or paths, features, ...)
    time : float
        Reconstruction time in Ma.

    Returns
    -------
    list of pygplates.Feature
        Resolved sub-segment features locating each gap or overlap. Each feature
        has a valid-time window of [time + 0.5, time - 0.5] so it displays only
        at that integral time step in GPlates.
    """
    time = float(time)
    resolved_topologies = []
    shared_boundary_sections = []
    pygplates.resolve_topologies(
        topology_features, rotation_model, resolved_topologies,
        time, shared_boundary_sections,
    )

    anomalous_features = []
    for shared_boundary_section in shared_boundary_sections:
        for shared_sub_segment in shared_boundary_section.get_shared_sub_segments():
            n_sharers = len(shared_sub_segment.get_sharing_resolved_topologies())
            if n_sharers == 2:
                continue  # OK: shared by exactly two boundaries

            # Deduplicate: same sub-segment can appear twice with reversed direction.
            duplicate_index = None
            for i, existing in enumerate(anomalous_features):
                existing_geom = existing.get_geometry(lambda p: True)
                sub_geom = shared_sub_segment.get_geometry()
                if (sub_geom == existing_geom
                        or sub_geom == pygplates.PolylineOnSphere(reversed(existing_geom))):
                    duplicate_index = i
                    break

            if duplicate_index is None:
                anomalous_features.append(shared_sub_segment.get_resolved_feature())
            else:
                # Same sub-segment showing up from two sides — cancel out.
                anomalous_features.pop(duplicate_index)

    for f in anomalous_features:
        f.set_valid_time(time + 0.5, time - 0.5)
    return anomalous_features


# ---------------------------------------------------------------------------
# Missing subduction polarity
# ---------------------------------------------------------------------------

def detect_missing_polarity_at_time(rotation_model, topology_features, time,
                                      unknown_is_anomalous=True):
    """Find subduction-zone features (used in a resolved topology) with no polarity.

    Parameters
    ----------
    rotation_model : pygplates.RotationModel
    topology_features : list of pygplates.FeatureCollection (or paths, features, ...)
    time : float
        Reconstruction time in Ma.
    unknown_is_anomalous : bool, default True
        If True, features whose polarity is set to the string "Unknown" also count.

    Returns
    -------
    list of pygplates.Feature
        Subduction-zone features with missing / unknown polarity, cloned and
        reconstructed to `time` with a display-window of [time + 0.5, time - 0.5].
    """
    time = float(time)
    resolved_topologies = []
    shared_boundary_sections = []
    pygplates.resolve_topologies(
        topology_features, rotation_model, resolved_topologies,
        time, shared_boundary_sections,
    )

    anomalous_features = []
    seen_ids = set()
    for section in shared_boundary_sections:
        feature = section.get_feature()
        if feature.get_feature_type() != pygplates.FeatureType.gpml_subduction_zone:
            continue
        polarity = feature.get_enumeration(pygplates.PropertyName.gpml_subduction_polarity)
        is_missing = not polarity
        is_unknown = unknown_is_anomalous and (polarity == "Unknown")
        if is_missing or is_unknown:
            fid = feature.get_feature_id().get_string()
            if fid in seen_ids:
                continue
            seen_ids.add(fid)
            anomalous_features.append(feature)

    # Reconstruct to `time` for display + apply narrow valid-time window
    reconstructed = []
    if anomalous_features:
        pygplates.reconstruct(anomalous_features, rotation_model,
                               reconstructed, time, group_with_feature=True)
        out = []
        for feature, recon_geoms in reconstructed:
            clone = feature.clone()
            clone.set_geometry([g.get_reconstructed_geometry() for g in recon_geoms])
            clone.set_valid_time(time + 0.5, time - 0.5)
            out.append(clone)
        return out
    return []


# ---------------------------------------------------------------------------
# Non-unique sections (same topological section added more than once)
# ---------------------------------------------------------------------------

def detect_non_unique_sections_at_time(topological_model, time,
                                         touch_threshold_km=0.1):
    """Find topologies where the same topological section is added more than once
    AND the duplicate sub-segments touch (real duplication, not a legitimate
    head-of-A + B + tail-of-A pattern).

    Parameters
    ----------
    topological_model : pygplates.TopologicalModel
        (Not a bare RotationModel + features — this detector needs the
        TopologicalModel wrapper introduced in pyGPlates 0.43+.)
    time : float
        Reconstruction time in Ma.
    touch_threshold_km : float, default 0.1
        Two sub-segments are "touching" if the great-circle distance between
        them is under this threshold (100 m by default).

    Returns
    -------
    tuple of (list of pygplates.Feature, list of pygplates.Feature)
        (anomalous_topology_features, anomalous_sub_segment_features).
        Both lists carry a valid-time window of [time + 0.5, time - 0.5].
    """
    time = float(time)
    snapshot = topological_model.topological_snapshot(time)
    resolved = snapshot.get_resolved_topologies(
        resolve_topology_types=(
            pygplates.ResolveTopologyType.line
            | pygplates.ResolveTopologyType.boundary
            | pygplates.ResolveTopologyType.network
        )
    )

    threshold_rad = touch_threshold_km / pygplates.Earth.mean_radius_in_kms
    anomalous_topologies = []
    anomalous_sub_segments = []

    for resolved_topology in resolved:
        try:
            sub_segments = resolved_topology.get_boundary_sub_segments()
        except AttributeError:
            sub_segments = resolved_topology.get_line_sub_segments()

        by_feature_id = {}
        for ss in sub_segments:
            fid = ss.get_feature().get_feature_id()
            by_feature_id.setdefault(fid, []).append(ss)

        topology_is_anomalous = False
        for group in by_feature_id.values():
            if len(group) < 2:
                continue
            # Do any pair of sub-segments (with the same feature ID) touch?
            resolved_features = [ss.get_resolved_feature() for ss in group]
            geometries = [rf.get_geometry() for rf in resolved_features]
            touches = False
            for i in range(len(geometries) - 1):
                for j in range(i + 1, len(geometries)):
                    if pygplates.GeometryOnSphere.distance(
                            geometries[i], geometries[j], threshold_rad) is not None:
                        touches = True
                        break
                if touches:
                    break
            if touches:
                anomalous_sub_segments.extend(resolved_features)
                topology_is_anomalous = True

        if topology_is_anomalous:
            anomalous_topologies.append(resolved_topology.get_resolved_feature())

    for f in anomalous_topologies + anomalous_sub_segments:
        f.set_valid_time(time + 0.5, time - 0.5)
    return anomalous_topologies, anomalous_sub_segments
