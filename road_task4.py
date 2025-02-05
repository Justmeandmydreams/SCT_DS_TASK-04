import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
data = pd.read_csv("C:/Users/joshi/Documents/Road.csv")

# Data cleaning
data.dropna(subset=['Area_accident_occured', 'Weather_conditions', 'Road_surface_conditions', 'Time', 'Cause_of_accident'], inplace=True)

# Parse time for grouping by hour
data['Hour'] = pd.to_datetime(data['Time'], errors='coerce').dt.hour

# 1. Accident Hotspots
hotspot_analysis = data['Area_accident_occured'].value_counts().head(10)
print("Top 10 Accident Hotspots:\n", hotspot_analysis)

# 2. Weather Conditions
weather_analysis = data['Weather_conditions'].value_counts(normalize=True) * 100
print("\nAccidents by Weather Conditions (%):\n", weather_analysis)

# 3. Road Surface Conditions
road_condition_analysis = data['Road_surface_conditions'].value_counts(normalize=True) * 100
print("\nAccidents by Road Surface Conditions (%):\n", road_condition_analysis)

# 4. Time of Day
time_analysis = data.groupby('Hour').size()
print("\nAccidents by Hour of Day:\n", time_analysis)

# 5. Contributing Factors
cause_analysis = data['Cause_of_accident'].value_counts().head(10)
print("\nTop 10 Contributing Factors:\n", cause_analysis)

# Visualizations
plt.figure(figsize=(16, 12))

# Plot 1: Accident Hotspots
plt.subplot(2, 2, 1)
sns.barplot(y=hotspot_analysis.index, x=hotspot_analysis.values, palette='viridis')
plt.title('Top 10 Accident Hotspots')
plt.xlabel('Number of Accidents')
plt.ylabel('Area')

# Plot 2: Weather Conditions
plt.subplot(2, 2, 2)
weather_analysis.plot(kind='bar', color='skyblue')
plt.title('Accidents by Weather Conditions')
plt.xlabel('Weather Conditions')
plt.ylabel('Percentage')

# Plot 3: Road Surface Conditions
plt.subplot(2, 2, 3)
road_condition_analysis.plot(kind='bar', color='orange')
plt.title('Accidents by Road Surface Conditions')
plt.xlabel('Road Conditions')
plt.ylabel('Percentage')

# Plot 4: Time of Day
plt.subplot(2, 2, 4)
time_analysis.plot(kind='line', marker='o', color='red')
plt.title('Accidents by Time of Day')
plt.xlabel('Hour of Day')
plt.ylabel('Number of Accidents')

plt.tight_layout()
plt.show()

# Contributing Factors Visualization
plt.figure(figsize=(10, 6))
sns.barplot(y=cause_analysis.index, x=cause_analysis.values, palette='coolwarm')
plt.title('Top 10 Contributing Factors')
plt.xlabel('Number of Accidents')
plt.ylabel('Cause of Accident')
plt.show()
