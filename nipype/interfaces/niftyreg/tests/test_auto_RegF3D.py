# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..reg import RegF3D


def test_RegF3D_inputs():
    input_map = dict(
        aff_file=dict(argstr="-aff %s", extensions=None,),
        amc_flag=dict(argstr="-amc",),
        args=dict(argstr="%s",),
        be_val=dict(argstr="-be %f",),
        cpp_file=dict(
            argstr="-cpp %s",
            extensions=None,
            name_source=["flo_file"],
            name_template="%s_cpp.nii.gz",
        ),
        environ=dict(nohash=True, usedefault=True,),
        fbn2_val=dict(argstr="-fbn %d %d",),
        fbn_val=dict(argstr="--fbn %d",),
        flo_file=dict(argstr="-flo %s", extensions=None, mandatory=True,),
        flo_smooth_val=dict(argstr="-smooF %f",),
        flwth2_thr_val=dict(argstr="-fLwTh %d %f",),
        flwth_thr_val=dict(argstr="--fLwTh %f",),
        fmask_file=dict(argstr="-fmask %s", extensions=None,),
        fupth2_thr_val=dict(argstr="-fUpTh %d %f",),
        fupth_thr_val=dict(argstr="--fUpTh %f",),
        incpp_file=dict(argstr="-incpp %s", extensions=None,),
        jl_val=dict(argstr="-jl %f",),
        kld2_flag=dict(argstr="-kld %d",),
        kld_flag=dict(argstr="--kld",),
        le_val=dict(argstr="-le %f",),
        ln_val=dict(argstr="-ln %d",),
        lncc2_val=dict(argstr="-lncc %d %f",),
        lncc_val=dict(argstr="--lncc %f",),
        lp_val=dict(argstr="-lp %d",),
        maxit_val=dict(argstr="-maxit %d",),
        nmi_flag=dict(argstr="--nmi",),
        no_app_jl_flag=dict(argstr="-noAppJL",),
        noconj_flag=dict(argstr="-noConj",),
        nopy_flag=dict(argstr="-nopy",),
        nox_flag=dict(argstr="-nox",),
        noy_flag=dict(argstr="-noy",),
        noz_flag=dict(argstr="-noz",),
        omp_core_val=dict(argstr="-omp %i", usedefault=True,),
        pad_val=dict(argstr="-pad %f",),
        pert_val=dict(argstr="-pert %d",),
        rbn2_val=dict(argstr="-rbn %d %d",),
        rbn_val=dict(argstr="--rbn %d",),
        ref_file=dict(argstr="-ref %s", extensions=None, mandatory=True,),
        ref_smooth_val=dict(argstr="-smooR %f",),
        res_file=dict(
            argstr="-res %s",
            extensions=None,
            name_source=["flo_file"],
            name_template="%s_res.nii.gz",
        ),
        rlwth2_thr_val=dict(argstr="-rLwTh %d %f",),
        rlwth_thr_val=dict(argstr="--rLwTh %f",),
        rmask_file=dict(argstr="-rmask %s", extensions=None,),
        rupth2_thr_val=dict(argstr="-rUpTh %d %f",),
        rupth_thr_val=dict(argstr="--rUpTh %f",),
        smooth_grad_val=dict(argstr="-smoothGrad %f",),
        ssd2_flag=dict(argstr="-ssd %d",),
        ssd_flag=dict(argstr="--ssd",),
        sx_val=dict(argstr="-sx %f",),
        sy_val=dict(argstr="-sy %f",),
        sz_val=dict(argstr="-sz %f",),
        vel_flag=dict(argstr="-vel",),
        verbosity_off_flag=dict(argstr="-voff",),
    )
    inputs = RegF3D.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_RegF3D_outputs():
    output_map = dict(
        avg_output=dict(),
        cpp_file=dict(extensions=None,),
        invcpp_file=dict(extensions=None,),
        invres_file=dict(extensions=None,),
        res_file=dict(extensions=None,),
    )
    outputs = RegF3D.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
