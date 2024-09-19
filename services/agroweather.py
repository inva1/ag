import requests
from config import WEATHER_API_KEY

def get_weather_forecast(selection):
    if len(selection) == 1:
        return "CON Enter your location:"
    else:
        location = selection[1]
        response = requests.get(f'http://api.weatherapi.com/v1/forecast.json?key={WEATHER_API_KEY}&q={location}&days=5')
        
        if response.status_code == 200:
            data = response.json()
            current_weather = data['current']['condition']['text']
            today_temp = data['current']['temp_c']
            forecast = data['forecast']['forecastday']
            
            weather_info = (f"Today's Weather: {current_weather}, {today_temp}°C\n"
                            f"5-Day Forecast:\n")
            for day in forecast:
                date = day['date']
                condition = day['day']['condition']['text']
                max_temp = day['day']['maxtemp_c']
                min_temp = day['day']['mintemp_c']
                weather_info += f"{date}: {condition}, {min_temp}°C - {max_temp}°C\n"
            
            return f"END {weather_info}"
        else:
            return "END Failed to fetch weather data. Please try again later."