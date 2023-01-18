---
title: "Geodata-Harvester"
subtitle: "Jumpstart your analysis with a ready-made set of spatial-temporal aligned raster maps and dataframes."
---

# Geodata-Harvester

<h3><em>Automate harvesting geodata from the web and jumpstart your analysis with a ready-made set of spatial-temporal processed maps and dataframes.</em></h3> 

<center><a><img src="quarto/images/dataharvester_logo.png" alt="Geodata-Harvester logo" width="100%"/></a></center>



<!-- Badges  start -->

[![License](https://img.shields.io/badge/License-GPL3-blue)](#license)

<!-- [![GitHub tag](https://img.shields.io/github/tag/Sydney-Informatics-Hub/AgReFed-DataHarvester?include_prereleases=&sort=semver&color=blue)](https://github.com/Sydney-Informatics-Hub/AgReFed-DataHarvester/releases/)
[![issues - AgReFed-DataHarvester](https://img.shields.io/github/issues/Sydney-Informatics-Hub/AgReFed-DataHarvester)](https://github.com/Sydney-Informatics-Hub/AgReFed-DataHarvester/issues) -->

<!-- Badges end -->

The Geodata-Harvester package offers reusable and automated workflows for data extraction from a wide range of geospatial and environmental data sources. User provided data is auto-completed with a suitable set of spatial- and temporal-aligned covariates as a ready-made dataset for machine learning and environmental models. In addition, all requested data layer maps are automatically extracted and aligned for a specific region and time period.

## Introduction

There is an enormous amount of national/global space-time data that is free and accessible. Examples are the numerous satellite platforms, weather, soil landscape grid of Australia. Many have a temporal dimension so for any point in Australia you can extract a time series of remote sensing and weather data and soil and terrain site variables. In the case of time series covariates there are a number of post-processing steps that a user can undertake to extract meaning, e.g. temporal means, aggregating in time. All of the above is a non-trivial task and a workflow where a user could enter a point (s) and get a tidy data frame of data cube variables would be a step towards people understanding its value and being able to jumpstart their analysis. This project will contribute processing tools for finding, extracting and converting these key data layers.

Developed as part of the Agricultural Research Federation (AgReFed), Geodata-Harvester is an open-source software that allows users to jumpstart their analysis with a suitable set of spatial-temporal aligned raster maps and dataframes.

## Data Sources

A detailed list of all available layers and their description can be found in [Data Overview](docs/Data_Overview.md).

The following main data sources are currently implemented:

- Soil and Landscape Grid of Australia (SLGA)
- SILO Climate Database
- National Digital Elevation Model (DEM) 1 Second Hydrologically Enforced
- Digital Earth Australia (DEA) Geoscience Earth Observations
- GSKY Data Server for DEA Geoscience Earth Observations
- Radiometric Data
- Google Earth Engine Data (GEE account needed), see for overview [Earth_Engine_Data_Overview](docs/Earth_Engine_Data_Overview.md).

## Functionality

The main goal of the Data Harvester is to enable researchers with reusable workflows for automatic data extraction and processing:

1. Retrieve: given set of locations, automatically access and download multiple data sources (APIs) from a diverse range of geospatial and soil data sources
2. Process: Spatial and temporal processing, conversion to dataframes and custom raster-files
3. Output: Ready-made dataset for machine learning (training set and prediction mapping)

Geodata-Harvester is designed as a modular and maintainable project in the form of a multi-stage pipeline by providing explicit boundaries among tasks. To encourage interaction and experimentation with the pipeline, multiple frontend notebooks and use case scenarios are provided. The core features are:

- automatic data retrieval from geo-spatial APIs for given locations and dates
- automatic geospatial conversion including reprojection of data, including clipping to bounding boxes, coordinate transformation, and changing resolution
- support for multiple temporal aggregation options
- automatic extraction of retrieved data into ready-made dataframes for ML training
- automatic generation of ready-made aligned maps and data for ML prediction models
- co-registration of different raster grids
- visualisation of final maps
- settings saving/loading via interactive widgets and yaml files

## Installation

Geodata-Harvester can be run on the cloud (e.g., in JupyterHub environment) or on your local machine. If you like to install Data Harvester locally, it is recommended to setup a virtual Python environment for the installation, e.g., via conda miniforge.

### Install via pip

to install via pip, first you need to have gdal installed (see installation guide) in your environment. Then install via

```bash
pip install geodata-harvester
```

### Install via Conda

to install via conda:

```bash
conda install -c conda-forge geodata-harvester
```

## How to get started

1. Options and user settings are defined by the user in the settings; see for settings documentation [Settings_Overview](docs/Settings_Overview.md)

2. Run the jupyter notebook (see example notebooks)

## Attribution and Acknowledgments

This software was developed by the Sydney Informatics Hub, a core research facility of the University of Sydney, as part of the Data Harvesting project for the Agricultural Research Federation (AgReFed).

Acknowledgments are an important way for us to demonstrate the value we bring to your research. Your research outcomes are vital for ongoing funding of the Sydney Informatics Hub.

If you make use of this software for your research project, please include the following acknowledgment:

“This research was supported by the Sydney Informatics Hub, a Core Research Facility of the University of Sydney, and the Agricultural Research Federation (AgReFed)."

AgReFed is supported by the Australian Research Data Commons (ARDC) and the Australian Government through the National Collaborative Research Infrastructure Strategy (NCRIS).

## License

Copyright 2023 The University of Sydney

This is free software: you can redistribute it and/or modify it under
the terms of the GNU Lesser General Public License (LGPL version 3) as
published by the Free Software Foundation.

This program is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Lesser
General Public License for more details.

You should have received a copy of the GNU Lesser General Public License along with this program (see LICENSE). If not, see
<https://www.gnu.org/licenses/>.
