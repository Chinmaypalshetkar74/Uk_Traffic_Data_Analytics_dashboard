import streamlit as st
import streamlit.components.v1 as components
import os

st.set_page_config(layout="wide")
st.title("🚗 Vehicles Traffic Flow in UK Regions (2000 - 2024)")

# Folder where HTML charts are stored
html_folder = r"Notebooks\html_visuals"

# Tabs and corresponding HTML filenames
tabs = st.tabs([
    "All vehicle Driven by Region",
    "All Motor Vehicles",
    "🚛 Heavy Goods Vehicles",
    "🚗 Cars and Taxis",
    "🏍️ Motorcycles",
    "🚌 Buses and Coaches",
    "🚐 Vans",
    "pedal Cycles"
])

html_files = {
    "All vehicle Driven by Region": "all_vehicles_by_region.html",
    "All Motor Vehicles":"motor_vehicle.html",
    "🚛 Heavy Goods Vehicles":"All_heavy_good_vehicles.html", 
    "🚗 Cars and Taxis":"cars_and_taxismiles_driven.html",
    "🏍️ Motorcycles":"motor_cycle.html",
    "🚌 Buses and Coaches":"buses_and_coaches.html",
    "🚐 Vans":"vans_traffic.html",
    "pedal Cycles":"pedal_cycle.html"
    
   
}

# Loop to show each chart
for tab, label in zip(tabs, html_files.keys()):
    with tab:
        st.subheader(label)
        file_path = os.path.join(html_folder, html_files[label])
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                components.html(f.read(), height=1000, scrolling=True)
        except FileNotFoundError:
            st.error(f"❌ Could not find: {file_path}")
