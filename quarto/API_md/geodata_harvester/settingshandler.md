Module geodata_harvester.settingshandler
========================================

Functions
---------

    
`DateEncoder(obj)`
:   JSON encoder for datetime objects.

    
`check_bbox(settings)`
:   Check if bbox is valid. 
    If no bbox is given, the bbox is calculated from the input points.
    
    Input:
        settings: settings namespace
    
    Output:
        settings: updated settings with bbox

    
`display_settings(fname_settings, print_option='json')`
:   Display settings from yaml file.
    
    Input:
        fname_settings: path and filename to settings file
        print_option: "display" or "json" (default)

    
`main(fname_settings='settings/settings_v0.1_default.yaml', to_namespace=True)`
:   Main function for running the script.
    
    Input:
        fname_settings: path and filename to settings file