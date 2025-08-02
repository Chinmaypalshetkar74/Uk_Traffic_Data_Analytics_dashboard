import streamlit as st
import streamlit.components.v1 as components
import os

st.set_page_config(layout="wide")
st.title("🚗 Vehicles Traffic Flow in UK Regions (2000 - 2024)")
st.subheader("Averages on Traffic Flow")
# Folder where HTML charts are stored
html_folder = "Notebooks/html_visuals"

# Tabs and corresponding HTML filenames
tabs = st.tabs([
    "Avg traffic Numbers travers by 10 busiest road ",
    "Avg traffic Numbers travers by 10 busiest roads by region",
    "Avg traffic Volume by region ",
    "Avg traffic volume by Each road"
    
])

html_files = {
    "Avg traffic Numbers travers by 10 busiest Highway local Authority Road ":"Avg_traffic_no_travers_by_10_buesiet_road_local_authority.html",
    "Avg traffic Numbers travers by 10 busiest roads by region ":"Avg_traffic_no_travers_by_10_buesiet_road_Region.html",
    "Avg traffic Volume by region ":"Avg_traffic_volume_by_each_Region.html",
    "Avg traffic volume by Each road":"Avg_traffic_volume_by_each_road.html"
    
    
   
   
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
