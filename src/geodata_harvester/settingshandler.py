# Settings reader and handler

import yaml
import urllib
import json
import os
import datetime
from types import SimpleNamespace
import geopandas as gpd
from IPython.display import display, JSON

# Defaul settings yaml file
_fname_settings = "settings/settings_v0.1_default.yaml"


def DateEncoder(obj):
    """
    JSON encoder for datetime objects.
    """
    if isinstance(obj, (datetime.datetime, datetime.date)):
        return obj.strftime('%Y-%m-%d')


def display_settings(fname_settings, print_option = "json"):
    """
    Display settings from yaml file.

    Input:
        fname_settings: path and filename to settings file
        print_option: "display" or "json" (default)
    """
    # Load settings from yaml file
    with open(fname_settings, "r") as f:
        settings = yaml.load(f, Loader=yaml.FullLoader)
    # Print settings
    if print_option == "display":
        display(JSON(settings))
    elif print_option == "json":
        print(json.dumps(settings, indent=4, sort_keys=True, default=DateEncoder))
    else:
        print("print_option must be 'display' or 'json'")


def check_bbox(settings):
    """
    Check if bbox is valid. 
    If no bbox is given, the bbox is calculated from the input points.

    Input:
        settings: settings namespace

    Output:
        settings: updated settings with bbox
    """
    if (settings.target_bbox is None) | (settings.target_bbox == ""):
        gdfpoints = gpd.read_file(settings.infile)
        longs = gdfpoints[settings.colname_lng].astype(float)
        lats = gdfpoints[settings.colname_lat].astype(float)
        if settings.target_bbox is None:
            settings.target_bbox = (
                min(longs) - 0.05,
                min(lats) - 0.05,
                max(longs) + 0.05,
                max(lats) + 0.05,
            )
    assert len(settings.target_bbox) == 4, "There must be 4 values in bbox list"
    assert settings.target_bbox[2] > settings.target_bbox[0], "Bounding box[0] must be smaller than box[2]"
    assert settings.target_bbox[3] > settings.target_bbox[1], "Bounding box[1] must be smaller than box[3]"
    return settings


def main(fname_settings=_fname_settings, to_namespace=True):
    """
    Main function for running the script.

    Input:
        fname_settings: path and filename to settings file
    """
    # Load settings from yaml file
    with open(fname_settings, "r") as f:
        settings = yaml.load(f, Loader=yaml.FullLoader)
    # Parse settings dictinary as namespace (settings are available as
    # settings.variable_name rather than settings['variable_name'])
    if to_namespace:
        settings = SimpleNamespace(**settings)

    # Check if bbox is valid
    settings = check_bbox(settings)

    return settings
