import os
import shutil
import pytest
import rioxarray
import datetime

import geodata_harvester
from geodata_harvester import getdata_dea, getdata_silo, temporal

from eeharvest import harvester as eeharvester

OUTPATH = "test_temporal"

# Remove folder with test data after tests:
REMOVE_TESTDATA = True

def get_testdata_silo():
    """
    Get SILO testdata
    """
    layernames = ["daily_rain"]
    date_start = '2019-01-01'
    date_end = '2020-06-01'
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
    for fname in file_list:
        assert os.path.exists(fname)
        xdr = temporal.combine_rasters_temporal(fname, channel_name="band", attribute_name="long_name")
        outfname_list, agg_list = temporal.aggregate_temporal(
            xdr,
            period="yearly", 
            agg=["mean"], 
            outfile=f"{fname.split('.')[0]}", 
            buffer = None)
        assert len(outfname_list) > 0
    if REMOVE_TESTDATA:
        shutil.rmtree(OUTPATH, ignore_errors=True)
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
    outfname_list, agg_list = temporal.aggregate_temporal(
        xdr,
        period=7, 
        agg=["mean"], 
        outfile=os.path.join(OUTPATH,"DEA_temporal_agg"), 
        buffer = None)
    assert len(outfname_list) > 0
    if REMOVE_TESTDATA:
        shutil.rmtree(OUTPATH, ignore_errors=True)
    print('temporal test passed for DEA')


def test_temporal_gee():
    """
    Test for temporal functions for GEE processing
    """
    path_to_config = os.path.join('settings', 'settings_test_temporal.yaml')

    eeharvester.initialise()

    gee = eeharvester.auto(config=path_to_config)
    if not isinstance(gee.filenames, list):
        # convert to list
        gee.filenames = [gee.filenames]

    # find all subdirectories OUTPATH that start with string 'ee_'
    ee_subdirs = [os.path.join(OUTPATH, name) for name in os.listdir(OUTPATH) if name.startswith('ee_')]

    cfg = gee.obj.config

    period = (cfg['date_max'] - cfg['date_min']).days // cfg['time_intervals']

    for layername in ee_subdirs:
        outfname_list = [os.path.join(layername,filename) for filename in gee.filenames]
        xdr = temporal.multiband_raster_to_xarray(outfname_list)
        outfname_list, agg_list = temporal.aggregate_temporal(
            xdr,
            period=2, 
            agg=["median"], 
            outfile=layername + "_temporal_agg", 
            buffer = None)
        assert len(outfname_list) > 0
    if REMOVE_TESTDATA:
        shutil.rmtree(OUTPATH, ignore_errors=True)
    print('temporal test passed for DEA')