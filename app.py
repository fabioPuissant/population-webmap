import folium
import pandas


def color_producer(elv):
    return 'red' if elv >= 3000 else 'orange' if elv >= 1000 else 'green'


volcanoes_data = pandas.read_csv("volcanoes.csv")
display_map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles="Stamen Terrain")
html = "<h4>Volcano information:</h4>" \
       "<b>Location</b>: <i>%s</i><br/>" \
       "<b>Height</b>: <i>%s<i/> <b>m</b>"

# Making the volcanoes display layer on the world map!
fg_volcanoes = folium.FeatureGroup(name="Volcanoes")
for (lat, lon, name, elevation) in zip(
        list(volcanoes_data["LAT"]),
        list(volcanoes_data["LON"]),
        list(volcanoes_data["NAME"]),
        list(volcanoes_data["ELEV"])
):
    iframe = folium.IFrame(html % (name, elevation), width=200, height=100)
    fg_volcanoes.add_child(
        folium.CircleMarker(
            location=(lat, lon),
            popup=folium.Popup(iframe, parse_html=True),
            radius=8,
            fill_color=color_producer(elevation),
            color="grey",
            fill_opacity=0.7
        )
    )

# Adding population Layer to the world map
fg_population = folium.FeatureGroup(name="Population")

fg_population.add_child(
    folium.GeoJson(
        data=open("world.json", "r", encoding="utf-8-sig").read(),
        style_function=lambda x: {'fillColor':
                                      'green' if x['properties']['POP2005'] < 10000000
                                      else
                                      'orange' if x['properties']['POP2005'] < 20000000
                                      else 'red'}
    )
)

#Important to first add a feature group before adding Layer control!!
display_map.add_child(fg_volcanoes)
display_map.add_child(fg_population)
display_map.add_child(folium.LayerControl()) #Now the layer control will be added to the map

display_map.save("Map1.html")
