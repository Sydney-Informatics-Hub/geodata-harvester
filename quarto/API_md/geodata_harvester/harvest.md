Module geodata_harvester.harvest
================================
This script is running the headless version of the geodata-harvester.

The following main steps are automatically executed within the run() function:
    - loading settings from config file
    - creating bounding box from input file points if not provided
    - downloading data layers as specified in config file
    - processing data layers as specified in config file
    - save downloaded image files to disk as GeoTiffs
    - save summary table of downloaded files as CSV
    - extract data for point locations provided in input file (name specified in settings)
    - save extracted point results to disk as CSV and as geopackage 

Example call within Python:
    from geodata_harvester import harvest
    harvest.run(path_to_config))

Functions
---------

    
`run(path_to_config, log_name='download_summary', preview=False, return_df=False)`
:   A headless version of the Data-Harvester (with some limitations).
    Results are saved to disk.
    
    Parameters
    ----------
    path_to_config : str
        Path to YAML config file
    log_name: name of log file (default: "download_log")
    preview : bool, optional
        Plots a matrix of downloaded images if set to True, by default False
    return_df : bool, optional (Default: False)
        if True, returns dataframe with results
    
    Returns
    -------
    None (if return_df is False)
    dataframe (if return_df is True)