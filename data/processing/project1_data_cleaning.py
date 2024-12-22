import pandas as pd
from sqlalchemy import create_engine

# Step 1: Load the data from a CSV file
print("Loading data...")
csv_path = "../global_terror1000.csv"
data = pd.read_csv(csv_path, encoding="ISO-8859-1")
print("Data loaded successfully.")

# Step 2: Clean the data
print("Cleaning data...")
# Selecting relevant columns
columns_to_keep = [
    "iyear", "imonth", "gname", "iday", "country", "country_txt", "city", "latitude", "longitude", "nkill", "nwound",
    "summary", "attacktype1", "region", "region_txt", "location", "nperps", "target1"
]

data = data[columns_to_keep]

# Dropping rows with missing geographic data
data = data.dropna(subset=["latitude", "longitude"])

# Filling missing values in 'nkill' and 'nwound' columns with 0
data["nkill"].fillna(0, inplace=True)
data["nwound"].fillna(0, inplace=True)
print("Data cleaned successfully.")

# Step 3: Save the cleaned data to a database
print("Saving data to database...")
# Create a SQLite database connection (can be replaced with PostgreSQL/MySQL configurations)
engine = create_engine("sqlite:///terror_data.db")

# Save the data into a table named 'terror_events'
table_name = "terror_events"
data.to_sql(table_name, engine, if_exists="replace", index=False)
print(f"Data saved to database table: {table_name}")

print("Process completed successfully.")
