import folium
map = folium.Map(location= [80, -100],)

map.save("Map1.html")

map = folium.Map(location=[38.58,-99.09], zoom_start=6)
map.save("Map2.html")
map.location = [38.58,-99.09]
map.zoom = 6
map.save("Map3.html")