from models.market_data import MarketData

def fetch_market_data(selection):
    if len(selection) == 1:
        return "CON Enter Crop Name to Check Price:"
    else:
        crop_name = selection[1]
        market_data = MarketData.query.filter_by(crop_name=crop_name).first()
        if market_data:
            return (f"END {crop_name} price per kg is {market_data.price_per_kg} Naira.\n"
                    f"Last updated on {market_data.last_updated}")
        else:
            return "END No data available for this crop."