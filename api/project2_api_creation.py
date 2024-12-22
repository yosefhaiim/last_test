from flask import Flask, jsonify
from sqlalchemy import create_engine
import pandas as pd

# Step 1: Initialize Flask application
app = Flask(__name__)

# Step 2: Connect to the database
# Ensure the path matches the database created in Project 1.
print("Connecting to the database...")
db_path = "sqlite:///data/terror_data.db"
engine = create_engine(db_path)

# Step 3: Define API endpoints

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Welcome to the Terror Data API!"})

@app.route("/events", methods=["GET"])
def get_events():
    try:
        # Fetch data from the database
        query = "SELECT * FROM terror_events LIMIT 100"
        df = pd.read_sql(query, con=engine)
        return df.to_json(orient="records"), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/events/<int:year>", methods=["GET"])
def get_events_by_year(year):
    try:
        # Fetch data for a specific year
        query = f"SELECT * FROM terror_events WHERE iyear = {year}"
        df = pd.read_sql(query, con=engine)
        return df.to_json(orient="records"), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Step 4: Run the application
if __name__ == "__main__":
    print("Starting Flask server...")
    app.run(debug=True, host="0.0.0.0", port=5000)
