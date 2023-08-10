import os
if "SPS_HOME" not in os.environ:
    os.environ["SPS_HOME"] = "/opt/hostedtoolcache/Python/fsps"

from rail.creation.engines import FSPSSedModeler, FSPSPhotometryCreator
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


@pytest.mark.parametrize(
    "settings,error",
    [
        ({"filter_folder": os.path.join(default_rail_fsps_files_folder, 'test_fsps_sed.fits')}, OSError),
    ],
)
def test_FSPSPhotometryCreator_bad_filter_folder(settings, error):
    """Test bad filter folder that should raise OS errors."""
    with pytest.raises(error):
        FSPSPhotometryCreator.make_stage(name='FSPSPhotometryCreator', **settings)


@pytest.mark.parametrize(
    "settings,error",
    [
        ({"Om0": 2}, ValueError),
    ],
)
def test_FSPSPhotometryCreator_bad_Om0(settings, error):
    """Test bad filter folder that should raise Value errors."""
    with pytest.raises(error):
        FSPSPhotometryCreator.make_stage(name='FSPSPhotometryCreator',
                                         filter_folder=os.path.join(default_rail_fsps_files_folder, 'filters'),
                                         **settings)


@pytest.mark.parametrize(
    "settings,error",
    [
        ({"Ode0": 2}, ValueError),
    ],
)
def test_FSPSPhotometryCreator_bad_Ode0(settings, error):
    """Test bad filter folder that should raise Value errors."""
    with pytest.raises(error):
        FSPSPhotometryCreator.make_stage(name='FSPSPhotometryCreator',
                                         filter_folder=os.path.join(default_rail_fsps_files_folder, 'filters'),
                                         **settings)


@pytest.mark.parametrize(
    "settings,error",
    [
        ({"h": 2}, ValueError),
    ],
)
def test_FSPSPhotometryCreator_bad_h(settings, error):
    """Test bad filter folder that should raise Value errors."""
    with pytest.raises(error):
        FSPSPhotometryCreator.make_stage(name='FSPSPhotometryCreator',
                                         filter_folder=os.path.join(default_rail_fsps_files_folder, 'filters'),
                                         **settings)
