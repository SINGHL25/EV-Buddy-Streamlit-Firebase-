# ───────────── app/routing.py ─────────────
# Placeholder for page routing if needed (can be expanded for multi-page app)


# ───────────── app/components/map_view.py ─────────────
import streamlit as st
import pandas as pd
import pydeck as pdk
from app.services.charger_api import get_all_stations

def render_map(lang):
    stations = get_all_stations()
    df = pd.DataFrame(stations)
    st.subheader("🔌 EV Charging Locations")
    st.map(df[['latitude', 'longitude']])
