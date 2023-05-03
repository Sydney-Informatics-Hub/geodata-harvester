"""
This script is running the headless version of the data harvester.

The following main steps are automatically executed within the run() function:
    - loading settings from config file
    - creating bounding box from input file points if not provided
    - downloading data layers as sepcified in config file
    - extract data for point locations provided in input file (name specified in settings)
    - save results to disk as csv and geopackage
"""

# TODO: add validation to infile, colname_lng, colname_lat, if not in config, to
# generate blanks so that the script doesn't crash. In the future, maybe let the
# main code handle this, but for now, this is a quick fix.

import os
from pathlib import Path
import geopandas as gpd
from termcolor import cprint
import yaml
import numpy as np
from datetime import datetime, timedelta
from geodata_harvester.widgets import harvesterwidgets as hw
from geodata_harvester.utils import init_logtable, update_logtable
from geodata_harvester import (getdata_dea, getdata_dem,  getdata_landscape,
                               getdata_radiometric, getdata_silo, getdata_slga,
                               utils, temporal)
from eeharvest import harvester as eeharvester


def run(path_to_config, log_name="download_log", preview=False, return_df=False):
    """
    A headless version of the Data-Harvester (with some limitations).
    Results are saved to disk.

    Parameters
    ----------
    path_to_config : str
        Path to YAML config file
    log_name: name of log file (default: "download_log")
    preview : bool, optional
        Plots a matrix of downloaded images if set to True, by default False
    return_df : bool, optional (Default: False)
        if True, returns dataframe with results

    Returns
    -------
    None (if return_df is False)
    dataframe (if return_df is True)
    """
    cprint("Starting the data harvester -----", "magenta", attrs=["bold"])

    # Load config file (based on notebook for now, will optimise later)
    # with open(path_to_config, "r") as f:
    # settings = yaml.load(f, Loader=yaml.SafeLoader)
    settings = hw.load_settings(path_to_config)

    # Count number of sources to download from
    count_sources = len(settings.target_sources)
    list_sources = list(settings.target_sources.keys())

    # If no infile provided, generate a blank one (including colnames)
    try:
        settings.infile
        if settings.infile is None:
            points_available = False
        else:
            points_available = True
    except (AttributeError, KeyError):
        settings.infile = None
        settings.colname_lng = None
        settings.colname_lat = None
        points_available = False

    # If no resolution set, make it 1 arc-second
    if settings.target_res is None:
        utils.msg_info(
            "No target resolution specified, using default of 1 arc-sec")
        settings.target_res = 1

    # Create bounding box if infile is provided and target_bbox is not provided
    if settings.infile is not None:
        gdfpoints = gpd.read_file(settings.infile)
        longs = gdfpoints[settings.colname_lng].astype(float)
        lats = gdfpoints[settings.colname_lat].astype(float)

        if settings.target_bbox is None:
            settings.target_bbox = (
                min(longs) - 0.05,
                min(lats) - 0.05,
                max(longs) + 0.05,
                max(lats) + 0.05,
            )

    # Stop if bounding box cannot be calculated or was not provided
    if settings.infile is None and settings.target_bbox is None:
        raise ValueError("No sampling file or bounding box provided")

    # Temporal range
    # convert date strings to datetime objects
    if settings.time_intervals is not None:
        period_days = (datetime.strptime(settings.date_max, "%Y-%m-%d") 
        - datetime.strptime(settings.date_min, "%Y-%m-%d")).days // settings.time_intervals
    else:
        period_days = None

    # Create download log
    download_log = init_logtable()
    # process each data source
    utils.msg_info(
        f"Found the following {count_sources} sources: {list_sources}")
    cprint("\nDownloading from API sources -----", "magenta", attrs=["bold"])

    # GEE
    if "GEE" in list_sources:
        # Try to initialise API if Earth Engine is selected
        try:
            eeharvester.initialise()
        except:
            eeharvester.initialise(auth_mode = 'notebook')

        cprint("\n⌛ Downloading Google Earth Engine data...", attrs=["bold"])
        # get data from GEE with eeharvest
        #gee = eeharvester.collect(config=path_to_config)
        #gee.preprocess()
        #gee.download()
        # use auto function to download and preprocess
        gee = eeharvester.auto(config=path_to_config)
        # add settings.outpath to all entries in list of gee.filenames
        # if gee.filenames is a list of strings
        if not isinstance(gee.filenames, list):
            # convert to list
            gee.filenames = [gee.filenames]
        outfnames = [settings.outpath  + filename for filename in gee.filenames]
        layernames = [Path(filename).resolve().stem for filename in gee.filenames]

        download_log = update_logtable(
            download_log,
            outfnames,
            layernames,
            "GEE",
            settings,
            layertitles=[],
            agfunctions=settings.target_sources['GEE']['preprocess']['reduce'],
            loginfos="downloaded",
        )

    # DEA
    if "DEA" in list_sources:
        cprint("\n⌛ Downloading DEA data...", attrs=["bold"])
        # get data from DEA
        dea_layernames = settings.target_sources["DEA"]
        outpath_dea = os.path.join(settings.outpath, "dea")
        # put into subdirectory
        files_dea = getdata_dea.get_dea_layers_daterange(
            dea_layernames,
            settings.date_min,
            settings.date_max,
            settings.target_bbox,
            settings.target_res,
            outpath_dea,
            crs="EPSG:4326",
            format_out="GeoTIFF",
        )
        if period_days is not None:
            # aggregate temporal data
            outfname_dea_list = []
            layer_list = []
            layer_titles = []
            for layername in dea_layernames:
                # get files for layername 
                files_layer = [os.path.basename(x) for x in files_dea if layername in x]
                xdr = temporal.multiband_raster_to_xarray(files_layer)

                # replace values with nan_value with nan so that aggregation works properly
                nan_value = xdr.attrs["_FillValue"]
                xdr = xdr.where(xdr != nan_value, np.nan)

                """
                Aggregate over temporal period (use median by default to avoid potential outliers such as clouds)
                Note that some DEA layers have quality flags that can be used to filter out clouds. 
                This is not implemented here because it is layer-specific.
                """
                outfname_list, agg_list = temporal.aggregate_temporal(
                    xdr,
                    period=period_days, 
                    agg=["median"], 
                    outfile=os.path.join(settings.outpath,f"DEA_{layername}"), 
                    buffer = None)
                outfname_dea_list += outfname_list

                # create layer titles with proper date range format
                for filename in outfname_list:
                    # get date from filename without extension
                    date_start = os.path.splitext(os.path.basename(filename).rsplit('_')[-1])[0]
                    # convert date string YYYY-MM-D to datetime object
                    date_start = datetime.strptime(date_start, "%Y-%m-%d")
                    date_end = date_start + timedelta(days=period_days)
                    date_str = date_start.strftime("%Y-%m-%d") + "-to-" + date_end.strftime("%Y-%m-%d")
                    new_name = "DEA_" + layername + "_median_" + date_str
                    layer_titles += [new_name]
                layer_list += [layername]*len(outfname_list)
            agg_list = ['median']*len(layer_titles),
        else:
            outfname_dea_list = files_dea
            # get string dea_layernames from filenames in files_dea
            layer_list = []
            for fname in files_dea:
                for layername in dea_layernames:
                    if layername in fname:
                        layer_list.append(layername)
                        break
            layer_titles = [os.path.basename(path).rsplit('.')[0] for path in files_dea]
            agg_list = ['None']*len(layer_titles)

        # Update download log table
        download_log = update_logtable(
            download_log,
            outfname_dea_list,
            layer_list,
            'DEA',
            settings,
            layertitles=layer_titles,
            agfunctions = agg_list,
            loginfos='downloaded'
        )

    # DEM
    if "DEM" in list_sources:
        cprint("\n⌛ Downloading DEM data...", attrs=["bold"])
        dem_layernames = settings.target_sources["DEM"]
        try:
            files_dem = getdata_dem.get_dem_layers(
                dem_layernames,
                settings.outpath,
                settings.target_bbox,
                settings.target_res,
            )
        except Exception as e:
            print(e)
        # Check if output if False (no data available) and skip if so
        if (files_dem == [False]) or files_dem is None:
            pass
        else:
            # Add extracted data to log dataframe
            download_log = update_logtable(
                download_log,
                files_dem,
                dem_layernames,
                'DEM',
                settings,
                layertitles=dem_layernames,
                loginfos='downloaded')

    if "Landscape" in list_sources:
        cprint("\n⌛ Downloading Landscape data...", attrs=["bold"])
        # get data from Landscape
        layernames = settings.target_sources["Landscape"]
        layertitles = ["landscape_" + layername for layername in layernames]

        files_ls = getdata_landscape.get_landscape_layers(
            layernames,
            settings.target_bbox,
            settings.outpath,
            resolution=settings.target_res,
        )
        # Add extracted data to log dataframe
        download_log = update_logtable(
            download_log,
            files_ls,
            layernames,
            "Landscape",
            settings,
            layertitles=layertitles,
            loginfos="downloaded",
        )
    if "Radiometric" in list_sources:
        cprint("\n⌛ Downloading Radiometric data...", attrs=["bold"])
        # get data from Radiometric
        # Download radiometrics
        layernames = settings.target_sources["Radiometric"]
        try:
            files_rd = getdata_radiometric.get_radiometric_layers(
                settings.outpath,
                layernames,
                bbox=settings.target_bbox,
                resolution=settings.target_res,
            )
        except Exception as e:
            print(e)
        var_exists = "files_rd" in locals() or "files_rd" in globals()
        if var_exists:
            # Add extracted data to log dataframe
            download_log = update_logtable(
                download_log,
                files_rd,
                layernames,
                "Radiometric",
                settings,
                layertitles=layernames,
                loginfos="downloaded",
            )
        else:
            pass
    if "SILO" in list_sources:
        cprint("\n⌛ Downloading SILO data...", attrs=["bold"])
        # get data from SILO
        fnames_out_silo = []
        silo_layernames = list(settings.target_sources["SILO"].keys())
        # print(silo_layernames)
        try:
            # run the download
            files_silo = os.path.join(settings.outpath, "silo")
            fnames_out = getdata_silo.get_SILO_layers(
                silo_layernames,
                settings.date_min,
                settings.date_max,
                files_silo,
                bbox=settings.target_bbox,
                format_out="tif"
            )
            # Save the layer name
            fnames_out_silo += fnames_out
        except Exception as e:
            print(e)
        # aggregate the data along time windows if period_days is not None
        if period_days is not None:
            try:
                outfname_list = []
                layername_list = []
                aggfunction_list = []
                layer_titles = []
                for i, fname in enumerate(fnames_out_silo):
                    xdr = temporal.combine_rasters_temporal(fname, channel_name="band", attribute_name="long_name")
                    outfnames_, agg_list = temporal.aggregate_temporal(
                        xdr,
                        period=period_days, 
                        agg=[settings.target_sources['SILO'][silo_layernames[i]]], 
                        outfile=f"{fname.split('.')[0]}", 
                        buffer = None)
                    outfname_list += outfnames_temp
                    layername_list += [silo_layernames[i]]*len(outfnames_temp)
                    aggfunction_list += agg_list

                    # define proper titles for the layers
                    layername = silo_layernames[i]
                    for filename in outfnames: 
                        # get date from filename without extension
                        date_start = os.path.splitext(os.path.basename(filename).rsplit('_')[-1])[0]
                        # convert date string YYYY-MM-D to datetime object
                        date_start = datetime.strptime(date_start, "%Y-%m-%d")
                        date_end = date_start + timedelta(days=period_days)
                        date_str = date_start.strftime("%Y-%m-%d") + "-to-" + date_end.strftime("%Y-%m-%d")
                        new_name = "SILO_" + layername + "_" + settings.target_sources['SILO'][silo_layernames[i]] + "_" + date_str
                        layer_titles += [new_name]
            except Exception as e:
                print(e)
        else:
            outfname_list = fnames_out_silo
            layername_list = silo_layernames
            aggfunction_list = ['']*len(fnames_out_silo)
            layer_titles = ["SILO_" + layername for layername in silo_layernames]
        var_exists = "files_silo" in locals() or "files_silo" in globals()
        if var_exists:
            # Add download info to log dataframe
            download_log = update_logtable(
                download_log,
                #fnames_out_silo,
                filenames = outfname_list,
                layernames = layername_list,
                datasource = "SILO",
                settings = settings,
                layertitles=[os.path.basename(fname).split('.')[0] for fname in outfname_list],
                agfunctions = aggfunction_list,
                loginfos="downloaded",
            )
        else:
            pass
    if "SLGA" in list_sources:
        cprint("\n⌛ Downloading SLGA data...", attrs=["bold"])
        # get data from SLGA
        slga_layernames = list(settings.target_sources["SLGA"].keys())
        # get min and max depth for each layername
        depth_min = []
        depth_max = []
        for layername in slga_layernames:
            depth_bounds = settings.target_sources["SLGA"][layername]
            dmin, dmax = getdata_slga.identifier2depthbounds(depth_bounds)
            depth_min.append(dmin)
            depth_max.append(dmax)
        try:
            files_slga = getdata_slga.get_slga_layers(
                slga_layernames,
                settings.target_bbox,
                settings.outpath,
                depth_min=depth_min,
                depth_max=depth_max,
                get_ci=True,
            )
        except Exception as e:
            print(e)
        var_exists = "files_slga" in locals() or "files_slga" in globals()
        if var_exists:
            if len(files_slga) != len(slga_layernames):
                # get filename stems of files_slga
                slga_layernames = [Path(f).stem for f in files_slga]
            download_log = update_logtable(
                download_log,
                files_slga,
                slga_layernames,
                "SLGA",
                settings,
                layertitles=[],
                loginfos="downloaded",
            )
        else:
            pass

    # save log to file
    logfile = settings.outpath + log_name + ".csv"
    download_log.to_csv(logfile, index=False)

    # extract filename from settings.infile
    # Select all processed data
    df_sel = download_log.copy()
    rasters = df_sel["filename_out"].values.tolist()
    titles = df_sel["layertitle"].values.tolist()
    if points_available:
        fn = Path(settings.infile).resolve().name
        cprint(
            f"\nExtracting data points for {fn}  -----", "magenta", attrs=["bold"])
        # Extract datatable from rasters given input coordinates
        gdf = utils.raster_query(longs, lats, rasters, titles)
        # Save the results table to a csv
        gdf.to_csv(
            os.path.join(settings.outpath, "results.csv"), index=True, mode="w"
        )
        # Save also as geopackage
        gdf.to_file(os.path.join(settings.outpath,
                    "results.gpkg"), driver="GPKG")
        utils.msg_success(
            f"Data points extracted to {settings.outpath}results.gpkg")

    if preview and points_available:
        utils.plot_rasters(rasters, longs, lats, titles)
    elif preview and not points_available:
        utils.plot_rasters(rasters, titles=titles)

    cprint("\n🎉 🎉 🎉 Harvest complete 🎉 🎉 🎉", "magenta", attrs=["bold"])

    if return_df and points_available:
        return gdf
    else:
        return None
