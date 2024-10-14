import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
import sys
import os

# Get the absolute path of the `module1` directory
eda_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../EDA"))
# Add it to sys.path
sys.path.append(eda_path)

# Now, you can import `eda.py`
import eda



st.header("🤖 Machine Learning")


# Define features and target
X = eda.filtered_data[['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g']].dropna()
y = eda.filtered_data['species'].dropna()

# Train-Test Split
if not X.empty and not y.empty:
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train the Random Forest Classifier
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Predictions
    y_pred = model.predict(X_test)

    # Display the classification report
    st.write("### Classification Report")
    st.text(classification_report(y_test, y_pred))

    # Confusion Matrix
    st.write("### Confusion Matrix")
    cm = confusion_matrix(y_test, y_pred)
    plt.figure(figsize=(10, 5))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=model.classes_, yticklabels=model.classes_)
    plt.title("Confusion Matrix")
    plt.xlabel("Predicted")
    plt.ylabel("True")
    st.pyplot(plt)
