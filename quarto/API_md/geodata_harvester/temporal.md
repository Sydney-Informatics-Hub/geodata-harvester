Module geodata_harvester.temporal
=================================
Utility functions for temporal processing.

--Main function list--

combine_rasters_temporal: Concatenates files by time returns xarray.
aggregate_temporal: Aggregates xarrays by specified function and time period.
temporal_crop: Cuts an xarray object by start and end times.
aggregate_temporal: Make a data aggregation (mean, median, sum, etc) through time on an xarray.

--Helper function list--

get_date_after_last_underscore: Extract the date from the file name after the last underscore.
get_mask_array: Return mask of the data, e.g. for cloud-cover.

Functions
---------

    
`aggregate_temporal(xdr, period='yearly', agg=['mean'], outfile='temporal_agg', buffer=None, fill_nan=True)`
:   Make a data aggregation (mean, median, sum, etc) through time on an xarray.
    Expects xarray coordinates to be x, y, time. Saves every aggregation for
    every time period as its own tif file.
    
    Example:
    file_list = ['../data/mvp_daily_rain_silo/daily_rain_2017_cropped.tif',
         '../data/mvp_daily_rain_silo/daily_rain_2018_cropped.tif']
    
    xdr = combine_rasters_temporal(file_list, channel_name='band',attribute_name='long_name')
    
    outfname_list, agg_list = aggregate_temporal(
        xdr,period=100,agg=['mean','sum'],outfile='temporal_agg')
    
    Parameters
    ----------
    xdr : xarray object of x,y,time
    period : string or int. Time period to perform aggregation,
        'yearly', 'monthly', or number of periods to aggregate over.
    agg: list of strings. Choice of aggregation methods to apply of
        ['mean','median','sum','perc95','perc5']
    outfile : string. Prefix of output file name.
    buffer: integer time period in same units as period to buffer into the future.
    fill_nan: boolean. If True (Default), will automatically try to find the value for missing data 
        from header and fills with nan before aggregating. If False, will not fill nan.
    
    Returns
    -------
    outfname_list : list of strings of output file names
    agg_list : list of strings of aggregation methods

    
`combine_rasters_temporal(file_list, channel_name='band', attribute_name='long_name')`
:   Combines multiple tif files into single xarray object. 
    Assumes additional channels contain sequential time step data. 
    If multiple files in file_list, files must be in temporal order and same data type.
    Also assumes files are of the same shape (x,y,t).
    
    Example:
    file_list = ['../data/mvp_daily_rain_silo/daily_rain_2017_cropped.tif',
             '../data/mvp_daily_rain_silo/daily_rain_2018_cropped.tif']
    
    xdr = combine_rasters_temporal(file_list, channel_name='band',attribute_name='long_name')
    
    Parameters
    ----------
    file_list : str or list of filename strings in date order to concatenate.
        Expected to be of the form "x,y" or "x,y,z1"
    channel_name : string of coordinate dimension to concatentate (band, time,
        etc). Check options with rioxarray.open_rasterio('filename').coords
    attribute_name : string name of rioxarray attribute holding a time/date
        label. Check with rioxarray.open_rasterio('filename').attrs
    
    Returns
    -------
    xdr : xarray object of x,y,time, with approriate metadata.

    
`get_date_after_last_underscore(file_list)`
:   Extract the date from the file name after the last underscore.
    
    Parameters
    ----------
    file_list : list of filename strings in date order to concatenate.
    
    Returns
    -------
    result : list of dates in date order to concatenate.

    
`get_mask_array(xdr, mask_band=None, verbose=True)`
:   Return mask of the data, e.g. for cloud-cover.
    The mask values will be set to True if the mask band is not 0, and False otherwise.
    If no mask band is provided, a mask band will be searched for in the xarray attribute metadata.
    
    Parameters
    ----------
    xdr : xarray
        xarray dataset to mask
    mask_band : str or int, optional   
        Name or index of the band to use as a mask. 
        If not provided, a mask abd will be searched for in the xarray attribute metadata.
    
    Returns
    -------
    mask: array, bool

    
`multiband_raster_to_xarray(file_list, date_list=None, mask_bandname=None)`
:   Converts a stack of multiband raster with different dates to an xarray object.
    
    Parameters
    ----------
    file_list : list of filename strings in date order to concatenate.
    date_list : list of dates in date order to concatenate. 
        If None provided, the dates will be extracted from the file names.
        This assumes that the date is given at the end of the file name after an underscore.

    
`temporal_crop(xdr, start_time, end_time)`
:   Cuts an xarray object by start and end times.
    
    Parameters
    ----------
    xdr : xarray object of x,y,time
    start_time : string time in 'yyyy-mm-dd' format.
    end_time : string time in 'yyyy-mm-dd' format.
    
    Returns
    -------
    xdr_crop : xarray object of x,y,time, with approriate metadata.