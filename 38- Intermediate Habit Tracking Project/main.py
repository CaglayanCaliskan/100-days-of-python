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
os.system('cls')
my_exercise = input('What did you today?')
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
print(exercises_response_list)
