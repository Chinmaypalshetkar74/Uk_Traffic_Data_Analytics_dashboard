import streamlit as st
import streamlit.components.v1 as components
import os

st.set_page_config(layout="wide")
st.title("🚗 Vehicles Traffic Flow in UK Region(2000 - 2024)")
st.subheader("trend on Major Road Classes")

# Folder where HTML charts are stored
html_folder = "Notebooks/html_visuals"

# Tabs and corresponding HTML filenames
tabs = st.tabs([
    "All Motorvehicles",
    "🚛 HeavyGoods Vehicles",
    "🚗 Cars And Taxis",
    "🏍️ Motorcycles",
    "🚌 Buses And Coaches",
    "🚐 Vans ",
    "pedal Cycles "
])

html_files = {
    "All Motor vehicles trend on Major Road Classes":"motor_vehicles_by_trend.html",
    "🚛 Heavy Goods Vehicles trend on Major Road Classes":" All_heavy_good_vehicles_trend.html",
    "🚗 Cars and Taxis trend on Major Road Classes":"cars_and_taxismiles_driven_trend.html",
    "🏍️ Motorcycles":"two_wheeled_trend.html",
    "🚌 Buses and Coaches trend on Major Road Classes":"buses_and_coaches_trend.html",
    "🚐 Vans trend on Major Road Classes":"vans_traffic_trend.html",
    "pedal Cycles trend on Major Road Classes":"pedal_cycle_trend.html"
    
   
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

