# Test functions for getdata_radiometric.py 

import shutil
import os
import pytest
from geodata_harvester import getdata_radiometric


def test_get_capabilities():
   """
   Test script to retrieve WCS capabilities
   """
   # Get capabilities
   keys, titles, descriptions, bboxs = getdata_radiometric.get_capabilities()
   assert len(keys) > 0
   print("get_capabilities test passed")


def test_get_times():
    """
    Test script to retrieve available times for a layer
    """
    url = "https://gsky.nci.org.au/ows/national_geophysical_compilations?service=WCS"
    layername = "radmap2019_grid_dose_terr_filtered_awags_rad_2019"
    times = getdata_radiometric.get_times(url, layername)
    assert len(times) > 0
    print('get_times test passed')

""" This test function takes a long time and is not necessary for download testing"""
# def test_times():
#     """
#     Check that there is only one time per layers.
#     """
#     url = "https://gsky.nci.org.au/ows/national_geophysical_compilations?service=WCS"
#     radiometricdict = getdata_radiometric.get_radiometricdict()
#     layernames = radiometricdict["layernames"]
#     for key in layernames:
#         times = getdata_radiometric.get_times(url, key)
#         print(f"{key}: {times}")
#         assert len(times) == 1
#     print("test_times passed")


def test_get_radiometric_image():
    """
    Test script to retrieve and save image for one layer
    """
    url = "https://gsky.nci.org.au/ows/national_geophysical_compilations?service=WCS"
    # "radmap2019_grid_dose_terr_awags_rad_2019"  # for some layers readout time of 30s is exceeding (server limited)
    layername = "radmap2019_grid_dose_terr_filtered_awags_rad_2019"
    crs = "EPSG:4326"  # WGS84
    # define sall bounding box for retrieval test
    bbox = (130, -30, 131, -29)
    # define resolution (in arcsecs per pixel since crs is in WGS84)
    resolution = 100
    # define output file name
    fname_out = f"test_{layername}.tif"
    # Get data
    download_ok = getdata_radiometric.get_radiometric_image(
        fname_out, layername, bbox, url, resolution=resolution
    )
    assert download_ok
    # remove file
    os.remove(fname_out)
    print("get_radiometric_image test passed")