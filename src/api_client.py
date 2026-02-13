import requests

class OpenWeatherMapClient:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "http://api.openweathermap.org/data/2.5/"

    def get_weather(self, city):
        url = f'{self.base_url}weather?q={city}&appid={self.api_key}'
        response = requests.get(url)
        return response.json()

class IPGeolocationClient:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.ipgeolocation.io/ipgeo"

    def get_geolocation(self, ip):
        url = f'{self.base_url}?apiKey={self.api_key}&ip={ip}'
        response = requests.get(url)
        return response.json()