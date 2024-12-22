# TODO: עדיין ךא סיימתי את זה צריך לסדר את הפרטים הקטנים משהו עם הקובץ של הHTML שצריך לייצר

import pandas as pd
import folium
from folium.plugins import HeatMap
from sqlalchemy import create_engine

# Step 1: Connect to the database
engine = create_engine("sqlite:///terror_data.db")

# Step 2: Load data for the map
query = """
SELECT latitude, longitude, nkill
FROM terror_events
WHERE latitude IS NOT NULL AND longitude IS NOT NULL AND nkill > 0;
"""
data = pd.read_sql(query, engine)

# Step 3: Create a base map
map_center = [20.0, 0.0]  # Approximate center of the world
base_map = folium.Map(location=map_center, zoom_start=2, tiles='cartodbpositron')

# Step 4: Add a HeatMap layer
heat_data = data[['latitude', 'longitude', 'nkill']].values.tolist()
HeatMap(heat_data, radius=10, blur=15, max_zoom=12).add_to(base_map)

# Step 5: Save the map to an HTML file
output_path = 'static/maps/terror_heatmap.html'
base_map.save(output_path)

print(f"Map visualization created and saved to {output_path}.")
