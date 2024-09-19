from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# You can import models here if needed
from models.user import User
from models.loan_application import LoanApplication
from models.market_data import MarketData, MarketListing