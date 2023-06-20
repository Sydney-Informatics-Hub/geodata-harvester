Module geodata_harvester.utils
==============================
Utility functions for use in the Agrefed data harvesting pipeline.

--Function List, in order of appearence--

plot_rasters: Plots a list of rasters.
_getFeatures (internal): Extracts rasterio compatible test from geodataframe.
reproj_mask: Masks a raster to the area of a shape, and reprojects.
reproj_rastermatch: Reproject a file to match the shape and projection of
    existing raster.
reproj_raster: Reproject and clip for a given output resolution, crs and bbox.
_read_file (internal): Reads raster with rasterio returns numpy array
aggregate_rasters: Averages (or similar) over multiple files and multiple
    channels.
aggregate_multiband: Averages (or similar) over multiple files but keeps
    multi-channels independent.
_get_coords_at_point (internal): Finds closest index of a point-location in an
    array (raster).
raster_query: Given a longitude,latitude value, return the value at that point
    of a raster/tif.
extract_values_from_rasters: Given a list of rasters, extract the values at coords.
init_logtable: Stores metdata for each step of raster download and processing.
update_logtable: Updates each the logtable with new information.

Functions
---------

    
`aggregate_multiband(file_list=None, data_dir=None, agg=['mean'], outfile='aggregation')`
:   Aggregates over multiple files but keeps channels independently.
    Results are written to new tif files.
    
    Parameters
    ----------
    file_list : list of strings
        List of files to aggregate
    data_dir : string
        Path to directory containing files
    agg : list of strings
        List of aggregation methods to apply
    outfile : string
        Name of output file
    
    Returns
    -------
    outfname_list : list of strings of output file names
    channel_list : list of strings of channel names
    agg_list : list of strings of aggregation methods

    
`aggregate_rasters(file_list=None, data_dir=None, agg=['mean'], outfile='aggregation')`
:   Aggregrates over multiple files and over all channels
    and writes results to new tif file(s).
    
    Parameters
    ----------
    file_list : list of strings
        List of files to aggregate
    data_dir : string
        Path to directory containing files
    agg : list of strings
        List of aggregation methods to apply (mean, median, sum, perc95, perc5)
    outfile : string
        Name of output file
    
    Returns
    -------
    list_outfnames : list of strings of output file names

    
`coreg_raster(i0, j0, data, region)`
:   Coregisters a point with a buffer region of a raster.
    
    INPUTS
        i0: column-index of point of interest
        j0: row-index of point of interest
        data: two-dimensional numpy array (raster)
        region: integer, same units as data resolution
    
    RETURNS
        pts: all values from array within region

    
`extract_values_from_rasters(coords, raster_files, method='nearest')`
:   Extract values from a list of raster files at given coordinates using rioxarray.
    Values will be extracted for all bands in each raster file.
    Return geopandas DataFrame with extracted values and geometry.
    
    Input:
        coords: A list of tuples containing longitude and latitude coordinates.
                Format: [(lng1, lat1), (lng2, lat2), ...]
    
        raster_files: A list of raster file paths.
                      Format: ["path/to/raster1.tif", "path/to/raster2.tif", ...]
    
        method: The method to select values from raster files for 
                inexact matches between input coords and raster coords:
                 {"nearest", "pad", "ffill", "backfill", "bfill"}, optional
            - nearest (Default): use nearest valid index value. 
            - pad / ffill: propagate last valid index value forward
            - backfill / bfill: propagate next valid index value backward
            - None: only exact matches
    
    Output:
        A geopandas DataFrame containing the extracted values and geometry, where each row represents
        a coordinate point and the columns represent the bands for each raster file.
        Output column names are the raster file name plus the band name.

    
`init_logtable()`
:   Create a log table to store information from the raster download or processing.
    
    RETURNS:
        df_log: dataframe to update

    
`msg_dl(message, log=False)`
:   Prints a downloading message

    
`msg_err(message, log=False)`
:   Prints an error message

    
`msg_info(message, icon=True, log=False)`
:   Prints an info message

    
`msg_success(message, log=False)`
:   Prints a success message

    
`msg_warn(message, log=False)`
:   Prints a warning message

    
`plot_rasters(rasters, longs=None, lats=None, titles=None)`
:   Plots multiple raster files (.tif) on a grid of nicely arranged figures.
    
    Parameters:
        raster: list of filenames (.tif).
            Will only read the first band/channel if multiband.
        longs: optional x values in list like object for plotting as points 
            over raster images.
        lats: optional x values in list like object for plotting as points
            over raster images.
        titles: title of plot default is raster file name.
    
    Returns:  
        None

    
`points_in_circle(circle, arr)`
:   A generator to return all points whose indices are within a given circle.
    http://stackoverflow.com/a/2774284
    Warning: If a point is near the the edges of the raster it will not loop
    around to the other side of the raster!
    
    INPUTS
    circle: a tuple of (i0, j0, r) where i0, j0 are the indices of the center of the circle and r is the radius
    
    arr: a two-dimensional numpy array
    
    RETURNS
    A generator that yields all points within the circle

    
`raster_query(longs, lats, rasters, titles=None)`
:   DEPRECATED: Use extract_values_from_rasters instead.
    
    given a longitude,latitude value, return the value at that point of the
        first channel/band in the raster/tif.
    
    INPUTS
        longs:list of longitudes
        lats:list of latitudes
        rasters:list of raster filenames (as strings)
        titles:list of column titles (as strings) that correspond to rasters (if none provided, rasternames will be used)
    
    RETURNS
        gdf: geopandas dataframe where each row is long/lat point,
            and columns are rasterfiles

    
`reproj_mask(filepath, bbox, crscode=4326, filepath_out=None)`
:   Clips a raster to the area of a shape, and reprojects.
    
    INPUTS
        filepath: input filename (tif)
        bbox: shapely geometry(polygon) defining mask boundary
        crscode: optional, coordinate reference system as defined by EPSG
        filepath_out: optional, the optional output filename of the raster. If False, 
        does not save a new file
    
    RETURNS
        out_img: numpy array of the clipped and reprojected raster

    
`reproj_raster(infile, outfile, bbox_out, resolution_out=None, crs_out='EPSG:4326', nodata=0)`
:   Reproject and clip for a given output resolution, crs and bbox.
    Output file is written to disk.
    
    Parameters
    ----------
    infile : (string) path to input file to reproject
    outfile : (string) path to output file tif
    bbox_out : (left, bottom, right, top)
    resolution_out : (float) resolution of output raster
    crs_out : default "EPSG:4326"
    nodata : (float) nodata value for output raster

    
`reproj_rastermatch(infile, matchfile, outfile, nodata)`
:   Reproject a file to match the shape and projection of existing raster.
    Output file is written to disk.
    
    Parameters
    ----------
    infile : (string) path to input file to reproject
    matchfile : (string) path to raster with desired shape and projection
    outfile : (string) path to output file tif
    nodata : (float) nodata value for output raster

    
`spin(message=None, colour='magenta', events=1, log=False)`
:   Spin animation as a progress inidicator

    
`update_logtable(df_log, filenames, layernames, datasource, settings, layertitles=[], agfunctions=[], loginfos=[], force=False)`
:   Update the dataframe table with the information from the raster download or processing.
    The dataframe is simultaneoulsy saved to a csv file in default output directory.
    
    INPUTS
    df_log: dataframe to update
    filenames: list of filenames to add to the dataframe (captured in output of getdata_* functions)
    layernames: list of layernames to add to the dataframe (must be same length as filenames)
    datasource: datasource of the rasters (e.g. 'SLGA', 'SILO', 'DEA', see settings)
    settings: settings Namespace object
    layertitles: list of layer titles to add to the dataframe; if empty or none provided, it will be inferred from settings
    agfunctions: list of aggregation functions to add to the dataframe; if empty or none provided, it will be inferred from settings
    loginfos: string or list of log information strings to add to the dataframe;
    
    RETURNS
    df_log: updated dataframe