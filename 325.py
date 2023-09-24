import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
import gdown

# Function to download data from Google Drive using file ID
def download_data_from_drive(file_id):
    url = f'https://drive.google.com/uc?id={file_id}'
    output = 'earthquake_data.csv'  # Output file name
    gdown.download(url, output, quiet=False)
    return pd.read_csv(output)

# Function to display earthquake locations on a map
def display_earthquake_locations(df):
    fig = px.scatter_geo(df, lat='latitude', lon='longitude', color='magnitude', hover_name='location', title='Earthquake Locations')
    st.plotly_chart(fig)

# Function to display magnitude distribution over time
def display_magnitude_distribution(df):
    fig = go.Figure(
        data=[go.Histogram(x=df['magnitude'], nbinsx=30)],
        layout=go.Layout(
            title='Magnitude Distribution Over Time',
            xaxis=dict(title='Magnitude'),
            yaxis=dict(title='Frequency')
        )
    )
    st.plotly_chart(fig)

# Function to display earthquake density contours by magnitude
def display_density_contours(df):
    fig = px.density_contour(df, x='longitude', y='latitude', color='magnitude', marginal_x='histogram', marginal_y='histogram',
                             labels={'longitude': 'Longitude', 'latitude': 'Latitude', 'magnitude': 'Magnitude'},
                             title='Earthquake Density Contours by Magnitude')
    st.plotly_chart(fig)

# Function to display 3D scatter plot of earthquake data
def display_3d_scatter_plot(df):
    fig = px.scatter_3d(df, x='depth', y='magnitude', z='gap', color='country',
                        size='nst', opacity=0.7, hover_name='title',
                        labels={'depth': 'Depth', 'magnitude': 'Magnitude', 'gap': 'Gap', 'country': 'Country', 'nst': 'NST'},
                        title='3D Scatter Plot of Earthquake Data (Depth, Magnitude, Gap)')
    st.plotly_chart(fig)

# Function to display earthquake count over time
def display_earthquake_count_over_time(df):
    # Convert 'date_time' column to datetime type
    df['date_time'] = pd.to_datetime(df['date_time'])

    # Sort the DataFrame by 'date_time' for cumulative counting
    df.sort_values(by='date_time', inplace=True)

    # Create a cumulative count of earthquakes over time
    df['cumulative_count'] = range(1, len(df) + 1)

    fig = go.Figure(
        data=[
            go.Scatter(
                x=df['date_time'],
                y=df['cumulative_count'],
                mode='lines+markers',
                line=dict(color='blue', width=2),
                marker=dict(size=6, color='red'),
                name='Cumulative Count',
            ),
        ],
        layout=go.Layout(
            title='Cumulative Earthquake Count Over Time',
            xaxis=dict(title='Date'),
            yaxis=dict(title='Cumulative Count')
        )
    )

    st.plotly_chart(fig)

# File ID for the earthquake dataset on Google Drive
file_id = "1hykoubWsMB3RLo2ZK55K7Qz9XynZWLam"

# Download Earthquake Data from Google Drive using file ID
df = download_data_from_drive(file_id)

# Streamlit app
st.title('Earthquake Data Analysis')

# Display earthquake locations
st.header('Earthquake Locations')
display_earthquake_locations(df)

# Display magnitude distribution over time
st.header('Magnitude Distribution Over Time')
display_magnitude_distribution(df)

# Display earthquake density contours by magnitude
st.header('Earthquake Density Contours by Magnitude')
display_density_contours(df)

# Display 3D scatter plot of earthquake data
st.header('3D Scatter Plot of Earthquake Data')
display_3d_scatter_plot(df)

# Display earthquake count over time
st.header('Cumulative Earthquake Count Over Time')
display_earthquake_count_over_time(df)
