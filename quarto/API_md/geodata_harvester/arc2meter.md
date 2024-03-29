Module geodata_harvester.arc2meter
==================================
Converter arc seconds to meter and vice versa.

Earth circumference around Equator is 40,075,017 meter
1 arc second at equatorial sea level = 1855.325m/60 = 30.922m

Earth circumference around Poles is 40,007,863 meter
1 arc second latitude = 1852.216m/60 = 30.87m

Formula for longitude: meters = arcsec * cos(degree latitude) * 30.922m
(conversion for latitude stays constant: arcsec * 30.87m)

Functions
---------

    
`calc_arc2meter(arcsec, latitude)`
:   Calculate arc seconds to meter
    
    Input
    -----
    arcsec: float, arcsec
    latitude: float, latitude
    
    Return
    ------
    (meters Long, meters Lat)

    
`calc_meter2arc(meter, latitude)`
:   Calculate meter to arc seconds
    
    Input
    -----
    meter: float, meter
    latitude: float, latitude
    
    Return
    ------
    (arcsec Long, arcsec Lat)