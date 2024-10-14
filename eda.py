# Import necessary libraries
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


st.header("Exploratory Data Analysis")


# Step 1: Load the penguins dataset
penguins = sns.load_dataset("penguins")

# Display the first 5 rows to understand the structure

def summary(filtered_data):

    # Summary statistics
    st.write("### Summary Statistics")
    st.write(filtered_data.describe())

    # Species distribution
    st.write("### Species Distribution")
    st.bar_chart(filtered_data['species'].value_counts())

def load_data():
    return sns.load_dataset("penguins").dropna()

penguins = load_data()



# Species selection
species = st.multiselect(
    "Select Species",
    options=penguins['species'].unique(),
    default=penguins['species'].unique()
)

# Filter data based on user selection
filtered_data = penguins[penguins['species'].isin(species)]
summary(filtered_data)


