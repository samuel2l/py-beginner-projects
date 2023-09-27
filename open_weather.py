import requests

api_key = "10a035ccccb3423c9f9848dd1d88d08f"

params = {
    "lat": 51.507351,
    "lon": -0.127758,
    "appid": api_key
}
response = requests.get(url="https://api.openweathermap.org/data/2.5/weather", params=params)
data = response.json()
response.raise_for_status()
weather = data["weather"][0]["main"]
description = data["weather"][0]["description"]
temp = data["main"]["temp"]
temp_min = data["main"]["temp_min"]
temp_max = data["main"]["temp_max"]
humidity = data["main"]["humidity"]
visibility = data["visibility"]

if weather == "Clear":
    print("Eno go rain today baba")
elif weather == "Rain":
    # send text message
    pass
else:
    pass
