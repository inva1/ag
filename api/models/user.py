from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    phone_number = db.Column(db.String(15), unique=True, nullable=False)
    full_name = db.Column(db.String(100), nullable=False)
    user_type = db.Column(db.String(20), nullable=False)  # Farmer, Buyer, Supplier
    location = db.Column(db.String(255), nullable=False)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    preferred_language = db.Column(db.String(10), nullable=False)
    farming_experience = db.Column(db.Integer)
    land_size = db.Column(db.Float)
    annual_income = db.Column(db.Float)
    crops_grown = db.Column(db.String(255))