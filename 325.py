import os
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

# Load earthquake data from the CSV file in the same directory
script_directory = os.path.dirname(os.path.abspath(__file__))
csv_file_path = os.path.join(script_directory, 'earthquake.csv')
df = pd.read_csv(csv_file_path)
