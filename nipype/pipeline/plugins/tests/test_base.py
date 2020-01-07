# -*- coding: utf-8 -*-
# emacs: -*- mode: python; py-indent-offset: 4; indent-tabs-mode: nil -*-
# vi: set ft=python sts=4 ts=4 sw=4 et:
"""Tests for the engine module
"""
import pytest
from pathlib import Path
import numpy as np
import scipy.sparse as ssp

def test_scipy_sparse():
    foo = ssp.lil_matrix(np.eye(3, k=1))
    goo = foo.getrowview(0)
    goo[goo.nonzero()] = 0
    assert foo[0, 1] == 0


"""
Can use the following code to test that a mapnode crash continues successfully
Need to put this into a unit-test with a timeout

import nipype.interfaces.utility as niu
import nipype.pipeline.engine as pe

wf = pe.Workflow(name='test')

def func(arg1):
    if arg1 == 2:
        raise Exception('arg cannot be ' + str(arg1))
    return arg1

funkynode = pe.MapNode(niu.Function(function=func, input_names=['arg1'],
                                    output_names=['out']),
                       iterfield=['arg1'],
                       name = 'functor')
funkynode.inputs.arg1 = [1,2]

wf.add_nodes([funkynode])
wf.base_dir = '/tmp'

wf.run(plugin='MultiProc')
"""

@pytest.mark.regression
def test_remove_nodes(tmp_path):
    import os
    import nipype.interfaces.utility as niu
    import nipype.pipeline.engine as pe

    wf = pe.Workflow(name='test')

    def func(arg1):
        try:
            if arg1 == 2:
                raise Exception('arg cannot be ' + str(arg1))
        except:
            pass
        return arg1

    funkynode = pe.MapNode(niu.Function(function=func, input_names=['arg1'],
                                        output_names=['out']),
                           iterfield=['arg1'],
                           name = 'functor')
    funkynode.inputs.arg1 = [1,2]

    wf.add_nodes([funkynode])
    wf.base_dir = tmpdir
    wf.config['execution']['remove_node_directories'] = 'true'
    wf.config['execution']['stop_on_first_crash'] = 'false'
    wf.config['logging']['crashdump_dir'] = str(tmp_path)
    res = wf.run(plugin='MultiProc')

    assert not Path.is_dir(tmp_path / "test" / "functor")
