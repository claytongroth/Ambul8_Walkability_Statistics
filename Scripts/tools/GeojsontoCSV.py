import json
import csv

with open('C:\MCD.json') as f:
    data = json.load(f)

for feature in data['features']:
    print feature['geometry']['type']
    print feature['geometry']['coordinates']
    with open('MCD.csv', 'a') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(feature['geometry']['coordinates'])
