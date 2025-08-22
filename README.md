Author: Congrong Wang (me@congrong.wang)

## Setup

### Python version

\>= 3.11

If multiple versions *have to* be installed on a same PC, I personally recommend using [pyenv-win](https://github.com/pyenv-win/pyenv-win?tab=readme-ov-file) to manage different Python versions.

### Installation

1. Clone the repository:
```bash
git clone https://github.com/congrong-wang/SMPS-Hourly-Auto-Plot.git
cd SMPS-Hourly-Auto-Plot
```

2. Install dependencies:
```bash
pip install -e .
```

## Usage

1. Modify `config.py` to set your file paths and date range. Normally, file paths and time zones only need to be set once, but date range need to be adjusted each time.

2. Run the scripts directly:
   - `python hourly_autoplot.py` - For continuous hourly plotting
   - `python plot_daily.py` - To plot SMPS heat map
   
   ![](docs/heatmap_2025-08-11.png)
   
   - `python plot_SMPS_weather.py` - To plot SMPS heat map with weather
   
   ![](/docs/PABI_daily_w_SMPS_2025-08-11.png)
