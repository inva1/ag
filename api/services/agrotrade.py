from models.market_data import MarketListing
from models import db

def list_produce(selection):
    if len(selection) == 1:
        return "CON Enter crop name to list for sale:"
    elif len(selection) == 2:
        return "CON Enter quantity (in kg):"
    elif len(selection) == 3:
        return "CON Enter price per kg (in Naira):"
    elif len(selection) == 4:
        return "CON Enter your location:"
    else:
        crop_name = selection[1]
        quantity = float(selection[2])
        price = float(selection[3])
        location = selection[4]
        
        listing = MarketListing(
            crop_name=crop_name,
            quantity=quantity,
            price=price,
            location=location
        )
        db.session.add(listing)
        db.session.commit()
        
        return f"END {crop_name} listed for sale successfully."

def view_listings(selection):
    if len(selection) == 1:
        return "CON Enter crop name to view available listings:"
    else:
        crop_name = selection[1]
        listings = MarketListing.query.filter_by(crop_name=crop_name).all()
        
        if listings:
            response = f"Available listings for {crop_name}:\n"
            for listing in listings:
                response += f"{listing.quantity} kg at {listing.price} Naira per kg - {listing.location}\n"
            return f"END {response}"
        else:
            return "END No listings available for this crop."