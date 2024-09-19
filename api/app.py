from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from services.ussd_handler import handle_ussd_request
#from models import db

db = SQLAlchemy()

app = Flask(__name__)

# Configure the app and database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///agrolink.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route('/', methods=['POST', 'GET'])
def ussd():
    session_id = request.form.get('sessionId')
    phone_number = request.form.get('phoneNumber')
    text = request.form.get('text')
    
    response = handle_ussd_request(session_id, phone_number, text)
    return response

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create the database tables
    app.run(debug=True)
