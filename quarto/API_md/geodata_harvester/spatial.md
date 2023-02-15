Module geodata_harvester.spatial
================================
Utility functions for for spatial processing.

--Function List, in order of appearence--

_points_in_circle(internal): Return all points whose indices are within a given
    circle.
_coreg_buffer(internal): Queries values of a raster around a point buffer
    region.
raster_buffer: Given a longitude,latitude point, a raster file, and a buffer
    region, find the values of all points in circular buffer.
_get_features(internal): Parse features from GeoDataFrame format to Rasterio
    format
_coreg_polygon(internal): Crops a raster to a polygon shape.
raster_polygon_buffer: Given list of longitudes and latitudes defining a
    polygon, crop raster file, return the values of all points in the polygon.

Functions
---------

    
`raster_buffer(long, lat, raster, buffer)`
:   given a longitude,latitude point, a raster file, and a buffer region,
        return the value values of all points in circular buffer.
    
    INPUTS:
    long: longitude point of interest
    lat: latitude point of interest
    raster: file path/name (as string)
    buffer: integer, raster array pixel units to return values for
    
    RETURNS
    values: list of raster array values around point of interest.

    
`raster_polygon_buffer(lngs, lats, raster)`
:   Given a list of longitudes and latitudes that define a polygone, crop a
        raster file, and return the values of all points in the polygon.
    
    INPUTS:
    lngs: list of longitudes
    lats: list of latitudes
    raster: file path/name (as string) of raster
    
    RETURNS
    values: list of raster array values inside polygon.