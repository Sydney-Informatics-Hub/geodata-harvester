Module geodata_harvester.getdata_slga
=====================================
Python script to download data from Soil and Landscape Grid of Australia (SLGA).

Core functionality:
- Retrieval of WCS capability  with function get_capabilities()
- automatic download SLGA data for given depth range and layer(s) via Web Coverage Service (WCS)
- clip data to custom bounding box
- save data as multi-band geotiff
- plot data as map

The SLGA layers and metadata are described as dictionary in the module function get_slgadict()
and the respective licensing and attribution are availabe with the module function getdict_license()

More details about the SLGA data and attributions can be found here:
https://www.clw.csiro.au/aclep/soilandlandscapegrid/ProductDetails-SoilAttributes.html

This package is part of the Data Harvester project developed for the Agricultural Research Federation (AgReFed).

Copyright 2022 Sydney Informatics Hub (SIH), The University of Sydney

This open-source software is released under the LGPL-3.0 License.

Author: Sebastian Haan

Functions
---------

    
`depth2identifier(depth_min, depth_max)`
:   Get identifiers that correspond to depths and their corresponding confidence interval identifiers
    that lie within the depth range depth_min to depth_max.
    
    Parameters
    ----------
    depth_min : minimum depth [cm]
    depth_max : maximum depth [cm]
    
    Returns
    -------
    identifiers : layer identifiers
    identifiers_ci_5pc : identifiers for confidence interval 5%
    identifiers_ci_95pc : identifiers for confidence interval 95%
    depth_lower : lower depth of interval
    depth_upper : upper depth of interval

    
`get_capabilities(url)`
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

    
`get_slga_layers(layernames, bbox, outpath, resolution=3, depth_min=0, depth_max=200, get_ci=True, verbose=False)`
:   Download layers from SLGA data server and saves as geotif.
    
    Parameters
    ----------
    layernames : list of layer names
    bbox : bounding box [min, miny, maxx, maxy] in
    resolution : resolution in arcsec (Default: 3 arcsec ~ 90m, which is native resolution of SLGA data)
    depth_min : minimum depth (Default: 0 cm). If depth_min and depth_max are lists, then must have same length as layernames
    depth_max : maximum depth (Default: 200 cm, maximum depth of SLGA data)
    outpath : output path
    
    Returns
    -------
    fnames_out : list of output file names
    
    TBD: check that Request image size does not exceeds allowed limit. Set Timeout?

    
`get_slgadict()`
:   Get dictionary of SLGA data.
    
    The Soil Facility produced a range of digital soil attribute products.
    Each product contains six digital soil attribute maps, and their upper and lower confidence limits,
    representing the soil attribute at six depths: 0-5cm, 5-15cm, 15-30cm, 30-60cm, 60-100cm and 100-200cm.
    These depths are consistent with the specifications of the GlobalSoilMap.net project (http://www.globalsoilmap.net/).
    The digital soil attribute maps are in raster format at a resolution of 3 arc sec (~90 x 90 m pixels).
    
    Period (temporal coverage; approximately): 1950-2013;
    Spatial resolution: 3 arc seconds (approx 90m);
    Data license : Creative Commons Attribution 3.0 (CC By);
    Target data standard: GlobalSoilMap specifications;
    Format: GeoTIFF.
    
    Run function get_capabilities(url) to update dictionary
    
    Returns
    -------
    slgadict : dictionary of National Soil Map data

    
`get_wcsmap(url, identifier, crs, bbox, resolution, outfname)`
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

    
`identifier2depthbounds(depths)`
:   Get min and max depth of list of depth strings
    
    Parameters
    ----------
    depth_list: list of depth
    
    Returns
    -------
    min depth
    max depth

    
`plot_raster(infname)`
:   Read in raster tif with rasterio and visualise as map
    
    Parameters
    ----------
    infname : str

    
`test_wcs()`
: