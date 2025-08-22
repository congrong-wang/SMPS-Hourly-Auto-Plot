# SMPS Hourly Auto Plot

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

1. Modify `config.py` to set your file paths and date range
2. Run the scripts directly:
   - `python hourly_autoplot.py` - For continuous hourly plotting
   - `python plot_SMPS_weather.py` - For plotting specific date ranges
   - `python plot_daily.py` - For daily plots
