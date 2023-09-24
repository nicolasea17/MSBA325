import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

# Load earthquake data from the CSV file in the same directory
df = pd.read_csv('earthquake.csv')