# ───────────── app/components/booking_form.py ─────────────
import streamlit as st
from app.services.charger_api import book_slot

def render_booking_form(lang):
    st.subheader("📅 Book a Charging Slot")
    name = st.text_input("Your Name")
    station_id = st.text_input("Station ID")
    slot_time = st.time_input("Preferred Time")
    if st.button("Book Slot"):
        success = book_slot(name, station_id, slot_time.strftime("%H:%M"))
        if success:
            st.success("Slot booked successfully!")
        else:
            st.error("Booking failed. Try again.")

