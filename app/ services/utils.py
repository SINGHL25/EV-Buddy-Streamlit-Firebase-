# ───────────── app/services/utils.py ─────────────

def validate_booking(name, station_id, slot_time):
    """
    Simple validation for booking form fields.
    """
    if not name or not station_id or not slot_time:
        return False, "All fields are required."
    return True, ""

def translate(text_key, lang_dict):
    """
    Utility to translate a key using selected language dictionary.
    """
    return lang_dict.get(text_key, text_key)

