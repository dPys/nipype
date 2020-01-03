# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..model import Level1Design


def test_Level1Design_inputs():
    input_map = dict(
        bases=dict(mandatory=True,),
        contrasts=dict(),
        interscan_interval=dict(mandatory=True,),
        model_serial_correlations=dict(mandatory=True,),
        orthogonalization=dict(usedefault=True,),
        session_info=dict(mandatory=True,),
    )
    inputs = Level1Design.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_Level1Design_outputs():
    output_map = dict(ev_files=dict(), fsf_files=dict(),)
    outputs = Level1Design.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
