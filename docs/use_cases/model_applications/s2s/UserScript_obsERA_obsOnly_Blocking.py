"""
Blocking Calculation: ERA RegridDataPlane, PcpCombine, and Blocking python code
================================================================================

model_applications/
s2s/
UserScript_obsERA_obsOnly_Blocking.py

"""

##############################################################################
# Scientific Objective
# --------------------
#
# To compute the frequency of blocking using the Pelly-Hoskins method.  Specifically
# the blocking calculation consits of computing the Central Blocking Latitude (CBL), 
# Instantaneousy blocked latitudes (IBL), Group Instantaneousy blocked latitudes (GIBL), 
# and the frequency of atmospheric blocking.  The CBL calculation had an option to use an 
# observed climatology.
#
# The following reference contains the specific equations and methodology used to compute 
# blocking:
#

##############################################################################
# Datasets
# --------
#
#  * Forecast dataset: None 
#  * Observation dataset: ERA Reanlaysis 500 mb height.

##############################################################################
# External Dependencies
# ---------------------
#
# You will need to use a version of Python 3.6+ that has the following packages installed::
#
# * numpy
# * netCDF4
# * datetime
# * bisect
# * scipy
#
# If the version of Python used to compile MET did not have these libraries at the time of compilation, you will need to add these packages or create a new Python environment with these packages.
#
# If this is the case, you will need to set the MET_PYTHON_EXE environment variable to the path of the version of Python you want to use. If you want this version of Python to only apply to this use case, set it in the [user_env_vars] section of a METplus configuration file.:
#
#    [user_env_vars]
#    MET_PYTHON_EXE = /path/to/python/with/required/packages/bin/python
#

##############################################################################
# METplus Components
# ------------------
#
# This use case runs the blocking driver script which runs the steps the user
# lists in STEPS_OBS.  The possible steps are regridding, time averaging, computing a 
# running mean, computing anomalies, computing CBLs (CBL), plotting CBLs (PLOTCBL), 
# computing IBLs (IBL), plotting IBL frequency (PLOTIBL), computing GIBLs (GIBL), 
# computing blocks (CALCBLOCKS), and plotting the blocking frequency (PLOTBLOCKS).  
# Regridding, time averaging, running means, and anomaloies are set up in the UserScript 
# .conf file and are formatted as follows:
# PROCESS_LIST = RegridDataPlane(regrid_obs), PcpCombine(daily_mean_obs), PcpCombine(running_mean_obs), PcpCombine(anomaly_obs), UserScript(script_blocking)
#
# The other steps are listed in the Blocking .conf file and are formatted as follows:
# OBS_STEPS = CBL+PLOTCBL+IBL+PLOTIBL+GIBL+CALCBLOCKS+PLOTBLOCKS 
#

##############################################################################
# METplus Workflow
# ----------------
#
# The blocking python code is run for each time for the forecast and observations 
# data. This example loops by valid time.  This version is set to only process the blocking
# steps (CBL, PLOTCBL, IBL, PLOTIBL, GIBL, CALCBLOCKS, PLOTBLOCKS), omitting the regridding, 
# time averaging, running mean, and anomaly pre-processing steps.  However, the configurations 
# for pre-processing are available for user reference.
#

##############################################################################
# METplus Configuration
# ---------------------
#
# METplus first loads all of the configuration files found in parm/metplus_config,
# then it loads any configuration files passed to METplus via the command line
# i.e. parm/use_cases/model_applications/s2s/UserScript_obsERA_obsOnly_Blocking.py.  
# The file UserScript_obsERA_obsOnly_Blocking.conf runs the python program, and the 
# variables for all steps of the Blocking use case are set in the [user_env_vars] 
# section.
#
# .. highlight:: bash
# .. literalinclude:: ../../../../parm/use_cases/model_applications/s2s/UserScript_obsERA_obsOnly_Blocking.conf
#

##############################################################################
# MET Configuration
# ---------------------
#
# METplus sets environment variables based on the values in the METplus configuration file.
# These variables are referenced in the MET configuration file. **YOU SHOULD NOT SET ANY OF THESE ENVIRONMENT VARIABLES YOURSELF! THEY WILL BE OVERWRITTEN BY METPLUS WHEN IT CALLS THE MET TOOLS!** If there is a setting in the MET configuration file that is not controlled by an environment variable, you can add additional environment variables to be set only within the METplus environment using the [user_env_vars] section of the METplus configuration files. See the 'User Defined Config' section on the 'System Configuration' page of the METplus User's Guide for more information.
#
# See the following files for more information about the environment variables set in this configuration file.
#
# parm/use_cases/met_tool_wrapper/RegridDataPlane/RegridDataPlane.py
# parm/use_cases/met_tool_wrapper/PCPCombine/PCPCombine_derive.py
# parm/use_cases/met_tool_wrapper/PCPCombine/PCPCombine_subtract.py

##############################################################################
# Python Scripts
# ----------------
#
# This use case uses Python scripts to perform the blocking calculation
#
# parm/use_cases/model_applications/s2s/UserScript_obsERA_obsOnly_Blocking/Blocking_driver.py:
# This script calls the requested steps in the blocking analysis for a forecast, observation, or both.
#
# metcalcpy/contributed/blocking_weather_regime/Blocking.py:
# This script runs the requested steps, containing the code for computing CBLs, computing IBLs, computing GIBLs,
# and computing blocks.  See the METcalcpy `Blocking Calculation Script <https://github.com/dtcenter/METcalcpy/blob/develop/metcalcpy/contributed/blocking_weather_regime/Blocking.py>`_ for more information.
#
# metcalcpy/contributed/blocking_weather_regime/Blocking_WeatherRegime_util.py:
# This script contains functions used by both the blocking anwd weather regime analysis, including the code for 
# determining which steps the user wants to run, and finding and reading the input files in the format from the output
# pre-processing steps.  See the METcalcpy `Utility script <https://github.com/dtcenter/METcalcpy/blob/develop/metcalcpy/contributed/blocking_weather_regime/Blocking_WeatherRegime_util.py>`_ for more information.
#
# .. highlight:: python
# .. literalinclude:: ../../../../parm/use_cases/model_applications/s2s/UserScript_obsERA_obsOnly_Blocking/Blocking_driver.py
#

##############################################################################
# Running METplus
# ---------------
#
# This use case is run in the following ways:
#
# 1) Passing in UserScript_obsERA_obsOnly_Blocking.py then a user-specific system configuration file::
#
#        run_metplus.py -c /path/to/METplus/parm/use_cases/model_applications/s2s/UserScript_obsERA_obsOnly_Blocking.py -c /path/to/user_system.conf
#
# 2) Modifying the configurations in parm/metplus_config, then passing in UserScript_obsERA_obsOnly_Blocking.py::
#
#        run_metplus.py -c /path/to/METplus/parm/use_cases/model_applications/s2s/UserScript_obsERA_obsOnly_Blocking.py
#
# The following variables must be set correctly:
#
# * **INPUT_BASE** - Path to directory where sample data tarballs are unpacked (See Datasets section to obtain tarballs). This is not required to run METplus, but it is required to run the examples in parm/use_cases
# * **OUTPUT_BASE** - Path where METplus output will be written. This must be in a location where you have write permissions
# * **MET_INSTALL_DIR** - Path to location where MET is installed locally
#
# Example User Configuration File::
#
#   [dir]
#   INPUT_BASE = /path/to/sample/input/data
#   OUTPUT_BASE = /path/to/output/dir
#   MET_INSTALL_DIR = /path/to/met-X.Y 
#

##############################################################################
# Expected Output
# ---------------
#
# Refer to the value set for **OUTPUT_BASE** to find where the output data was generated. Output for this use 
# case will be found in model_applications/s2s/Blocking (relative to **OUTPUT_BASE**) and will contain output 
# for the steps requested.  This may include the regridded data, daily averaged files, running mean files, 
# and anomaly files.  In addition, output CBL, IBL, and Blocking frequency plots can be generated.  The location
# of these output plots can be specified as BLOCKING_PLOT_OUTPUT_DIR.  If it is not specified, plots will be sent 
# to OUTPUT_BASE/plots.  MET format matched pair output will also be generated for IBLs and blocks if a user runs 
# these steps on both the model and observation data.  The location the matched pair output can be specified as 
# BLOCKING_MPR_OUTPUT_DIR.  If it is not specified, plots will be sent to OUTPUT_BASE/mpr.
#

##############################################################################
# Keywords
# --------
#
# .. note::
#
#   * RegridDataPlaneUseCase
#   * PCPCombineUseCase
#   * S2SAppUseCase
#   * NetCDFFileUseCase
#   * GRIB2FileUseCase
#
#   Navigate to the :ref:`quick-search` page to discover other similar use cases.
#
#
#
# sphinx_gallery_thumbnail_path = '_static/s2s-OBS_ERA_blocking_frequency.png'
#
