Module geodata_harvester.widgets.harvesterwidgets
=================================================
This script generates interactive notebook widgets for selecting the settings.

Widgets are defined using the package ipywidgets, for more details see:

https://ipywidgets.readthedocs.io/en/stable/index.html

and examples:
https://coderzcolumn.com/tutorials/python/interactive-widgets-in-jupyter-notebook-using-ipywidgets

This package is part of the Data Harvester project developed for the Agricultural Research Federation (AgReFed).

Copyright 2023 Sydney Informatics Hub (SIH), The University of Sydney

This open-source software is released under the LGPL-3.0 License.

Functions
---------

    
`eval_widgets(w_settings, names)`
:   This function is converting widget settings into dictionary.
    
    If widget settings change, add settings here too.
    
    Input:
        w_settings: list of settings
        names: list of setting names
    
    Output:
        dict_settings: dictionary of settings

    
`gen_accordion(panels, panel_titles)`
:   Generate accordion of panels
    
    Input:
        panels: list of panels
        panel_titles: list of panel titles
    
    Output:
        accordion_main: accordion of panels

    
`gen_loadwidget()`
:   Generate widget for loading settings from yaml file
    
    Input:
        None
    
    Output:
        w_load: widget for loading settings

    
`gen_maintab()`
:   Generate New Settings Tab
    
    Input:
        None
    
    Output:
        tab_nest: tab containing New Settings and Load Settings
        w_settings: widget for settings
        names_settings: list of names of settings
        w_load: widget for loading settings

    
`gen_panel_dea()`
:   Generate panel for DEA settings
    
    Input:
        None
    
    Output:
        panel_dea: panel for DEA settings
        w_dea: widget for DEA settings
        options_dea: list of DEA options

    
`gen_panel_dem()`
:   Generate panel for DEM settings
    
    Input:
        None
    
    Output:
        panel_dem: panel for DEM settings
        w_dem: widget for DEM settings
        options_dem: list of DEM options

    
`gen_panel_ee()`
:   Generate panel for Google Earth Engine settings
    
    Input:
        None
    
    Output:
        panel_ee: panel for Google Earth Engine settings
        w_ee: widget for Google Earth Engine settings
        names_ee: list of widget names

    
`gen_panel_io()`
:   Generate panel for input and output settings
    
    Input:
        None
    
    Output:
        panel_io: panel for input and output settings
        w_io: widget for input path
        w_names: list of names of widgets

    
`gen_panel_landscape()`
:   Generate panel for landscape settings
    
    Input:
        None
    
    Output:
        panel_ls: panel for landscape settings
        w_ls: widget for landscape settings
        options_ls: list of landscape options

    
`gen_panel_radiometric()`
:   Generate panel for radiometric settings
    
    Input:
        None
    
    Output:
        panel_rm: panel for radiometric settings
        w_rm: widget for radiometric settings
        options_rm: list of radiometric options

    
`gen_panel_silo()`
:   Generate panel for SILO settings
    
    Input:
        None
    
    Output:
        panel_silo: panel for SILO settings
        w_silo: widget for SILO settings
        options_silo: list of SILO options

    
`gen_panel_slga()`
:   Generate panel for SLGA settings
    
    Input:
        None
    
    Output:
        panel_slga: panel for SLGA settings
        w_slga: widget for SLGA settings
        options_slga: list of available SLGA layers

    
`gen_panel_st()`
:   Generate panel for spatial-temporal settings
    
    Input:
        None
    
    Output:
        panel_st: panel for spatial-temporal settings
        settings_st: list of settings
        settings_names: list of names of settings

    
`gen_panels()`
:   Generate all settings panels
    
    Input:
        None
    
    Output:
        panels: list of panels
        w_settings: list of widgets for all settings
        names_settings: list of widget names
        panel_titles: list of panel titles

    
`gen_savebutton()`
:   Generate Save button
    
    Input:
        None
    
    Output:
        w_savebutton: widget for saving settings

    
`load_settings(fname_settings)`
:   Load settings from yaml file
    
    Input:
        fname_settings: path and filename to settings file
    
    Output:
        settings: settings as namespace

    
`print_settings(settings)`
:   print settings
    
    Input:
        settings: settings object
    
    Output: 
        None

    
`save_dict_settings(dict_settings, yaml_outfname)`
:   save dictionary to yaml file
    
    Input:
        dict_settings: dictionary of settings
        yaml_outfname: path and filename to save settings
    
    Output:
        None

    
`savebutton_onclick(params)`
:   Save settings to yaml file
    
    Input:
        params: list of widgets, list of names of widgets, output filename
    
    Output:
        None