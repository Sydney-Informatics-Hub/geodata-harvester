Module geodata_harvester.validate_settings
==========================================
# How to: 
import validate_settings
validate_settings.validate(fname_settings)

Functions
---------

    
`check_schema(settings)`
:   Validate Schema

    
`check_schema2(settings)`
:   Validate Schema with package schema
    
    Requirements: schema

    
`check_target_dates(dates)`
:   Validate date range

    
`check_target_size(bbox, target_res, nmax_pixels=100000000.0)`
:   Validate bounding box and check number of raster pixels
    
    INPUT
    -----
    bbox: list, target bounding box
    target_res: float or int, target resolution
    nmax_pixels: maximum number of raster pixels for target image (nmax = nx * ny)

    
`check_target_sources(target_sources)`
:   Validate selected data layers and options
    
    TBD: GEE validations

    
`validate(fname_settings, verbose=False)`
:   Validates all settings with regard
        - schema
        - date range
        - data size and bounding box
        - data layers and options
    
    INPUT:
    fname_settings: str, path + filename of settings