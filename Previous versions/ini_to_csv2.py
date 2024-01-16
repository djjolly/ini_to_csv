import pandas as pd
import configparser

# Provide the file paths using double backslashes
input_file_path = "C:\\Users\\david.jolly\\dev\\ini_to_csv\\input.ini"
output_file_path = "C:\\Users\\david.jolly\\dev\\ini_to_csv\\result.csv"

config = configparser.ConfigParser()
config.read(input_file_path)

data = []
exclude_keys = ['Checksum', 'LastModified', 'TableIsocentric', 'TableColumnRotation', 
                'NominalScanDose-2-44', 'NominalScanDose-A1-2-44', 'Phantom', 'TriggerInterval', 'Version']  # Keys to be excluded

all_keys = set()

# Collect all unique keys across all sections
for section in config.sections():
    all_keys.update(key.lower() for key in config[section].keys())

for section in config.sections():
    section_data = {key: value for key, value in config[section].items()
                    if key.lower() not in [k.lower() for k in exclude_keys]}  # Case-insensitive exclusion

    # Ensure all keys are present in the section, filling with None if missing
    for key in all_keys:
        section_data.setdefault(key, None)

    section_data['Preset Name'] = section  # Add 'Preset Name' column with section name
    data.append(section_data)

# Rearrange columns to place 'Preset Name' as the first column
if data:
    columns = ['Preset Name'] + [col for col in data[0] if col != 'Preset Name']
    data = [{col: row.get(col) for col in columns} for row in data]

df = pd.DataFrame(data)

# Exclude the specified keys after constructing the DataFrame
df = df.drop(columns=[key.lower() for key in exclude_keys], errors='ignore')

print(df)

df.to_csv(output_file_path, index=False)  # Save the CSV file to the specified output_file_path

