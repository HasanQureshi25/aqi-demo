import requests

API_KEY = "api key from website" #https://aqicn.org/data-platform/token/

CITY = "delhi"

def get_air_quality(city):
    url = f"https://api.waqi.info/feed/
    {city}/?token={API_KEY}"
    response = requests.get(url)
    data = response.json()


    if data["status"] == "ok":
        aqi = data["data"]["aqi"]
        print(f"\n City: {city.capitalize()}")
        print(f" AQI: {aqi}")

        if aqi <=50:
            print("Good 🟢")
        elif aqi <= 100:
            print("Moderate 🟡")
        elif aqi <= 150:
            print("unhealthy for some peoples 🟠")
        elif aqi <= 200:
            print("unhealthy 🔴")
        elif aqi <= 300:
            print("Very hazardous 🟣")
    else:
        print("Error:Could not fetch data. Try another city.")

get_air_quality(CITY)