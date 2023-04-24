import os
import pytest

import geodata_harvester
from geodata_harvester import getdata_dea, getdata_silo, temporal

OUTPATH = "test_temporal"


def get_testdata_silo():
    """
    Get SILO testdata
    """
    layernames = ["daily_rain","max_temp"]
    date_start = '2019-01-01'
    date_end = '2020-02-01'
    outpath = "silo_test"
    bbox = (130, -44, 153.9, -11)
    # test first for tif output format
    format_out = "tif"
    fnames_out = getdata_silo.get_SILO_layers(layernames, date_start, date_end, OUTPATH, bbox, format_out)
    return fnames_out



def test_temporal_silo():
    """
    Test script to retrieve and save images for a given year
    """
    os.makedirs(name=OUTPATH, exist_ok=True)
    # Download test data using dea
    file_list = get_testdata_silo()
    # Test temporal
    xdr = temporal.combine_rasters_temporal(file_list, channel_name="band", attribute_name="long_name")
    outfname_list, agg_list = temporal.aggregate_temporal(xdr,period="yearly", agg=["mean"], outfile="temporal_agg", buffer = None)
    assert len(outfname_list) > 0
    #shutil.rmtree(OUTPATH, ignore_errors=True)
    print('temporal test passed for DEA')
