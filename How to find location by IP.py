import geocoder, folium
g =geocoder.ip('150.109.244.5')
my_add = g.latlng
my_map = folium.Map(location=my_add,zoom_street=12)
my_map.save("loc.html")
