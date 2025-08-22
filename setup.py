#!/usr/bin/env python3
"""
Setup script for SMPS Hourly Auto Plot
"""

import shutil
from pathlib import Path

def setup_config():
    """Copy config template to config.py if it doesn't exist"""
    config_file = Path("config.py")
    template_file = Path("config.py.template")
    
    if not config_file.exists() and template_file.exists():
        shutil.copy2(template_file, config_file)
        print("✓ Created config.py from template")
        print("Please edit config.py to set your file paths and preferences")
    elif config_file.exists():
        print("✓ config.py already exists")
    else:
        print("✗ Error: config.py.template not found")
        return False
    
    return True

if __name__ == "__main__":
    print("Setting up SMPS Hourly Auto Plot...")
    if setup_config():
        print("\nSetup complete! You can now:")
        print("1. Edit config.py to set your file paths")
        print("2. Run the scripts: python hourly_autoplot.py")
    else:
        print("Setup failed!")
