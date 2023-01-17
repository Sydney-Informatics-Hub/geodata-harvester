---
title: Settings Overview
---

# Overview and Description of Settings for the AgReFed Data-Harvester

The following documentation outlines the available settings for the Data Harvester

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
fname_settings = 'settings_v0.3.yaml'
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

The spatial extent of the requested images can be given as bounding box list in the settings `target_bbox`, in the order: lng_min, lat_min, lng_max, lat_max (left, bottom, right, top corner of box). If no bounding box is provided, Data-Harvetser will automatically infer a padded bounding box based on the extent of the coordinates given in the input file.

The spatial resolution of the requested images is specified in `target_res` and given in arcsec (1 arcsec corresponds to roughly 30m on the Equator, please see `arc2meter.py`for calculating exact conversion of meter to arcsec and vice versa).

The years for the requested data is specified via `target_dates` and can be one specific year or a list of multiple years.

TBD:
- The temporal resolution specifies the length of the time (in days) for which data is aggregated. The date range will then be subdivided in n bins = maximum year - minimum year divided by temporal resolution
- Spatial buffer


**Example:**

```yaml
#Bounding Box as (lng_min, lat_min, lng_max, lat_max):
target_bbox: ''

#Select years:
target_dates:
  - 2021

#Spatial Resolution [in arcsec]:
target_res: 6.0

#Temporal Resolution [in days, from 1 to 365 days], TBD
temp_res: 365
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

For each requested SILO data layer, at least one temporal aggregation method has to be provided, which will be applied to aggregate climate data over the specified temporal range. The following aptions are available: 'mean', 'median', 'sum', 'std', 'perc95', 'perc5', 'max', 'min'

### Soil data from SLGA 

An overview of the soil attributes is given in in [Data Overview SLGA](Data_Overview.md#soil-data-3d-slga).

Each soil attribute has six depth layers (plus their upper and lower confidence limits), with the following options:'0-5cm', '5-15cm', '15-30cm', '30-60cm', '60-100cm' and '100-200cm'. 

### Google Earth Engine  Data

An overview of the available Google Earth Engine (GEE) data is provided in [Data Overview GEE](Earth_Engine_Data_Overview.md) 

Documentation of options: TBD


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
      collection: LANDSAT/LC09/C02/T1_L2

      #### if supplied, will use 'buffer' and 'bound'. else, will use bbox above
      coords: [149.769345, -30.335861]

      #### If date range is supplied, will use below. Else, will use `target_dates`
      date: 2021-01-01
      end_date: 2021-12-31

      #### circular buffer in metres
      buffer: null

      #### convert buffer into square bounding box instead
      bound: null

      #### cloud masking option
      mask_clouds: True

      #### if null, will download all available images. Else, will reduce to single

      #### composite image based on summary stat provided
      reduce: median

      #### spectral indices to calculate via Awesome Spectral Indices site
      spectral:
        - NDVI
        - NDWI
    aggregate:
      
      #### group data by period. Available: year, month, week
      frequency: year 
      #### summarise group by method
      method: mean  

    download:
      bands: 
        - NDVI
        - SR_B2
        - SR_B3
        - SR_B4
      scale: 100   # in metres
      format: tif  # available: tif, png
```