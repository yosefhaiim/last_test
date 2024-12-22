from sqlalchemy import create_engine
engine = create_engine("sqlite:///terror_data.db")

import pandas as pd


# query 1
query = """
SELECT summary, SUM(nkill) AS total_kills, SUM(nwound) AS total_wounds
FROM terror_events
WHERE (nkill = 2 OR nwound = 1)
GROUP BY summary
ORDER BY total_kills DESC, total_wounds DESC
LIMIT 5;
"""

# Execute the query and load the result into a DataFrame
df = pd.read_sql(query, engine)

# Print the results
print(df)


# query 2 (3)

query2 = """
SELECT gname, SUM(nkill) + SUM(nwound) AS total_victims
FROM terror_events
GROUP BY gname
ORDER BY total_victims DESC
LIMIT 5;
"""

df = pd.read_sql(query2, engine)
print(df)
