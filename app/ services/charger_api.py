# ───────────── app/services/charger_api.py ─────────────
from app.services.firebase_service import db

def get_all_stations():
    docs = db.collection("stations").stream()
    return [{**doc.to_dict(), "id": doc.id} for doc in docs]

def book_slot(name, station_id, slot_time):
    try:
        db.collection("bookings").add({
            "name": name,
            "station_id": station_id,
            "slot_time": slot_time
        })
        return True
    except:
        return False
