# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from nipype.testing import assert_equal
from nipype.interfaces.mrtrix.tracking import StreamlineTrack

def test_StreamlineTrack_inputs():
    input_map = dict(args=dict(argstr='%s',
    ),
    cutoff_value=dict(argstr='-cutoff %s',
    units='NA',
    ),
    desired_number_of_tracks=dict(argstr='-number %d',
    ),
    do_not_precompute=dict(argstr='-noprecomputed',
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    exclude_file=dict(argstr='-exclude %s',
    position=2,
    ),
    exclude_spec=dict(argstr='-seed %s',
    position=2,
    sep=',',
    units='mm',
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    in_file=dict(argstr='%s',
    mandatory=True,
    position=-2,
    ),
    include_file=dict(argstr='-include %s',
    position=2,
    ),
    include_spec=dict(argstr='-seed %s',
    position=2,
    sep=',',
    units='mm',
    ),
    initial_cutoff_value=dict(argstr='-initcutoff %s',
    units='NA',
    ),
    initial_direction=dict(argstr='-initdirection %s',
    units='voxels',
    ),
    inputmodel=dict(argstr='%s',
    position=-3,
    usedefault=True,
    ),
    mask_file=dict(argstr='-exclude %s',
    position=2,
    ),
    mask_spec=dict(argstr='-seed %s',
    position=2,
    sep=',',
    units='mm',
    ),
    maximum_number_of_tracks=dict(argstr='-maxnum %d',
    ),
    maximum_tract_length=dict(argstr='-length %s',
    units='mm',
    ),
    minimum_radius_of_curvature=dict(argstr='-curvature %s',
    units='mm',
    ),
    minimum_tract_length=dict(argstr='-minlength %s',
    units='mm',
    ),
    no_mask_interpolation=dict(argstr='-nomaskinterp',
    ),
    out_file=dict(argstr='%s',
    genfile=True,
    position=-1,
    ),
    seed_file=dict(argstr='-seed %s',
    position=2,
    ),
    seed_spec=dict(argstr='-seed %s',
    position=2,
    sep=',',
    units='mm',
    ),
    step_size=dict(argstr='-step %s',
    units='mm',
    ),
    stop=dict(argstr='-gzip',
    ),
    terminal_output=dict(mandatory=True,
    nohash=True,
    ),
    unidirectional=dict(argstr='-unidirectional',
    ),
    )
    inputs = StreamlineTrack.input_spec()

    for key, metadata in input_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(inputs.traits()[key], metakey), value

def test_StreamlineTrack_outputs():
    output_map = dict(tracked=dict(),
    )
    outputs = StreamlineTrack.output_spec()

    for key, metadata in output_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(outputs.traits()[key], metakey), value

