# Test getdata_dea.py functionalities

import os
import pytest
from geodata_harvester import getdata_dea


def test_get_capabilities():
    """
    Test script to retrieve WCS capabilities
    """
    # DEA layer
    url = "https://ows.dea.ga.gov.au/?version=1.3.0"
    # Get capabilities
    keys, title_list, description_list, bbox_list, timelimits, nbands = getdata_dea.get_capabilities(url)
    assert len(keys) > 0
    print('get_capabilities test passed')


def test_get_times():
    """
    Test script to retrieve available times for a layer
    """
    layername = "ga_ls8c_ard_3"
    url = "https://ows.dea.ga.gov.au/?version=1.3.0"
    times = getdata_dea.get_times(url, layername)
    assert len(times) > 0
    print('get_times test passed')


def test_get_times_startend():
    """
    Test script to retrieve available times for a layer
    """
    layername = "ga_ls8c_ard_3"
    url = "https://ows.dea.ga.gov.au/?version=1.3.0"
    dt_start = "2020-01-01"
    dt_end = "2020-01-10"
    times = getdata_dea.get_times_startend(url, layername, dt_start, dt_end)
    assert len(times) > 0
    print('get_times_startend test passed')


def test_get_wcsmap():
    """
    Test script to retrieve and save image for one layer and date
    """
    url = "https://ows.dea.ga.gov.au/?version=1.3.0"
    layername = "ga_ls8c_ard_3"
    times = getdata_dea.get_times(url, layername)
    crs = "EPSG:4326"  # WGS84
    # define bounding box for retrieval (simple test here for entire Australia)
    bbox = [130, -40, 150, -20]
    # define resolution (in arcsecs per pixel since crs is in WGS84)
    resolution = 100
    # get latest image
    time = times[-1]
    # define output file name
    fname_out = f"test_{layername}_{time}.tif"
    # Get data
    download_ok = getdata_dea.get_wcsmap(fname_out, layername, bbox, time, resolution, url)
    assert download_ok
    print('get_wcsmap test passed')


def test_get_dea_images():
    """
    Test script to retrieve and save images for a given year
    """
    url = "https://ows.dea.ga.gov.au/?version=1.3.0"
    # Get data (here only for first layer)
    layername = "ga_ls8c_ard_3"
    # Crs for output
    crs = "EPSG:4326"  # WGS84
    # define bounding box for retrieval (simple test here for entire Australia)
    bbox = [120, -40, 140, -20]
    # define resolution (in arcsecs per pixel since crs is in WGS84)
    resolution = 100
    # define year
    year = 2019
    # define outpath
    outpath = "test_dea"
    # Get data
    outfnames = getdata_dea.get_dea_images(layername, year, bbox, resolution, outpath, crs=crs)
    assert len(outfnames) > 0
    for fname in outfnames:
        assert os.path.exists(fname)
        os.remove(fname)
    shutil.rmtree(outpath, ignore_errors=True)
    print('get_dea_images test passed')


def test_get_dea_images_daterange():
    """
    Test script to retrieve and save images for a given year
    """
    url = "https://ows.dea.ga.gov.au/?version=1.3.0"
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
    date_max = '2019-01-10' 
    # define outpath
    outpath = "test_dea"
    # Get data
    outfnames = getdata_dea.get_dea_images_daterange(layername, date_min, date_max, bbox, resolution, outpath, crs=crs)
    assert len(outfnames) > 0
    shutil.rmtree(outpath, ignore_errors=True)
    print('get_dea_images_daterange test passed')