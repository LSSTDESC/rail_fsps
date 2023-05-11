import os
if "SPS_HOME" not in os.environ:
    os.environ["SPS_HOME"] = "/opt/hostedtoolcache/Python/fsps"

import tables_io
from rail.creation.engines import FSPSSedModeler
import pytest
from rail.core.stage import RailStage
import numpy as np

from rail.core.utils import RAILDIR
test_data = os.path.join(RAILDIR, 'rail', 'examples_data', 'creation_data', 'data', 'fsps_default_data',
                         'test_fsps_sed.fits')


@pytest.mark.parametrize(
    "settings,error",
    [
        ({"min_wavelength": -1}, ValueError),
        ({"max_wavelength": -1}, ValueError),
    ],
)
def test_FSPSSedGenerator_bad_wavelength_range(settings, error):
    """Test bad wavelength range that should raise Value and Type errors."""
    with pytest.raises(error):
        FSPSSedModeler.make_stage(name='sed_generator_test', **settings)


@pytest.mark.parametrize(
    "settings,error",
    [
        ({"zcontinuous": 4}, ValueError),
    ],
)
def test_FSPSSedGenerator_bad_zcontinous(settings, error):
    """Test bad wavelength range that should raise Value and Type errors."""
    with pytest.raises(error):
        FSPSSedModeler.make_stage(name='sed_generator_test', **settings)


@pytest.mark.parametrize(
    "settings,error",
    [
        ({"imf_type": 6}, ValueError),
    ],
)
def test_FSPSSedGenerator_bad_imf_type(settings, error):
    """Test bad wavelength range that should raise Value and Type errors."""
    with pytest.raises(error):
        FSPSSedModeler.make_stage(name='sed_generator_test', **settings)


@pytest.mark.parametrize(
    "settings,error",
    [
        ({"sfh_type": 6}, ValueError),
    ],
)
def test_FSPSSedGenerator_bad_sfh_type(settings, error):
    """Test bad wavelength range that should raise Value and Type errors."""
    with pytest.raises(error):
        FSPSSedModeler.make_stage(name='sed_generator_test', **settings)


@pytest.mark.parametrize(
    "settings,error",
    [
        ({"dust_type": 7}, ValueError),
    ],
)
def test_FSPSSedGenerator_bad_dust_type(settings, error):
    """Test bad wavelength range that should raise Value and Type errors."""
    with pytest.raises(error):
        FSPSSedModeler.make_stage(name='sed_generator_test', **settings)
