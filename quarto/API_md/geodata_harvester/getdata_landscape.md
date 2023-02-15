Module geodata_harvester.getdata_landscape
==========================================
Download landscape data from Soil and Landscape Grid of Australia (SLGA).

Core functionality:
- Retrieval of WCS capability  with function get_capabilities()
- automatic download landscape data via Web Coverage Service (WCS)
- clip data to custom bounding box
- save data as multi-band geotif
- plot data as map

The landscape layers and metadata are described as dictionary in the module function get_landscapedict()
and the respective licensing and attribution are available with the module function getdict_license()

More details about the data and attributions can be found here:
https://www.clw.csiro.au/aclep/soilandlandscapegrid/ProductDetails-LandscapeAttributes.html

This package is part of the Data Harvester project developed for the Agricultural Research Federation (AgReFed).

Copyright 2022 Sydney Informatics Hub (SIH), The University of Sydney

This open-source software is released under the LGPL-3.0 License.

Author: Sebastian Haan

Functions
---------

    
`get_capabilities()`
:   Get capabilities from WCS layer
    
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

    
`get_landscape_layers(layernames, bbox, outpath, resolution=3)`
:   Download landscape layers from SLGA data server and saves as geotif.
    
    Parameters
    ----------
    layernames : list of layer names
    bbox : bounding box [min, miny, maxx, maxy] in
    resolution : resolution in arcsec (Default: 3 arcsec ~ 90m, which is native resolution of SLGA data)
    outpath : output path
    
    Returns
    -------
    fnames_out : list of output file names
    
    TBD: check that Request image size does not exceeds allowed limit. Set Timeout?

    
`get_landscapedict()`
:   Get dictionary of landscape SLGA data.
    The landscape attribute products available from the Soil and Landscape Grid of Australia (SLGA)
    were derived from DEM-S, the smoothed version of the national 1 second resolution Digital Elevation Model,
    which was derived from the 1 second resolution Shuttle Radar Topography Mission (SRTM) data acquired by NASA in February 2000.
    
    Spatial resolution: 3 arc seconds (approx 90m);
    Data license : Creative Commons Attribution 3.0 (CC By);
    Format: GeoTIFF.
    
    Run function get_capabilities(url) to update dictionary
    
    Returns
    -------
    ldict : dictionary of National Soil Map data

    
`get_wcsmap(url, identifier, crs, bbox, resolution, outfname, layername)`
:   Download and save geotiff from WCS layer
    
    Parameters
    ----------
    url : str
    identifier : str
        layer identifier
    crs : str
        layer crs
    bbox : list
        layer bounding box
    resolution : int
        layer resolution
    outfname : str
        output file name

    
`getdict_license()`
:   Retrieves the SLGA license and attribution information as dict

    
`plot_raster(infname)`
:   Read in raster tif with rasterio and visualise as map
    
    Parameters
    ----------
    infname : str

    
`test_wcs()`
: