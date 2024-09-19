from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class MarketData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    crop_name = db.Column(db.String(100), nullable=False)
    price_per_kg = db.Column(db.Float, nullable=False)
    last_updated = db.Column(db.DateTime, nullable=False)
    
class MarketListing(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    crop_name = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Float, nullable=False)
    price = db.Column(db.Float, nullable=False)
    location = db.Column(db.String(255), nullable=False)
    seller_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)