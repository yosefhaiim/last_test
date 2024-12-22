# Project: Terror Data Analysis Platform

## Description
This project is designed to analyze and visualize terror data from 1970 to 2022. The platform integrates multiple data sources, performs statistical computations, and presents insights via interactive maps and graphs.

### Key Features:
1. **Data Cleaning & Integration**: Import, clean, and integrate data from CSV files.
2. **REST API Development**: Flask-based API to interact with the processed data.
3. **Statistical Analysis**: Perform in-depth analysis using SQL and Python libraries.
4. **Visualization**: Display data insights on maps and graphs.
5. **Real-Time Updates**: Integrate live data using external APIs.
6. **Textual Search**: Implement a search engine for efficient text-based queries.

---

## Project Structure
```
├── data
│   ├── raw
│   └── processed
├── database
├── api
├── analysis
├── visualization
├── static
├── templates
├── tests
└── README.md
```

### Directory Explanation:
- **data**: Contains raw and processed data.
- **database**: Scripts for database setup and maintenance.
- **api**: Flask application and REST API endpoints.
- **analysis**: Code for statistical analysis and computations.
- **visualization**: Scripts to generate maps and graphs.
- **static**: CSS and JS files.
- **templates**: HTML templates for Flask.
- **tests**: Unit and integration tests for the platform.

---

## Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```bash
   cd <project-directory>
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Set up the database:
   ```bash
   python setup_database.py
   ```
5. Start the Flask server:
   ```bash
   python app.py
   ```

---

## Technologies Used
- **Programming Language**: Python
- **Framework**: Flask
- **Data Analysis**: Pandas, Numpy, SQL
- **Visualization**: Matplotlib, Folium
- **Database**: PostgreSQL
- **APIs**: NewsAPI, OpenCage

---

## Usage
1. Open your browser and navigate to the local server:
   ```
   http://127.0.0.1:5000
   ```
2. Interact with:
   - **Graphs**: Visualize statistical insights.
   - **Maps**: Explore geographic data.
   - **Search**: Use the search bar for textual queries.

---

## Future Enhancements
- Implement machine learning models for predictive analysis.
- Add support for multilingual data sources.
- Enhance the user interface with modern frameworks like React or Angular.

---

## License
This project is licensed under the MIT License - see the LICENSE file for details.

---

### Preview
Below is an example of the type of visualization created by the platform:

![Example Visualization](/image.png)

