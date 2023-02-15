Module geodata_harvester.temporal
=================================
Utility functions for for temporal processing.

--Function List, in order of appearence--

combine_rasters_temporal: Concatenates files by time returns xarray.
aggregate_temporal: Aggregates xarrays by specified function and time period.

Functions
---------

    
`aggregate_temporal(xdr, period='yearly', agg=['mean'], outfile='temporal_agg', buffer=None)`
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
    
    Returns
    -------
    outfname_list : list of strings of output file names
    agg_list : list of strings of aggregation methods

    
`combine_rasters_temporal(file_list, channel_name='band', attribute_name='long_name')`
:   Combines multiple tif files into single xarray object. Assumes files are in
    temporal order, and additional channels contain sequential time step data.
    Also assumes files are of the same shape (x,y,t).
    
    Example:
    file_list = ['../data/mvp_daily_rain_silo/daily_rain_2017_cropped.tif',
             '../data/mvp_daily_rain_silo/daily_rain_2018_cropped.tif']
    
    xdr = combine_rasters_temporal(file_list, channel_name='band',attribute_name='long_name')
    
    Parameters
    ----------
    file_list : list of filename strings in date order to concatenate.
        Expected to be of the form "x,y" or "x,y,z1"
    channel_name : string of coordinate dimension to concatentate (band, time,
        etc). Check options with rioxarray.open_rasterio('filename').coords
    attribute_name : string name of rioxarray attribute holding a time/date
        label. Check with rioxarray.open_rasterio('filename').attrs
    
    Returns
    -------
    xdr : xarray object of x,y,time, with approriate metadata.

    
`group_by_custom_periods(xdr, periods: int, agg_range: int)`
:   NOTE: NOT ALL IMPLEMENTED!!! Specifcally multiband data. But I don't think
    we want to deal with that, as it is already accounted for previously? Maybe.
    
    Aggregates over multiple files but keeps channels independently.
    Results are written to new tif files.
    
    This function should
    
    dates of the from "yyyy-mm-dd"
    rolling mean
    
    Unit of measurment you are working in seconds, daily, monthly, yearly (or integers)
    Time steps of channels (e.g. 12xmonthly)
    time steps of files (each file represents X length of time)
    time steps of aggregation (e.g. average monthly)
    time steps of
    
    
    
    Aggregrates over multiple files and over all channels
    and writes results to new tif file(s).
    
    Step 1: combine files (assumes consistent times and start finish points)
    Step 2: roll data into outtime chunks
    Step 3: perform aggregation on chunks
    
    e.g. aggregate daily rainfall data for each month (for the duration of the files.)
    e.g. aggregate monthly temperature data over a year (for the duration of the files.)
    
    e.g. aggregate common months over multiple years, average rainfall in July from 2015 to 2020
    
    
    Takes a stream of temporal data in a particular time increment and converts
    to a new time-increment by averaging.

    
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