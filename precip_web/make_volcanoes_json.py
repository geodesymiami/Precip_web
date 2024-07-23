#! /usr/bin/env python
# convert excel file to json
import os
import pandas as pd
import json

FILE_PATH = os.environ.get('PRECIP_HOME')
FILE_PATH += '/src/precip/Holocene_Volcanoes_precip_cfg..xlsx'
df = pd.read_excel(FILE_PATH, skiprows=1)

# Process the DataFrame to create a list of volcano dictionaries
volcanoes = []
for _, row in df.iterrows():
    volcano = {
        'id': row['Volcano Number'],
        'name': row['Volcano Name'],
        'country': row['Country'],
        'type': row['Primary Volcano Type'],
        'activity_evidence': row['Activity Evidence'],
        'last_known_eruption': row['Last Known Eruption'],
        'region': row['Region'],
        'subregion': row['Subregion'],
        'latitude': row['Latitude'],
        'longitude': row['Longitude'],
        'elevation': row['Elevation (m)'],
        'dominant_rock_type': row['Dominant Rock Type'],
        'tectonic_setting': row['Tectonic Setting'],
        'precip': row['Precip']
    }
    volcanoes.append(volcano)

print(df['Precip'].value_counts())

print('# of volcanoes:', len(volcanoes))
# remove volcanoes with precip != False
volcanoes = [volcano for volcano in volcanoes if volcano['precip'] != False]
print('# of volcanoes with precip:', len(volcanoes))
# Create the final JSON structure
volcano_data = {
    'volcanoes': volcanoes
}


print()
print(volcanoes[0])


# fix name if it has a comma
for volcano in volcanoes:
    name = volcano['name']
    if ',' in name:
        name = name.split(',')[::-1]
        name = [part.strip() for part in name]
        volcano['name'] = ' '.join(name)

# move the json file to the data directory
# Write the JSON data to a file
json_file = 'data/volcanoes.json'
with open(json_file, 'w') as json_file:
    json.dump(volcano_data, json_file, indent=4)

print(f'JSON file created: {json_file}')

