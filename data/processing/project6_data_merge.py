# Project 6: Merging Additional Data
#
# This script merges new terror event data from an additional CSV file into the existing database.

import pandas as pd
from sqlalchemy import create_engine

# Step 1: Load the new data
# Replace "path_to_new_file.csv" with the path to your additional dataset.
print("Loading new data...")
new_csv_path = "../5000_rows.csv"
new_data = pd.read_csv(new_csv_path, encoding='ISO-8859-1')
print("New data loaded successfully.")

# Step 2: Clean the new data
print("Cleaning new data...")
# Renaming columns to match the existing database schema
new_data.rename(columns={
    "Date": "iyear",  # Assuming the year is parsed from the Date
    "City": "city",
    "Country": "country_txt",
    "Perpetrator": "gname",
    "Weapon": "weaptype1_txt",
    "Injuries": "nwound",
    "Fatalities": "nkill",
    "Description": "summary"
}, inplace=True)

# Keeping only the necessary columns
columns_to_keep = [
    "iyear", "city", "country_txt", "gname", "weaptype1_txt", "nwound", "nkill", "summary"
]
new_data = new_data[columns_to_keep]

# Handling missing values
new_data["nwound"].fillna(0, inplace=True)
new_data["nkill"].fillna(0, inplace=True)
print("New data cleaned successfully.")

# Step 3: Connect to the existing database
print("Connecting to the database...")
db_path = "sqlite:///terror_data.db"
engine = create_engine(db_path)

# Step 4: Merge the new data into the existing database
print("Merging data...")
new_data.to_sql("terror_events", engine, if_exists="append", index=False)
print("New data merged successfully into the database.")
