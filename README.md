# EV-Buddy-Streamlit-Firebase-
A web-based EV support app using Streamlit + Firebase or MongoDB Atlas
# ───────────── README.md ─────────────
# EV Buddy – Your Charging Companion

## 🔧 Features
- Real-time charging station map
- Booking system
- Hindi + English support
- Firebase Firestore integration

## 🚀 Setup Instructions
1. Clone the repo
2. Install requirements: `pip install -r requirements.txt`
3. Add your `firebase_config.json` under `db_config/`
4. Run with: `streamlit run app/main.py`

## 🗺️ Map API
- Uses Streamlit + Pydeck for basic map (can be extended to Google Maps)

## 🔗 Firebase
- Firestore structure:
  - `stations`: station metadata
  - `bookings`: user bookings

## 📁 Folder Structure
- `app/`: all logic
- `data/`: dummy JSON/CSV
- `db_config/`: firebase config
- `docs/`: architecture
