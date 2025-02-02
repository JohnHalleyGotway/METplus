"""
Grid-Stat and MODE: Sea Ice Validation   
====================================================================================================

model_applications/marine_and_cryosphere/GridStat_MODE_fcstIMS
_obsNCEP_sea_ice.conf

"""
####################################################################################################
# Scientific Objective
# --------------------
#
# Run Grid-Stat and MODE to compare the National Ice Center (NIC) Interactive Multisensor Snow
# and Ice Mapping System (IMS) and the National Centers for Environmental Prediction (NCEP)
# sea ice analysis.  This is a validation and diagnostics use case because it is limited to a
# comparison between IMS analysis to NCEP analysis.

####################################################################################################
# Datasets
# --------
#
# Both IMS and NCEP sea ice analyses are observation datasets. For the purposes
# of MET, IMS is referred to as "forecast" and NCEP is referred to as "observation".
#
#  * Forecast dataset: IMS Sea Ice Concentration
#      - Variable of interest: ICEC; ICEC is a binary field where "1" means a sea ice concentration of >=0.40 and "0" means a sea ice concentration of <0.40.
#      - Level: Z0 (surface)
#      - Dates: 20190201 - 20190228
#      - Valid time: 22 UTC
#      - Format: Grib2
#      - Projection: 4-km Polar Stereographic
#
#  * Observation dataset: NCEP Sea Ice Concentration
#      - Variable of interest: ICEC; ICEC is the sea ice concentration with values from 0.0 - 1.0. Values >1.0 && <=1.28 indicate flagged data to be included and should be set to ==1.0 when running MET. Values >1.28 should be ignored as that indicates an invalid observation.
#      - Level: Z0 (surface)
#      - Dates: 20190201 - 20190228
#      - Valid time: 00 UTC
#      - Format: Grib2
#      - Projection: 12.7-km Polar Stereographic
#    
#  * Data source: Received from Robert Grumbine at EMC. IMS data is originally from the NIC. NCEP data is originally from NCEP.
#  
#  * Location: IMS: https://www.natice.noaa.gov/ims/index.html; IMS - (https://polar.ncep.noaa.gov/seaice/Analyses.shtml) 

###################################################################################################
# METplus Components
# ------------------
#
# This use case runs the MET GridStat and MODE tools.

###################################################################################################
# METplus Workflow
# ----------------
# 
# The workflow processes the data by valid time, meaning that each tool will be run for each time 
# before moving onto the next valid time. The GridStat tool is called first followed by the MODE
# tool. It processes analysis times from 2019-02-01 to 2019-02-05. The valid times for each analysis
# are different from one another (please see `Datasets`_ section for more information).

###################################################################################################
# METplus Configuration
# ---------------------
# 
# METplus first loads all of the configuration files found in parm/metplus_config. Then, it loads
# any configuration files passed to METplus by the command line with the -c option.
#
# .. highlight:: bash
# .. literalinclude:: ../../../../parm/use_cases/model_applications/marine_and_cryosphere/GridStat_MODE_fcstIMS_obsNCEP_sea_ice.conf
#

###################################################################################################
# MET Configuration
# -----------------
#
# METplus sets environment variables based on user settings in the METplus configuration file. 
# See :ref:`How METplus controls MET config file settings<metplus-control-met>` for more details. 
#
# **YOU SHOULD NOT SET ANY OF THESE ENVIRONMENT VARIABLES YOURSELF! THEY WILL BE OVERWRITTEN BY METPLUS WHEN IT CALLS THE MET TOOLS!**
#
# If there is a setting in the MET configuration file that is currently not supported by METplus you'd like to control, please refer to:
# :ref:`Overriding Unsupported MET config file settings<met-config-overrides>`
#
# **GridStatConfig_wrapped**
#
# .. note:: See the :ref:`GridStat MET Configuration<grid-stat-met-conf>` section of the User's Guide for more information on the environment variables used in the file below:
#
# .. highlight:: bash
# .. literalinclude:: ../../../../parm/met_config/GridStatConfig_wrapped
#
# **MODEConfig_wrapped**
#
# .. note:: See the :ref:`MODE MET Configuration<mode-met-conf>` section of the User's Guide for more information on the environment variables used in the file below:
#
# .. highlight:: bash
# .. literalinclude:: ../../../../parm/met_config/MODEConfig_wrapped

###################################################################################################
# Running METplus
# ---------------
#
# This use case can be run two ways:
#
# 1) Passing in GridStat_MODE_fcstIMS_obsNCEP_sea_ice.conf then a user-specific system configuration file::
#       
#        run_metplus.py -c /path/to/METplus/parm/use_cases/model_applications/marine_and_cryosphere/GridStat_MODE_fcstIMS_obsNCEP_sea_ice.conf -c /path/to/user_system.conf
#
# 2) Modifying the configurations in parm/metplus_config, then passing in GridStat_MODE_fcstIMS_obsNCEP_sea_ice.conf::
#
#        run_metplus.py -c /path/to/METplus/parm/use_cases/model_applications/marine_and_cryosphere/GridStat_MODE_fcstIMS_obsNCEP_sea_ice.conf
#
# The former method is recommended. Whether you add them to a user-specific configuration file or modify the metplus_config files, the following variables must be set correctly:
#
# * **INPUT_BASE** - Path to directory where sample data tarballs are unpacked (See Datasets section to obtain tarballs).
# * **OUTPUT_BASE** - Path where METplus output will be written. This must be in a location where you have write permissions
# * **MET_INSTALL_DIR** - PAth to location where MET is installed locally
#
# Example User Configuration File::
#
#   [dir]
#   INPUT_BASE = /path/to/sample/input/data
#   OUTPUT_BASE = /path/to/output/dir
#   MET_INSTALL_DIR = /path/to/met-X.Y
#
# **NOTE** All of these items must be found under the [dir] section.
#

####################################################################################################
# Expected Output
# ---------------
#
# A successful run of this use case will output the following to the screen and logfile::
#  
#    INFO: METplus has successfully finished running.
#
# A successful run will have the following output files in the location defined by {OUTPUT_BASE}, which
# is located in the metplus_system.conf configuration file located in /path/to/METplus/parm/metplus_config.
# This list of files should be found for every time run through METplus. 
# GridStat output will be in model_applications/marine_and_cryosphere/sea_ice/GridStat relative to the {OUTPUT_BASE}.
# MODE output will be in model_applications/marine_and_cryosphere/sea_ice/MODE relative to the {OUTPUT_BASE}.
# Using the output for 20190201 as an example:
#
# **GridStat output**:
#
# * grid_stat_IMS_ICEC_vs_NCEP_ICEC_Z0_000000L_20190201_220000V_pairs.nc
# * grid_stat_IMS_ICEC_vs_NCEP_ICEC_Z0_000000L_20190201_220000V.stat
#
# **MODE output**:
#
# * mode_IMS_ICEC_vs_NCEP_ICEC_000000L_20190201_220000V_000000A_R1_T1_cts.txt
# * mode_IMS_ICEC_vs_NCEP_ICEC_000000L_20190201_220000V_000000A_R1_T1_obj.nc
# * mode_IMS_ICEC_vs_NCEP_ICEC_000000L_20190201_220000V_000000A_R1_T1_obj.txt
# * mode_IMS_ICEC_vs_NCEP_ICEC_000000L_20190201_220000V_000000A_R1_T1.ps
# * mode_IMS_ICEC_vs_NCEP_ICEC_000000L_20190201_220000V_000000A_R2_T1_cts.txt
# * mode_IMS_ICEC_vs_NCEP_ICEC_000000L_20190201_220000V_000000A_R2_T1_obj.nc 
# * mode_IMS_ICEC_vs_NCEP_ICEC_000000L_20190201_220000V_000000A_R2_T1_obj.txt
# * mode_IMS_ICEC_vs_NCEP_ICEC_000000L_20190201_220000V_000000A_R2_T1.ps
# * mode_IMS_ICEC_vs_NCEP_ICEC_000000L_20190201_220000V_000000A_R3_T1_cts.txt
# * mode_IMS_ICEC_vs_NCEP_ICEC_000000L_20190201_220000V_000000A_R3_T1_obj.nc
# * mode_IMS_ICEC_vs_NCEP_ICEC_000000L_20190201_220000V_000000A_R3_T1_obj.txt
# * mode_IMS_ICEC_vs_NCEP_ICEC_000000L_20190201_220000V_000000A_R3_T1.ps
# * mode_IMS_ICEC_vs_NCEP_ICEC_000000L_20190201_220000V_000000A_R4_T1_cts.txt
# * mode_IMS_ICEC_vs_NCEP_ICEC_000000L_20190201_220000V_000000A_R4_T1_obj.nc
# * mode_IMS_ICEC_vs_NCEP_ICEC_000000L_20190201_220000V_000000A_R4_T1_obj.txt
# * mode_IMS_ICEC_vs_NCEP_ICEC_000000L_20190201_220000V_000000A_R4_T1.ps
# * mode_IMS_ICEC_vs_NCEP_ICEC_000000L_20190201_220000V_000000A_R5_T1_cts.txt
# * mode_IMS_ICEC_vs_NCEP_ICEC_000000L_20190201_220000V_000000A_R5_T1_obj.nc
# * mode_IMS_ICEC_vs_NCEP_ICEC_000000L_20190201_220000V_000000A_R5_T1_obj.txt
# * mode_IMS_ICEC_vs_NCEP_ICEC_000000L_20190201_220000V_000000A_R5_T1.ps 
#

###################################################################################################
# Keywords
# --------
#
#
# .. note::
#
#   * GridStatToolUseCase
#   * MODEToolUseCase
#   * MarineAndCryosphereAppUseCase
#   * ValidationUseCase
#   * S2SAppUseCase
#   * NOAAEMCOrgUseCase
#   * DiagnosticsUseCase
#
#   Navigate to the :ref:`quick-search` page to discover other similar use cases.
#
#
#
# sphinx_gallery_thumbnail_path = '_static/marine_and_cryosphere_GridStat_MODE_fcstIMS_obsNCEP_Sea_Ice.png'
