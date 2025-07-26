# ───────────── app/components/station_card.py ─────────────
# ───────────── app/components/station_card.py ─────────────
import streamlit as st
from app.services.charger_api import get_all_stations

def render_station_cards(lang):
    st.subheader("🔌 All EV Stations")

    stations = get_all_stations()
    if not stations:
        st.error("No stations found.")
        return

    status_color = {
        "available": "green",
        "busy": "red",
        "maintenance": "gray"
    }

    for stn in stations:
        status = stn["status"].lower()
        status_badge = f"<span style='color:white;background-color:{status_color.get(status,'blue')};padding:2px 8px;border-radius:8px'>{status.title()}</span>"

        st.markdown(f"""
        <div style='border:1px solid #ccc;padding:10px;border-radius:10px;margin-bottom:10px'>
        <h4>{stn['name']} — {status_badge}</h4>
        <p>📍 {stn['location']}<br>🆔 ID: {stn['id']}</p>
        <a href='?page=book&station_id={stn["id"]}' target='_self'>
            <button style='margin-top:5px'>Book Now</button>
        </a>
        </div>
        """, unsafe_allow_html=True)
