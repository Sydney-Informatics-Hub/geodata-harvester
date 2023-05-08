#!/bin/python
"""

Utility functions for for temporal processing.

--Function List, in order of appearence--

combine_rasters_temporal: Concatenates files by time returns xarray.
aggregate_temporal: Aggregates xarrays by specified function and time period.

"""

import numpy as np
import pandas as pd
import rioxarray
import xarray as xr
import datetime


def combine_rasters_temporal(
    file_list, channel_name="band", attribute_name="long_name"
):
    """
    Combines multiple tif files into single xarray object. 
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

    """
    #print("Concatenating", channel_name, "and", attribute_name, "over", file_list)
    # file_list = glob(os.path.join(data_dir, '*.tif'))

    if type(file_list) == str:
        file_list = [file_list]

    # Append all data/channels, collect metadata lists
    array_list = []
    attrs = ()
    first = True
    for x in file_list:
        xds = rioxarray.open_rasterio(x)

        if channel_name not in xds.coords:
            raise ValueError(
                channel_name + " not a channel in the raster " + x + " Options are",
                [t for t in xds.coords],
            )
            return None

        if attribute_name not in xds.attrs:
            raise ValueError(
                attribute_name
                + " not an attribute in the raster "
                + x
                + " Options are",
                [t for t in xds.attrs],
            )
            return None

        array_list.append(xds)
        attrs = attrs + xds.attrs[attribute_name]
        if first == True:
            coords = xds[channel_name].values

            first = False
        else:
            coords = np.append(coords, xds[channel_name].values + coords[-1])

    xdr = xr.concat(array_list, channel_name)
    # print(agg,coords,attrs)
    # xdr = xdr.assign_attrs({attr: attrs})
    xdr = xdr.assign_coords({channel_name: np.array(pd.to_datetime(attrs))})
    xdr = xdr.rename({channel_name: "time"})
    del xdr.attrs[attribute_name]

    return xdr


def multiband_raster_to_xarray(file_list, date_list = None, mask_bandname = None):
    """
    Converts a stack of multiband raster with different dates to an xarray object.
    
    Parameters
    ----------
    file_list : list of filename strings in date order to concatenate.
    date_list : list of dates in date order to concatenate. 
        If None provided, the dates will be extracted from the file names.
        This assumes that the date is given at the end of the file name after an underscore.
    """
    # Extract the dates from the file names if no date list is provided
    if date_list is None:
        date_list = get_date_after_last_underscore(file_list)

    # Check if the lists have the same length
    assert len(file_list) == len(date_list), "File list and date list must have the same length."
    
    # Create an empty list to store the DataArrays
    data_arrays = []

    for file, date in zip(file_list, date_list):
        # Read the raster file using rioxarray
        xds = rioxarray.open_rasterio(file)

        # Assign the time coordinate
        xds = xds.assign_coords({"time": pd.to_datetime(date)})
        xds = xds.expand_dims("time")

        # Append the DataArray to the list
        data_arrays.append(xds)

    # Concatenate the DataArrays along the time dimension
    stacked_data = xr.concat(data_arrays, dim="time")

    return stacked_data


def temporal_crop(xdr, start_time, end_time):
    """
    Cuts an xarray object by start and end times.

    Parameters
    ----------
    xdr : xarray object of x,y,time
    start_time : string time in 'yyyy-mm-dd' format.
    end_time : string time in 'yyyy-mm-dd' format.

    Returns
    -------
    xdr_crop : xarray object of x,y,time, with approriate metadata.
    """

    xdr_crop = xdr.sel(time=slice(start_time, end_time))

    return(xdr_crop)


def aggregate_temporal(xdr,
    period="yearly", agg=["mean"], outfile="temporal_agg", buffer = None, fill_nan = True):
    """
    Make a data aggregation (mean, median, sum, etc) through time on an xarray.
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

    """

    if fill_nan:
        # Define the possible attribute names for fill values
        nodata_names = ["_FillValue", "missing_value", "nodata", "nodatavalue"]
        nodata_name_found = False
        for nodata_name in nodata_names:
            if nodata_name in xdr.attrs:
                xdr = xdr.where(xdr != xdr.attrs[nodata_name], np.nan)
                nodata_name_found = True
                break
        # Check for case-insensitive nodata names
        if not nodata_name_found:
            for key, value in xdr.attrs.items():
                if key.lower() in [attr.lower() for attr in nodata_names]:
                    xdr = xdr.where(xdr != value, np.nan)
                    nodata_name_found = True
                    break
        if not nodata_name_found:
            print("No nodata value found in attributes. Will not fill nan values.")


    # Check the aggregation methods are okay
    agg_types = ["mean", "median", "sum", "perc95", "perc5", "max", "min"]
    aggcheck = [a for a in agg if a in agg_types]
    if aggcheck is None:
        raise ValueError("Invalid Aggregation type. Expected any of: %s" % agg_types)
    #else:
        #print("Finding", aggcheck, " out of possible", agg_types)
        #print("for", period, " period.")

    # Group by the appropriate time period
    if period == "yearly":
        xdr_groups = xdr.groupby("time.year")

        if buffer != None:
            xx = xdr_groups.apply(lambda x: x.isel(time=slice(0,buffer)))
            xdr_groups = xx.groupby("time.year")

    elif period == "monthly":
        xdr_groups = xdr.groupby("time.month")

        if buffer != None:
            xx = xdr_groups.apply(lambda x: x.isel(time=slice(0,buffer)))
            xdr_groups = xx.groupby("time.month")

    elif type(period) == int:
        bins = int(np.floor(len(xdr) / period))
        xdr_groups = xdr.groupby_bins("time", bins)

        if buffer != None:
            xx = xdr_groups.apply(lambda x: x.isel(time=slice(0,buffer)))
            xdr_groups = xx.groupby_bins("time", period)


    else:
        raise ValueError(
            "Invalid temporal period. Expected any of: 'yearly', 'monthly', or an integer period"
        )

    aggdict = {}
    for agg_type in aggcheck:
        if agg_type == "mean":
            aggdict["mean"] = xdr_groups.mean()
        elif agg_type == "median":
            aggdict["median"] = xdr_groups.median()
        elif agg_type == "sum":
            aggdict["sum"] = xdr_groups.sum()
        elif agg_type == "perc95":
            aggdict["perc95"] = xdr_groups.quantile(q=0.95)
        elif agg_type == "perc5":
            aggdict["perc5"] = xdr_groups.quantile(q=0.05)
        elif agg_type == "max":
            aggdict["max"] = xdr_groups.max()
        elif agg_type == "min":
            aggdict["min"] = xdr_groups.min()


    # Keep track of the names of all files produced
    outfname_list = []
    agg_list = []

    # For all the different aggregation methods
    for a in aggcheck:
        # For each period of time in each of the groups, save it out!
        for p in aggdict[a]:

            # Each temporal grouping results in different group labels
            if period == "yearly":
                label = str(p["year"].values)
            elif period == "monthly":
                label = str(p["month"].values).zfill(2)
            elif type(period) == int:
                label = str(p["time_bins"].values)[1:11]

            p.rio.to_raster(outfile + "_" + a + "_" + label + ".tif")
            outfname_list.append(outfile + "_" + a + "_" + label + ".tif")
            agg_list.append(a)

            print(a, "of", label, "saved in:", outfile + "_" + a + "_" + label + ".tif")

    return outfname_list, agg_list


def get_date_after_last_underscore(file_list):
    result = []

    for filename in file_list:
        split_string = filename.rsplit('_', 1)  # Split the string from the right side, keeping only the last part

        # Check if the string was split
        if len(split_string) > 1:
            last_part = split_string[-1]  # Get the part after the last "_"
        else:
            last_part = filename  # If the string didn't have any "_", return the original string

        # Remove the file format ending
        last_part = last_part.rsplit('.', 1)[0]

        # test if the last part is a date
        try:
            datetime.datetime.strptime(last_part, '%Y-%m-%d')
        except ValueError:
            print("The last part of the filename is not a date: ", last_part)
            raise ValueError

        result.append(last_part)

    return result


def get_mask_array(xdr, mask_band = None, verbose = True):
    """
    Return mask of the data, e.g. for cloud-cover.
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
    """
    if mask_band is not None:
        if isinstance(mask_band, int):
            if verbose: print(f"Masking values with Nan where mask band {mask_band} is not 0")
        elif isinstance(mask_band, str):
            if verbose: print(f"Masking values with Nan where mask band {mask_band} is not 0")
            mask_band = [i for i, s in enumerate(xdr.attrs['long_name']) if s == mask_band]
            mask_band = mask_band[0] + 1
        else:
            if verbose: print("Mask band must be an integer or string")
            return
        mask = xdr.sel(band=mask_band).values != 0

    if mask_band is None:
        # find band number for attribute that includes 'mask'
        mask_band = [i for i, s in enumerate(xdr.attrs['long_name']) if 'mask' in s]
        if len(mask_band) == 0:
            if verbose: print('No mask band found in attributes. Proceeding without masking.')
        else:
            if len(mask_band) > 1:
                if verbose: print(f"Multiple mask bands found in attributes. Proceeding with mask band: {xdr.attrs['long_name'][mask_band[0]]}")
            mask_band = mask_band[0] + 1
            if verbose: print(f"Masking values with Nan where mask band {xdr.attrs['long_name'][mask_band[0]]} is valid")
            mask = xdr.sel(band=mask_band).values != 0

    return mask

