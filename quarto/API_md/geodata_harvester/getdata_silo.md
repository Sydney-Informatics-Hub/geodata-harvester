Module geodata_harvester.getdata_silo
=====================================
Python script to automatically download and crop climate data layers from SILO.

Functionalities:
- download SILO data for custom time period and layer(s) as defined in dictionary
- clip data to custom bounding box
- save data as multi-band geotiff or netCDF

The SILO climate layers are described as dictionary in the module function get_silodict()
and the SILO licensing and attribution are availabe with the module function getdict_license()

More details on the SILO climate variables can be found here:
https://www.longpaddock.qld.gov.au/silo/about/climate-variables/
and more details about the gridded data structure here:
https://www.longpaddock.qld.gov.au/silo/gridded-data/
and a data index:
https://s3-ap-southeast-2.amazonaws.com/silo-open-data/Official/annual/index.html

This package is part of the Data Harvester project developed for the Agricultural Research Federation (AgReFed).

Copyright 2022 Sydney Informatics Hub (SIH), The University of Sydney

This open-source software is released under the LGPL-3.0 License.

Author: Sebastian Haan

Functions
---------

    
`download_file(url, layername, year, outpath='.')`
:   download file from url
    
    INPUT:
    url : str
    outpath : str
    
    OUTPUT:
    file : str

    
`get_SILO_layers(layernames, date_start, date_end, outpath, bbox=None, format_out='tif', delete_tempfiles=False, verbose=False)`
:   Get raster data from SILO for certain climate variable and save data as geotif.
    If multiple times are requested, then each time will be saved in on band of multi-band geotif.
    All layers are available with daily resolution (except 'monthly_rain')
    
    This function includes validation of years and automatically download of data from SILO in temporary folder.
    
    Input:
        layernames : list climate variable names (see below)
        date_start : str, start date of time series in format 'YYYY-MM-DD'
        date_end : str, end date of time series in format 'YYYY-MM-DD'
        outpath : str, path to save output data
        bbox : list of bounding box coordinates (optional)
        format_out : str, format of output data: either 'NetCDF' (nc) or 'GeoTIFF' (tif)
        delete_tempfiles : bool, delete temporary files after processing
    
    Returns:
        fnames_out : list of output filenames
    
    layer names:
        - 'daily_rain' (Daily rainfall, mm)
        - 'monthly_rain' (Monthly rainfall, mm)
        - 'max_temp' (Maximum temperature, deg C)
        - 'min_temp'  (Minimum temperature. deg C)
        - 'vp' (Vapour pressure, hPa)
        - 'vp_deficit' (Vapour pressure deficit, hPa)
        - 'evap_pan' (Class A pan evaporation, mm)
        - 'evap_syn' (Synthetic estimate, mm)
        - 'evap_comb' (Combination: synthetic estimate pre-1970, class A pan 1970 onwards, mm)
        - 'evap_morton_lake' (Morton's shallow lake evaporation, mm)
        - 'radiation'   (Solar radiation: Solar exposure, consisting of both direct and diffuse components, MJ/m2)
        - 'rh_tmax'     (Relative humidity:     Relative humidity at the time of maximum temperature, %)
        - 'rh_tmin'     (Relative humidity at the time of minimum temperature, %)
        - 'et_short_crop' (Evapotranspiration FAO564 short crop, mm)
        - 'et_tall_crop' (ASCE5 tall crop6, mm)
        - 'et_morton_actual' (Morton's areal actual evapotranspiration, mm)
        - 'et_morton_potential' (Morton's point potential evapotranspiration, mm)
        - 'et_morton_wet' (Morton's wet-environment areal potential evapotranspiration over land, mm)
        - 'mslp' (Mean sea level pressure Mean sea level pressure, hPa)
    
    For more details see:
    SILO data structure doc for gridded data:
    https://www.longpaddock.qld.gov.au/silo/gridded-data/
    
    Notes: Here we use the SILO annual raster API to download the data and then trim to date range. 
    For data ranges much smaller than a year, one could also use the SILO daily raster API and combine dates.

    
`get_SILO_raster(layername, years, outpath, bbox=None, format_out='nc', delete_temp=False, verbose=False)`
:   Get raster data from SILO for certain climate variable and save data as geotif.
    If multiple times are requested, then each time will be saved in on band of multi-band geotif.
    All layers are available with daily resolution (except 'monthly_rain')
    
    This function includes validation of years and automatically download of data from SILO in temporary folder.
    
    Input:
        layername : str, climate variable name (see below)
        years : list of years
        outpath : str, path to save output data
        bbox : list of bounding box coordinates (optional)
        format_out : str, format of output data: either 'nc' (netCDF) or 'tif' (geotiff)
        delete_temp : bool, delete temporary folder after download
    
    Returns:
        fnames_out : list of output filenames
    
    
    
    layer names:
        - 'daily_rain' (Daily rainfall, mm)
        - 'monthly_rain' (Monthly rainfall, mm)
        - 'max_temp' (Maximum temperature, deg C)
        - 'min_temp'  (Minimum temperature. deg C)
        - 'vp' (Vapour pressure, hPa)
        - 'vp_deficit' (Vapour pressure deficit, hPa)
        - 'evap_pan' (Class A pan evaporation, mm)
        - 'evap_syn' (Synthetic estimate, mm)
        - 'evap_comb' (Combination: synthetic estimate pre-1970, class A pan 1970 onwards, mm)
        - 'evap_morton_lake' (Morton's shallow lake evaporation, mm)
        - 'radiation'   (Solar radiation: Solar exposure, consisting of both direct and diffuse components, MJ/m2)
        - 'rh_tmax'     (Relative humidity:     Relative humidity at the time of maximum temperature, %)
        - 'rh_tmin'     (Relative humidity at the time of minimum temperature, %)
        - 'et_short_crop' (Evapotranspiration FAO564 short crop, mm)
        - 'et_tall_crop' (ASCE5 tall crop6, mm)
        - 'et_morton_actual' (Morton's areal actual evapotranspiration, mm)
        - 'et_morton_potential' (Morton's point potential evapotranspiration, mm)
        - 'et_morton_wet' (Morton's wet-environment areal potential evapotranspiration over land, mm)
        - 'mslp' (Mean sea level pressure Mean sea level pressure, hPa)
    
    For more details see:
    SILO data structure doc for gridded data:
    https://www.longpaddock.qld.gov.au/silo/gridded-data/
    
    SILO url structure:
    url = "https://s3-ap-southeast-2.amazonaws.com/silo-open-data/Official/annual/<variable>/<year>.<variable>.nc
    e.g. url = "https://s3-ap-southeast-2.amazonaws.com/silo-open-data/Official/annual/monthly_rain/2005.monthly_rain.nc"

    
`get_silodict()`
:   Get dictionary of available layers and meta data
    
    OUTPUT:
    layerdict : dict
        dictionary of meta data and available layer names

    
`getdict_license()`
:   Retrieves the SILO license and attribution information as dict

    
`process_raster_daterange(infnames, date_start, date_end, outfname, layername)`
:   Combines all the raster data into one xarray dataset, trimming to the date range, 
    and saves it as a multiband tif file.
    
    Input:
        infnames : list of input filenames
        date_start : str, start date of time series in format 'YYYY-MM-DD'
        date_end : str, end date of time series in format 'YYYY-MM-DD'
        outfname : str, path+name of output file

    
`test_get_SILO_layers()`
:   test script

    
`test_get_SILO_raster()`
:   test script

    
`xarray2tif(ds, outfname, layername)`
:   Convert rio xarray dataset to multi-band geotiff with each time as separate band.
    
    TBD: optional: save separate tif each time slice
    
    INPUT:
    ds : xarray dataset
    outfname : str
        path+name of output file (".tif")
    
    OUTPUT:
    tif : str, name of multi-band geotiff