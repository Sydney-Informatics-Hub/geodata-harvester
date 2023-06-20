# Test harvest function
import os
import shutil
import pytest
import pandas as pd
from geodata_harvester import harvest

def test_harvest():
    """
    Test script to harvest data
    """
     # Define input file
    path_settings = 'settings'
    fname_settings = 'settings_test_harvest.yaml'
    fname_in = os.path.join(path_settings,fname_settings)
    path_harvest = 'test_results_harvest'
    # Harvest data
    df = harvest.run(fname_in, return_df = True)
    # Check output table with ccordinates
    assert df is not None, "No data returned"
    assert len(df) == 82, "Incorrect number of rows returned"
    # check output tif files
    df_log = pd.read_csv(os.path.join(path_harvest,'download_summary.csv'))
    fnames_out = df_log['filename_out'].tolist()
    assert len(fnames_out) > 0, "No files downloaded"
    # Check output file exists
    # Loop over fnames_out and check if tif exists
    for fname_out in fnames_out:
        if os.path.isfile(fname_out):
            tif_exists = True
        else:
            tif_exists = False
        assert tif_exists, "File does not exist: {}".format(fname_out)
    # Remove output directory
    shutil.rmtree(path_harvest, ignore_errors=True)
    print("Test for test_harvest passed.")
