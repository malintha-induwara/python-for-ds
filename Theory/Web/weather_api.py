import requests

base_url = "https://api.open-meteo.com/v1/forecast"

def fetch_weather_data(latitude, longitude):    
    params = {
        'latitude': latitude, 
        'longitude': longitude, 
        'current': 'temperature_2m,windspeed_10m'  
    }
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        return response.json()
    else:
        return None

def parse_weather_data(data):
    if data :
        current = data['current']
        print(current['temperature_2m_min'])
        # print(current.get('windspeed_10m'))
    
    else:
        print("No weather data available")


result = fetch_weather_data(12.9716, 77.5946)
if result:
    print('API call successful')
    parse_weather_data(result)
else:
    print('API call failed')
