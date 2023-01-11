# import os
# import requests

# from dotenv import load_dotenv

# load_dotenv()

# token = os.getenv('PIXELA_TOKEN')


# os.system('cls')
# name = input('name?: ')
# last = input('last name?: ')
# email = input('email?: ')

# sheet_url = "https://api.sheety.co/75eeefdc1b0ff1eefcf921a509cfa181/flightTracking/users"

# headers = {
#     "Authorization": f"Bearer {token}"
# }

# body = {
#     "user": {
#         "firstName": name,
#         "lastName": last,
#         "email": email,
#     }}

# response = requests.post(url=sheet_url, json=body, headers=headers)
# print(response)
