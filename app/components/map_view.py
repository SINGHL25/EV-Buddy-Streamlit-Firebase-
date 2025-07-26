# ───────────── app/components/map_view.py ─────────────
# ───────────── app/components/map_view.py ─────────────
import streamlit as st
import pandas as pd
from folium import Map, Marker, Icon, Popup
from streamlit_folium import st_folium
from app.services.charger_api import get_all_stations

def render_map(lang):
    st.subheader("🌐 EV Station Map Viewer")

    stations = get_all_stations()
    if not stations:
        st.warning("No stations available.")
        return

    df = pd.DataFrame(stations)

    # Status filter
    status_options = df['status'].unique().tolist()
    selected_status = st.multiselect("⚙️ Filter by status", status_options, default=status_options)

    # Filter by status
    filtered_df = df[df['status'].isin(selected_status)]

    # Default center
    center_lat = filtered_df['latitude'].mean()
    center_lon = filtered_df['longitude'].mean()

    fmap = Map(location=[center_lat, center_lon], zoom_start=10)

    for _, row in filtered_df.iterrows():
        icon_color = {
            "available": "green",
            "busy": "red",
            "maintenance": "gray"
        }.get(row["status"].lower(), "blue")

        popup_html = f"""
        <b>{row['name']}</b><br>
        📍 {row['location']}<br>
        ⚡ Status: <b>{row['status'].title()}</b><br>
        <a href='?page=book&station_id={row["id"]}' target='_self'>
            <button style="margin-top:5px;">Book Now</button>
        </a>
        """

        popup = Popup(popup_html, max_width=300)
        Marker(
            location=[row["latitude"], row["longitude"]],
            popup=popup,
            icon=Icon(color=icon_color)
        ).add_to(fmap)

    st_data = st_folium(fmap, width=700, height=500)


