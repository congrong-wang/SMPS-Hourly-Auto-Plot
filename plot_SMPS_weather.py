import time
import zoneinfo
import cr_asos.io
import cr_asos.plotting
from cr_smps import SMPSDataset
import cr_asos
import os
import datetime

from config import (
    WORK_DIR,
    WEATHER_CSV_DIR,
    SMPS_DATA_DIR,
    SMPS_WEATHER_PLOT_DIR,
    LOCAL_TIMEZONE,
    SMPS_DATA_TIMEZONE,
    START_DATE,
    END_DATE,
)


dt_smps = SMPSDataset.read_from_dir(SMPS_DATA_DIR, time_zone=SMPS_DATA_TIMEZONE)


def plot_SMPS_weather(date_range, use_1min=True, use_separate_precip=False):
    # Convert datetime objects to date objects and format strings
    start_date = date_range[0].date()
    end_date = date_range[1].date()

    # Format datetime objects to strings for API calls
    start_date_str = start_date.strftime("%Y-%m-%d")
    end_date_str = end_date.strftime("%Y-%m-%d")
    date_range_str = (start_date_str, end_date_str)

    # Download and read the weather data
    os.chdir(WEATHER_CSV_DIR)  # change to the weather data directory
    if use_1min:
        cr_asos.io.download_asos_1min_data(date_range_str)
        dt = cr_asos.io.read_asos_1min_csv(
            "PABI_ASOS_1min_" + start_date_str + "_" + end_date_str + ".csv"
        )
    else:
        cr_asos.io.download_asos_5min_data(date_range_str)
        dt = cr_asos.io.read_asos_5min_csv(
            "PABI_ASOS_5min_" + start_date_str + "_" + end_date_str + ".csv"
        )

    if use_separate_precip:
        cr_asos.io.download_asos_hourly_precip_data(date_range_str)
        dt_precip = cr_asos.io.read_asos_hourly_precip_csv(
            "PABI_ASOS_1h_precip_" + start_date_str + "_" + end_date_str + ".csv"
        )
    else:
        dt_precip = None
    os.chdir(WORK_DIR)  # change back to the working directory

    # loop through each date in the range
    current_date = start_date
    while current_date <= end_date:
        plot_date_str = current_date.strftime("%Y-%m-%d")

        cr_asos.plotting.daily_plot_w_SMPS(
            dt=dt,
            dt_smps=dt_smps,
            plot_date=plot_date_str,
            output_dir=SMPS_WEATHER_PLOT_DIR,
            SMPS_plotting_timezone=LOCAL_TIMEZONE,
            dt_precip=dt_precip,
        )

        current_date += datetime.timedelta(days=1)


if __name__ == "__main__":
    os.chdir(WORK_DIR)

    plot_SMPS_weather(
        # Use datetime objects from config
        (START_DATE, END_DATE),
        # You might need to MODIFY this, if you want to use 1/5 min weather
        #     data or to use/not use a separate precip
        use_1min=False,
        use_separate_precip=True,
    )
