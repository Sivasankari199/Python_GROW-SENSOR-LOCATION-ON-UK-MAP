import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

# Reads the CSV data
df = pd.read_csv("Growlocations.csv")

# Swaping latitude and longitude column names
df = df.rename(columns={"Latitude": "Temp_Latitude", "Longitude": "Temp_Longitude"})
df = df.rename(columns={"Temp_Latitude": "Longitude", "Temp_Longitude": "Latitude"})

# Filtering the values within the valid latitude and longitude ranges for the UK map
df_filtered = df[(df["Latitude"] >= 50.681) & (df["Latitude"] <= 57.985) &
                 (df["Longitude"] >= -10.592) & (df["Longitude"] <= 1.6848)]

# Handling missing values
missing_values = df_filtered.isnull().sum()
print("Missing Values:")
print(missing_values)

# Droping duplicate rows
df_filtered = df_filtered.drop_duplicates()

# Converting "BeginTime" and "EndTime" to datetime format
df_filtered['BeginTime'] = pd.to_datetime(df_filtered['BeginTime'], errors='coerce')
df_filtered['EndTime'] = pd.to_datetime(df_filtered['EndTime'], errors='coerce')

# Displaying the descriptive statistics
print("\nDescriptive Statistics:")
print(df_filtered[['Latitude', 'Longitude']].describe())

# Displaying the inconsistent data
inconsistent_data = df_filtered[df_filtered.duplicated(subset=['Serial', 'Latitude', 'Longitude', 'Type', 'SensorType', 'Code', 'BeginTime', 'EndTime'], keep=False)]
print("\nInconsistent Data:")
print(inconsistent_data)

# Loading the background map image
map_img = Image.open("map7.png")  

# Creating a figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Ploting the sensor locations on the background map
ax.imshow(map_img, extent=(-10.592, 1.6848, 50.681, 57.985))  # Set the extent based on the image and map boundaries
ax.scatter(df_filtered["Longitude"], df_filtered["Latitude"], marker="o", color="red", label="Sensor Locations")

# Customizing plot
ax.set_xlabel("Longitude")
ax.set_ylabel("Latitude")
ax.set_title("GROW Sensor Locations on UK Map")
ax.legend()

# Displays the plot
plt.show()
