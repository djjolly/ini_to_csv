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
df = pd.DataFrame.from_dict({section: {k: v for k, v in config[section].items() if k.lower() not in exclude_keys_lower} for section in config.sections()}, orient='index')

# Fill missing values with zeros and ensure numeric for angle columns
angle_columns = ['startacqangle', 'stopacqangle']
df[angle_columns] = df[angle_columns].fillna(0).astype(float)

# Add 'arclength' column
df['arclength'] = df[angle_columns].abs().sum(axis=1)

# Reset index and reorder columns
df = df.rename_axis('Preset Name').reset_index()
df = df[sorted(df.columns)].sort_values('Preset Name')

# Save to CSV
df.to_csv(output_file_path, index=False)

print(df)











