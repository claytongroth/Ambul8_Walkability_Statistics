import osmnx as ox
import networkx as nx
import re
import requests
import pandas as pd
import csv
import matplotlib.cm as cm
import matplotlib.colors as colors
#ox.config(log_file=True, log_console=True, use_cache=True)

#point1 = (55.348905, -131.67241)
#G = ox.core.graph_from_point(point1, distance = 500, network_type='walk')
#ox.plot_graph(G)

colnames = ['0','WS','lat', 'lon']
df1 = pd.read_csv('C:\MCDWSF.csv', index_col = None, usecols=['WS','lat','lon'])
df1 = df1.apply(pd.to_numeric, errors='coerce')
df1 = df1.dropna(thresh=2)
df1s = df_elements = df1.sample(n=1000)

counter = 0
with open('lbasicStatsAll5.csv', 'wb') as f:
    writer = csv.writer(f)
    header = ('lat', 'lon', 'WS','street_density_km','node_density_km',  'street_segments_count')
    writer.writerow(header)
    while True:
        try:
            for i, row in df1s.iterrows():
                counter += 1
                WS = row['WS']
                lat = row['lat']
                lon = row['lon']
                point = (lat,lon)
                G = ox.core.graph_from_point(point, distance = 500, network_type='walk')
                print "basic stats working", counter
                stats = ox.basic_stats(G, area=500)
                print "writing row", counter
                rowtowrite = ('lat', 'lon', 'WS',row['street_density_km'],row['node_density_km'],  row['street_segments_count'])
                writer.writerow(rowtowrite)
                print "row",counter, "written"
        except:
            pass
#add  stats['street_segments_count']
