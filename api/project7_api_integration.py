# Project 7: Real-Time Data Integration from an External API
#
# This script fetches real-time data from an external API (e.g., NewsAPI) and integrates it into the existing database.

import requests
import pandas as pd
from sqlalchemy import create_engine

# Step 1: Set up the API configuration
api_key = "your_newsapi_key_here"  # Replace with your actual API key
base_url = "https://newsapi.org/v2/everything"
query_params = {
    "q": "terror attack",
    "from": "2024-01-01",
    "sortBy": "relevance",
    "apiKey": api_key,
}

# Step 2: Fetch data from the API
print("Fetching data from the NewsAPI...")
response = requests.get(base_url, params=query_params)
if response.status_code == 200:
    articles = response.json()["articles"]
    print("Data fetched successfully.")
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")
    exit()

# Step 3: Process the fetched data
print("Processing data...")
data = pd.DataFrame(articles)
# Select relevant fields and rename them to match the database schema
data = data.rename(columns={
    "title": "summary",
    "description": "gname",  # Assuming perpetrator info is stored here
    "publishedAt": "iyear",  # Extract the year from the timestamp
    "source.name": "country_txt"  # Using the source as a placeholder for country
})
data = data[["summary", "gname", "iyear", "country_txt"]]  # Keep only required columns

# Parse the year from the timestamp
data["iyear"] = pd.to_datetime(data["iyear"]).dt.year

# Fill missing values
data.fillna("Unknown", inplace=True)
print("Data processed successfully.")

# Step 4: Connect to the database and insert the data
print("Inserting data into the database...")
db_path = "sqlite:///terror_data.db"
engine = create_engine(db_path)
data.to_sql("terror_events", engine, if_exists="append", index=False)
print("Real-time data integrated successfully.")
