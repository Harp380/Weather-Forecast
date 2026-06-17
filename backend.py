import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")


def get_data(place, forecast_days, kind):
    geo_url = f"http://api.openweathermap.org/geo/1.0/direct?q={place}&limit=1&appid={API_KEY}"
    try:
        geo_response = requests.get(geo_url)
        geo_response.raise_for_status()
        geo_data = geo_response.json()

        if not geo_data:
            return [], []

        lat = geo_data[0]["lat"]
        lon = geo_data[0]["lon"]

        forecast_url = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API_KEY}&units=imperial"
        forecast_response = requests.get(forecast_url)
        forecast_response.raise_for_status()
        data = forecast_response.json()

        num_intervals = forecast_days * 8
        filtered_data = data["list"][:num_intervals]

        dates = [item["dt_txt"] for item in filtered_data]

        if kind == "Temperature":
            values = [item["main"]["temp"] for item in filtered_data]
        elif kind == "Sky":
            values = [item["weather"][0]["main"] for item in filtered_data]
        else:
            values = []

        return dates, values

    except requests.exceptions.RequestException:
        return [], []