import folium
import pandas

vulcanos_data = pandas.read_csv("volcanoes.csv")
# Clean Data
vulcanos_data = vulcanos_data.drop(0)

map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles="Stamen Terrain")
# print(vulcanos_data)

fg = folium.FeatureGroup(name="My Map")
for vulcano in vulcanos_data.itertuples():
    coordinates = [vulcano.LAT, vulcano.LON]
    fg.add_child(folium.Marker(
        location=coordinates,
        popup="%s %s" % (vulcano.ELEV, vulcano.NAME),
        icon=folium.Icon(color="green"))
    )
map.add_child(fg)
map.save("Map1-alt.html")

