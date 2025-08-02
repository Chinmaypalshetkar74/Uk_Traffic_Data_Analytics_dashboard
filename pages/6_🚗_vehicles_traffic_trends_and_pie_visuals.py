import streamlit as st
import streamlit.components.v1 as components
import os

# Folder where HTMLs are saved
html_folder = "Notebooks/html_visuals"

# Mapping tab titles to their HTML files
html_files = {
    "Motor Vehicles": ["motorvehicles_line.html", "motorvehicles_pie.html"],
    "All Vehicles":["Allvehicles_line.html", "Allvehicles_pie.html"],
    "Heavy Vehicles": ["HeavyVehicles_line.html", "heavyvehicles_pie.html"],
    "Cars and Taxies":[ "CarsTaxies_line.html", "CarsTaxies_pie.html"],
    "motorcycles": ["motorcycles_line.html", "motorcycles_pie.html"],
    "Buses and Coaches": ["BusesCoaches_line.html", "BusesCoaches_pie.html"],
    "vans": ["vans_line.html", "vans_pie.html"],
    "pedal_cycle":["pedal_line.html", "pedal_pie.html"]
    

   
}

# Create tabs dynamically
tabs = st.tabs(list(html_files.keys()))

# Loop through each tab
for tab, label in zip(tabs, html_files.keys()):
    with tab:
        st.subheader(f"{label} - Line Chart")
        file_path = os.path.join(html_folder, html_files[label][0])
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                components.html(f.read(), height=500, scrolling=True)
        except FileNotFoundError:
            st.error(f"❌ Could not find: {file_path}")

        st.subheader(f"{label} - Pie Chart")
        file_path = os.path.join(html_folder, html_files[label][1])
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                components.html(f.read(), height=1000, scrolling=True)
        except FileNotFoundError:
            st.error(f"❌ Could not find: {file_path}")
