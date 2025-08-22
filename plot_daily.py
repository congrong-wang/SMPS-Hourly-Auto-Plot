from cr_smps import SMPSDataset
import os
from datetime import datetime, timedelta
from config import (
    WORK_DIR,
    SMPS_DATA_DIR,
    SMPS_PLOT_DIR,
    LOCAL_TIMEZONE,
    SMPS_DATA_TIMEZONE,
    START_DATE,
    END_DATE,
)

os.chdir(WORK_DIR)

ds = SMPSDataset.read_from_dir(SMPS_DATA_DIR, time_zone=SMPS_DATA_TIMEZONE)

current_date = START_DATE
while current_date <= END_DATE:
    date_str = current_date.strftime("%Y-%m-%d")
    ds.plot_heatmap(
        time_range=date_str,
        output_dir=SMPS_PLOT_DIR,
        output_time_zone=LOCAL_TIMEZONE,
    )
    current_date += timedelta(days=1)
