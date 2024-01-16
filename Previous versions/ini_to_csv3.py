import pandas as pd
import configparser

# Provide the file paths using double backslashes
input_file_path = "C:\\Users\\david.jolly\\dev\\ini_to_csv\\input.ini"
output_file_path = "C:\\Users\\david.jolly\\dev\\ini_to_csv\\result.csv"

config = configparser.ConfigParser()
config.read(input_file_path)

exclude_keys = {'Checksum', 'LastModified', 'TableIsocentric', 'TableColumnRotation', 
                'NominalScanDose-2-44', 'NominalScanDose-A1-2-44', 'Phantom', 'TriggerInterval', 'Version'}  # Keys to be excluded

# Convert exclude_keys to lowercase
exclude_keys_lower = {key.lower() for key in exclude_keys}

# Create a DataFrame from the entire configuration
df = pd.DataFrame.from_dict({section: dict(config[section]) for section in config.sections()}, orient='index')

# Add 'Preset Name' column with section names
df['Preset Name'] = df.index

# Reorder columns
df = df[['Preset Name'] + sorted(df.columns[:-1])]

# Exclude specified keys
df = df.drop(columns=[key for key in df.columns if key.lower() in exclude_keys_lower], errors='ignore')

print(df)

df.to_csv(output_file_path, index=False)




