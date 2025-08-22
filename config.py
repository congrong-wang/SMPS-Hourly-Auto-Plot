from datetime import datetime
from pathlib import Path


# MODIFY THESE, according to your file locations
WORK_DIR = Path("/home/wcr/Desktop/cr_smps")
WEATHER_CSV_DIR = WORK_DIR / "weather_data"  # Place of downloaded weather data
SMPS_DATA_DIR = WORK_DIR / "SMPS_data"  # Place of your SMPS data
SMPS_PLOT_DIR = WORK_DIR / "plots"  # Place to save SMPS plots (w/o weather)
SMPS_WEATHER_PLOT_DIR = WORK_DIR / "plots"  # Place to save SMPS plots (w/ weather)


LOCAL_TIMEZONE = "America/Anchorage"  # Modify this if needed
SMPS_DATA_TIMEZONE = "UTC"  # Modify this if your SMPS data is in a different timezone


# MODIFY THESE, according to the time you want to plot
START_DATE = datetime(2025, 8, 10)
END_DATE = datetime(2025, 8, 12)
