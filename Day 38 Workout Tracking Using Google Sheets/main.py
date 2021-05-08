import requests
import datetime
from decouple import config  # config to get variable from .env file



GENDER = 'male'
WEIGHT_KG = 77
HEIGHT_CM = 177
AGE = '25'

API_KEY = config('NUTRITIONIX_API_KEY')
API_ID = config('NUTRITIONIX_API_ID')

nutritionix_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'

exercise_text = input('The exercises you did: ')

headers = {
    'x-app-id': API_ID,
    'x-app-key': API_KEY
}

request_body = {
    'query': exercise_text,
    'gender': GENDER,
    'weight_kg': WEIGHT_KG,
    'height_cm': HEIGHT_CM,
    'age': AGE
}

response = requests.post(url=nutritionix_endpoint, json=request_body, headers=headers)
result = response.json()['exercises']

date = datetime.datetime.now()
date_today = date.strftime('%d/%m/%Y')
time_now = date.strftime('%X')


exercise_list = []
for dict in result:
    print(dict)
    exercise_dict = {
        'date': date_today,
        'time': time_now,
        'exercise': dict['name'].title(),
        'duration': dict['duration_min'],
        'calories': dict['nf_calories']
    }
    exercise_list.append(exercise_dict)

print(exercise_list)



sheety_api_url = config('SHEETY_API_URL')
sheety_headers = {
    'Authorization': 'Basic ZGFuaWVseXU3NDpsYWtzZGpmMjkwam9va2FqMjBqbGtqQVNHajglJFI='
}

sheety_username = config('SHEETY_USERNAME')
sheety_password = config('SHEETY_PASSWORD')

for dict in exercise_list:
    print(dict)
    sheety_request_body = {
        'workout': dict
    }

    response = requests.post(url=sheety_api_url, json=sheety_request_body, auth=(sheety_username, sheety_password))
    print(response.json())