# Test harvest function
import os
import shutil
import pytest
from geodata_harvester import harvest

def test_harvest():
    """
    Test script to harvest data
    """
     # Define input file
    path_settings = 'settings'
    fname_settings = 'settings_test_harvest.yaml'
    fname_in = os.path.join(path_settings,fname_settings)
    path_temp = 'test_results_temp'
    # Harvest data
    df = harvest.run(fname_in, return_df = True)
    
    assert df is not None
    assert len(df)>10
    # Check output file exists
    assert os.path.exists(fname_out)
    tif_exists = False
    for root, dirs, files in os.walk(path_temp ):
        for file in files:
            if file.endswith(".tif"):
                tif_exists = True
    assert tif_exists is True
    # Remove output directory
    shutil.rmtree(path_temp, ignore_errors=True)
    print("Test passed")
