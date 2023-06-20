# Tests for getdata_silo.py functions

import os
import shutil
import pytest
from geodata_harvester import getdata_silo

def test_get_SILO_raster():
    """
    test script
    """
    layername = "monthly_rain"
    years = 2019
    outpath = "silo_test"
    bbox = (140, -30, 150, -20)
    # test first for tif output format
    format_out = "tif"
    fnames_out = getdata_silo.get_SILO_raster(layername, years, outpath, bbox, format_out)
    assert len(fnames_out) > 0
    for fname in fnames_out:
        assert os.path.exists(fname)
        os.remove(fname)
    shutil.rmtree(outpath, ignore_errors=True)
    print("get_SILO_raster test passed")


def test_get_SILO_layers():
    """
    test script
    """
    layernames = ["daily_rain"]
    date_start = '2019-01-01'
    date_end = '2019-01-10'
    outpath = "silo_test"
    bbox = (140, -30, 150, -20)
    # test first for tif output format
    format_out = "tif"
    fnames_out = getdata_silo.get_SILO_layers(layernames, date_start, date_end, outpath, bbox, format_out)
    assert len(fnames_out) > 0
    for fname in fnames_out:
        assert os.path.exists(fname)
        os.remove(fname)
    shutil.rmtree(outpath, ignore_errors=True)
    print("get_SILO_layers test passed")
