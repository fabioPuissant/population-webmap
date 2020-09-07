import folium
import pandas

vulcanos_data = pandas.read_csv("volcanoes.csv")
# Clean Data
vulcanos_data = vulcanos_data.drop(0)

map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles="Stamen Terrain")
# print(vulcanos_data)
html = "<h4>Volcano information:</h4>" \
       "<b>Name</b>: <i>%s</i><br/>" \
       "<b>Height</b>: <i>%s<i/> <b>m</b>"
fg = folium.FeatureGroup(name="My Map")
for vulcano in vulcanos_data.itertuples():
    iframe = folium.IFrame(html % (vulcano.NAME, vulcano.ELV), width=200, height=100)
    coordinates = [vulcano.LAT, vulcano.LON]
    fg.add_child(folium.Marker(
        location=coordinates,
        popup=folium.Popup(iframe, parse_html=True),
        icon=folium.Icon(color="green"))
    )
map.add_child(fg)
map.save("Map1-alt.html")

