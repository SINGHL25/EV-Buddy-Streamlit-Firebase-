# ───────────── app/components/station_card.py ─────────────
def render_station_card(station):
    st.markdown(f"### {station['name']}")
    st.write(f"📍 {station['location']}")
    st.write(f"⚡ Charger Type: {station['type']}")
    st.write(f"🔋 Status: {station['status']}")
    st.button("Book Now", key=f"book_{station['id']}")
