import pandas as pd
import numpy as np
import folium
from folium.plugins import HeatMap

df_dataset = pd.read_csv("dataset.csv")
df_dataset = df_dataset.head(10000)
df = pd.read_csv("teste.csv")
df = df.head(10000)
df_final = pd.merge(df_dataset,df, right_on="Country/Region", left_on="Country", how="right")

m = folium.Map(tiles = 'Stamen Terrain',min_zoom = 1.5)
display(m)

url = 'https://raw.githubusercontent.com/python-visualization/folium/master/examples/data'
country_shapes = f'{url}/world-countries.json'
folium.Choropleth(
    geo_data = country_shapes,
    min_zoom=2,
    name='Covid-19',
    data=df_final,
    columns=['Country/Region', 'Confirmed'],
    key_on='feature.properties.name',
    fill_color='OrRd',
    nan_fill_color='green',
    legend_name = 'Total Confirmed COVID cases',
).add_to(m)
m

def plotDot(point):
    folium.CircleMarker(location = (point.Lat, point.Long),
                       radius = 6,
                       weight = 4,
                       popup = [point.Country, point.Confirmed, point.Recovered],
                       fill_color = '#000000').add_to(m)
df_final.apply(plotDot, axis = 1)
m.fit_bounds(m.get_bounds())
m