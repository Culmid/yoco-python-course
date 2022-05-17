from operator import itemgetter
import os
import requests
from dotenv import load_dotenv


def weather() -> None:
    try:
        # Get Geo-Location from IP
        response = requests.request("GET", "http://ipwho.is/").json()
        country, region, city, lat, lon = itemgetter(
            "country", "region", "city", "latitude", "longitude")(response)
    except Exception as e:
        print(e)

    load_dotenv()
    API_KEY = os.getenv("X-RapidAPI-Key")

    try:
        url = "https://community-open-weather-map.p.rapidapi.com/weather"

        querystring = {"lat": lat, "lon": lon, "units": "metric"}

        headers = {
            "X-RapidAPI-Host": "community-open-weather-map.p.rapidapi.com",
            "X-RapidAPI-Key": API_KEY
        }

        response = requests.request(
            "GET", url, headers=headers, params=querystring).json()

        weather, temp, wind, cloud = itemgetter(
            "weather", "main", "wind", "clouds")(response)
    except Exception as e:
        print(e)

    weather = weather[0]
    print(f"{city}, {region}, {country}:")
    print("-" * 100)
    print(f"Weather: {weather['main']} -> {weather['description']}")
    print(f"Temperature:")
    print(f"\tCurrent: {temp['temp']}°C | Feels Like: {temp['feels_like']}°C")
    print(f"\tMin: {temp['temp_min']}°C | Max: {temp['temp_max']}°C")
    print(f"\tHumidity: {temp['humidity']}%")
    print(f"Wind: {round(float(wind['speed']) * 3.6, 2)} km/h {wind['deg']}°")
    print(f"Cloud Coverage: {cloud['all']}%")


if __name__ == "__main__":
    weather()
