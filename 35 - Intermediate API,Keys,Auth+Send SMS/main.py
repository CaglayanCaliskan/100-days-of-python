import requests
api_key = "API KEY FROM SITE"
web = "https://api.openweathermap.org/data/2.5/onecall"

parameters = {
    "lat": 38.42,
    "lon": 27.14,
    "exclude": "current",
    "appid": api_key
}

response = requests.get(web, params=parameters)
data = response.json()
print(data)
