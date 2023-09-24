import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Load earthquake data
df = pd.read_csv("earthquake_data.csv")

# Plotting earthquake locations using Matplotlib
st.write("Earthquake Locations")
plt.scatter(df['longitude'], df['latitude'], c=df['magnitude'], cmap='viridis', alpha=0.7)
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('Earthquake Locations')
st.pyplot()

# Magnitude Distribution Over Time (Animated Histogram) using Matplotlib
st.write("Magnitude Distribution Over Time")
plt.hist(df['magnitude'], bins=30, alpha=0.7, color='blue')
plt.xlabel('Magnitude')
plt.ylabel('Frequency')
plt.title('Magnitude Distribution Over Time')
st.pyplot()

# 3D Scatter Plot using Matplotlib
st.write("3D Scatter Plot of Earthquake Data (Depth, Magnitude, Gap)")
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(df['depth'], df['magnitude'], df['gap'], c=df['country'], s=df['nst'], alpha=0.7)
ax.set_xlabel('Depth')
ax.set_ylabel('Magnitude')
ax.set_zlabel('Gap')
ax.set_title('3D Scatter Plot of Earthquake Data (Depth, Magnitude, Gap)')
st.pyplot()

# Cumulative Earthquake Count Over Time (Animated Line Chart) using Matplotlib
st.write("Cumulative Earthquake Count Over Time")
df['date_time'] = pd.to_datetime(df['date_time'])
df.sort_values(by='date_time', inplace=True)
df['cumulative_count'] = range(1, len(df) + 1)

plt.figure()
plt.plot(df['date_time'], df['cumulative_count'], color='blue', marker='o')
plt.xlabel('Date')
plt.ylabel('Cumulative Count')
plt.title('Cumulative Earthquake Count Over Time')
plt.xticks(rotation=45)
st.pyplot()
