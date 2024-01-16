# INI to CSV Converter

This Python script, written by David Jolly and finalized on 17/1/24, converts a configuration INI file (used in the config for Elekta iView) into CSV format.

## Usage

- Edit the `input.ini` file with your configuration data.
- Run the script: `python ini_to_csv.py`
- The resulting CSV file (`result.csv`) will be generated in the specified directory.

## Configuration

Customize the script by modifying the `exclude_keys` list in `ini_to_csv.py` to exclude specific keys from the CSV.

## Features

- Automatically calculates the CBCT arc length.

## Requirements

- Python 3.x
- pandas

