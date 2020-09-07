import folium
import pandas

volcanoes_data = pandas.read_csv("volcanoes.csv")
map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles="Stamen Terrain")
html = "<h4>Volcano information:</h4>" \
       "<b>Name</b>: <i>%s</i><br/>" \
       "<b>Height</b>: <i>%s<i/> <b>m</b>"
fg = folium.FeatureGroup(name="My Map")
for (lat, lon, name, elevation) in zip(
        list(volcanoes_data["LAT"]),
        list(volcanoes_data["LON"]),
        list(volcanoes_data["NAME"]),
        list(volcanoes_data["ELEV"])
):
    coordinates = [lat, lon]
    iframe = folium.IFrame(html % (name, elevation), width=200, height=100)
    fg.add_child(folium.Marker(
        location=coordinates,
        popup= folium.Popup(iframe, parse_html=True),
        icon=folium.Icon(color="green"))
    )

map.add_child(fg)
map.save("Map1.html")
