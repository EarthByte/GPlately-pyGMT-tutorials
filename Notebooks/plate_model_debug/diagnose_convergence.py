
"""
    Copyright (C) 2020 The University of Sydney, Australia
    
    This program is free software; you can redistribute it and/or modify it under
    the terms of the GNU General Public License, version 2, as published by
    the Free Software Foundation.
    
    This program is distributed in the hope that it will be useful, but WITHOUT
    ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
    FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License
    for more details.
    
    You should have received a copy of the GNU General Public License along
    with this program; if not, write to Free Software Foundation, Inc.,
    51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
"""


###########################################################################################################
#
# This script resolves topological plate polygons (and deforming networks) through time and calculates
# orthogonal convergence velocities any gaps and overlaps in their global coverage. Anomalous sub-segments, locating the gaps/overlaps,
# are written to a file that can be loaded into GPlates to visualise alongside the dynamic plate polygons.
# 
# Gaps and overlaps are caused when:
# 
#   1) there is an area of the globe not covered by a topological boundary or network, or
#   2) two (or more) topological boundary polygons overlap in some area of the globe.
# 
# This can also happen if two topological line sections are identical when ideally there should only
# be one of them (and it should be shared by two neighbouring topological boundaries).
#
# This script also detects any subduction zones with missing subduction polarity (or specified as unknown).
#
##################################################################################################


import sys
import math
import pygplates


# Required pygplates version.
# Version 22 is required for pygplates.ResolvedTopologicalSharedSubSegment.get_sub_segments().
PYGPLATES_VERSION_REQUIRED = pygplates.Version(22)

# The default threshold sampling distance along trenches (subduction zones).
DEFAULT_THRESHOLD_SAMPLING_DISTANCE_DEGREES = 0.5
DEFAULT_THRESHOLD_SAMPLING_DISTANCE_RADIANS = math.radians(DEFAULT_THRESHOLD_SAMPLING_DISTANCE_DEGREES)
DEFAULT_THRESHOLD_SAMPLING_DISTANCE_KMS = DEFAULT_THRESHOLD_SAMPLING_DISTANCE_RADIANS * pygplates.Earth.equatorial_radius_in_kms

DEFAULT_VELOCITY_DELTA_TIME = 1.0


def diagnose_topology_convergence(
        rotation_features_or_model,
        topology_features,
        time,
        convergent_velocity_threshold_cms_yr = None,
        divergent_velocity_threshold_cms_yr = None,
        boundary_feature_types = None,
        threshold_sampling_distance_radians = DEFAULT_THRESHOLD_SAMPLING_DISTANCE_RADIANS,
        velocity_delta_time = DEFAULT_VELOCITY_DELTA_TIME,
        anchor_plate_id = 0):
    # Docstring in numpydoc format...
    """Calculate convergence velocities of the topological model at particular times.
    
    Parameters
    ----------
    rotation_features_or_model : pygplates.RotationModel, or any combination of str, pygplates.FeatureCollection, pygplates.Feature
        The rotation model can be specified as a RotationModel. Or it can be specified as a rotation feature collection,
        or rotation filename, or rotation feature, or sequence of rotation features, or a sequence (eg, list or tuple) of any combination
        of those four types.
    topology_features: any combination of str, pygplates.FeatureCollection, pygplates.Feature
        The topological boundary and network features and the topological section features they reference (regular and topological lines).
        Can be specified as a feature collection, or filename, or feature, or sequence of features, or a sequence (eg, list or tuple)
        of any combination of those four types.
    young_time: int
        The younger time of the time range to diagnose.
    old_time: int
        The older time of the time range to diagnose.
    anchor_plate_id: int, optional
        The anchor plate of the rotation model. Defaults to zero.
    
    Returns
    -------
    list of pygplates.Feature
        The resolved sub-segment features that locate problematic parts of the resolved topological model at a particular time.
        Each resolved feature has a valid time of '[t + 0.5, t - 0.5]' where 't' is integral so that it is only displayed for a single integral time step.
    
    Notes
    -----
    """
    
    # Turn rotation data into a RotationModel (if not already).
    rotation_model = pygplates.RotationModel(rotation_features_or_model)
    
    # Turn topology data into a list of features (if not already).
    topology_features = pygplates.FeaturesFunctionArgument(topology_features).get_features()

    # Convergence sub-segment features.
    convergence_features = []
    convergence_velocities = []

    time = float(time)
        
        
    # Resolve our topological plate polygons (and deforming networks) to the current 'time'.
    # We generate both the resolved topology boundaries and the boundary sections between them.
    resolved_topologies = []
    shared_boundary_sections = []
    pygplates.resolve_topologies(topology_features, rotation_model, resolved_topologies, time, shared_boundary_sections)

    # Iterate over the shared boundary sections.
    for shared_boundary_section in shared_boundary_sections:
        
        # If looking for specific feature types then check the current boundary feature in among those types.
        boundary_feature_type = shared_boundary_section.get_feature().get_feature_type()
        if (boundary_feature_types is not None and
            boundary_feature_type not in boundary_feature_types):
            continue
        
        convergence_data = []
        convergence_vels = []
        
        # Iterate over the sub-segments that actually contribute to a topology boundary.
        for shared_sub_segment in shared_boundary_section.get_shared_sub_segments():
            
            sub_segments_of_topological_line_sub_segment = shared_sub_segment.get_sub_segments()
            if sub_segments_of_topological_line_sub_segment:
                # Iterate over the sub-sub-segments associated with the topological line shared sub-segment.
                for sub_sub_segment in sub_segments_of_topological_line_sub_segment:
                    sub_sub_segment_plate_id = sub_sub_segment.get_feature().get_reconstruction_plate_id()
                    sub_sub_segment_geometry = sub_sub_segment.get_resolved_geometry()
                    
                    _calc_convergence(
                            convergence_data,
                            convergence_vels,
                            time,
                            sub_sub_segment_geometry,
                            sub_sub_segment_plate_id,
                            threshold_sampling_distance_radians,
                            convergent_velocity_threshold_cms_yr,
                            divergent_velocity_threshold_cms_yr,
                            velocity_delta_time,
                            resolved_topologies,
                            shared_sub_segment.get_sharing_resolved_topologies(),
                            rotation_model,
                            anchor_plate_id)
                    
            else: # It's not a topological line...
                sub_segment_plate_id = shared_sub_segment.get_feature().get_reconstruction_plate_id()
                sub_segment_geometry = shared_sub_segment.get_resolved_geometry()
                
                _calc_convergence(
                        convergence_data,
                        convergence_vels,
                        time,
                        sub_segment_geometry,
                        sub_segment_plate_id,
                        threshold_sampling_distance_radians,
                        convergent_velocity_threshold_cms_yr,
                        divergent_velocity_threshold_cms_yr,
                        velocity_delta_time,
                        resolved_topologies,
                        shared_sub_segment.get_sharing_resolved_topologies(),
                        rotation_model,
                        anchor_plate_id)
        
        if convergence_data:
            convergence_features.append(
                    _create_convergence_feature(convergence_data, time, boundary_feature_type))
            convergence_velocities.append(convergence_vels)

    return convergence_features, convergence_velocities


def _calc_convergence(
        convergence_data,
        convergence_vels,
        time,
        shared_sub_segment_geometry,
        shared_sub_segment_plate_id,
        threshold_sampling_distance_radians,
        convergent_velocity_threshold_cms_yr,
        divergent_velocity_threshold_cms_yr,
        velocity_delta_time,
        all_resolved_topologies,
        sharing_resolved_topologies,
        rotation_model,
        anchor_plate_id):
    
    # Ensure the shared sub-segment is tessellated to within the threshold sampling distance.
    tessellated_shared_sub_segment_polyline = (
            shared_sub_segment_geometry.to_tessellated(threshold_sampling_distance_radians))
    
    # Iterate over the great circle arcs of the tessellated polyline to get the
    # arc midpoints, lengths and normals.
    # There is an arc between each adjacent pair of points in the polyline.
    arc_midpoints = []
    arc_lengths = []
    normals = []
    for arc in tessellated_shared_sub_segment_polyline.get_segments():
        if not arc.is_zero_length():
            arc_midpoints.append(arc.get_arc_point(0.5))
            arc_lengths.append(arc.get_arc_length())
            normals.append(arc.get_great_circle_normal())
    
    # Shouldn't happen, but just in case the shared sub-segment polyline coincides with a point.
    if not arc_midpoints:
        return
    
    one_km_on_unit_sphere = 1.0 / pygplates.Earth.mean_radius_in_kms
    
    for arc_index in range(len(arc_midpoints)):
        point = arc_midpoints[arc_index]
        length = arc_lengths[arc_index]
        normal = normals[arc_index]
        
        left_point = pygplates.PointOnSphere((pygplates.Vector3D(point.to_xyz()) + one_km_on_unit_sphere * normal).to_normalized().to_xyz())
        right_point = pygplates.PointOnSphere((pygplates.Vector3D(point.to_xyz()) - one_km_on_unit_sphere * normal).to_normalized().to_xyz())
        
        resolved_topology_containing_left_point = _find_resolved_topology_containing_point(left_point, sharing_resolved_topologies)
        if not resolved_topology_containing_left_point:
            resolved_topology_containing_left_point = _find_resolved_topology_containing_point(left_point, all_resolved_topologies)
            if not resolved_topology_containing_left_point:
                continue
        
        resolved_topology_containing_right_point = _find_resolved_topology_containing_point(right_point, sharing_resolved_topologies)
        if not resolved_topology_containing_right_point:
            resolved_topology_containing_right_point = _find_resolved_topology_containing_point(right_point, all_resolved_topologies)
            if not resolved_topology_containing_right_point:
                continue
        
        if isinstance(resolved_topology_containing_left_point, pygplates.ResolvedTopologicalNetwork):
            left_plate_id = shared_sub_segment_plate_id
        else:
            left_plate_id = resolved_topology_containing_left_point.get_feature().get_reconstruction_plate_id()
        
        if isinstance(resolved_topology_containing_right_point, pygplates.ResolvedTopologicalNetwork):
            right_plate_id = shared_sub_segment_plate_id
        else:
            right_plate_id = resolved_topology_containing_right_point.get_feature().get_reconstruction_plate_id()
        
        if left_plate_id == right_plate_id:
            continue
        
        left_equivalent_stage_rotation = rotation_model.get_rotation(
                time,
                left_plate_id,
                time + velocity_delta_time,
                anchor_plate_id=anchor_plate_id)
        right_equivalent_stage_rotation = rotation_model.get_rotation(
                time,
                right_plate_id,
                time + velocity_delta_time,
                anchor_plate_id=anchor_plate_id)
        
        left_velocity = pygplates.calculate_velocities(
                (point,), left_equivalent_stage_rotation,
                velocity_delta_time, pygplates.VelocityUnits.cms_per_yr)[0]
        right_velocity = pygplates.calculate_velocities(
                (point,), right_equivalent_stage_rotation,
                velocity_delta_time, pygplates.VelocityUnits.cms_per_yr)[0]
        
        # Orthogonal convergence velocity (cms/yr). Positive/negative is convergenet/divergent.
        convergence_normal_velocity_signed_magnitude = (
            pygplates.Vector3D.dot(left_velocity, -normal) +
            pygplates.Vector3D.dot(right_velocity, normal))
        
        if ((convergent_velocity_threshold_cms_yr is None or convergence_normal_velocity_signed_magnitude >= convergent_velocity_threshold_cms_yr) and
            (divergent_velocity_threshold_cms_yr is None or convergence_normal_velocity_signed_magnitude <= divergent_velocity_threshold_cms_yr)):
            convergence_data.append((point, convergence_normal_velocity_signed_magnitude))
            convergence_vels.append(convergence_normal_velocity_signed_magnitude)

            #print(len(convergence_data), len(convergence_vels))
    


def _find_resolved_topology_containing_point(
        point,
        resolved_topologies):
    
    for resolved_topology in resolved_topologies:
        if resolved_topology.get_resolved_boundary().is_point_in_polygon(point):
            return resolved_topology


def _create_convergence_feature(
        convergence_data,
        time,
        feature_type):
    
    # Convert the list of tuples (one tuple per sample point) into a tuple of lists (one list per data parameter).
    parameter_lists = list(zip(*convergence_data))
    
    # Put all convergence data for the current reconstruction time into a single feature.
    coverage_feature = pygplates.Feature(feature_type)
    
    # Make it only appear at 'time'.
    coverage_feature.set_valid_time(time + 0.5, time - 0.5)
    
    # Extract the non-optional parameters.
    all_points = parameter_lists[0]
    all_convergence_velocity_magnitude = parameter_lists[1]
    
    # Add each data parameter as a separate scalar coverage.
    coverage_geometry = pygplates.MultiPointOnSphere(all_points)
    coverage_scalars = {
        pygplates.ScalarType.create_gpml('ConvergenceVelocityMagnitude') : all_convergence_velocity_magnitude,
    }
    
    coverage_feature.set_geometry((coverage_geometry, coverage_scalars))
    
    return coverage_feature


if __name__ == '__main__':
    
    import os.path
    
    
    # Check the imported pygplates version.
    if not hasattr(pygplates, 'Version') or pygplates.Version.get_imported_version() < PYGPLATES_VERSION_REQUIRED:
        print('{0}: Error - imported pygplates version {1} but version {2} or greater is required'.format(
                os.path.basename(__file__), pygplates.Version.get_imported_version(), PYGPLATES_VERSION_REQUIRED),
            file=sys.stderr)
        sys.exit(1)
    
    
    import argparse

    DEFAULT_OUTPUT_FILENAME = 'convergence_velocities.gpml'
    
    
    def main():
    
        __description__ = \
    """Locate problematic parts of the topological model at particular times.

    The anomalous (problematic) features are written to an output file that can be loaded into GPlates,
    along with the topological model, to help locate areas that need fixing.

    NOTE: Separate the positional and optional arguments with '--' (workaround for bug in argparse module).
    For example...

    python %(prog)s -r rotations.rot -m topologies.gpml -t 0 410 -- convergence.gpml
     """

        # The command-line parser.
        parser = argparse.ArgumentParser(description = __description__, formatter_class=argparse.RawDescriptionHelpFormatter)
        
        parser.add_argument('-r', '--rotation_filenames', type=str, nargs='+', required=True,
                metavar='rotation_filename', help='Rotation files associated with topological model.')
        parser.add_argument('-m', '--topology_filenames', type=str, nargs='+', required=True,
                metavar='topology_filename', help='All topology files in topological model.')
        parser.add_argument('-a', '--anchor', type=int, default=0,
                dest='anchor_plate_id',
                help='Anchor plate id used for reconstructing. Defaults to zero.')

        parser.add_argument('-t', '--time_range', type=int, nargs=2, required=True,
                metavar=('young_time', 'old_time'),
                help='The time range (in Ma) from young time to old time.')
        
        # Can specify only one of '-i', '-l' or '-t'.
        threshold_sampling_distance_group = parser.add_mutually_exclusive_group()
        threshold_sampling_distance_group.add_argument('-s', '--threshold_sampling_distance_degrees', type=float,
                help='Threshold sampling distance along trenches (in degrees). '
                    'Defaults to {0} degrees.'.format(DEFAULT_THRESHOLD_SAMPLING_DISTANCE_DEGREES))
        threshold_sampling_distance_group.add_argument('-k', '--threshold_sampling_distance_kms', type=float,
                help='Threshold sampling distance along trenches (in Kms). '
                    'Defaults to {0:.2f} Kms (which is equivalent to {1} degrees).'.format(
                            DEFAULT_THRESHOLD_SAMPLING_DISTANCE_KMS,
                            DEFAULT_THRESHOLD_SAMPLING_DISTANCE_DEGREES))
        
        def parse_positive_number(value_string):
            try:
                value = float(value_string)
            except ValueError:
                raise argparse.ArgumentTypeError("%s is not a number" % value_string)
            
            if value <= 0:
                raise argparse.ArgumentTypeError("%g is not a positive number" % value)
            
            return value
        
        parser.add_argument('-v', '--velocity_delta_time', type=parse_positive_number,
                default=DEFAULT_VELOCITY_DELTA_TIME,
                help='The delta time interval used to calculate velocities in My. '
                     'Defaults to {0} My.'.format(DEFAULT_VELOCITY_DELTA_TIME))
        
        parser.add_argument('-c', '--convergent_velocity_threshold_cms_yr', type=float,
                help='Optional velocity threshold. Only orthogonal velocities above this value are output '
                     '(positive/negative is convergent/divergent). By default, no convergent threshold is used.')
        
        parser.add_argument('-d', '--divergent_velocity_threshold_cms_yr', type=float,
                help='Optional velocity threshold. Only orthogonal velocities below this value are output '
                     '(positive/negative is convergent/divergent). By default, no divergent threshold is used.')
        
        parser.add_argument('-f', '--boundary_feature_types', type=str, nargs='+',
                help='Optional boundary feature types to restrict limit output to. '
                     'For example, specify "Transform MidOceanRidge" to limit output to transform faults and mid-ocean ridges. '
                     'By default, all boundary features types are output.')
    
        parser.add_argument('output_filename', type=str, nargs='?',
                default='{0}'.format(DEFAULT_OUTPUT_FILENAME),
                help="The output file to contain the convergence velocities - the default is '{0}'".format(DEFAULT_OUTPUT_FILENAME))
        
        # Parse command-line options.
        args = parser.parse_args()
        
        if args.time_range[0] > args.time_range[1]:
            raise argparse.ArgumentTypeError("First (young) value in time range is greater than second (old) value")
        
        if args.boundary_feature_types:
            boundary_feature_types = [pygplates.FeatureType.create_gpml(feature_type_str) for feature_type_str in args.boundary_feature_types]
        else:
            boundary_feature_types = None
        
        # Determine threshold sampling distance.
        if args.threshold_sampling_distance_degrees:
            threshold_sampling_distance_radians = math.radians(args.threshold_sampling_distance_degrees)
        elif args.threshold_sampling_distance_kms:
            threshold_sampling_distance_radians = args.threshold_sampling_distance_kms / pygplates.Earth.equatorial_radius_in_kms
        else: # default...
            threshold_sampling_distance_radians = math.radians(DEFAULT_THRESHOLD_SAMPLING_DISTANCE_DEGREES)
        
        # Diagnose topology convergence.
        convergence_features = diagnose_topology_convergence(
                args.rotation_filenames,
                args.topology_filenames,
                args.time_range[0],
                args.time_range[1],
                args.convergent_velocity_threshold_cms_yr,
                args.divergent_velocity_threshold_cms_yr,
                boundary_feature_types,
                threshold_sampling_distance_radians,
                args.velocity_delta_time,
                args.anchor_plate_id)
        
        # Write the anomalous resolved sub-segment features to disk (even if there are no features).
        pygplates.FeatureCollection(convergence_features).write(args.output_filename)
        
        sys.exit(0)
    
    import traceback
    
    try:
        main()
        sys.exit(0)
    except Exception as exc:
        print('ERROR: {0}'.format(exc), file=sys.stderr)
        # Uncomment this to print traceback to location of raised exception.
        traceback.print_exc()
        sys.exit(1)
