from services.user import register_user
from services.agrocredit import handle_loan_application
from services.agromarket import fetch_market_data
from services.agroweather import get_weather_forecast
from services.agrotrade import list_produce, view_listings
from services.agroadvice import get_agricultural_advice

def handle_ussd_request(session_id, phone_number, text):
    if text == "":
        return ("CON Welcome to AgroLink. Choose a service:\n"
                "1. Register\n"
                "2. Apply for Loan\n"
                "3. Check Market Prices\n"
                "4. Weather Information\n"
                "5. Trade Produce\n"
                "6. Agricultural Advice")

    selection = text.split("*")
    
    if selection[0] == "1":
        # Register user logic
        if len(selection) == 1:
            return "CON Enter Full Name:"
        elif len(selection) == 2:
            return "CON Enter User Type (Farmer/Buyer/Supplier):"
        elif len(selection) == 3:
            return "CON Enter Location:"
        elif len(selection) == 4:
            return "CON Enter Preferred Language:"
        else:
            # Register user
            response = register_user(phone_number, selection[1], selection[2], selection[3], selection[4])
            return f"END {response}"
    
    elif selection[0] == "2":
        return handle_loan_application(selection)
    
    elif selection[0] == "3":
        return fetch_market_data(selection)
    
    elif selection[0] == "4":
        return get_weather_forecast(selection)
    
    elif selection[0] == "5":
        return list_produce(selection)
    
    elif selection[0] == "6":
        return get_agricultural_advice(selection)
    
    else:
        return "END Invalid option."