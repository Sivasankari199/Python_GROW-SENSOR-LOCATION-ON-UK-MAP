📊 GROW Sensor Data Visualization Script
This project provides a Python script for analyzing and visualizing sensor location data across the UK. The workflow is designed to clean, validate, and plot geospatial sensor data on a background map image, allowing users to quickly identify sensor placements and data quality issues.

📝 What Does the Code Do?
Reads Data

Loads location and metadata for GROW sensors from a CSV file (Growlocations.csv).

Cleans Latitude/Longitude

Swaps incorrectly labeled Latitude and Longitude columns for proper mapping.

Filters Data by Geographic Bounds

Keeps only locations within valid UK latitude (50.681 to 57.985) and longitude (-10.592 to 1.6848) ranges.

Handles Data Quality

Checks for missing values in all columns.

Removes duplicate rows to maintain unique sensor entries.

Converts time columns (BeginTime, EndTime) to a standard datetime format, handling errors gracefully.

Prints basic descriptive statistics (count, mean, std, min, max of coordinates).

Detects Inconsistencies

Identifies any records that are still duplicated across key identity fields.

Visualizes on a Map

Loads a UK map image (map7.png) as a background.

Overlays the filtered sensor locations as red dots based on their geographic coordinates.

Adds labels and a legend for clarity.

Shows the generated map plot with all sensor locations highlighted.

📂 Example Project Structure
text
Locations_UK
├── Growlocations.csv     
├── map7.png              
├── sensor_map.py         

└── README.md
🚀 How to Use
Install Requirements

If not already installed, use:

text
pip install pandas matplotlib Pillow
Prepare Data

Ensure you have Growlocations.csv (with sensor info) and map7.png (UK map image) in your project directory.

Run the Script

Execute the script:

text
python sensor_map.py
View Output

The script will print:

Any missing values per column

Descriptive statistics for filtered locations

Any detected data inconsistencies

A window will appear displaying the map with all valid sensor locations plotted as red dots.

🛡️ Key Features
Automated column fixing (latitude/longitude swap)

UK-only filtering to avoid outlier/invalid locations

Duplicate and null data handling for reliable analysis

Dynamic background mapping—you can swap in any compatible map image

Immediate data diagnostics with console outputs

Clear geographic visualization for science, engineering, or IoT sensor deployment projects
