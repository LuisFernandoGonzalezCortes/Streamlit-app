import streamlit as st
import sys
import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# Get the absolute path of the `module1` directory
eda_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../EDA"))
# Add it to sys.path
sys.path.append(eda_path)

# Now, you can import `eda.py`
import eda

# Speciesselection
species = st.multiselect(
    "Select Species",
    options=eda.penguins['species'].unique(),
    default=eda.penguins['species'].unique(),
    
)


# Filter data based on user selection
eda.filtered_data = eda.penguins[eda.penguins['species'].isin(species)]


# Display data distribution for selected numeric columns
st.write("### Data Distribution")
eda.selected_numeric = st.selectbox("Select Numeric Column", options=eda.penguins.select_dtypes(include=['float64']).columns)

# Create a histogram for the selected numeric column
plt.figure(figsize=(10, 5))
sns.histplot(eda.filtered_data[eda.selected_numeric], bins=20, kde=True)
plt.title(f'Distribution of {eda.selected_numeric}')
plt.xlabel(eda.selected_numeric)
plt.ylabel('Frequency')
st.pyplot(plt)

# Boxplot to compare distributions across species
st.write("### Boxplot for Selected Numeric Column by Species")
plt.figure(figsize=(10, 5))
sns.boxplot(data=eda.filtered_data, x='species', y=eda.selected_numeric)
plt.title(f'Boxplot of {eda.selected_numeric} by Species')
plt.xlabel('Species')
plt.ylabel(eda.selected_numeric)
st.pyplot(plt)

# Pairplot option
st.write("### Pairplot")
if st.sidebar.checkbox("Show Pairplot"):
    st.write("**Pairplot of Selected Species**")
    pairplot_data = eda.filtered_data.dropna()  # Drop NaN values for plotting
    sns.pairplot(pairplot_data, hue="species")
    st.pyplot(plt)


# Add footer
st.write("### About this App")
st.write("This app allows you to explore the Palmer Penguins dataset interactively. You can visualize data distributions and compare different species.")
