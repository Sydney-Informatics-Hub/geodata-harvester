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


def get_testdata_dea():
    # Get data (here only for first layer)
    layername = "ga_ls8c_ard_3"
    # Crs for output
    crs = "EPSG:4326"  # WGS84
    # define bounding box for retrieval (simple test here for entire Australia)
    bbox = [120, -40, 140, -20]
    # define resolution (in arcsecs per pixel since crs is in WGS84)
    resolution = 100
    # define daterange
    date_min = '2019-01-01' 
    date_max = '2019-01-14' 
    # Get data
    outfnames = getdata_dea.get_dea_images_daterange(layername, date_min, date_max, bbox, resolution, OUTPATH, crs=crs)
    assert len(outfnames) > 0
    return outfnames


def test_temporal_dea():
    """
    Test script to retrieve and save images for a given year
    """
    os.makedirs(name=OUTPATH, exist_ok=True)
    # Download test data using dea
    file_list = get_testdata_dea()
    # Test temporal
    xdr = temporal.multiband_raster_to_xarray(file_list)
    outfname_list, agg_list = temporal.aggregate_temporal(xdr,period=7, agg=["mean"], outfile="temporal_agg", buffer = None)
    assert len(outfname_list) > 0
    #shutil.rmtree(OUTPATH, ignore_errors=True)
    print('temporal test passed for DEA')