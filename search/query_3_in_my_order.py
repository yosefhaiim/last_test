# TODO:  יש בעיה עם קווי אורך ורוחב לעבור על זה ולבדר

import pandas as pd
from sqlalchemy import create_engine
import folium
from folium.plugins import MarkerCluster

# יצירת חיבור למסד נתונים
engine = create_engine("sqlite:///terror_data.db")

# שאילתת SQL
query = """
WITH yearly_attack_counts AS (
    SELECT iyear, country_txt, COUNT(*) AS attack_count
    FROM terror_events
    GROUP BY iyear, country_txt
)
SELECT 
    current.country_txt,
    current.iyear AS year,
    current.attack_count AS current_count,
    previous.attack_count AS previous_count,
    CASE 
        WHEN previous.attack_count = 0 THEN NULL
        ELSE (current.attack_count - previous.attack_count) * 100.0 / previous.attack_count
    END AS percentage_change
FROM yearly_attack_counts current
LEFT JOIN yearly_attack_counts previous
    ON current.country_txt = previous.country_txt 
    AND current.iyear = previous.iyear + 1
ORDER BY current.country_txt, current.iyear;
"""

# הרצת השאילתא והחזרת התוצאות כ-DataFrame
df = pd.read_sql(query, engine)

# יצירת מפה
m = folium.Map(location=[20,0], zoom_start=2)

# יצירת MarkerCluster לאזורים
marker_cluster = MarkerCluster().add_to(m)

# הנחה - יש לך רשימת ערכים עם מיקומים גיאוגרפיים (latitude, longitude)
# עבור כל אזור, הוסף סימן על המפה עם אחוז השינוי
for index, row in df.iterrows():
    if row['percentage_change'] is not None:  # אם יש אחוז שינוי
        # הצגת מידע כמרקר על המפה
        folium.Marker(
            location=[row['latitude'], row['longitude']],  # הנחה שיש לך עמודות של latitude ו-longitude
            popup=f"{row['country_txt']} ({row['year']}): {row['percentage_change']:.2f}% שינוי",
            icon=folium.Icon(color="blue")
        ).add_to(marker_cluster)

# שמירת המפה לקובץ HTML
m.save("attack_percentage_map.html")

print("The map has been saved as 'attack_percentage_map.html'")
