# Settings reader and handler

import yaml
import urllib
import json
import os
import datetime
from types import SimpleNamespace
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

    return settings
