import os
if "SPS_HOME" not in os.environ:
    os.environ["SPS_HOME"] = "/opt/hostedtoolcache/Python/fsps"

from rail.creation.engines import FSPSSedModeler
import pytest
import rail.fsps

RAIL_FSPS_DIR = os.path.abspath(os.path.join(os.path.dirname(rail.fsps.__file__), '..', '..'))
default_rail_fsps_files_folder = os.path.join(RAIL_FSPS_DIR, 'rail', 'examples_data', 'creation_data', 'data',
                                              'fsps_default_data')

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
        FSPSSedModeler.make_stage(name='FSPSSedModeler', **settings)


@pytest.mark.parametrize(
    "settings,error",
    [
        ({"zcontinuous": 4}, ValueError),
    ],
)
def test_FSPSSedGenerator_bad_zcontinous(settings, error):
    """Test bad wavelength range that should raise Value and Type errors."""
    with pytest.raises(error):
        FSPSSedModeler.make_stage(name='FSPSSedModeler', **settings)


@pytest.mark.parametrize(
    "settings,error",
    [
        ({"imf_type": 6}, ValueError),
    ],
)
def test_FSPSSedGenerator_bad_imf_type(settings, error):
    """Test bad wavelength range that should raise Value and Type errors."""
    with pytest.raises(error):
        FSPSSedModeler.make_stage(name='FSPSSedModeler', **settings)


@pytest.mark.parametrize(
    "settings,error",
    [
        ({"sfh_type": 6}, ValueError),
    ],
)
def test_FSPSSedGenerator_bad_sfh_type(settings, error):
    """Test bad wavelength range that should raise Value and Type errors."""
    with pytest.raises(error):
        FSPSSedModeler.make_stage(name='FSPSSedModeler', **settings)


@pytest.mark.parametrize(
    "settings,error",
    [
        ({"dust_type": 7}, ValueError),
    ],
)
def test_FSPSSedGenerator_bad_dust_type(settings, error):
    """Test bad wavelength range that should raise Value and Type errors."""
    with pytest.raises(error):
        FSPSSedModeler.make_stage(name='FSPSSedModeler', **settings)
