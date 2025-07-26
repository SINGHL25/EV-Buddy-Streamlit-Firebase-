# ───────────── app/main.py ─────────────
import streamlit as st
from app.translations.lang_strings import LANGUAGES
from app.components.map_view import render_map
from app.components.booking_form import render_booking_form
from app.services.firebase_service import init_firebase

# Initialize Firebase
init_firebase()

# Language selector
lang = st.sidebar.selectbox("Select Language", options=list(LANGUAGES.keys()))
T = LANGUAGES[lang]


lang = st.selectbox("🌐 Language", ["English", "Hindi"])
if lang == "Hindi":
    st.title("🔌 ईवी चार्जिंग स्टेशन बुकिंग")
else:
    st.title("🔌 EV Charging Station Booking")


st.title(T['app_title'])

# Tabs
tab = st.sidebar.radio(T['select_view'], [T['map_view'], T['book_slot']])

if tab == T['map_view']:
    render_map(lang)
elif tab == T['book_slot']:
    render_booking_form(lang)
