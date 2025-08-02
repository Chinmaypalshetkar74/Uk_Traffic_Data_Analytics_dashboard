import streamlit as st
import streamlit.components.v1 as components
import os

st.set_page_config(layout="wide")
st.title("🚗 Vehicles Traffic Flow in UK Regions (2000 - 2024)")
st.subheader("trend on 10 busiest Roads")
# Folder where HTML charts are stored
html_folder = r"Notebooks\html_visuals"

# Tabs and corresponding HTML filenames
tabs = st.tabs([
    "All vehicle Driven",
    "All Motor Vehicles",
    "🚛 Heavy Goods Vehicles",
    "🚗 Cars and Taxis driven",
    "🏍️ Motorcycles driven",
    "🚌 Buses and Coaches",
    "🚐 Vans",
    "pedal Cycles "
])

html_files = {
    "All vehicle Driven by top 10 busiest Roads":"All_vehicle_traffic_trend_on_10_busiest_road.html",
    "All Motor Vehicles driven by 10 busiest Roads":"All_motor_vehicle_traffic_trend_on_10_busiest_road.html",
    "🚛 Heavy Goods Vehicles driven by 10 busiest Roads":"All_Heavy_vehicle_traffic_trend_on_10_busiest_road.html",
    "🚗 Cars and Taxis driven by 10 busiest Roads":"All_Cars_and_taxies_traffic_trend_on_10_busiest_road.html",
    "🏍️ Motorcycles driven by 10 busiest Roads":"All_two-wheeled_traffic_trend_on_10_busiest_road.html",
    "🚌 Buses and Coaches driven by 10 busiest Roads":"Buses_and_Coaches_traffic_trend_on_10_busiest_road.html",
    "🚐 Vans driven by 10 busiest Roads":"Vans_traffic_trend_on_10_busiest_road.html",
    "pedal Cycles driven by 10 busiest Roads":"pedal_cycle_traffic_trend_on_10_busiest_road.html"
    
   
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
