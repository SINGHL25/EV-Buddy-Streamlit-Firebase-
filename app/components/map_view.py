# ───────────── app/components/map_view.py ─────────────
import streamlit as st
import pandas as pd
import pydeck as pdk
from app.services.charger_api import get_all_stations

def render_map(lang):
    st.subheader("🔌 EV Charging Locations")

    stations = get_all_stations()
    if not stations:
        st.warning("No charger data available.")
        return

    df = pd.DataFrame(stations)
    
    # Show interactive map using pydeck
    st.pydeck_chart(pdk.Deck(
        map_style='mapbox://styles/mapbox/streets-v12',
        initial_view_state=pdk.ViewState(
            latitude=df['latitude'].mean(),
            longitude=df['longitude'].mean(),
            zoom=10,
            pitch=50,
        ),
        layers=[
            pdk.Layer(
                'ScatterplotLayer',
                data=df,
                get_position='[longitude, latitude]',
                get_color='[200, 30, 0, 160]',
                get_radius=500,
                pickable=True,
            ),
        ],
        tooltip={"text": "{name}\n{location}\nStatus: {status}"}
    ))

