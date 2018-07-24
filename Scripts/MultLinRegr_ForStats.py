#edge_density_km , street_density_km, node_density_km, n, intersection_density_km
import osmnx as ox
import networkx as nx
import pandas as pd
import csv
from sklearn import linear_model
import statsmodels.api as sm

colnames = ['0','WS','lat', 'lon']
df1 = pd.read_csv('C:\MCDWSF.csv', index_col = None, usecols=['WS','lat','lon'])
df1 = df1.apply(pd.to_numeric, errors='coerce')
df1 = df1.dropna(thresh=2)
df1s = df_elements = df1.sample(n=50)
print df1s
counter = 0

df2header = ('lat', 'lon', 'WS', 'edge_density_km', 'street_density_km', 'node_density_km', 'n', 'intersection_density_km' )
statslist = []

for i, row in df1s.iterrows():
    counter += 1
    WS = row['WS']
    lat = row['lat']
    lon = row['lon']
    point = (lat,lon)
    try:
        G = ox.core.graph_from_point(point, distance = 500, network_type='walk')
        stats = ox.basic_stats(G, area=500)
        rowtowrite = (lat, lon, WS, stats['edge_density_km'], stats['street_density_km'], stats['node_density_km'], stats['n'], stats['intersection_density_km'] )
        #print rowtowrite
        statslist.append(rowtowrite)
        print counter
    except:
        print "exception"

df2 = pd.DataFrame(statslist)
df2.columns = df2header
for i in df2header:
    df1 = pd.DataFrame(data= df2, columns=[i])
    target = pd.DataFrame(data= df2, columns=["WS"])
    X = df1
    y = target['WS']
    lm = linear_model.LinearRegression()
    model = lm.fit(X,y)
    RSqrtScore = lm.score(X,y) #gives Rsquared value
    print i, "has an Rsqt of",  RSqrtScore, "with WS"
