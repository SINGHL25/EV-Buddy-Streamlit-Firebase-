# ───────────── app/services/firebase_service.py ─────────────
import firebase_admin
from firebase_admin import credentials, firestore

def init_firebase():
    if not firebase_admin._apps:
        cred = credentials.Certificate("db_config/firebase_config.json")
        firebase_admin.initialize_app(cred)

db = firestore.client()
