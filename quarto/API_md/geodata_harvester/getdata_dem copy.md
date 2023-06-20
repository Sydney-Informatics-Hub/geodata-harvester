Module geodata_harvester.getdata_dem copy
=========================================
This script downloads the National Digital Elevation Model (DEM) 1 Second Hydrologically Enforced product,
derived from the National DEM SRTM 1 Second and National Watercourses, lakes and Reservoirs.
The output image is a geotiff file with a user defined resolution and bbox.
This script also includes the capabilities to generate slope and aspect from the extracted DEM.

Core functions:
    get_capabilities(): get the available layers and their metadata
    getwcs_dem(): download the data as geotiff file for given bbox and resolution
    dem2slope(): convert geotiff to slope raster
    dem2aspect(): convert geotiff to aspect raster
    getdict_license(): get the license and attributes for the DEM 1 arc second grid

The DEM layer metadata can be retrieved with the function get_capabilities().
and the respective licensing and attribution are availabe with the module function getdict_license()

To download the DEM data, the function getwcs_dem() is used.

For more details about the data, see:
https://ecat.ga.gov.au/geonetwork/srv/eng/catalog.search#/metadata/72759

WCS url:
https://services.ga.gov.au/site_9/services/DEM_SRTM_1Second_Hydro_Enforced/MapServer/WCSServer?request=GetCapabilities&service=WCS

This package is part of the Data Harvester project developed for the Agricultural Research Federation (AgReFed).

Copyright 2022 Sydney Informatics Hub (SIH), The University of Sydney

This open-source software is released under the LGPL-3.0 License.

Author: Sebastian Haan

Functions
---------

    
`calc_gradiant(raster_dem)`
:   Calculate the gradiant from a DEM raster with rioxarray

    
`dem2aspect(fname_dem)`
:   Calculate aspect from DEM and save as geotiff
    
    Parameters
    ----------
    fname_dem : str
        DEM file name

    
`dem2slope(fname_dem)`
:   Calculate slope from DEM and save as geotiff
    
    Parameters
    ----------
    fname_dem : str
        DEM path + file name

    
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

    
`get_dem_layers(layernames, outpath, bbox, resolution=1, crs='EPSG:4326')`
:   Wrapper funtion to get the layers from the Geoscience Australia DEM 1 arc second grid
    and to calculate slope and aspect layers
    
    Parameters
    ----------
    layernames : list
        list of layer names to download
        ['DEM', 'Slope', 'Aspect']
    outpath : str
        output directory for the downloaded file
    bbox : list
        layer bounding box
    resolution : int
        layer resolution in arcsec (default 1)
    crs: str
        crs default 'EPSG:4326'
    
    Return
    ------
    Output outnames: lits of output filenames

    
`get_demdict()`
:   Get dictionary of meta data
    
    OUTPUT:
    layerdict : dict
        dictionary of meta data

    
`getdict_license()`
:   Retrieves the Geoscience Australia data license for the DEM Web Map Service as dict

    
`getwcs_dem(outpath, bbox, resolution=1, url='https://services.ga.gov.au/site_9/services/DEM_SRTM_1Second_Hydro_Enforced/MapServer/WCSServer?request=GetCapabilities&service=WCS', crs='EPSG:4326', verbose=False)`
:   Function to download and save geotiff from WCS layer.
    Default downloads the DEM 1 arc second grid from Geoscience Australia using the folllwing WCS url:
    Url = https://services.ga.gov.au/site_9/services/DEM_SRTM_1Second_Hydro_Enforced/MapServer/WCSServer?request=GetCapabilities&service=WCS
    
    Parameters
    ----------
    outpath : str
        output directory for the downloaded file
    bbox : list
        layer bounding box
    resolution : int
        layer resolution in arcsec (default 1)
    url : str
        url of wcs server, default is the Geoscience Australia DEM 1 arc second grid
    crs: str
        crs default 'EPSG:4326'
    
    Return
    ------
    Output filename

    
`plot_raster(infname)`
:   Read in raster tif with rasterio and visualise as map
    
    Parameters
    ----------
    infname : str

    
`test_getwcs_dem(outpath='./test_DEM/')`
:   Test script