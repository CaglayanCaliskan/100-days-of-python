import os
from dotenv import load_dotenv
import requests
from datetime import datetime
load_dotenv()

nut_api = os.getenv('NUTRITION_API_KEY')
nut_id = os.getenv('NUTRITION_API_ID')
google_sheets = os.getenv('GOOGLESHEETS')
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

today_date = datetime.today().strftime('%d/%m/%Y')
current_time = datetime.now().strftime('%H:%M:%S')

os.system('cls')

my_exercise = input('What did you today?')
# input example : ran 10km, swim 1km, cycling 45minutes

query = {
    "query": my_exercise,
    "gender": "male",
    "weight_kg": 83.5,
    "height_cm": 190,
    "age": 55
}

headers = {
    "x-app-id": nut_id,
    "x-app-key": nut_api,
}

response = requests.post(url=exercise_endpoint, headers=headers, json=query)
exercises_response_list = response.json()['exercises']


for exercise in exercises_response_list:

    body = {
        "datum": {
            "date": today_date,
            "time": current_time,
            "exercise": str(exercise['name']).capitalize(),
            "duration": int(exercise['duration_min']),
            "calories": int(exercise['nf_calories']),
        }
    }
    requests.post(url=google_sheets, json=body)


print('.')
print('...')
print('.....')
print('........')
print('..........')
print('Thanks, Your info added to googlesheets')
