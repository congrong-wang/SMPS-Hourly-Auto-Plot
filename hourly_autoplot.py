import time
import zoneinfo
from cr_smps import SMPSDataset
import os
from datetime import datetime, timedelta

from plot_SMPS_weather import plot_SMPS_weather
from config import (
    WORK_DIR,
    SMPS_DATA_DIR,
    SMPS_PLOT_DIR,
    LOCAL_TIMEZONE,
    SMPS_DATA_TIMEZONE,
)


os.chdir(WORK_DIR)

while True:
    now = datetime.now(zoneinfo.ZoneInfo(LOCAL_TIMEZONE))
    print(f"Current time in {LOCAL_TIMEZONE}:", now.strftime("%Y-%m-%d"))
    today_str = now.strftime("%Y-%m-%d")
    today_datetime = datetime.combine(now.date(), datetime.min.time())

    ds = SMPSDataset.read_from_dir(SMPS_DATA_DIR, time_zone=SMPS_DATA_TIMEZONE)
    ds.plot_heatmap(
        time_range=today_str,
        output_dir=SMPS_PLOT_DIR,
        output_time_zone=LOCAL_TIMEZONE,
    )
    # Plot SMPS w PABI weather
    # You might need to MODIFY this, if you want to use 1/5 min weather
    #     data or to use/not use a separate precip
    plot_SMPS_weather(
        (today_datetime, today_datetime),
        use_1min=False,
        use_separate_precip=True,
    )

    print(f"Plotted heatmap for {today_str}")

    # if it's just over midnight, also plot the previous day
    if now.hour < 3:
        yesterday = (now - timedelta(days=1)).strftime("%Y-%m-%d")
        ds.plot_heatmap(
            time_range=yesterday,
            output_dir=SMPS_PLOT_DIR,
            output_time_zone=LOCAL_TIMEZONE,
        )
        print(f"Also plotted heatmap for previous day: {yesterday}")

    print("Waiting for another hour...")

    seconds_until_next_hour = (
        3600 - (now.minute * 60 + now.second) + 360
    )  # plus 6 minutes' delay, I don't want to run it on the hour
    time.sleep(seconds_until_next_hour)
