"""
This script generates interactive notebook widgets for selecting the settings.

Widgets are defined using the package ipywidgets, for more details see:

https://ipywidgets.readthedocs.io/en/stable/index.html

and examples:
https://coderzcolumn.com/tutorials/python/interactive-widgets-in-jupyter-notebook-using-ipywidgets


This package is part of the Data Harvester project developed for the Agricultural Research Federation (AgReFed).

Copyright 2023 Sydney Informatics Hub (SIH), The University of Sydney

This open-source software is released under the LGPL-3.0 License.
"""

import os
import ast
import yaml
import sys
import ipywidgets as widgets
from IPython.display import display
import datetime
from types import SimpleNamespace

# import data dictionaries
#sys.path.append("../")
from .ipyfilechooser import FileChooser
from geodata_harvester.getdata_slga import get_slgadict
from geodata_harvester.getdata_silo import get_silodict
from geodata_harvester.getdata_dea import get_deadict
from geodata_harvester.getdata_radiometric import get_radiometricdict
from geodata_harvester.getdata_landscape import get_landscapedict
from eeharvest.harvester import supported_collections
# from geodata_harvester.getdata_ee import supported_collections


def gen_accordion(panels, panel_titles):
    """
    Generate accordion of panels

    Input:
        panels: list of panels
        panel_titles: list of panel titles

    Output:
        accordion_main: accordion of panels
    """
    accordion_main = widgets.Accordion(children=panels)
    # in future version its is possible to use title attribute in accordion
    # titles=[io_title, st_title, slga_title, silo_title, dea_title, dem_title]
    for i in range(len(accordion_main.children)):
        accordion_main.set_title(i, panel_titles[i])
    return accordion_main


def save_dict_settings(dict_settings, yaml_outfname):
    """
    save dictionary to yaml file

    Input:
        dict_settings: dictionary of settings
        yaml_outfname: path and filename to save settings

    Output:
        None
    """
    f = open(yaml_outfname, "w+")
    yaml.dump(dict_settings, f, allow_unicode=True, default_flow_style=False)
    print(f"Settings saved to file {yaml_outfname}")


def load_settings(fname_settings):
    """
    Load settings from yaml file

    Input:
        fname_settings: path and filename to settings file

    Output:
        settings: settings as namespace
    """
    # Load settings from yaml file
    with open(fname_settings, "r") as f:
        settings = yaml.load(f, Loader=yaml.FullLoader)
    # Parse settings dictinary as namespace (settings are available as
    # settings.variable_name rather than settings['variable_name'])
    settings = SimpleNamespace(**settings)
    settings.date_min = str(settings.date_min)
    settings.date_max = str(settings.date_max)
    return settings


def gen_loadwidget():
    """
    Generate widget for loading settings from yaml file

    Input:
        None
    
    Output:
        w_load: widget for loading settings
    """
    w_yamlfile = FileChooser(os.getcwd(), title="Settings File:")
    return w_yamlfile


def gen_maintab():
    """
    Generate New Settings Tab

    Input:
        None

    Output:
        tab_nest: tab containing New Settings and Load Settings
        w_settings: widget for settings
        names_settings: list of names of settings
        w_load: widget for loading settings
    """
    w_load = gen_loadwidget()
    # panels, w_settings, w_names, w_save = gen_widgets()
    panels, w_settings, names_settings, panel_titles = gen_panels()
    accordion = gen_accordion(panels, panel_titles)
    # w_save = gen_savebutton()
    # w_new = widgets.VBox([accordion, w_save])
    w_new = accordion
    tab_nest = widgets.Tab()
    tab_nest.children = [w_new, w_load]
    tab_titles = ["New Settings", "Load Settings"]
    for i in range(len(tab_nest.children)):
        tab_nest.set_title(i, tab_titles[i])
    return tab_nest, w_settings, names_settings, w_load


def gen_savebutton():
    """
    Generate Save button

    Input:
        None

    Output:
        w_savebutton: widget for saving settings
    """
    w_savebutton = widgets.ToggleButton(
        description="Save Settings",
        # button_style='', # 'success', 'info', 'warning', 'danger' or ''
        # tooltip='Click me',
        # icon='check'
    )
    return w_savebutton


def savebutton_onclick(params):
    """
    Save settings to yaml file

    Input:
        params: list of widgets, list of names of widgets, output filename

    Output:
        None
    """
    # functionality with non-name params not supported yet by widgets
    w_settings, name_settings, yaml_outfname = params
    save_dict_settings(eval_widgets(w_settings, names_settings), yaml_outfname)
    print(f"Settings saved to file {yaml_outfname}")


def gen_panel_io():
    """
    Generate panel for input and output settings

    Input:
        None

    Output:
        panel_io: panel for input and output settings
        w_io: widget for input path
        w_names: list of names of widgets
    """ 
    w_inpath = FileChooser(os.getcwd(), title="Input File:")

    # Write name relative output path
    w_outpath = widgets.Text(
        value="../../dataresults/",
        placeholder="Type name of output path",
        description="Output Path:",
        disabled=False,
    )

    # Write name of longitude
    w_colname_lng = widgets.Text(
        value="",
        placeholder="Type name of Longitude column",
        description="",
        disabled=False,
    )

    # Write name of latitude
    w_colname_lat = widgets.Text(
        value="",
        placeholder="Type name of Latitude column",
        description="",
        disabled=False,
    )

    items = [
        w_inpath,
        widgets.Box([widgets.Label("Headername of Longitude:"), w_colname_lng]),
        w_outpath,
        widgets.Box([widgets.Label("Headername of Latitude:"), w_colname_lat]),
    ]

    panel_io = widgets.GridBox(
        items, layout=widgets.Layout(grid_template_columns="2fr 3fr")
    )

    w_io = [w_inpath, w_outpath, w_colname_lng, w_colname_lat]
    w_names = ["infile", "outpath", "colname_lng", "colname_lat"]
    return panel_io, w_io, w_names


def gen_panel_st():
    """
    Generate panel for spatial-temporal settings
    
    Input:
        None
    
    Output:
        panel_st: panel for spatial-temporal settings
        settings_st: list of settings
        settings_names: list of names of settings
    """
    w_target_bbox = widgets.Text(
        value="",
        placeholder="[Lng_min, Lat_min, Lng_max, Lat_max]",
        description="",
        disabled=False,
    )

    w_target_res = widgets.FloatSlider(
        value=3,
        min=0.3,
        max=100,
        step=0.1,
        description="",
        disabled=False,
        continuous_update=False,
        orientation="horizontal",
        readout=True,
        slider_color="white",
    )

    w_date_min = widgets.DatePicker(
    description='',
    disabled=False
)
    w_date_max = widgets.DatePicker(
    description='',
    disabled=False
)

    w_temp_intervals = widgets.IntSlider(
        value=1,
        min=1,
        max=365,
        step=1,
        description="",
        disabled=False,
        continuous_update=False,
        orientation="horizontal",
        readout=True,
        slider_color="white",
    )

    w_temp_buffer = widgets.IntSlider(
        value=1,
        min=1,
        max=365,
        step=1,
        description="",
        disabled=False,
        continuous_update=False,
        orientation="horizontal",
        readout=True,
        slider_color="white",
    )

    items = [
        widgets.GridBox([widgets.Label("Bounding Box :"), w_target_bbox], layout=widgets.Layout(grid_template_columns="1fr 2fr")),
        widgets.GridBox([widgets.Label("Spatial Resolution [arcsec]:"), w_target_res], layout=widgets.Layout(grid_template_columns="1fr 2fr")),
        widgets.GridBox([widgets.Label(f"Start Date:".rjust(2)), w_date_min], layout=widgets.Layout(grid_template_columns="1fr 2fr")),
        widgets.GridBox([widgets.Label(f"Number of Temporal Slices:".rjust(3)), w_temp_intervals], layout=widgets.Layout(grid_template_columns="1fr 2fr")),
        widgets.GridBox([widgets.Label(f"End Date:".rjust(4)), w_date_max], layout=widgets.Layout(grid_template_columns="1fr 2fr")),
        widgets.GridBox([widgets.Label(f"Temporal Buffer Window in Days:"), w_temp_buffer], layout=widgets.Layout(grid_template_columns="1fr 2fr")),
        # widgets.Box([widgets.Label("Select years:"), w_target_dates]),
        # widgets.Box([widgets.Label("Temporal Resolution [days]:"), w_temp_res]),
        ]

    settings_st = [w_target_bbox, w_target_res, w_date_min, w_temp_intervals, w_date_max, w_temp_buffer]
    settings_names = ["target_bbox", "target_res", "date_min", "temp_intervals", "date_max", "temp_buffer"]
    panel_st = widgets.GridBox(
        items, layout=widgets.Layout(grid_template_columns="6fr 6fr")
    )
    return panel_st, settings_st, settings_names


def gen_panel_slga():
    """
    Generate panel for SLGA settings

    Input:
        None

    Output:
        panel_slga: panel for SLGA settings
        w_slga: widget for SLGA settings
        options_slga: list of available SLGA layers
    """
    dict_slga = get_slgadict()
    options_slga = list(dict_slga["layers_url"].keys())

    w_slga = []
    box_slga = []
    for option in options_slga:
        w_sel = widgets.Checkbox(
            value=False, description=option, disabled=False, indent=False
        )
        w_depth = widgets.SelectMultiple(
            options=["0-5cm", "5-15cm", "15-30cm", "30-60cm", "60-100cm", "100-200cm"],
            value=["0-5cm"],
            rows=2,
            description="Depths:",
            disabled=False,
        )

        w_slga.append([w_sel, w_depth])
        box = widgets.HBox([w_sel, w_depth])
        box_slga.append(box)

    panel_slga = widgets.VBox(box_slga)
    return panel_slga, w_slga, options_slga


def gen_panel_silo():
    """
    Generate panel for SILO settings

    Input:
        None

    Output:
        panel_silo: panel for SILO settings
        w_silo: widget for SILO settings
        options_silo: list of SILO options
    """
    dict_silo = get_silodict()
    options_silo = list(dict_silo["layernames"].keys())
    desc_silo = list(dict_silo["layernames"].values())

    w_silo = []
    box_silo = []
    for i in range(len(options_silo)):
        option = options_silo[i]
        desc = desc_silo[i]
        w_sel = widgets.Checkbox(
            value=False, description=option, disabled=False, indent=False
        )
        w_temp = widgets.SelectMultiple(
            # options=['Total','Median','Mean','Std','5pct','10pct','15pct','25pct','75pct','85pct','90pct','95pct'],
            options=["mean", "median", "sum", "std", "perc95", "perc5", "max", "min"],
            value=["median"],
            rows=2,
            description="",
            disabled=False,
        )
        w_silo.append([w_sel, w_temp])
        items = [
            w_sel,
            widgets.Box([widgets.Label("Temporal Stats: "), w_temp]),
            widgets.Label(desc),
        ]
        box = widgets.GridBox(
            items, layout=widgets.Layout(grid_template_columns="1fr 2fr 3fr")
        )
        # box = widgets.HBox([w_sel, widgets.Box([widgets.Label("Temporal Stats: "), w_temp]), widgets.Label(desc)])
        box_silo.append(box)

    panel_silo = widgets.VBox(box_silo)
    return panel_silo, w_silo, options_silo


def gen_panel_dea():
    """
    Generate panel for DEA settings

    Input:
        None

    Output:
        panel_dea: panel for DEA settings
        w_dea: widget for DEA settings
        options_dea: list of DEA options 
    """
    dict_dea = get_deadict()
    options_dea = list(dict_dea["layernames"].keys())
    desc_dea = list(dict_dea["layernames"].values())

    w_dea = []
    box_dea = []
    for i in range(len(options_dea)):
        option = options_dea[i]
        desc = desc_dea[i]
        w_sel = widgets.Checkbox(
            value=False, description=option, disabled=False, indent=False
        )
        # If any temporal aggregation needed, uncomment following lines
        # w_temp = widgets.SelectMultiple(
        # value=['Median'],
        # rows=2,
        # description='',
        # disabled=False
        # )
        # w_dea.append([w_sel, w_temp])
        # items = [w_sel, widgets.Box([widgets.Label("Temporal Stats: "), w_temp]), widgets.Label(desc)]
        # box = widgets.GridBox(items, layout=widgets.Layout(grid_template_columns="1fr 2fr 3fr"))
        w_dea.append([w_sel])
        items = [w_sel, widgets.Label(desc)]
        box = widgets.GridBox(
            items, layout=widgets.Layout(grid_template_columns="1fr 3fr")
        )
        # box = widgets.HBox([w_sel, widgets.Box([widgets.Label("Temporal Stats: "), w_temp]), widgets.Label(desc)])
        box_dea.append(box)
    panel_dea = widgets.VBox(box_dea)
    return panel_dea, w_dea, options_dea


def gen_panel_dem():
    """
    Generate panel for DEM settings

    Input:
        None

    Output:
        panel_dem: panel for DEM settings
        w_dem: widget for DEM settings
        options_dem: list of DEM options 
    """
    options_dem = ["DEM", "Slope", "Aspect"]
    desc_dem = [
        "Digital Elevation Model (DEM) of Australia derived from STRM with 1 Second Grid - Hydrologically Enforced.",
        "DEM Slope",
        "DEM Aspect Ratio",
    ]
    w_dem = []
    box_dem = []
    for i in range(len(options_dem)):
        option = options_dem[i]
        desc = desc_dem[i]
        w_sel = widgets.Checkbox(
            value=False, description=option, disabled=False, indent=False
        )
        w_dem.append([w_sel])
        items = [w_sel, widgets.Label(desc)]
        box = widgets.GridBox(
            items, layout=widgets.Layout(grid_template_columns="1fr 4fr")
        )
        # box = widgets.HBox([w_sel, widgets.Box([widgets.Label("Temporal Stats: "), w_temp]), widgets.Label(desc)])
        box_dem.append(box)

    panel_dem = widgets.VBox(box_dem)
    return panel_dem, w_dem, options_dem


def gen_panel_radiometric():
    """
    Generate panel for radiometric settings

    Input:
        None
    
    Output:
        panel_rm: panel for radiometric settings
        w_rm: widget for radiometric settings
        options_rm: list of radiometric options
    """
    dict_rm = get_radiometricdict()
    desc_rm = list(dict_rm["layernames"].values())
    options_rm = list(dict_rm["layernames"].keys())

    w_rm = []
    box_rm = []
    for i in range(len(options_rm)):
        option = options_rm[i]
        desc = desc_rm[i]
        w_sel = widgets.Checkbox(
            value=False, description=option, disabled=False, indent=False
        )
        w_rm.append([w_sel])
        items = [w_sel, widgets.Label(desc)]
        box = widgets.GridBox(
            items, layout=widgets.Layout(grid_template_columns="2fr 3fr")
        )
        box_rm.append(box)
    panel_rm = widgets.VBox(box_rm)
    return panel_rm, w_rm, options_rm


def gen_panel_landscape():
    """
    Generate panel for landscape settings

    Input:
        None

    Output:
        panel_ls: panel for landscape settings
        w_ls: widget for landscape settings
        options_ls: list of landscape options
    """
    dict_ls = get_landscapedict()
    options_ls = list(dict_ls["layernames"].keys())
    w_ls = []
    box_ls = []
    for i in range(len(options_ls)):
        option = options_ls[i]
        w_sel = widgets.Checkbox(
            value=False, description=option, disabled=False, indent=False
        )
        w_ls.append([w_sel])
        items = [w_sel]
        box = widgets.GridBox(items, layout=widgets.Layout(grid_template_columns="1fr"))
        box_ls.append(box)
    panel_ls = widgets.VBox(box_ls)
    return panel_ls, w_ls, options_ls

def gen_panel_ee():
    """
    Generate panel for Google Earth Engine settings

    Input:
        None

    Output:
        panel_ee: panel for Google Earth Engine settings
        w_ee: widget for Google Earth Engine settings
        names_ee: list of widget names  
    """
    dict_ee = supported_collections()
    options_ee = list(dict_ee.keys())
    w_sel = widgets.SelectMultiple(
        options = options_ee,
        description = '', 
        rows = 3,
        disabled=False)

    w_other = widgets.Text(
        value="",
        placeholder="Enter other collection name",
        description="",
        disabled=False,
    )

    w_spectral = widgets.Select(
            options=['None', 'NDVI', 'EVI', 'AVI', 'BI', 'NDMI', 'NBR', 'BNDVI', 'GNDVI', 'SAVI', 'MSI', 'ARVI', 'SIPI', 'NDSI', 'NDWI'],
            value='NDVI',
            rows=3,
            description="",
            disabled=False,
        )
    w_cloud = widgets.Checkbox(
            value=False, description='', disabled=False, indent=False
        )

    w_cloud_prob = widgets.Text(
        value="",
        placeholder="0.7",
        description="",
        disabled=False,
    )

    w_reduce = widgets.Select(
            options=["median", "mean", "mode", "min", "max", "sum", "stdDev"],
            value="median",
            rows=3,
            description="",
            disabled=False,
        )

    w_band = widgets.Text(
        value="",
        placeholder="7,8",
        description="",
        disabled=False,
    )

    items = [
        widgets.GridBox([widgets.Label("Collection Name:".rjust(2)), w_sel], layout=widgets.Layout(grid_template_columns="1fr 2fr")),
        widgets.GridBox([widgets.Label(f"Other Collection:"), w_other], layout=widgets.Layout(grid_template_columns="1fr 2fr")),
        widgets.GridBox([widgets.Label(f"Spectral Index:".rjust(2)), w_spectral], layout=widgets.Layout(grid_template_columns="1fr 2fr")),
        widgets.GridBox([widgets.Label(f"Reduce Method:".rjust(3)), w_reduce], layout=widgets.Layout(grid_template_columns="1fr 2fr")),
        widgets.GridBox([widgets.Label(f"Band Numbers:".rjust(4)), w_band], layout=widgets.Layout(grid_template_columns="1fr 2fr")),
        widgets.GridBox([widgets.Label(f"Cloud Masking:".rjust(3)), w_cloud], layout=widgets.Layout(grid_template_columns="1fr 2fr")),
        widgets.GridBox([widgets.Label(f"Mask Probability:"), w_cloud_prob], layout=widgets.Layout(grid_template_columns="1fr 2fr")),
        ]

    w_ee = [w_sel, w_other, w_spectral, w_reduce, w_band, w_cloud, w_cloud_prob]

    names_ee = ['collection', 'collection_other', 'spectral', 'reduce', 'bands', 'mask_clouds', 'mask_probability']

    panel_ee = widgets.GridBox(
        items, layout=widgets.Layout(grid_template_columns="6fr")
    )
    return panel_ee, w_ee, names_ee



def gen_panels():
    """
    Generate all settings panels

    Input:
        None

    Output:
        panels: list of panels
        w_settings: list of widgets for all settings
        names_settings: list of widget names
        panel_titles: list of panel titles
    """
    panel_io, w_io, names_io = gen_panel_io()

    panel_st, w_st, names_st = gen_panel_st()

    panel_slga, w_slga, names_slga = gen_panel_slga()

    panel_silo, w_silo, names_silo = gen_panel_silo()

    panel_dea, w_dea, names_dea = gen_panel_dea()

    panel_dem, w_dem, names_dem = gen_panel_dem()

    panel_rm, w_rm, names_rm = gen_panel_radiometric()

    panel_ls, w_ls, names_ls = gen_panel_landscape()

    panel_ee, w_ee, names_ee  = gen_panel_ee()

    ## define return objects
    w_settings = [
        w_io,
        w_st,
        w_slga,
        w_silo,
        w_dea,
        w_dem,
        w_rm,
        w_ls,
        w_ee,
    ]

    panels = [
        panel_io,
        panel_st,
        panel_slga,
        panel_silo,
        panel_dea,
        panel_dem,
        panel_rm,
        panel_ls,
        panel_ee,
    ]

    names_settings = [
        names_io,
        names_st,
        names_slga,
        names_silo,
        names_dea,
        names_dem,
        names_rm,
        names_ls,
        names_ee,
    ]

    io_title = "Input and Output Specifications"
    st_title = "Settings for Spatial and Temporal Specifications"
    slga_title = "SLGA Data Selection"
    silo_title = "SILO Data Selection"
    dea_title = "DEA Data Selection"
    dem_title = "DEM Data Selection"
    rm_title = "Radiometrics Data Selection"
    ls_title = "Landscape Data Selection"
    ee_title = "Google Earth Engine Selection"

    panel_titles = [
        io_title,
        st_title,
        slga_title,
        silo_title,
        dea_title,
        dem_title,
        rm_title,
        ls_title,
        ee_title,
    ]

    return panels, w_settings, names_settings, panel_titles


def eval_widgets(w_settings, names):
    """
    This function is converting widget settings into dictionary.

    If widget settings change, add settings here too.

    Input:
        w_settings: list of settings
        names: list of setting names

    Output:
        dict_settings: dictionary of settings
    """
    w_io, w_st, w_slga, w_silo, w_dea, w_dem, w_rm, w_ls, w_ee = w_settings
    (
        names_io,
        names_st,
        names_slga,
        names_silo,
        names_dea,
        names_dem,
        names_rm,
        names_ls,
        names_ee,
    ) = names

    dict_settings = {}
    # I/O
    assert len(names_io) == len(w_io)
    for i in range(len(w_io)):
        dict_settings[names_io[i]] = w_io[i].value
    # ST settings
    assert len(names_st) == len(w_st)
    for i in range(len(w_st)):
        dict_settings[names_st[i]] = w_st[i].value
    # target sources settings
    # define for target source a dictionary
    # Loop over all settings and add the ones that are selected
    dict_sources = {}
    # SLGA
    slist = {}
    for i in range(len(w_slga)):
        if w_slga[i][0].value:
            slist[names_slga[i]] = list(w_slga[i][1].value)
    dict_sources["SLGA"] = slist
    # SILO
    slist = {}
    for i in range(len(w_silo)):
        if w_silo[i][0].value:
            slist[names_silo[i]] = list(w_silo[i][1].value)
    dict_sources["SILO"] = slist
    # DEA
    slist = []
    for i in range(len(w_dea)):
        if w_dea[i][0].value:
            # slist.append({names_dea[i]: list(w_dea[i][1].value)})
            slist.append(names_dea[i])
    dict_sources["DEA"] = slist
    # DEM
    slist = []
    for i in range(len(w_dem)):
        if w_dem[i][0].value:
            slist.append(names_dem[i])
    dict_sources["DEM"] = slist
    # Radiometric
    slist = []
    for i in range(len(w_rm)):
        if w_rm[i][0].value:
            slist.append(names_rm[i])
    dict_sources["Radiometric"] = slist
    slist = []
    # Landscape
    for i in range(len(w_ls)):
        if w_ls[i][0].value:
            slist.append(names_ls[i])
    dict_sources["Landscape"] = slist
    # Google Earth Engine
    # Top level dict:
    slist = {} 
    ## Sublevel dict:
    slist_preprocess = {}
    slist_download = {}
    for i in range(len(w_ee)):
        if names_ee[i] == 'bands':
            if w_ee[i].value:
                slist_download[names_ee[i]] = w_ee[i].value
            else:
                slist_download[names_ee[i]] = None
        else:
            if w_ee[i].value:
                slist_preprocess[names_ee[i]] = w_ee[i].value
            else:
                slist_preprocess[names_ee[i]] = None
    if slist_preprocess['collection_other'] != None:
        slist_preprocess['collection'] = slist_preprocess['collection_other']
    del slist_preprocess['collection_other']
    # check if list or string
    if isinstance(slist_preprocess['collection'], tuple):
        slist_preprocess['collection'] = list(slist_preprocess['collection'])
    if (slist_download['bands'] != None) & (slist_download['bands'] != ''):
        try:
            slist_download['bands'] = ast.literal_eval(slist_download['bands'])
        except:
            pass
        if isinstance(slist_preprocess['bands'], tuple):
            slist_preprocess['bands'] = list(slist_preprocess['bands'])
        if len(slist_download['bands']) == 1:
            slist_download['bands'] = slist_download['bands'][0]
    slist["preprocess"] = slist_preprocess
    slist["download"] = slist_download
    dict_sources["GEE"] = slist
    # Add here any new settings or data sources
    dict_settings["target_sources"] = dict_sources

    # Check bounding box:
    if type(dict_settings["target_bbox"]) == str:
        # remove string from list
        dict_settings["target_bbox"] = ast.literal_eval(dict_settings["target_bbox"])
    return dict_settings


def print_settings(settings):
    """
    print settings

    Input:
        settings: settings object

    Output: 
        None
    """
    print("Settings loaded:")
    print("----------------")
    for key in settings.__dict__:
        if key == "target_sources":
            print(f"settings.{key}:")
            for source in settings.target_sources:
                print(f"   '{source}': {settings.target_sources[source]}")
        else:
            print(f"settings.{key} : {settings.__dict__[key]}")
