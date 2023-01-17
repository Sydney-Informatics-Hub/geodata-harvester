---
title: Data Overview
---

# Data Overview

## Table of Contents
- [Soil Data 3D SLGA](#soil-data-3d-slga)
- [SILO Climate Database](#silo-climate-database)
- [National Digital Elevation Model 1 Second Hydrologically Enforced](#national-digital-elevation-model-1-second-hydrologically-enforced)
- [Digital Earth Australia Geoscience Earth Observations](#digital-earth-australia-geoscience-earth-observations)
- [GSKY Data Server for DEA Geoscience Earth Observations](#gsky-data-server-for-dea-geoscience-earth-observations)
- [Radiometric Data](#radiometric-data)
- [Landscape Data SLGA](#landscape-data-slga)

## Soil Data 3D SLGA

Description: The Soil Facility produced a range of digital soil attribute products as Soil and Landscape Grid of Australia (SLGA). Each product contains six digital soil attribute maps, and their upper and lower confidence limits, representing the soil attribute at six depths: 0-5cm, 5-15cm, 15-30cm, 30-60cm, 60-100cm and 100-200cm. 

Module name: getdata_slga.py

Bounding Box: Long_min: 113.00, Lat_min: -44.00, Long_max: 154.00, Lat_max: -10.00

Period (temporal coverage; approximately): 1950-2013

Resolution: 3 arcsec

Source: https://www.clw.csiro.au/aclep/soilandlandscapegrid/ProductDetails-SoilAttributes.html

License: Creative Commons Attribution 3.0 (CC By)

Attribution: CSIRO Australia, TERN (University of Queensland), and Geoscience Australia

Layernames:

- 'Bulk_Density' :
   - Title: Bulk Density (whole earth)
   - Description: Bulk Density of the whole soil (including coarse fragments) in mass per unit volume by a method equivalent to the core method
   - Unit: g/cm3
- 'Organic_Carbon' :
   - Title: Organic Carbon
   - Description: Mass fraction of carbon by weight in the < 2 mm soil material as determined by dry combustion at 900 Celcius
   - Unit: %
- 'Clay' :
   - Title: Clay
   - Description: < 2 um mass fraction of the < 2 mm soil material determined using the pipette method
   - Unit: %
- 'Silt' :
   - Title: Silt
   - Description: 2-20 um mass fraction of the < 2 mm soil material determined using the pipette method
   - Unit: %
- 'Sand' :
   - Title: Sand
   - Description: 20 um - 2 mm mass fraction of the < 2 mm soil material determined using the pipette method
   - Unit: %
- 'pH_CaCl2' :
   - Title: pH (CaCl2)
   - Description: pH of 1:5 soil/0.01M calcium chloride extract
   - Unit: none
- 'Available_Water_Capacity' :
   - Title: Available Water Capacity
   - Description: Available water capacity computed for each of the specified depth increments
   - Unit: %
- 'Total_Nitrogen' :
   - Title: Total Nitrogen
   - Description: Mass fraction of total nitrogen in the soil by weight
   - Unit: %
- 'Total_Phosphorus' :
   - Title: Total Phosphorus
   - Description: Mass fraction of total phosphorus in the soil by weight
   - Unit: %
- 'Effective_Cation_Exchange_Capacity' :
   - Title: Effective Cation Exchange Capacity
   - Description: Cations extracted using barium chloride (BaCl2) plus exchangeable H + Al
   - Unit: meq/100g
- 'Depth_of_Regolith' :
   - Title: Depth of Regolith
   - Description: Depth to hard rock. Depth is inclusive of all regolith.
   - Unit: m
- 'Depth_of_Soil' :
   - Title: Depth of Soil
   - Description: Depth of soil profile (A & B horizons)
   - Unit: m



## SILO Climate Database

Description: SILO is containing continuous daily climate data for Australia from 1889 to present.

Module name: getdata_silo.py

Bounding Box = Long_min: 112.00, Lat_min: -44.00, Long_max: 154.00, Lat_max: -10.00

Updates: Daily

Resolution: native: 180 arcsec

Source: https://www.longpaddock.qld.gov.au/silo/gridded-data/

License: Creative Commons Attribution 4.0 International (CC BY 4.0)

Attribution: State of Queensland (Queensland Department of Environment and Science) 2020.

Layernames:

- 'daily_rain' (Daily rainfall, mm)
- 'monthly_rain' (Monthly rainfall, mm)
- 'max_temp' (Maximum temperature, deg C)
- 'min_temp'  (Minimum temperature. deg C)
- 'vp' (Vapour pressure, hPa)
- 'vp_deficit' (Vapour pressure deficit, hPa)
- 'evap_pan' (Class A pan evaporation, mm)
- 'evap_syn' (Synthetic estimate, mm)
- 'evap_comb' (Combination: synthetic estimate pre-1970, class A pan 1970 onwards, mm)
- 'evap_morton_lake' (Morton's shallow lake evaporation, mm)
- 'radiation'	(Solar radiation: Solar exposure, consisting of both direct and diffuse components, MJ/m2)
- 'rh_tmax'	(Relative humidity:	Relative humidity at the time of maximum temperature, %)
- 'rh_tmin'	(Relative humidity at the time of minimum temperature, %)
- 'et_short_crop' (Evapotranspiration FAO564 short crop, mm)
- 'et_tall_crop' (ASCE5 tall crop6, mm)
- 'et_morton_actual' (Morton's areal actual evapotranspiration, mm)
- 'et_morton_potential'	(Morton's point potential evapotranspiration, mm)
- 'et_morton_wet' (Morton's wet-environment areal potential evapotranspiration over land, mm)
- 'mslp' (Mean sea level pressure Mean sea level pressure, hPa)


## National Digital Elevation Model 1 Second Hydrologically Enforced

Description: Digital Elevation Model (DEM) of Australia derived from STRM with 1 Second Grid - Hydrologically Enforced

Module name: getdata_dem.py

Bounding Box = Long_min: 112.00, Lat_min: -44.00, Long_max: 154.00, Lat_max: -10.00

Updates: None

Resolution: native: 1 arcsec

Source: https://www.clw.csiro.au/aclep/soilandlandscapegrid/ProductDetails.html

License: Creative Commons Attribution 4.0 International (CC BY 4.0)

Attribution: Commonwealth of Australia (Geoscience Australia)

Layernames:

- 'DEM_1s'
   - Title: DEM SRTM 1 Second Hydro Enforced
   - Description: The 1 second SRTM derived hydrologically enforced DEM (DEM-H Version 1.0) is a 1 arc second (~30 m) gridded digital elevation model (DEM) that has been hydrologically conditioned and drainage enforced. The DEM-H captures flow paths based on SRTM elevations and mapped stream lines, and supports delineation of catchments and related hydrological attributes.


## Digital Earth Australia Geoscience Earth Observations


Description: Digital Earth Australia's (DEA) Landsat Surface Reflectance products take Landsat 5 Thematic Mapper (TM), Landsat 7 Enhanced Thematic Mapper Plus (ETM+) and Landsat 8 Operational Land Imager (OLI) imagery captured over the Australian continent and corrects for inconsistencies across land and coastal fringes. The result is accurate and standardised surface reflectance data, which is instrumental in identifying and quantifying environmental change. DEA’s Landsat Surface Reflectance products form a single, cohesive Analysis Ready Data (ARD) package, which allows you to analyse surface reflectance data as is without the need to apply additional corrections.

Module name: getdata_dea.py

Bounding Box: variable (see layernames)

Resolution: variable (depending on layer, typically 25m)

Updates: Daily to yearly

Source: https://docs.dea.ga.gov.au/notebooks/DEA_datasets/DEA_Landsat_Surface_Reflectance.html

License: Creative Commons Attribution 4.0 International (CC BY 4.0)

Attribution: Digital Earth Australia (DEA)

Layernames:

- 'ga_ls_ard_3':
  - title: DEA Surface Reflectance (Landsat)
  - description: Geoscience Australia Landsat 5 Thematic Mapper Analysis Ready Data Collection 3
  - bounding box: (110.696007613984, -45.6734535062289, 156.154528040633, -8.13764292647926)
  - date limits: ['1986-08-16', '2022-09-05']
  - Number of bands: 7
- 's2_nrt_granule_nbar_t':
  - title: DEA Surface Reflectance (Sentinel-2 Near Real-Time)
  - description: Sentinel-2A MSI ARD NRT - NBAR NBART and Pixel Quality
  - bounding box: (109.989859933428, -45.2413329418709, 155.307643731418, -9.9300073889701)
  - date limits: ['2022-06-20', '2022-09-19']
  - Number of bands: 23
- 's2_ard_granule_nbar_t':
  - title: DEA Surface Reflectance (Sentinel-2)
  - description: Sentinel-2A MSI Definitive ARD - NBART and Pixel Quality
  - bounding box: (109.968510816964, -45.2234942244028, 156.101505058599, -9.02727104242043)
  - date limits: ['2015-07-12', '2022-09-13']
  - Number of bands: 12
- 'ga_ls8c_nbart_gm_cyear_3':
  - title: DEA GeoMAD (Landsat 8 OLI-TIRS)
  - description: Geoscience Australia Landsat Nadir BRDF Adjusted Reflectance Terrain, Landsat 8 Geomedian Calendar Year Collection 3
  - bounding box: (110.413246718272, -46.2302085135865, 157.044900204052, -8.10857383542487)
  - date limits: ['2013-01-01', '2021-01-01']
  - Number of bands: 10
- 'ga_ls7e_nbart_gm_cyear_3':
  - title: DEA GeoMAD (Landsat 7 ETM+)
  - description: Geoscience Australia Landsat Nadir BRDF Adjusted Reflectance Terrain, Landsat 7 Geomedian Calendar Year Collection 3
  - bounding box: (110.413246718272, -45.1432282004529, 156.432609321534, -8.21783704144064)
  - date limits: ['1999-01-01', '2021-01-01']
  - Number of bands: 10
- 'ga_ls5t_nbart_gm_cyear_3':
  - title: DEA GeoMAD (Landsat 5 TM)
  - description: Geoscience Australia Landsat Nadir BRDF Adjusted Reflectance Terrain, Landsat 5 Geomedian Calendar Year Collection 3
  - bounding box: (110.413246718272, -45.0401572488294, 156.432609321534, -7.21314878610402)
  - date limits: ['1986-01-01', '2011-01-01']
  - Number of bands: 10
- 'ga_ls8c_ard_3':
  - title: DEA Surface Reflectance (Landsat 8 OLI-TIRS)
  - description: Geoscience Australia Landsat 8 Operational Land Imager and Thermal Infra-Red Scanner Analysis Ready Data Collection 3
  - bounding box: (110.718297795307, -45.6734535062289, 156.154528040633, -9.07553770894522)
  - date limits: ['2013-03-19', '2022-09-05']
  - Number of bands: 9
- 'ga_ls7e_ard_3':
  - title: DEA Surface Reflectance (Landsat 7 ETM+)
  - description: Geoscience Australia Landsat 7 Enhanced Thematic Mapper Plus Analysis Ready Data Collection 3
  - bounding box: (110.696007613984, -44.1889410289207, 155.711647298981, -9.15270092381057)
  - date limits: ['1999-05-28', '2022-04-06']
  - Number of bands: 8
- 'ga_ls5t_ard_3':
  - title: DEA Surface Reflectance (Landsat 5 TM)
  - description: Geoscience Australia Landsat 5 Thematic Mapper Analysis Ready Data Collection 3
  - bounding box: (110.757249124468, -44.2624681575318, 155.662004153478, -8.13764292647926)
  - date limits: ['1986-08-16', '2011-11-17']
  - Number of bands: 7
- 'ga_ls8c_ard_provisional_3':
  - title: DEA Surface Reflectance (Landsat 8 OLI-TIRS, Provisional)
  - description: Geoscience Australia Landsat 8 Operational Land Imager and Thermal Infra-Red Scanner Analysis Ready Data Collection 3 (provisional)
  - bounding box: (110.746179078976, -44.2480872929322, 156.113923365678, -9.07570747846392)
  - date limits: ['2022-06-20', '2022-09-19']
  - Number of bands: 9
- 'ga_ls7e_ard_provisional_3':
  - title: DEA Surface Reflectance (Landsat 7 ETM+, Provisional)
  - description: Geoscience Australia Landsat 7 Enhanced Thematic Mapper Plus Analysis Ready Data Collection 3 (provisional)
  - bounding box: (113.36982861436, -42.7522970095266, 155.249275549932, -9.18167640172494)
  - date limits: ['2022-06-22', '2022-08-24']
  - Number of bands: 8
- 'ga_ls_ard_provisional_3':
  - title: DEA Surface Reflectance (Landsat, Provisional)
  - description: Geoscience Australia Landsat 7 Enhanced Thematic Mapper Plus Analysis Ready Data Collection 3 (provisional)
  - bounding box: (110.746179078976, -44.2480872929322, 156.113923365678, -9.07570747846392)
  - date limits: ['2022-06-20', '2022-09-19']
  - Number of bands: 7
- 's2b_nrt_granule_nbar_t':
  - title: DEA Surface Reflectance (Sentinel-2B MSI Near Real-Time)
  - description: Sentinel-2B MSI ARD NRT - NBAR NBART and Pixel Quality
  - bounding box: (109.989859933428, -45.2413329418709, 155.307643731418, -9.9300073889701)
  - date limits: ['2022-06-20', '2022-09-19']
  - Number of bands: 23
- 's2a_nrt_granule_nbar_t':
  - title: DEA Surface Reflectance (Sentinel-2A MSI Near Real-Time)
  - description: Sentinel-2A MSI ARD NRT - NBAR NBART and Pixel Quality
  - bounding box: (109.989859933428, -45.2413329418709, 155.307643731418, -9.9300073889701)
  - date limits: ['2022-06-20', '2022-09-19']
  - Number of bands: 23
- 's2_nrt_provisional_granule_nbar_t':
  - title: DEA Surface Reflectance (Sentinel-2, Provisional)
  - description: Geoscience Australia Sentinel 2a MSI Analysis Ready Data Collection 3 (provisional)
  - bounding box: (111.958960179236, -44.3413038768651, 155.219674237016, -9.93000738897011)
  - date limits: ['2022-06-20', '2022-09-19']
  - Number of bands: 12
- 's2b_nrt_provisional_granule_nbar_t':
  - title: DEA Surface Reflectance (Sentinel-2B MSI, Provisional)
  - description: Geoscience Australia Sentinel 2b MSI Analysis Ready Data Collection 3 (provisional)
  - bounding box: (111.959041001616, -44.341297231057, 155.219281688203, -9.93000738897011)
  - date limits: ['2022-06-20', '2022-09-19']
  - Number of bands: 12
- 's2a_nrt_provisional_granule_nbar_t':
  - title: DEA Surface Reflectance (Sentinel-2A MSI, Provisional)
  - description: Geoscience Australia Sentinel 2a MSI Analysis Ready Data Collection 3 (provisional)
  - bounding box: (111.958960179236, -44.3413038768651, 155.219674237016, -9.93000738897011)
  - date limits: ['2022-06-20', '2022-09-19']
  - Number of bands: 12
- 's2a_ard_granule_nbar_t':
  - title: DEA Surface Reflectance (Sentinel-2A MSI)
  - description: Sentinel-2A MSI Definitive ARD - NBART and Pixel Quality
  - bounding box: (109.968510816964, -45.2234942244028, 156.101505058599, -9.02727104242043)
  - date limits: ['2015-07-12', '2022-09-13']
  - Number of bands: 12
- 's2b_ard_granule_nbar_t':
  - title: DEA Surface Reflectance (Sentinel-2B MSI)
  - description: Sentinel-2B MSI Definitive ARD - NBART and Pixel Quality
  - bounding box: (110.294393028751, -44.7864137985832, 156.101505058599, -9.02727104242043)
  - date limits: ['2017-06-30', '2022-09-13']
  - Number of bands: 12
- 'ga_ls_landcover':
  - title: DEA Land Cover Calendar Year (Landsat)
  - description: Geoscience Australia Landsat Land Cover Calendar Year Collection 2.0
  - bounding box: (112.731828633068, -44.2342184871416, 154.267421772154, -9.93509678400507)
  - date limits: ['1988-01-01', '2020-01-01']
  - Number of bands: 2
- 'ga_ls_landcover_descriptors':
  - title: DEA Land Cover Environmental Descriptors
  - description: Geoscience Australia Landsat Land Cover Calendar Year Collection 2.0
  - bounding box: (112.731828633068, -44.2342184871416, 154.267421772154, -9.93509678400507)
  - date limits: ['1988-01-01', '2020-01-01']
  - Number of bands: 5
- 'ga_ls_fc_3':
  - title: DEA Fractional Cover (Landsat)
  - description: Geoscience Australia Landsat Fractional Cover Collection 3
  - bounding box: (110.696007613984, -45.6734535062289, 156.154528040633, -8.13764292647926)
  - date limits: ['1986-08-16', '2022-09-05']
  - Number of bands: 4
- 'ga_ls_fc_pc_cyear_3':
  - title: DEA Fractional Cover Percentiles Calendar Year (Landsat)
  - description: Geoscience Australia Landsat Fractional Cover Percentile Calendar Year Collection 3
  - bounding box: (112.343354889631, -44.2467683625153, 154.378185360282, -8.51120628432549)
  - date limits: ['1987-01-01', '2021-01-01']
  - Number of bands: 10
- 'ga_ls_mangrove_cover_cyear_3':
  - title: DEA Mangroves (Landsat)
  - description: Geoscience Australia Landsat Mangrove Cover Calendar Year Collection 3
  - bounding box: (112.492257439061, -39.1292216144938, 154.264053741666, -9.5698963139854)
  - date limits: ['1987-01-01', '2021-01-01']
  - Number of bands: 1
- 's2_barest_earth':
  - title: GA Barest Earth (Sentinel-2)
  - description: The Sentinel-2 Barest Earth
  - bounding box: (112.324372771065, -43.9381826788341, 154.70510751296, -8.82186564540388)
  - date limits: ['2017-01-01', '2017-01-01']
  - Number of bands: 10
- 'ls8_barest_earth_mosaic':
  - title: GA Barest Earth (Landsat 8 OLI/TIRS)
  - description: Landsat-8 Barest Earth pixel composite albers 25 metre, 100km tile, Australian Albers Equal Area projection (EPSG:3577)
  - bounding box: (111.492400120054, -44.3357065215098, 155.066563941708, -8.83515695199939)
  - date limits: ['2013-01-01', '2013-01-01']
  - Number of bands: 6
- 'landsat_barest_earth':
  - title: GA Barest Earth (Landsat)
  - description: Landsat-5/Landsat-7/Landsat-8 combined Barest Earth pixel composite albers 25 metre, 100km tile, Australian Albers Equal Area projection (EPSG:3577)
  - bounding box: (111.033686003887, -44.4285210281062, 155.790571411147, -8.49453875182811)
  - date limits: ['1980-01-01', '1980-01-01']
  - Number of bands: 6
- 'ga_ls_tcw_percentiles_2':
  - title: DEA Wetness Percentiles (Landsat)
  - description: Geoscience Australia Landsat Tasseled Cap Wetness Percentiles Collection 2, 25 metre, 100km tile, Australian Albers Equal Area projection (EPSG:3577)
  - bounding box: (112.501524524947, -44.315077785668, 154.340852639902, -9.07349125191758)
  - date limits: ['1987-01-01', '1987-01-01']
  - Number of bands: 3
- 'ga_ls_tc_pc_cyear_3':
  - title: DEA Tasseled Cap Indices Percentiles Calendar Year (Landsat)
  - description: Geoscience Australia Landsat Tasseled Cap Percentile Calendar Year Collection 3
  - bounding box: (112.343354889631, -44.2467683625153, 154.378185360282, -8.51120628432549)
  - date limits: ['1987-01-01', '2021-01-01']
  - Number of bands: 9
- 'ga_ls_wo_3':
  - title: DEA Water Observations (Landsat)
  - description: Geoscience Australia Landsat Water Observations Collection 3
  - bounding box: (110.696007613984, -45.6734414490927, 156.154528040633, -9.07557070726103)
  - date limits: ['1986-08-16', '2022-09-05']
  - Number of bands: 1
- 'ga_ls_wo_fq_myear_3':
  - title: DEA Water Observations Multi Year (Landsat)
  - description: Geoscience Australia Landsat Water Observations Frequency Multi Year Collection 3
  - bounding box: (110.413246718272, -46.1419438144744, 157.044900204052, -8.10857383542487)
  - date limits: ['1986-01-01', '1986-01-01']
  - Number of bands: 3
- 'ga_ls_wo_fq_cyear_3':
  - title: DEA Water Observations Calendar Year (Landsat)
  - description: Geoscience Australia Landsat Water Observations Frequency Calendar Year Collection 3
  - bounding box: (110.413246718272, -46.1419438144744, 157.044900204052, -8.10857383542487)
  - date limits: ['1986-01-01', '2021-01-01']
  - Number of bands: 3
- 'ga_ls_wo_fq_apr_oct_3':
  - title: DEA Water Observations April to October (Landsat)
  - description: Geoscience Australia Landsat Water Observations Frequency April to October Collection 3
  - bounding box: (110.413246718272, -46.1419438144744, 157.044900204052, -8.10857383542487)
  - date limits: ['1986-04-01', '2021-04-01']
  - Number of bands: 3
- 'ga_ls_wo_fq_nov_mar_3':
  - title: DEA Water Observations November to March (Landsat)
  - description: Geoscience Australia Landsat Water Observations Frequency November to March Collection 3
  - bounding box: (110.413246718272, -46.1419438144744, 157.044900204052, -8.21783704144064)
  - date limits: ['1987-11-01', '2021-11-01']
  - Number of bands: 3
- 'wofs_filtered_summary':
  - title: DEA Multi-Year Water Observation Frequency Filtered Statistics (Landsat, DEPRECATED)
  - description: Water Observations from Space Statistics confidence filtered
  - bounding box: (111.859562290899, -44.9351287319957, 155.169368098324, -9.00692244744483)
  - date limits: ['1970-01-01', '1970-01-01']
  - Number of bands: 2
- 'wofs_summary_clear':
  - title: DEA Multi-Year Clear Observation Statistics (Landsat, DEPRECATED)
  - description: Water Observations from Space Statistics
  - bounding box: (112.99986111, -44.0008652894921, 153.999861110328, -10.0001388899999)
  - date limits: ['1970-01-01', '1970-01-01']
  - Number of bands: 3
- 'wofs_summary_wet':
  - title: DEA Multi-Year Wet Observation Statistics (Landsat, DEPRECATED)
  - description: Water Observations from Space Statistics
  - bounding box: (112.99986111, -44.0008652894921, 153.999861110328, -10.0001388899999)
  - date limits: ['1970-01-01', '1970-01-01']
  - Number of bands: 3
- 'Water Observations from Space Statistics':
  - title: DEA Multi-Year Water Observation Frequency Statistics (Landsat, DEPRECATED)
  - description: Water Observations from Space Statistics
  - bounding box: (112.99986111, -44.0008652894921, 153.999861110328, -10.0001388899999)
  - date limits: ['1970-01-01', '1970-01-01']
  - Number of bands: 3
- 'wofs_filtered_summary_confidence':
  - title: DEA Multi-Year Water Observation Confidence Statistics (Landsat, DEPRECATED)
  - description: Water Observations from Space Statistics confidence filtered
  - bounding box: (111.859562290899, -44.9351287319957, 155.169368098324, -9.00692244744483)
  - date limits: ['1970-01-01', '1970-01-01']
  - Number of bands: 2
- 'ITEM_V2.0.0':
  - title: DEA Intertidal Extents (Landsat)
  - description: Relative Extents Model
  - bounding box: (112.459622677896, -43.7203758299765, 153.670408736335, -10.3096529183452)
  - date limits: ['1986-01-01', '1986-01-01']
  - Number of bands: 1
- 'ITEM_V2.0.0_Conf':
  - title: DEA Intertidal Extents confidence
  - description: Average ndwi Standard Deviation, the Confidence Layer
  - bounding box: (112.459622677896, -43.7203758299765, 153.670408736335, -10.3096529183452)
  - date limits: ['1986-01-01', '1986-01-01']
  - Number of bands: 1
- 'NIDEM':
  - title: DEA Intertidal Elevation (Landsat)
  - description: National Intertidal Digital Elevation Model 25m 1.0.0
  - bounding box: (112.223058990767, -43.8291965530654, 154.080299801132, -10.2371048142508)
  - date limits: ['1986-01-01', '1986-01-01']
  - Number of bands: 1
- 'high_tide_composite':
  - title: DEA High Tide Imagery (Landsat)
  - description: High tide 20 percentage composites 25m v. 2.0.0
  - bounding box: (112.223058990767, -43.8291965530654, 154.080299801132, -10.2371048142508)
  - date limits: ['2000-01-01', '2000-01-01']
  - Number of bands: 6
- 'low_tide_composite':
  - title: DEA Low Tide Imagery (Landsat)
  - description: Low tide 20 percentage composites 25m v. 2.0.0
  - bounding box: (112.223058990767, -43.8291965530654, 154.080299801132, -10.2371048142508)
  - date limits: ['2000-01-01', '2000-01-01']
  - Number of bands: 6
- 'ga_s2_ba_provisional_3':
  - title: DEA Burnt Area Characteristic Layers (Sentinel 2 Near Real-Time, Provisional)
  - description: Sentinel 2 Burnt Area Collection 3 (Provisional)
  - bounding box: (111.966746816605, -44.3414673034495, 155.213824039639, -9.93000738897011)
  - date limits: ['2021-10-01', '2022-09-19']
  - Number of bands: None
- 'alos_displacement':
  - title: ALOS Displacement
  - description: CEMP InSAR ALOS Displacement
  - bounding box: (150.330509919584, -34.5250413940276, 151.258021405841, -33.772472435988)
  - date limits: ['2008-02-11', '2010-10-22']
  - Number of bands: 4
- 'alos_velocity':
  - title: ALOS Velocity
  - description: CEMP InSAR ALOS Velocity
  - bounding box: (150.331038253243, -34.5250413940276, 151.258021405841, -33.772472435988)
  - date limits: ['2009-06-15', '2009-06-15']
  - Number of bands: 4
- 'envisat_displacement':
  - title: ENVISAT Displacement
  - description: CEMP InSAR Envisat Displacement
  - bounding box: (150.416357298779, -34.5283535864513, 151.184355816078, -33.5035077252927)
  - date limits: ['2006-06-26', '2010-08-28']
  - Number of bands: 4
- 'envisat_velocity':
  - title: ENVISAT Velocity
  - description: CEMP InSAR Envisat Velocity
  - bounding box: (150.416357298779, -34.5283535864513, 151.184355816078, -33.5035077252927)
  - date limits: ['2008-06-15', '2008-06-15']
  - Number of bands: 4
- 'radarsat2_displacement':
  - title: RADARSAT2 Displacement
  - description: CEMP InSAR Radarsat-2 Displacement
  - bounding box: (150.540420399293, -34.3792688432228, 151.151613477574, -33.8798432478719)
  - date limits: ['2015-07-15', '2019-05-31']
  - Number of bands: 4
- 'radarsat2_velocity':
  - title: RADARSAT2 Velocity
  - description: CEMP InSAR Radarsat-2 Velocity
  - bounding box: (150.540420399293, -34.3792688432228, 151.151613477574, -33.8798432478719)
  - date limits: ['2017-06-15', '2017-06-15']
  - Number of bands: 4
- 'aster_false_colour':
  - title: False Colour Mosaic
  - description: ASTER
  - bounding box: (112.917275536606, -44.013698912363, 153.640054299875, -10.2856586)
  - date limits: ['2000-02-01', '2000-02-01']
  - Number of bands: 3
- 'aster_regolith_ratios':
  - title: Regolith Ratios
  - description: ASTER
  - bounding box: (112.917275536606, -44.013698912363, 153.640054299875, -10.2856586)
  - date limits: ['2000-02-01', '2000-02-01']
  - Number of bands: 3
- 'aster_aloh_group_composition':
  - title: AlOH Group Composition
  - description: ASTER
  - bounding box: (112.917275536606, -43.7806433511675, 153.640054299875, -10.2856586)
  - date limits: ['2000-02-01', '2000-02-01']
  - Number of bands: 1
- 'aster_aloh_group_content':
  - title: AlOH Group Content
  - description: ASTER
  - bounding box: (112.917275536606, -43.7806433511675, 153.640054299875, -10.2856586)
  - date limits: ['2000-02-01', '2000-02-01']
  - Number of bands: 1
- 'aster_feoh_group_content':
  - title: FeOH Group Content
  - description: ASTER
  - bounding box: (112.917275536606, -43.7806433511675, 153.640054299875, -10.2856586)
  - date limits: ['2000-02-01', '2000-02-01']
  - Number of bands: 1
- 'aster_ferric_oxide_composition':
  - title: Ferric Oxide Composition
  - description: ASTER
  - bounding box: (112.917275536606, -43.7806433511675, 153.640054299875, -10.2856586)
  - date limits: ['2000-02-01', '2000-02-01']
  - Number of bands: 1
- 'aster_ferric_oxide_content':
  - title: Ferric Oxide Content
  - description: ASTER
  - bounding box: (112.917275536606, -43.7806433511675, 153.640054299875, -10.2856586)
  - date limits: ['2000-02-01', '2000-02-01']
  - Number of bands: 1
- 'aster_ferrous_iron_content_in_mgoh':
  - title: Ferrous Iron Content in MgOH/Carbonate
  - description: ASTER
  - bounding box: (112.917275536606, -43.7806433511675, 153.640054299875, -10.2856586)
  - date limits: ['2000-02-01', '2000-02-01']
  - Number of bands: 1
- 'aster_ferrous_iron_index':
  - title: Ferrous Iron Index
  - description: ASTER
  - bounding box: (112.917275536606, -43.7806433511675, 153.640054299875, -10.2856586)
  - date limits: ['2000-02-01', '2000-02-01']
  - Number of bands: 1
- 'aster_green_vegetation':
  - title: Green Vegetation Content
  - description: ASTER
  - bounding box: (112.917275536606, -43.7806433511675, 153.640054299875, -10.2856586)
  - date limits: ['2000-02-01', '2000-02-01']
  - Number of bands: 1
- 'aster_gypsum_index':
  - title: Gypsum Index
  - description: ASTER
  - bounding box: (112.917024138111, -43.7806027057097, 153.640358457438, -10.28257228)
  - date limits: ['2000-02-01', '2000-02-01']
  - Number of bands: 1
- 'aster_kaolin_group_index':
  - title: Kaolin Group Index
  - description: ASTER
  - bounding box: (112.917275536606, -43.7806433511675, 153.640054299875, -10.2856586)
  - date limits: ['2000-02-01', '2000-02-01']
  - Number of bands: 1
- 'aster_mgoh_group_composition':
  - title: MgOH Group Composition
  - description: ASTER
  - bounding box: (112.917275536606, -43.7806433511675, 153.640054299875, -10.2856586)
  - date limits: ['2000-02-01', '2000-02-01']
  - Number of bands: 1
- 'aster_mgoh_group_content':
  - title: MgOH Group Content
  - description: ASTER
  - bounding box: (112.917275536606, -43.7806433511675, 153.640054299875, -10.2856586)
  - date limits: ['2000-02-01', '2000-02-01']
  - Number of bands: 1
- 'aster_opaque_index':
  - title: Opaque Index
  - description: ASTER
  - bounding box: (112.917275536606, -43.7806433511675, 153.640054299875, -10.2856586)
  - date limits: ['2000-02-01', '2000-02-01']
  - Number of bands: 1
- 'aster_silica_index':
  - title: TIR Silica index
  - description: ASTER
  - bounding box: (112.917024138111, -43.7806027057097, 153.640358457438, -10.28257228)
  - date limits: ['2000-02-01', '2000-02-01']
  - Number of bands: 1
- 'aster_quartz_index':
  - title: TIR Quartz Index
  - description: ASTER
  - bounding box: (112.917024138111, -43.7806027057097, 153.640358457438, -10.28257228)
  - date limits: ['2000-02-01', '2000-02-01']
  - Number of bands: 1
- 'multi_scale_topographic_position':
  - title: Multi-Scale Topographic Position
  - description: Multi-scale Topographic Position Image
  - bounding box: (112.9995833, -44.0004167, 153.9995833, -10.0004167)
  - date limits: ['2018-01-01', '2018-01-01']
  - Number of bands: 3
- 'weathering_intensity':
  - title: Weathering Intensity
  - description: Weathering Intensity Model
  - bounding box: (112.9995833, -44.0004167, 153.9995833, -10.0004167)
  - date limits: ['2018-01-01', '2018-01-01']
  - Number of bands: 1
  

## GSKY Data Server for DEA Geoscience Earth Observations

Description: Digital Earth Australia's (DEA) Landsat Surface Reflectance products take Landsat 5 Thematic Mapper (TM), Landsat 7 Enhanced Thematic Mapper Plus (ETM+) and Landsat 8 Operational Land Imager (OLI) imagery captured over the Australian continent and corrects for inconsistencies across land and coastal fringes. This product has been corrected to remove the influences of the atmosphere, the time of year, terrain shadow and satellite view angles. Some of the layers include image composites that are made from images acquired within a 16 day period. 

Module name: getdata_dea_nci.py

Resolution: variable (typically 1 arcsec)

Updates: daily to yearly

Source: https://opus.nci.org.au/display/Help/Datasets

License: Creative Commons Attribution 4.0 International (CC BY 4.0)

Attribution: The data products are produced using Digital Earth Australia. The WCS service relies on GSKY - A Scalable, Distributed Geospatial Data Service from the National Centre for Environmental Information (NCI).

Layernames:

- 'blend_sentinel2_landsat_nbart_daily' :
   - title: Multi-sensor (Landsat and Sentinel 2) surface reflectance (Beta)
   - description: This multi-sensor service has been corrected to remove the influences of the atmosphere, the time of year, terrain shadow and satellite view angles using the methods described in Li et al. 2012 https://doi.org/10.1016/j.rse.2012.06.018. This service combines terrain corrected surface reflectance observations from three Landsat sensors (Landsat 5 TM, Landsat 7 ETM+, Landsat 8 OLI) and two Sentinel 2 sensors (Sentinel 2A and 2B). More detailed information about the terrain corrected surface reflectance product suite produced using Digital Earth Australia including CCBY4.0 is available at http://dx.doi.org/10.4225/25/5a7a76d2e129e. The service for each day is composed from all acquisitions that occurred over the Australian region on that calendar day.
- 'hltc_high' :
   - title: DEA High Tide Composite 25m v2.0
   - description: The High and Low Tide Composites product is composed of two surface reflectance composite mosaics of Landsat TM and ETM+ (Landsat 5 and Landsat 7 respectively) and OLI (Landsat 8) surface reflectance data Li et al. 2010 https://doi.org/10.1109/JSTARS.2010.2042281. These products have been produced using Digital Earth Australia (DEA). The two mosaics allow cloud free and noise reduced visualisation of the shallow water and inter-tidal coastal regions of Australia, as observed at high and low tide respectively. The composites are generated utilising the geomedian approach of Roberts et al. (2017) (https://doi.org/10.1109/TGRS.2017.2723896) to ensure a valid surface reflectance spectra suitable for uses such as habitat mapping. The time range used for composite generation in each polygon of the mosaic is tailored to ensure dynamic coastal features are captured whilst still allowing a clean and cloud free composite to be generated (see Sagar et al. 2018 (https://doi.org/10.3390/rs10030480)). The concepts of the Observed Tidal Range (OTR), and Highest and Lowest Observed Tide (HOT, LOT) are discussed and described fully in Sagar et al. (2017) (https://doi.org/10.1016/j.rse.2017.04.009). This service provides access to the High Tide Composite v2.0 product. More detailed information including CCBY4.0 is available at http://dx.doi.org/10.4225/25/5a615705d20f7 .
- 'hltc_low' :
   - title: DEA Low Tide Composite 25m v2.0
   - description: The High and Low Tide Composites product is composed of two surface reflectance composite mosaics of Landsat TM and ETM+ (Landsat 5 and Landsat 7 respectively) and OLI (Landsat 8) surface reflectance data Li et al. 2010 https://doi.org/10.1109/JSTARS.2010.2042281. These products have been produced using Digital Earth Australia (DEA). The two mosaics allow cloud free and noise reduced visualisation of the shallow water and inter-tidal coastal regions of Australia, as observed at high and low tide respectively. The composites are generated utilising the geomedian approach of Roberts et al. (2017) (https://doi.org/10.1109/TGRS.2017.2723896) to ensure a valid surface reflectance spectra suitable for uses such as habitat mapping. The time range used for composite generation in each polygon of the mosaic is tailored to ensure dynamic coastal features are captured whilst still allowing a clean and cloud free composite to be generated (see Sagar et al. 2018 (https://doi.org/10.3390/rs10030480)). The concepts of the Observed Tidal Range (OTR), and Highest and Lowest Observed Tide (HOT, LOT) are discussed and described fully in Sagar et al. (2017) (https://doi.org/10.1016/j.rse.2017.04.009). This service provides access to the Low Tide Composite v2.0 product. More detailed information including CCBY4.0 is available at http://dx.doi.org/10.4225/25/5a615705d20f7 .
- 'item_relative' :
   - title: DEA Intertidal Extents Model Relative Layer 25m v2.0
   - description: The Intertidal Extents Model (ITEM) product is a national dataset characterising the spatial extents of the exposed intertidal zone; the land between the observed highest and lowest tide, at intervals of the observed tidal range. ITEM provides the extent and topography of the intertidal zone of Australia's coastline (excluding offshore Territories). This information was derived using observations in the Landsat archive since 1986. ITEM v2.0 has implemented an improved tidal modelling framework over that utilised in ITEM v1.0 (Sagar et al. 2017, 2018) (https://doi.org/10.1016/j.rse.2017.04.009, https://doi.org/10.3390/rs10030480). The expanded Landsat archive within the Digital Earth Australia (DEA) has also enabled the model extent to be increased from ITEM v1.0 to cover a number of offshore reefs, including the full Great Barrier Reef and southern sections of the Torres Strait Islands. ITEM can be a valuable complementary dataset to both onshore LiDAR survey data and coarser offshore bathymetry data, enabling a more realistic representation of the land and ocean interface. More detailed information including CCBY4.0 is available at http://dx.doi.org/10.4225/25/5a602cc9eb358. This service provides access to the Intertidal Extents Model v2.0 Relative Layer product. The relative layer displays the modelled extents of the exposed intertidal zone, at percentile intervals of the observed tidal range (OTR). For example, the region defined as 0-10% denotes an area that only exposes at the lowest 10% of tides in relation to the OTR.
- 'item_stddev' :
   - title: DEA Intertidal Extents Model Confidence Layer 25m v2.0
   - description: The Intertidal Extents Model (ITEM) product is a national dataset characterising the spatial extents of the exposed intertidal zone; the land between the observed highest and lowest tide, at intervals of the observed tidal range. ITEM provides the extent and topography of the intertidal zone of Australia's coastline (excluding offshore Territories). This information was derived using observations in the Landsat archive since 1986. ITEM v2.0 has implemented an improved tidal modelling framework over that utilised in ITEM v1.0 (Sagar et al. 2017, 2018) (https://doi.org/10.1016/j.rse.2017.04.009, https://doi.org/10.3390/rs10030480). The expanded Landsat archive within the Digital Earth Australia (DEA) has also enabled the model extent to be increased from ITEM v1.0 to cover a number of offshore reefs, including the full Great Barrier Reef and southern sections of the Torres Strait Islands. ITEM can be a valuable complementary dataset to both onshore LiDAR survey data and coarser offshore bathymetry data, enabling a more realistic representation of the land and ocean interface. More detailed information including CCBY4.0 is available at http://dx.doi.org/10.4225/25/5a602cc9eb358. This service provides access to the Intertidal Extents Model v2.0 Confidence Layer product. The confidence layer displays the standard deviation of the water index values (NDWI) derived across the tidal intervals used in generating the core ITEM relative extents product. High values indicate regions where inundation patterns are not driven by tidal influences. This can be a result of change (shoreline, geomorphic, anthropogenic), or caused by errors in the underlying tidal model.
- 'landsat5_nbar_16day' :
   - title: 16-day DEA Landsat 5 surface reflectance
   - description: This product has been corrected to remove the influences of the atmosphere, the time of year and satellite view angles using the methods described in Li et al. 2010 https://doi.org/10.1109/JSTARS.2010.2042281. Landsat 5 Thematic Mapper (TM) data is available from August 1986 to November 2011. More detailed information about the surface reflectance product suite produced using Digital Earth Australia including CCBY4.0 is available at http://dx.doi.org/10.4225/25/5a7a501e1c5af. This service provides access to Landsat 5 TM surface reflectance data. The image composites are made from images acquired within a 16 day period, and may include clouds.
- 'landsat5_nbar_daily' :
   - title: Daily DEA Landsat 5 surface reflectance
   - description: This product has been corrected to remove the influences of the atmosphere, the time of year and satellite view angles using the methods described in Li et al. 2010 https://doi.org/10.1109/JSTARS.2010.2042281. Landsat 5 Thematic Mapper (TM) data is available from August 1986 to November 2011. More detailed information about the surface reflectance product suite produced using Digital Earth Australia including CCBY4.0 is available at http://dx.doi.org/10.4225/25/5a7a501e1c5af. This service provides access to Landsat 5 TM surface reflectance data. The image composites are made from images acquired within a 24 hour period, and may include clouds.
- 'landsat5_nbart_16day' :
   - title: 16-day DEA Landsat 5 terrain corrected surface reflectance
   - description: This product has been corrected to remove the influences of the atmosphere, the time of year, terrain shadow and satellite view angles using the methods described in Li et al. 2012 https://doi.org/10.1016/j.rse.2012.06.018. Landsat 5 Thematic Mapper (TM) data is available from August 1986 to November 2011. More detailed information about the terrain corrected surface reflectance product suite produced using Digital Earth Australia including CCBY4.0 is available at http://dx.doi.org/10.4225/25/5a7a76d2e129e. This service provides access to Landsat 5 Thematic Mapper (TM) terrain corrected surface reflectance data. The image composites are made from images acquired within a 16 day period, and may include clouds.
- 'landsat5_nbart_daily' :
   - title: Daily DEA Landsat 5 terrain corrected surface reflectance
   - description: This product has been corrected to remove the influences of the atmosphere, the time of year, terrain shadow and satellite view angles using the methods described in Li et al. 2012 https://doi.org/10.1016/j.rse.2012.06.018. Landsat 5 Thematic Mapper (TM) data is available from August 1986 to November 2011. More detailed information about the terrain corrected surface reflectance product suite produced using Digital Earth Australia including CCBY4.0 is available at http://dx.doi.org/10.4225/25/5a7a76d2e129e. This service provides access to Landsat 5 Thematic Mapper (TM) terrain corrected surface reflectance data. The image composites are made from images acquired within a 24 hour period, and may include clouds.
- 'landsat7_nbar_16day' :
   - title: 16-day DEA Landsat 7 surface reflectance
   - description: This product has been corrected to remove the influences of the atmosphere, the time of year and satellite view angles using the methods described in Li et al. 2010 https://doi.org/10.1109/JSTARS.2010.2042281. Landsat 7 Enhanced Thematic Mapper (ETM+) data is available from May 1999 and onwards. Please note that images from 1st of June 2003 onwards are affected by the failure of scan line corrector which results in strips of missing data. More detailed information about the surface reflectance product suite produced using Digital Earth Australia including CCBY4.0 is available at http://dx.doi.org/10.4225/25/5a7a501e1c5af. This service provides access to Landsat 7 ETM+ terrain corrected surface reflectance data. The image composites are made from images acquired within a 16 day period, and may include clouds.
- 'landsat7_nbar_daily' :
   - title: Daily DEA Landsat 7 surface reflectance
   - description: This product has been corrected to remove the influences of the atmosphere, the time of year and satellite view angles using the methods described in Li et al. 2010 https://doi.org/10.1109/JSTARS.2010.2042281. Landsat 7 Enhanced Thematic Mapper (ETM+) data is available from May 1999 and onwards. Please note that images from 1st of June 2003 onwards are affected by the failure of scan line corrector which results in strips of missing data. More detailed information about the surface reflectance product suite produced using Digital Earth Australia including CCBY4.0 is available at http://dx.doi.org/10.4225/25/5a7a501e1c5af. This service provides access to Landsat 7 ETM+ terrain corrected surface reflectance data. The image composites are made from images acquired within a 24 hour period, and may include clouds.
- 'landsat7_nbart_16day' :
   - title: 16-day DEA Landsat 7 terrain corrected surface reflectance
   - description: This product has been corrected to remove the influences of the atmosphere, the time of year, terrain shadow and satellite view angles using the methods described in Li et. al. 2012 https://doi.org/10.1016/j.rse.2012.06.018. Landsat 7 Enhanced Thematic Mapper (ETM+) data is available from May 1999 and onwards. Please note that images from 1st of June 2003 are affected by the failure of scan line corrector which results in strips of missing data. More detailed information about the surface reflectance product suite produced using Digital Earth Australia including CCBY4.0 is available at http://dx.doi.org/10.4225/25/5a7a76d2e129e. This service provides access to Landsat 7 ETM+ terrain corrected surface reflectance data. The image composites are made from images acquired within a 16 day period, and may include clouds.
- 'landsat7_nbart_daily' :
   - title: Daily DEA Landsat 7 terrain corrected surface reflectance
   - description: This product has been corrected to remove the influences of the atmosphere, the time of year, terrain shadow and satellite view angles using the methods described in Li et. al. 2012 https://doi.org/10.1016/j.rse.2012.06.018. Landsat 7 Enhanced Thematic Mapper (ETM+) data is available from May 1999 and onwards. Please note that images from 1st of June 2003 are affected by the failure of scan line corrector which results in strips of missing data. More detailed information about the surface reflectance product suite produced using Digital Earth Australia including CCBY4.0 is available at http://dx.doi.org/10.4225/25/5a7a76d2e129e. This service provides access to Landsat 7 ETM+ terrain corrected surface reflectance data. The image composites are made from images acquired within a 24 hour period, and may include clouds.
- 'landsat8_nbar_16day' :
   - title: 16-day DEA Landsat 8 surface reflectance
   - description: This product has been corrected to remove the influences of the atmosphere, the time of year and satellite view angles using the methods described in Li et al. 2010 https://doi.org/10.1109/JSTARS.2010.2042281. Landsat 8 Operational Land Imager (OLI) data is available from March 2013 and onwards. More detailed information about the surface reflectance product suite produced using Digital Earth Australia including CCBY4.0 is available at http://dx.doi.org/10.4225/25/5a7a501e1c5af. This service provides access to Landsat 8 OLI surface reflectance data. The image composites are made from images acquired within a 16 day period, and may include clouds.
- 'landsat8_nbar_daily' :
   - title: Daily DEA Landsat 8 surface reflectance
   - description: This product has been corrected to remove the influences of the atmosphere, the time of year and satellite view angles using the methods described in Li et al. 2010 https://doi.org/10.1109/JSTARS.2010.2042281. Landsat 8 Operational Land Imager (OLI) data is available from March 2013 and onwards. More detailed information about the surface reflectance product suite produced using Digital Earth Australia including CCBY4.0 is available at http://dx.doi.org/10.4225/25/5a7a501e1c5af. This service provides access to Landsat 8 OLI surface reflectance data. The image composites are made from images acquired within a 24 hour period, and may include clouds.
- 'landsat8_nbart_16day' :
   - title: 16-day DEA Landsat 8 terrain corrected surface reflectance
   - description: This product has been corrected to remove the influences of the atmosphere, the time of year, terrain shadow and satellite view angles using the methods described in Li et al. 2012 https://doi.org/10.1016/j.rse.2012.06.018. Landsat 8 Operational Land Imager (OLI) data is available from March 2013 and onwards. More detailed information about the terrain corrected surface reflectance product suite produced using Digital Earth Australia including CCBY4.0 is available at http://dx.doi.org/10.4225/25/5a7a76d2e129e. This service provides access to Landsat 8 OLI terrain corrected surface reflectance data. The image composites are made from images acquired within a 16 day period, and may include clouds.
- 'landsat8_nbart_daily' :
   - title: Daily DEA Landsat 8 terrain corrected surface reflectance
   - description: This product has been corrected to remove the influences of the atmosphere, the time of year, terrain shadow and satellite view angles using the methods described in Li et al. 2012 https://doi.org/10.1016/j.rse.2012.06.018. Landsat 8 Operational Land Imager (OLI) data is available from March 2013 and onwards. More detailed information about the terrain corrected surface reflectance product suite produced using Digital Earth Australia including CCBY4.0 is available at http://dx.doi.org/10.4225/25/5a7a76d2e129e. This service provides access to Landsat 8 OLI terrain corrected surface reflectance data. The image composites are made from images acquired within a 24 hour period, and may include clouds.
- 'sentinel2_nbart_daily' :
   - title: Sentinel 2 Analysis Ready Data
   - description: The Surface Reflectance product has been corrected to account for variations caused by atmospheric properties, sun position and sensor view angle at time of image capture. These corrections have been applied to all satellite imagery in the Sentinel-2 archive. This is undertaken to allow comparison of imagery acquired at different times, by different sensors, in different seasons and in different geographic locations. These products also indicate where the imagery has been affected by cloud or cloud shadow, contains missing data or has been affected in other ways. The Surface Reflectance products are useful as a fundamental starting point for any further analysis and are the underlying data of all other Digital Earth Australia products.


## Radiometric Data

Description: This radiometric sub-collection of the Geoscience Australia Geophysics Reference Data Collection are compilations of radiometric data from an extensive archive of geophysical surveys dating back to 1947, which are contained in other sub-collections of this collection. The individual survey datasets have been acquired by Geoscience Australia and its State and Territory Government partners. The compilations of radiometric data involved the levelling and merging (mosaicking) of regularly interpolated grid (raster) data, from selected individual geophysical surveys, into near-seamless national scale grids for each datatype and creating derivations thereof. The selected individual surveys are chosen based on the spatial resolution and accuracy of individual surveys within a given area. 

Module name: getdata_radiometric.py

Resolution: 100m (0.001 deg)

Updates: None

Source: https://opus.nci.org.au/display/Help/Datasets, 

License: Creative Commons Attribution 4.0 International (CC BY 4.0)

Attribution: Geoscience Australia. The WCS service relies on GSKY - A Scalable, Distributed Geospatial Data Service from the National Centre for Environmental Information (NCI).

Layernames:

- 'radmap2019_grid_dose_terr_awags_rad_2019'
   - title: Radiometric Grid of Australia (Radmap) v4 2019 unfiltered terrestrial dose rate
   - description: The unfiltered terrestrial dose rate grid is a derivative of the 2019 radiometric or gamma-ray grid of Australia, which is a merge of over 600 individual gamma-ray spectrometric surveys. The radiometric, or gamma-ray spectrometric method, measures the natural variations in the gamma-rays detected near the Earth's surface as the result of the natural radioactive decay of potassium (K), uranium (U) and thorium (Th). The data are collected on airborne geophysical surveys conducted by Commonwealth, State and Northern Territory Governments and the private sector.The unfiltered terrestrial dose rate grid is derived as a linear combination of the unfiltered K, U and Th grids, and has a cell size of about 100m (0.001 degrees).
- 'radmap2019_grid_dose_terr_filtered_awags_rad_2019'
   - title: Radiometric Grid of Australia (Radmap) v4 2019 filtered terrestrial dose rate
   - description: The filtered terrestrial dose rate grid is a derivative of the 2019 radiometric or gamma-ray grid of Australia, made of a combination of over 600 individual survey grids. The radiometric, or gamma-ray spectrometric method, measures the natural variations in the gamma-rays detected near the Earth's surface as the result of the natural radioactive decay of potassium (K), uranium (U) and thorium (Th). The data are collected on airborne geophysical surveys conducted by Commonwealth, State and Northern Territory Governments and the private sector.The terrestrial dose rate grid is derived as a linear combination of the filtered K, U and Th grids. A low pass filter is applied to the unfiltered grid to generate the filtered terrestrial dose rate grid. The grid cell size is about 100m (0.001 degrees).
- 'radmap2019_grid_k_conc_awags_rad_2019'
   - title: Radiometric Grid of Australia (Radmap) v4 2019 unfiltered pct potassium
   - description: The unfiltered potassium grid is a derivative of the 2019 radiometric grid of Australia. The radiometric, or gamma-ray spectrometric method, measures the natural variations in the gamma-rays detected near the Earth's surface as the result of the natural radioactive decay of potassium (K), uranium (U) and thorium (Th). The data are collected on airborne geophysical surveys conducted by Commonwealth, State and Northern Territory Governments and the private sector. The 2019 unfiltered potassium grid has a cell size of about 100 m (0.001 degrees) and shows potassium element concentrations of the Australia region. Potassium is the seventh most abundant element in the Earth's crust. The potassium concentration grid can be used to locate minerals and compounds containing potassium.
- 'radmap2019_grid_k_conc_filtered_awags_rad_2019'
   - title: Radiometric Grid of Australia (Radmap) v4 2019 filtered pct potassium grid
   - description: The filtered potassium grid is a derivative of the 2019 radiometric or gamma-ray grid of Australia. The radiometric, or gamma-ray spectrometric method, measures the natural variations in the gamma-rays detected near the Earth's surface as the result of the natural radioactive decay of potassium, uranium and thorium. The data are collected on airborne geophysical surveys conducted by Commonwealth, State and Northern Territory Governments and the private sector.The 2019 filtered potassium grid has a cell size of about 100m (0.001 degrees) and shows potassium element concentrations of the Australia region. It was obtained by applying a low-pass filter to the original potassium grid. Potassium is the seventh most abundant element in the Earth's crust. This potassium concentration grid can be used to locate minerals and compounds containing potassium.
- 'radmap2019_grid_th_conc_awags_rad_2019'
   - title: Radiometric Grid of Australia (Radmap) v4 2019 unfiltered ppm thorium
   - description: The unfiltered thorium grid is a derivative of the 2019 radiometric or gamma-ray grid of Australia which is a merge of over 600 individual gamma-ray spectrometric surveys. The radiometric, or gamma-ray spectrometric method, measures the natural variations in the gamma-rays detected near the Earth's surface as the result of the natural radioactive decay of potassium (K), uranium (U) and thorium (Th). The data are collected on airborne geophysical surveys conducted by Commonwealth, State and Northern Territory Governments and the private sector.The 2019 unfiltered thorium grid has a cell size of about 100 m (0.001 degrees) and shows thorium element concentrations of the Australia region.
- 'radmap2019_grid_th_conc_filtered_awags_rad_2019'
   - title: Radiometric Grid of Australia (Radmap) v4 2019 filtered ppm thorium
   - description: The filtered thorium grid is a derivative of the 2019 radiometric or gamma-ray grid of Australia. The radiometric, or gamma-ray spectrometric method, measures the natural variations in the gamma-rays detected near the Earth's surface as the result of the natural radioactive decay of potassium (K), uranium (U) and thorium (Th). The data are collected on airborne geophysical surveys conducted by Commonwealth, State and Northern Territory Governments and the private sector. The 2019 filtered thorium grid was derived by seamlessly merging over 600 airborne gamma-ray spectrometric surveys. The final grid has a cell size of about 100m (0.001 degrees) and shows thorium element concentrations of the Australia region.
- 'radmap2019_grid_thk_ratio_awags_rad_2019'
   - title: Radiometric Grid of Australia (Radmap) v4 2019 ratio thorium over potassium
   - description: The thorium over potassium grid is a derivative of the 2019 radiometric or gamma-ray grid of Australia. The radiometric, or gamma-ray spectrometric method, measures the natural variations in the gamma-rays detected near the Earth's surface as the result of the natural radioactive decay of potassium (K), uranium (U) and thorium (Th). The data are collected on airborne geophysical surveys conducted by Commonwealth, State and Northern Territory Governments and the private sector.The 2019 thorium over potassium was derived by seamlessly merging over 600 airborne gamma-ray spectrometric surveys. The final grid has a cell size of about 100m (0.001 degrees) and is derived from the filtered thorium and potassium grids.
- 'radmap2019_grid_u2th_ratio_awags_rad_2019'
   - title: Radiometric Grid of Australia (Radmap) v4 2019 ratio uranium squared over thorium
   - description: The uranium squared over thorium grid is a derivative of the 2019 radiometric or gamma-ray grid of Australia. The radiometric, or gamma-ray spectrometric method, measures the natural variations in the gamma-rays detected near the Earth's surface as the result of the natural radioactive decay of potassium (K), uranium (U) and thorium (Th). The data are collected on airborne geophysical surveys conducted by Commonwealth, State and Northern Territory Governments and the private sector.The 2019 uranium squared over thorium was derived by seamlessly merging over 600 airborne gamma-ray spectrometric surveys. The final grid has a cell size of about 100m (0.001 degrees) and is derived from the filtered uranium and thorium grids.
- 'radmap2019_grid_u_conc_awags_rad_2019'
   - title: Radiometric Grid of Australia (Radmap) v4 2019 unfiltered ppm uranium
   - description: The unfiltered uranium grid is a derivative of the 2019 radiometric or gamma-ray grid of Australia which is a merge of over 600 individual gamma-ray spectrometric surveys. The radiometric, or gamma-ray spectrometric method, measures the natural variations in the gamma-rays detected near the Earth's surface as the result of the natural radioactive decay of potassium, uranium and thorium. The data are collected on airborne geophysical surveys conducted by Commonwealth, State and Northern Territory Governments and the private sector.The 2019 unfiltered uranium grid has a cell size of about 100m (0.001 degrees) and shows uranium element concentrations of the Australia region.
- 'radmap2019_grid_u_conc_filtered_awags_rad_2019'
   - title: Radiometric Grid of Australia (Radmap) v4 2019 filtered ppm uranium
   - description: The filtered uranium grid is a derivative of the 2019 radiometric or gamma-ray grid of Australia. The radiometric, or gamma-ray spectrometric method, measures the natural variations in the gamma-rays detected near the Earth's surface as the result of the natural radioactive decay of potassium (K), uranium (U) and thorium (Th). The data are collected on airborne geophysical surveys conducted by Commonwealth, State and Northern Territory Governments and the private sector.The 2019 filtered uranium grid was derived by seamlessly merging over 600 airborne gamma-ray spectrometric surveys. The final grid has a cell size of about 100m (0.001 degrees) and shows uranium element concentrations of the Australia region.
- 'radmap2019_grid_uk_ratio_awags_rad_2019'
   - title: Radiometric Grid of Australia (Radmap) v4 2019 ratio uranium over potassium
   - description: The uranium over potassium grid is a derivative of the 2019 radiometric or gamma-ray grid of Australia comprising over 600 airborne gamma-ray spectrometric surveys. The radiometric, or gamma-ray spectrometric method, measures the natural variations in the gamma-rays detected near the Earth's surface as the result of the natural radioactive decay of potassium (K), uranium (U) and thorium (Th). The data are collected on airborne geophysical surveys conducted by Commonwealth, State and Northern Territory Governments and the private sector.The 2019 uranium over potassium grid has a cell size of about 100 m (0.001 degrees) and is derived from the filtered uranium and potassium grids.
- 'radmap2019_grid_uth_ratio_awags_rad_2019'
   - title: Radiometric Grid of Australia (Radmap) v4 2019 ratio uranium over thorium
   - description: The uranium over thorium grid is a derivative of the 2019 radiometric or gamma-ray grid of Australia which is a merge of over 600 individual gamma-ray spectrometric surveys. The radiometric, or gamma-ray spectrometric method, measures the natural variations in the gamma-rays detected near the Earth's surface as the result of the natural radioactive decay of potassium (K), uranium (U) and thorium (Th). The data are collected on airborne geophysical surveys conducted by Commonwealth, State and Northern Territory Governments and the private sector.The 2019 uranium over thorium grid has a cell size of about 100 m (0.001 degrees) and is derived from the filtered uranium and thorium grids.


## Landscape Data SLGA

Description: The landscape attribute products available from the Soil and Landscape Grid of Australia (SLGA) were derived from DEM-S, the smoothed version of the national 1 second resolution Digital Elevation Model, which was derived from the 1 second resolution Shuttle Radar Topography Mission (SRTM) data acquired by NASA in February 2000.

Module name: getdata_landscape.py

Resolution: 3 arcsec

Updates: None

Source: https://www.clw.csiro.au/aclep/soilandlandscapegrid/ProductDetails.html"

License: Creative Commons Attribution 4.0 International (CC BY 4.0)

Attribution: CSIRO Australia, TERN (University of Queensland)

Bounding Box: (112.99958, -44.00042, 153.99958, -10.0004)

Layernames:

- 'Prescott_index'
   - key: '1'
   - title: Prescott Index
   - description: Prescott Index derived from 1 second DEM-S version 0.1
- 'net_radiation_jan'
   - key: '2'
   - title: Net Radiation [January]
   - description: None
- 'net_radiation_july'
   - key: '3'
   - title: Net Radiation [July]
   - description: None
- 'total_shortwave_sloping_surf_jan'
   - key: '4'
   - title: Total Shortwave Sloping Surf [January]
   - description: None
- 'total_shortwave_sloping_surf_july'
   - key: '5'
   - title: Total Shortwave Sloping Surf [July]
   - description: None
- 'Slope'
   - key: '6'
   - title: Slope [percent]
   - description: Percent slope (3” resolution) derived from 1 second DEM-S version 0.1
- 'Slope_median_300m'
   - key: '7'
   - title: Slope [percent] Median 300m Radius
   - description: Median of Percent slope at 300m radius (3” resolution) derived from 1 second DEM-S version 0.1
- 'Slope_relief_class'
   - key: '8'
   - title: Slope Relief Class
   - description: Slope relief (3” resolution) derived from 1 second DEM-S version 0.1
- 'Aspect'
   - key: '9'
   - title: Aspect
   - description: Aspect (3” resolution) derived from 1 second DEM-S version 0.1
- 'Relief_1000m'
   - key: '10'
   - title: Relief [1000m radius]
   - description: 1000 m elevation range (3” resolution) derived from 1 second DEM-S version 0.1
- 'Relief_300m'
   - key: '11'
   - title: Relief [300m radius]
   - description: 300 m elevation range (3” resolution) derived from 1 second DEM-S version 0.1
- 'Topographic_wetness_index'
   - key: '12'
   - title: Topographic Wetness Index
   - description: Topographic Wetness Index (3” resolution) derived from 1 second DEM-H version 1.0
- 'TPI_mask'
   - key: '13'
   - title: TPI Mask
   - description: None
- 'SRTM_TopographicPositionIndex'
   - key: '14'
   - title: SRTM_TopographicPositionIndex
   - description: Topographic position index (3” resolution) derived from 1 second DEM-S version 0.1
- 'Contributing_area'
   - key: '15'
   - title: Contributing Area [partial]
   - description: Contributing Area - Multiple Flow Direction (Partial), 3” resolution, derived from 1 second DEM-H version 1.0
- 'MrVBF'
   - key: '16'
   - title: MrVBF
   - description: Multi-resolution Valley Bottom Flatness (MrVBF) at 3 second resolution derived from 1 second DEM-S version 1.0
- 'Plan_curvature'
   - key: '17'
   - title: Plan Curvature
   - description: Plan curvature (3” resolution) derived from 1 second DEM-S version 0.1
- 'Profile_curvature'
   - key: '18'
   - title: Profile Curvature
   - description: Profile curvature (3”resolution) derived from 1 second DEM-S version 0.1