import os
from dotenv import load_dotenv
import requests
from datetime import datetime
load_dotenv()

nut_api = os.getenv('NUTRITION_API_KEY')
nut_id = os.getenv('NUTRITION_API_ID')
google_sheets = os.getenv('GOOGLESHEETS')
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
