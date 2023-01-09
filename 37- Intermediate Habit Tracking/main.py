import requests
from dotenv import load_dotenv
import os
from datetime import datetime
load_dotenv()

pixela_URL = "https://pixe.la"
token = os.getenv('PIXELA_TOKEN')
USERNAME = "caosfreemandev"

# 1

# user_params = {
#     "token": token,
#     "username": USERNAME,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes",
# }

# 2

# graph_params = {
#     "id": "ver-1",
#     "name": "Python_Lessons",
#     "unit": "commit",
#     "type": "int",
#     "color": "sora",
#     "timezone": "Europe/Istanbul",
#     "isSecret": False,
#     "publishOptionalData": True
# }

# 3

graph_header = {
    "X-USER-TOKEN": token
}

# graph_params = {
#     "date": datetime.today().strftime('%Y%m%d'),
#     "quantity": "7"
# }


# 1 - Create an Account
# response = requests.post(url=f"{pixela_URL}/v1/users", json=user_params)

# 2 - Create a Graph
# response = requests.post(
#     url=f"{pixela_URL}/v1/users/{USERNAME}/graphs", headers={"X-USER-TOKEN": token}, json=graph_params)

# 3 - Post value to the graph

# response = requests.post(
#     url=f"{pixela_URL}/v1/users/{USERNAME}/graphs/ver-1", headers=graph_header, json=graph_params)

# 4 - Get a pixel

# response = requests.get(
#     url=f"{pixela_URL}/v1/users/{USERNAME}/graphs/ver-1/20230107", headers={"X-USER-TOKEN": token})

# 5 - Update pixel

# response = requests.put(
#     url=f"{pixela_URL}/v1/users/{USERNAME}/graphs/ver-1/20230105", headers=graph_header, json={"quantity": "5"})

# 6 - Delete pixel

response = requests.delete(
    f"{pixela_URL}/v1/users/{USERNAME}/graphs/ver-1/20230105", headers=graph_header)

print(response.text)
