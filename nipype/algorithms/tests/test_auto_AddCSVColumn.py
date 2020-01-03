# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..misc import AddCSVColumn


def test_AddCSVColumn_inputs():
    input_map = dict(
        extra_column_heading=dict(),
        extra_field=dict(),
        in_file=dict(extensions=None, mandatory=True,),
        out_file=dict(extensions=None, usedefault=True,),
    )
    inputs = AddCSVColumn.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_AddCSVColumn_outputs():
    output_map = dict(csv_file=dict(extensions=None,),)
    outputs = AddCSVColumn.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
