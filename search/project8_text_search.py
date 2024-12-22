# Project 8: Text Search Implementation
#
# This script implements a simple textual search mechanism for the terror events database using SQLite full-text search (FTS).

import sqlite3
import pandas as pd

# Step 1: Connect to the database
print("Connecting to the database...")
db_path = "terror_data.db"
connection = sqlite3.connect(db_path)
cursor = connection.cursor()

# Step 2: Create an FTS virtual table if it doesn't exist
print("Setting up the FTS table...")
cursor.execute("""
CREATE VIRTUAL TABLE IF NOT EXISTS terror_events_fts USING FTS5(
    summary, gname, country_txt, iyear
);
""")

# Step 3: Populate the FTS table with existing data
print("Populating the FTS table...")
cursor.execute("DELETE FROM terror_events_fts;")  # Clear existing data if needed
cursor.execute("""
INSERT INTO terror_events_fts (summary, gname, country_txt, iyear)
SELECT summary, gname, country_txt, iyear FROM terror_events;
""")
connection.commit()
print("FTS table populated successfully.")

# Step 4: Define a search function
def search_terror_events(query):
    print(f"Searching for: {query}")
    query = f"%{query}%"
    result = pd.read_sql_query(
        """
        SELECT * FROM terror_events_fts
        WHERE summary LIKE ? OR gname LIKE ? OR country_txt LIKE ?;
        """,
        connection,
        params=(query, query, query),
    )
    return result

# Step 5: Test the search function
if __name__ == "__main__":
    search_query = "bombing"
    search_results = search_terror_events(search_query)
    print("Search Results:")
    print(search_results)

# Close the database connection
connection.close()
print("Database connection closed.")
