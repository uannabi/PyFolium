import folium 

m = folium.Map(location=[23.796191088646523, 90.40880567259967], tiles="Stamen Toner", zoom_start=13)

folium.Circle(
    radius=5,
    location=[45.5244, -122.6699],
    popup="The Waterfront",
    color="crimson",
    fill=False,
).add_to(m)

folium.CircleMarker(
    location=[23.781394234534165, 90.41642152993026],
    radius=10,
    popup="Laurelhurst Park",
    color="#3186cc",
    fill=True,
    fill_color="#3186cc",
).add_to(m)

m.save("index.html")