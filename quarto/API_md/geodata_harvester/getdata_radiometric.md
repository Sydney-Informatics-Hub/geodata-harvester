Module geodata_harvester.getdata_radiometric
============================================
Script to download Radiometric data from NCI’s GSKY Data Server (using WCS) for a given
resolution, and bounding box. Final data is saved as geotiff or NetCDF.

A full ist of datasets can be retrieved with get_radiometricdict() or get_capabilities() for a given url
An overview of all datasets can be also found here:
https://opus.nci.org.au/display/Help/Datasets

For more details of the NCI GSKY WCS, please see here:
https://opus.nci.org.au/pages/viewpage.action?pageId=137199852

LIMITATIONS: for some layers the server readout time can occasionally exceed 30s (longer readout time in request seems to be ignored)
In case this happens please try later again when the NCI server is less loaded.

This package is part of the Data Harvester project developed for the Agricultural Research Federation (AgReFed).

Copyright 2022 Sydney Informatics Hub (SIH), The University of Sydney

This open-source software is released under the LGPL-3.0 License.

Author: Sebastian Haan

Functions
---------

    
`get_capabilities()`
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

    
`get_radiometric_image(outfname, layername, bbox, url, resolution=1, crs='EPSG:4326', format_out='GeoTIFF')`
:   Download radiometric data layer and save geotiff from WCS layer.
    
    Parameters
    ----------
    outfname : str
        output file name
    layername : str
        layer identifier
    bbox : list
        layer bounding box
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

    
`get_radiometric_layers(outpath, layernames, bbox, resolution=1, crs='EPSG:4326', format_out='GeoTIFF')`
:   Wrapper function for downloading radiometric data layers and save geotiffs from WCS layer.
    
    Parameters
    ----------
    outpath: str
        output path
    layername : list of strings
        layer identifiers
    bbox : list
        layer bounding box
    resolution : int
        layer resolution in arcsec
    url : str
        url of wcs server
    crs: str
        crsm default 'EPSG:4326'
    format_out: str
        output format, either "GeoTIFF" or "NetCDF"
    
    Return
    ------
    list of output filenames

    
`get_radiometricdict()`
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

    
`getdict_license()`
:   Retrieves the Geoscience Australia data license and NCI attribution information as dict

    
`plot_raster(infname)`
:   Read in raster tif with rasterio and visualise as map.
    
    Parameters
    ----------
    infname : str