from models import db, User
from geopy.geocoders import Nominatim

def register_user(phone_number, full_name, user_type, location, language, experience=None, land_size=None, income=None, crops=None):
    geolocator = Nominatim(user_agent="agrolink")
    location_data = geolocator.geocode(location)
    
    user = User(
        phone_number=phone_number,
        full_name=full_name,
        user_type=user_type,
        location=location,
        latitude=location_data.latitude,
        longitude=location_data.longitude,
        preferred_language=language,
        farming_experience=experience,
        land_size=land_size,
        annual_income=income,
        crops_grown=crops
    )
    db.session.add(user)
    db.session.commit()

    return f"User {full_name} registered successfully."