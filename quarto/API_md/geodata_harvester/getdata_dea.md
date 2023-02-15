Module geodata_harvester.getdata_dea
====================================
Script to download satellite data from Digital Earth Australia (DEA)for a given time,
resolution, and bounding box. Final data is saved as geotiff or NetCDF.

Satellite data sources are calibrated by DEA for Australia and include datasets for Landsat and Sentinel2.

An overview of DEA data is available here
https://docs.dea.ga.gov.au/notebooks/DEA_datasets/README.html
and explanation of datasets here:
https://docs.dea.ga.gov.au/notebooks/Beginners_guide/02_DEA.html

A full ist of data layer names can be retrieved with get_deadict() or get_capabilities() for a given url
The DEA WCS service capabilities are also available online at:
https://docs.dea.ga.gov.au/setup/gis/web_services.html#Web-Coverage-Service-(WCS)

For more complex data processing use DEA's excellent Jupyter notebooks within their Sandbox (authentication needed)
that leverage the Open Data Cube software package (datacube-core)
https://docs.dea.ga.gov.au/setup/Sandbox/sandbox.html

Other resources:
- NCI (authentication needed)
https://docs.dea.ga.gov.au/setup/NCI/README.html

- SpatioTemporal Asset Catalog (STAC) endpoint  (authentication needed):
https://docs.dea.ga.gov.au/notebooks/Frequently_used_code/Downloading_data_with_STAC.html

LIMITATIONS: for large bbox the server can exceeds limits and the data is not returned.

This package is part of the Data Harvester project developed for the Agricultural Research Federation (AgReFed).

Copyright 2022 Sydney Informatics Hub (SIH), The University of Sydney

This open-source software is released under the LGPL-3.0 License.

Author: Sebastian Haan

TBF:
- apply cloud mask to downloaded images automatically (accept "valid", "water", "snow")
- include some DEA tools https://github.com/GeoscienceAustralia/dea-notebooks/blob/stable/Tools/dea_tools/

Functions
---------

    
`get_capabilities(url)`
:   Get capabilities from WCS layer.
    
    Parameters
    ----------
    url : str
        layer url
    
    Returns
    -------
    keys    : list
        layer identifiers
    titles  : list  of str
        layer titles
    descriptions : list of str
        layer descriptions
    bboxs   : list of floats
        layer bounding boxes

    
`get_dea_images(layername, year, bbox, resolution, outpath, crs='EPSG:4326', format_out='GeoTIFF', verbose=False)`
:   Get all satellite images from DEA for a given layer and year.
    Downloaded images are saved either as GeoTIFF or NetCDF.
    
    Parameters
    ----------
    layername : str
        layer identifier
    year : str
        selected year for images
    bbox : list
        layer bounding box
    resolution : int
        layer resolution in arcsec
    outpath : str
        output directory
    crs: str
        crs, default 'EPSG:4326'
    format: str
        output format, either "GeoTIFF" or "NetCDF"
    
    Return
    ------
    Exited ok: boolean

    
`get_dea_images_daterange(layername, date_min, date_max, bbox, resolution, outpath, crs='EPSG:4326', format_out='GeoTIFF', verbose=False)`
:   Get all satellite images from DEA for a given layer and year.
    Downloaded images are saved either as GeoTIFF or NetCDF.
    
    Parameters
    ----------
    layername : str
        layer identifier
    date_min : str
        start datetime string for images (format: YYYY-MM-DD)
    date_max : str
        end datetime string for images (format: YYYY-MM-DD)
    bbox : list
        layer bounding box
    resolution : int
        layer resolution in arcsec
    outpath : str
        output directory
    crs: str
        crs, default 'EPSG:4326'
    format: str
        output format, either "GeoTIFF" or "NetCDF"
    
    Return
    ------
    Exited ok: boolean

    
`get_dea_layers(layernames, years, bbox, resolution, outpath, crs='EPSG:4326', format_out='GeoTIFF', verbose=False)`
:   Get all images for all layers and all years.
    Downloaded images are saved in outpath.
    
    Parameters
    ----------
    layernames : list of strings
        layer identifiers
    years : list
        years, e.g. [2019, 2020]
    bbox : list
        layer bounding box
    resolution : int
        layer resolution in arcsec
    outpath : str
        output directory
    crs: str
        crs, default 'EPSG:4326'
    format: str
        output format, either "GeoTIFF" or "NetCDF"
    
    Return
    ------
    list of output filenames for each layer

    
`get_dea_layers_daterange(layernames, date_start, date_end, bbox, resolution, outpath, crs='EPSG:4326', format_out='GeoTIFF', verbose=False)`
:   Get all images for all layers and all dates between start_date and end_date.
    Downloaded images are saved in outpath.
    
    Parameters
    ----------
    layernames : list of strings
        layer identifiers
    date_start : str
        start date in dateformat YYYY-MM-DD
    date_end : str
        end date in dateformat YYYY-MM-DD
    bbox : list
        layer bounding box
    resolution : int
        layer resolution in arcsec
    outpath : str
        output directory
    crs: str
        crs, default 'EPSG:4326'
    format: str
        output format, either "GeoTIFF" or "NetCDF"
    
    Return
    ------
    list of output filenames for each layer

    
`get_deadict()`
:   Returns dictionary of keys and layer titles
    
    To update manually please run get_capabilities() to retrieve all current layer details

    
`get_times(url, layername, year=None)`
:   Return available dates for layer.
    
    Parameters
    ----------
    url: str, layer url
    layername: str, name of layer id
    year: int or str, year of interest (if None, times for all available years are returned)
    
    Return
    ------
    list of dates

    
`get_times_startend(url, layername, dt_start, dt_end)`
:   Return all available images datetimes for layer in range
    between start and end date.
    
    Parameters
    ----------
    url: str, layer url
    layername: str, name of layer id
    dt_start: str, start date in dateformat YYYY-MM-DD
    dt_end: str, end date in dateformat YYYY-MM-DD
    
    Return
    ------
    list of dates

    
`get_wcsmap(outfname, layername, bbox, date, resolution, url, crs='EPSG:4326', format_out='GeoTIFF')`
:   Download and save geotiff from WCS layer.
    
    Parameters
    ----------
    outfname : str
        output file name
    layername : str
        layer identifier
    bbox : list
        layer bounding box
    date : str
        datetime
    resolution : int
        layer resolution in arcsec
    url : str
        url of wcs server
    crs: str
        crsm default 'EPSG:4326'
    format: str
        output format, either "GeoTIFF" or "NetCDF"
    
    Return
    ------
    Exited ok: boolean

    
`getdict_cloudmask()`
:   return dict of cloud mask

    
`getdict_license()`
:   Retrieves the DEA data license and NCI attribution information as dict

    
`plot_raster(infname)`
:   Read in raster tif with rasterio and visualise as map.
    
    Parameters
    ----------
    infname : str

    
`test_get_capabilities()`
:   Test script to retrieve WCS capabilities

    
`test_get_dea_images()`
:   Test script to retrieve and save images for a given year

    
`test_get_dea_images_daterange()`
:   Test script to retrieve and save images for a given year

    
`test_get_times()`
:   Test script to retrieve available times for a layer

    
`test_get_times_startend()`
:   Test script to retrieve available times for a layer

    
`test_get_wcsmap()`
:   Test script to retrieve and save image for one layer and date

    
`write_deadict()`
:   Generates new DEA dictionary from crawling WCS url