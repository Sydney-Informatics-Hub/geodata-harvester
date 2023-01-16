# Earth Engine Data Overview

Version 0.1.0 | 5 Aug 2022

## Introduction

Through the [Google Earth Engine
API](https://earthengine.google.com/), the AgReFed Data-Harvester provides access
to the following satellite products:

- [USGS Landsat 9 Level 2, Collection 2, Tier 1](https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_LC09_C02_T1_L2?hl=en)
- [USGS Landsat 8 Level 2, Collection 2, Tier 1](https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_LC08_C02_T1_L2)
- [USGS Landsat 7 Level 2, Collection 2, Tier 1](https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_LE07_C02_T1_L2)
- [USGS Landsat 5 Level 2, Collection 2, Tier 1](https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_LT05_C02_T1_L2)
- [Sentinel-2 MSI: MultiSpectral Instrument, Level-2A](https://developers.google.com/earth-engine/datasets/catalog/COPERNICUS_S2_SR?hl=en)

**Note that Earth Engine is still under active development.** Download and
access limits apply, including a maximum download size of 32 MB
(but, ~50MB raw).
The Data Harvester uses the [`geedim`](https://github.com/dugalh/geedim) package
to overcome this ceiling but cloud processing limits (e.g. during compositing of
images) will continue to limit the amount of data that can be downloaded.

## Landsat
The USGS/NASA Landsat Program provides satellite spectral and thermal data of
the Earth from 1972. [Collection 2, Tier
1](https://www.usgs.gov/landsat-missions/landsat-collection-2-level-1-data)
products in the catalog represent data of the highest available quality with
inclusions of corrections for improved geometric accuracy, digital elevation
modeling and radiometric calibrations. Strips of collected data are packaged
into overlapping "scenes" covering approximately 170 km x 183 km using a
[standardized reference
grid](https://landsat.gsfc.nasa.gov/about/the-worldwide-reference-system/).

**Coverage**: See coverage [here](https://sentinel.esa.int/web/sentinel/user-guides/sentinel-2-msi/revisit-coverage)

**Resolution**: [15/30/100 m](https://www.usgs.gov/faqs/what-are-band-designations-landsat-satellites)

**Period (y-m-d)**:

- Landsat 9  : 2021-10-31 – present
- Landsat 8  : 2013-03-18 – present
- Landsat 7  : 1999-05-28 – 2022-04-06
- Landsat 5  : 1984-03-16 – 2012-05-05 

**Updates**: Daily

**Revisit frequency**: 16 days

**Attribution**: tbd

## Sentinel-2, Level 2A
Sentinel-2 is part of a constellation of satellites in the [Copernicus
Program](https://www.copernicus.eu/en) and surface reflectance images have been
available from 2017. [Level 2A
images](https://docs.sentinel-hub.com/api/latest/data/sentinel-2-l2a/) provide
orthorectified and atmospherically corrected surface reflectance data. Each
Level 2A product is composed of 100 km^2^ tiles in cartographic geometry
(UTM/WGS84 projection).

**Coverage**: See coverage [here](https://sentinel.esa.int/web/sentinel/user-guides/sentinel-2-msi/revisit-coverage)

**Resolution**: [10/20/60 m](https://sentinels.copernicus.eu/web/sentinel/missions/sentinel-2/instrument-payload/resolution-and-swath)

**Period (y-m-d)**: 2017-03-28 – present

**Updates**: Daily

**Revisit frequency**: 5 days

**Attribution**: tbd


## Functionality

The following functionality are supported:
 
- Selecting image(s) based on date(s)
- Automatic cloud masking, shadow masking, using `eemont` and `geedim`
- Automatic scale and offsetting, using `eemont` 
- Image compositioning/reduction
- Automatic calculation of spectral indices (via [Awesome Spectral
  Indices](https://github.com/awesome-spectral-indices/awesome-spectral-indices))
- Interactive map previews, with automatic pixel stretching, using `geemap` and `geetools`
- Download image(s) using split-download-assemble method to overcome size
  limits, using `geedim` 

