from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class LoanApplication(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    farming_experience = db.Column(db.Integer, nullable=False)
    land_size = db.Column(db.Float, nullable=False)
    annual_income = db.Column(db.Float, nullable=False)
    loan_amount = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(50), default='Pending')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)