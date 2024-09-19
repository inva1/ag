import requests
from config import SOIL_API_KEY, PEST_API_KEY

def get_agricultural_advice(selection):
    if len(selection) == 1:
        return "CON Enter crop name for specific advice:"
    else:
        crop_name = selection[1]
        advice = ""

        # Fetch weather data
        weather_response = requests.get(f'http://api.weatherapi.com/v1/current.json?key={WEATHER_API_KEY}&q=Nigeria')
        if weather_response.status_code == 200:
            weather_data = weather_response.json()
            current_weather = weather_data['current']['condition']['text']
            advice += f"Current Weather: {current_weather}\n"
        
        # Fetch pest and disease alerts
        pest_response = requests.get(f'http://pestapi.com/v1/alerts?crop={crop_name}&key={PEST_API_KEY}')
        if pest_response.status_code == 200:
            pest_data = pest_response.json()
            pest_alerts = pest_data.get('alerts', [])
            advice += "Pest Alerts:\n"
            for alert in pest_alerts:
                advice += f"{alert['pest']} - {alert['description']}\n"
        
        # Fetch soil health recommendations
        soil_response = requests.get(f'http://soilapi.com/v1/health?crop={crop_name}&key={SOIL_API_KEY}')
        if soil_response.status_code == 200:
            soil_data = soil_response.json()
            soil_health = soil_data.get('health', 'Optimal')
            advice += f"Soil Health: {soil_health}\n"
        
        return f"END {advice if advice else 'No advice available for this crop.'}"