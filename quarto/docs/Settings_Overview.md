---
title: Settings Overview
---

# Overview and Description of Settings for the AgReFed Data-Harvester

The following documentation outlines the available settings for the Data Harvester.
For a more interactive exploration of settings, please use the harvesterwidget (see, e.g., [example widget notebook](https://github.com/Sydney-Informatics-Hub/geodata-harvester/blob/main/notebooks/example_harvest_with_widgets.ipynb)).

## Table of Contents
- [YAML File Format](#yaml-file-format)
- [Jupyter Settings Widget](#jupyter-settings-widget)
- [Settings Validation](#settings-validation)
- [Input and Output Settings](#input-and-output-settings)
- [Spatial and Temporal Settings](#spatial-and-temporal-settings)
- [Data Selection Settings](#data-selection-settings)


## YAML File Format
The settings are specified by the user in a .yaml settings file (see e.g., settings/settings_v0.3.yaml). A YAML file is a Unicode based language and is designed for human interaction and to work well with modern programming languages, and is typically used for configuration settings and reusable workflows. YAML uses the .yaml extension (alternatively .yml) for its files. Its syntax is independent of a specific programming language. 

Templates for the .yaml settings file are provided in the folder `settings`. More information about YAML Syntax can be found [here](https://docs.fileformat.com/programming/yaml/).


## Jupyter Settings Widget
Alternatively, settings can be selected in the interactive widget of the Jupyter Notebook, which also automatically saves all settings for a run in a .yaml file as well. The interactive widgets are powered by ipywidgets and are currently supported for the Jupyter Notebooks. The widget also allows the user to load a saved .yaml file.

Note for developers: To make changes to the functionality of the widgets (e.g, extending with new settings or options), please see the script `harvesterwidgets.py` in the folder `widgets`.


## Settings Validation 
The settings file can be validated and checked for correct options (e.g. valid schema, data types, and data ranges) via the function `validate` in `validate_settings.py`, e.g.:
```python
fname_settings = 'settings_harvest.yaml'
import validate_settings
validate_settings.validate(fname_settings)
```

Note for developers: Please update `validate_settings.py` and version if new data layers or options are added to the Data-Harvester.


## Input and Output Settings

The input file name is specified in `infile` and is a .csv file that and must include at least point coordinates. The Data Harvester will download new data for these coordinates and  align with any given data in the input file. Th  column names for the latitude and longitude coordinates are selected by the settings `colname_lat` and `colname_lng`, respectively.

All data results and images will be saved in the output directory as specified in the settings `outpath`.

**Example:**

```yaml
#Input File:
infile: ../testdata/Pointdata_Llara.csv

#Output Path:
outpath: ../../dataresults/

#Headername of Latitude in input file:
colname_lat: Lat

#Headername of Longitude in input file:
colname_lng: Long

```


## Spatial and Temporal Settings

The spatial extent of the requested images can be given as bounding box list in the settings `target_bbox`, in the order: lng_min, lat_min, lng_max, lat_max (left, bottom, right, top corner of box). If no bounding box is provided, Geodata-Harvester will automatically infer a padded bounding box based on the extent of the coordinates given in the input file.

The spatial resolution of the requested images is specified in `target_res` and given in arcsec (1 arcsec corresponds to roughly 30m on the Equator, please see `arc2meter.py`for calculating exact conversion of meter to arcsec and vice versa).

The time range for the requested data is specified via minimum date `date_min` and maximum date `date_max` (format: YYYY-MM-DD). All data available withon this time interval will be extracted.

For data extraction, the user can choose a number of times slices for the given period which is given as integer number `temp_intervals`. The time buffer window can be provided as number of days in `temp_buffer`, which specifies the number of days for which data is aggregated around each time slice. For example, if `date_min` to `date_max` is 24 weeks, `temp_intervals` = 24, and `temp_buffer` = 7, the data-table will be populated with the aggregated stats for each week within the specified time period. If `temp_buffer` is set to 1, the nearest available date will be extracted for each time slice.


**Example:**

```yaml
#Bounding Box as (lng_min, lat_min, lng_max, lat_max):
target_bbox: ''

#Select start date:
date_min: : 2023-01-01

#Select end date:
date_max: : 2023-02-01

#Spatial Resolution [in arcsec]:
target_res: 6.0

#Temporal buffer window (in days)
temp_buffer: 1

# Number of time interval slices in given date range
temp_intervals: 4
```


## Data Selection Settings

The requested layers are specified in the settings `target_sources`. The following data sources are currently supported:

### Satellite data from Digital Earth Australia:
These are pre-processed and national calibrated satellite image layers provided  Digital Earth Australia (DEA) Geoscience Earth Observations. Multiple layers can be given as list in the settings. For more details see [Data Overview DEA](Data_Overview.md#digital-earth-australia-geoscience-earth-observations). 


### Digital Elevation Model (DEM):
The DEM data is given by the National Digital Elevation Model 1 Second Hydrologically Enforced. Options are: 'DEM', 'Slope', and 'Aspect'. For more info see [Data Overview DEM](Data_Overview.md#national-digital-elevation-model-1-second-hydrologically-enforced).

### Landscape from SLGA 
Landscape data can be retrieved from SLGA. For an overview of all available layers see [Data Overview Landscape](Data_Overview.md#landscape-data-slga).

### Radiometric
For an overview of the radiometric layer options see [Data Overview Radiometric](Data_Overview.md#radiometric-data).

### SILO Climate Database

SILO is containing continuous daily climate data for Australia. An overview of the available data layers is provided in [Data Overview SILO](Data_Overview.md#silo-climate-database).

For each requested SILO data layer, at least one temporal aggregation method has to be provided, which will be applied to aggregate climate data over the specified temporal range. The following options are available: 'mean', 'median', 'sum', 'std', 'perc95', 'perc5', 'max', 'min'

### Soil data from SLGA 

An overview of the soil attributes is given in in [Data Overview SLGA](Data_Overview.md#soil-data-3d-slga).

Each soil attribute has six depth layers (plus their upper and lower confidence limits), with the following options:'0-5cm', '5-15cm', '15-30cm', '30-60cm', '60-100cm' and '100-200cm'. 

### Google Earth Engine Data

An overview of the available Google Earth Engine (GEE) data and options is provided in [Data Overview GEE](Earth_Engine_Data_Overview.md).
Settings for GEE are added in the entry `GEE` (see example with descriptions below). 

A complete list of the available spectral indices can be found [here](https://github.com/awesome-spectral-indices/awesome-spectral-indices)

For more details on GEE settings, please visit the [GEE API documentation](https://developers.google.com/earth-engine/apidocs) or [eeharvest documentation ](https://github.com/Sydney-Informatics-Hub/eeharvest). 

Note that GEE requires a Google account and a GEE authorization. If this is you first time using GEE, please follow [these instructions](https://earthengine.google.com/signup/). In the next step you must authorise Geodata-Harvester to use the Google Earth Engine API. See a preview of the process [here](https://sydney-informatics-hub.github.io/AgReFed-Workshop/pydocs/setup-gee.html#part-ii-authorising-your-workstation-with-gee).


**Example:**

```yaml
target_sources:
  #Satellite data from Digital Earth Australia
  DEA:
  - landsat_barest_earth

  #National Digital Elevation Model (DEM) 1 Second
  DEM:
  - DEM
  
  #Landscape Data 
  Landscape:
  - Slope
  - Aspect
  - Relief_300m

  #Radiometric Data
  Radiometric:
  - radmap2019_grid_dose_terr_awags_rad_2019
  - radmap2019_grid_dose_terr_filtered_awags_rad_2019

  # SILO Climate Data
  # temporal aggregation options: 'mean', 'median', 'sum', 'std', 'perc95', 'perc5', 'max', 'min'
  SILO:
    max_temp:
    - Median
    min_temp:
    - Median
    monthly_rain:
    - Total

  #Soil data from SLGA
  SLGA:
   Bulk_Density:
    - 0-5cm
   Clay:
    - 0-5cm

  #Satellite data layers from Google Earth Engine
  GEE: 
    preprocess:

      ### collection as defined in the Earth Engine Catalog 
      # NEW: for multiple collections please add list of collection names
      collection: LANDSAT/LC09/C02/T1_L2

      #### circular buffer in metres (optional)
      buffer: null

      #### convert buffer into square bounding box instead (optional)
      bound: null

      #### cloud masking option
      mask_clouds: True

      #### Set probability for mask cloud (between 0 to 1), optional
      mask_probability: null

      #### composite image based on summary stat provided
      # e.g.: min, max, median, mean, stdDev (see GEE API references)
      reduce: median

      #### spectral indices to calculate via Awesome Spectral Indices site
      # examples: NDVI, EVI, AVI, BI 
      spectral:
        - NDVI

    download:
      # set bands (either band names or spectral index names) If multiple collections are selected, 
      # add for each collection a list of bands, e.g., [[NDVI, SR_B2],[SR_B23, SR_B4]]
      bands: 
        - NDVI
        - SR_B2
        - SR_B3
        - SR_B4
```