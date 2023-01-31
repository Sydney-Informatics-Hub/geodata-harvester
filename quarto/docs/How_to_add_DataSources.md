# How to add new Data Sources

The Geodata-Harvester is designed to be extendable and new data source modules can be added as Python modules. The naming convention for the data modules are `getdata_SOURCENAME.py` with `SOURCENAME` as the data source name. For an example adding a WebMap service request (WMS/WCS) see getdata_radiometric.py, or for requesting raster data from an AWS server, see as example getdata_silo.py.  

Each data source module consists of at least three core functions:

- get_layers function with the following main arguments:
    - date_start
    - date_end
    - bbox
    - resolution
    - outpath
    - verbose (boolean, for logging options)
    other optional arguments could be crs (typically "EPSG:4326"), output_format (typically "GeoTIFF" or "netCDF")
- get_capabilities() : returns data server capabilities such as available layernames and metadata (helpful for developing get data requests and documentation)
- get_dict(): returns dictionary of data source selected layernames, options, attributions and license (helpful for validation test, widget selections, and automating attributions/ licensing)

To invoke the new data source module, you need to import the module (e.g., in your Jupyter notebook) and add new source-name to the settings YAML file under the entry `target_sources:`, with layername and options as sublist or dict (see existing data source settings as example). This will enable to load the settings into the settings Namespace (via load_settings function in harvesterwidgets.py). 

To integrate a new module into the geodata-harvester package, you may need to modify the following files:

- src/geodata_harveseter/__init__.py (for making new module available in package NameSpace)
- src/geodata_harveseter/harvest.py (to automate aggregation with all other layers by callinbg one function)
- src/geodata_harveseter/widgets/harvesterwidgets.py (to include and select settings for the new data source via Jupyter widgets)
- src/geodata_harveseter/validate_settings.py (optional)
- update documentation [Data_Overview.md](quarto/docs/Data_Overview.md)

Please add test functions for the new data module (either in the module file or as sepepare test script in folder `tests`). Adding an example notebook that demonstrates how to use new data source is encouraged as well.


For development of new data source modules, we recommend to fork the geodata-harvester repo and develop new modules in a local environment (see environment.yaml). If you would like to contribute your data source module to the geodata-harvester package, please visit the [geodata-harvester contribution guidelines](https://github.com/Sydney-Informatics-Hub/geodata-harvester/quarto/docs/Contributing.md).