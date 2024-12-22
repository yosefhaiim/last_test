import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

engine = create_engine("sqlite:///terror_data.db")


# Query to retrieve total fatalities and injuries by region
query = """
SELECT country_txt AS region, SUM(nkill) AS total_kills, SUM(nwound) AS total_wounds
FROM terror_events
GROUP BY country_txt
ORDER BY total_kills DESC;
"""
data = pd.read_sql(query, engine)

# Step 3: Bar Chart - Total Fatalities by Region
plt.figure(figsize=(10, 6))
plt.bar(data['region'], data['total_kills'], color='red', alpha=0.7)
plt.xlabel('Region')
plt.ylabel('Total Fatalities')
plt.title('Total Fatalities by Region')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
# על מנת לשמור את התמונה ולשלוח אותה לHTML בהמשך
# plt.savefig('static/visualizations/fatalities_by_region.png')
plt.show()

# Step 4: Pie Chart - Proportion of Injuries by Region
plt.figure(figsize=(8, 8))
plt.pie(data['total_wounds'], labels=data['region'], autopct='%1.1f%%', startangle=140, colors=plt.cm.tab20.colors)
plt.title('Proportion of Injuries by Region')
plt.tight_layout()
# על מנת לשמור את התמונה ולשלוח אותה לHTML בהמשך
# plt.savefig('static/visualizations/injuries_by_region.png')
plt.show()

print("Visualizations generated and saved successfully.")
