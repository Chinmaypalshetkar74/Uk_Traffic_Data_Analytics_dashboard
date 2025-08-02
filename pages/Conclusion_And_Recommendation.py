import streamlit as st

st.set_page_config(page_title="📝 Conclusion & Recommendations", layout="wide")
st.title("📝 Conclusion and Recommendations")

# --- Summary Header ---
st.markdown("### 📌 Project Overview")
st.write("""
This dashboard provides an analytical overview of UK vehicle traffic trends from **2000 to 2024**, focusing on miles driven by different vehicle types across UK regions. All insights are drawn using data visualization and interactive analysis built with Streamlit.
""")

# --- Section: Key Insights ---
st.markdown("### 📈 Key Conclusions from Data (2000–2024)")
st.markdown("""
- 🚗 **Steady Growth till 2018**: Traffic volumes for most vehicle types, especially **Cars, Taxis, and Light Vans**, increased consistently from 2000 to 2018.
- 📉 **2020 Traffic Drop**: A significant **decline in miles driven** was observed in 2020 across all vehicle types and regions, likely due to pandemic-related lockdowns.
- 🔄 **Post-2020 Recovery**: Data shows a **clear recovery trend by 2024**, with some categories nearing or surpassing pre-pandemic levels.
- 🚲 **Cycling Popularity in London**: Pedal cycles saw **strong growth in London**, indicating a shift toward sustainable transport.
- 🚌 **Public Transport Variation**: **Buses and Coaches declined overall**, but **London remained relatively stable**, thanks to its extensive public transport infrastructure.
- 🚚 **Rise in Light Vans**: Steady growth from 2000–2024, reflecting increased commercial and delivery activities.

""")

# --- Section: Dashboard Strengths ---
st.markdown("### 🧠 Dashboard Strengths")
st.markdown("""
- ✅ Interactive filtering by vehicle type and region
- 📊 Dynamic line, bar, and pie charts showing traffic trends
- 📍 Region-wise comparison with visual context
- 🕵️ Clear visibility into changes over time without statistical modeling
""")

# --- Section: Limitations ---
st.markdown("### ⚠️ Limitations")
st.markdown("""
- Data is **aggregated annually** — finer time intervals (e.g., monthly) are not explored.
- The dashboard reflects **descriptive analytics only**; no predictive models or forecasting were applied.
- External factors (e.g., fuel prices, policy changes, population shifts) are **not incorporated** in this analysis.
""")

# --- Section: Recommendations ---
st.markdown("### ✅ Recommendations")
st.markdown("""
- 🚴 Expand cycling infrastructure in other UK regions based on London's success.
- 🛻 Monitor and manage the rise of Light Van traffic due to environmental and road usage impact.
- 🚌 Address the **declining use of public transport** in non-London regions with targeted policy support.
- 🧪 Consider integrating **monthly or regional-level socioeconomic data** for deeper analysis in future work.
""")

# --- Footer ---
st.markdown("---")
st.markdown("✅ *This analysis-driven dashboard is built entirely using Streamlit and provides an interactive lens on UK traffic trends from 2000 to 2024.*")
