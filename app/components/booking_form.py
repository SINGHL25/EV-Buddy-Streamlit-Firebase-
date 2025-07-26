# ───────────── app/components/booking_form.py ─────────────
# ───────────── app/components/booking_form.py ─────────────
import streamlit as st
from app.services.charger_api import get_station_by_id, save_booking
from datetime import datetime

def render_booking_form(lang):
    st.subheader("📝 EV Station Booking")

    # Get station_id from URL
    station_id = st.query_params.get("station_id")
    station = get_station_by_id(station_id) if station_id else None

    if station:
        st.success(f"Booking for: {station['name']} ({station['location']})")
    else:
        st.warning("No station selected. Please choose one from the map.")

    # Booking form
    with st.form("booking_form"):
        user_name = st.text_input("👤 Your Name", value="")
        vehicle_number = st.text_input("🚗 Vehicle Number", value="")
        phone = st.text_input("📞 Contact Number", value="")
        slot_time = st.time_input("⏰ Preferred Time")
        station_name = station["name"] if station else st.text_input("🔌 Station Name")
        station_loc = station["location"] if station else st.text_input("📍 Station Location")
        
        submit = st.form_submit_button("✅ Book Slot")

    if submit:
        booking_data = {
            "user": user_name,
            "vehicle": vehicle_number,
            "phone": phone,
            "station_id": station_id,
            "station_name": station_name,
            "location": station_loc,
            "time": slot_time.strftime("%H:%M"),
            "timestamp": datetime.now().isoformat()
        }

        save_booking(booking_data)
        st.success("✅ Booking Confirmed!")

