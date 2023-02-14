"""
Geodata-Harvester
-----------------

An automation tool for harvesting and processing geodata from the web 
into spatial-temporal aligned maps and dataframes.

The following main data sources are currently implemented:

- Soil and Landscape Grid of Australia (SLGA), see getdata_slga.py
- SILO Climate Database, see getdata_silo.py
- National Digital Elevation Model (DEM), see getdata_dem.py
- Digital Earth Australia (DEA) Geoscience Earth Observations, see getdata_dea.py
- Radiometric Data, see getdata_radiometric.py
- Google Earth Engine Data (GEE account needed), see docs for eeharvest
"""

__version__ = "0.2.1"
__title__ = "Geodata-Harvester"
__description__ = """
This Python package provides automation tools for harvesting and processing geodata from the web.
"""
__uri__ = "https://github.com/Sydney-Informatics-Hub/geodata-harvester"
__doc__ = __description__ + " <" + __uri__ + ">"

__license__ = "LGPL-3.0"

from . import harvest, spatial, temporal
from . import arc2meter, settingshandler, validate_settings
