import requests
api_key = "5f4ed2e892ddd9ac2db91866cea160e3"
web = "https://api.openweathermap.org/data/2.5/onecall"

parameters = {
    "lat": 38.42,
    "lon": 27.14,
    "exclude": "daily,minutely,current",
    "appid": api_key
}

response = requests.get(web, params=parameters)

weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False


for hour_data in weather_slice:
    condition_code = (hour_data["weather"][0]["id"])
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    print("bring an umbrella")
