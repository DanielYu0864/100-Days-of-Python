import requests
import os
from twilio.rest import Client
#  twilio: https://www.twilio.com/console
#  pythonanywhere: https://www.pythonanywhere.com/
#  openweather_api: https://openweathermap.org/
OMN_Endpoint = 'https://api.openweathermap.org/data/2.5/onecall'
api_key = 'openweathermap_api_key'
twilio_id = 'twilio_user_id'
auth_token = 'twilio_auth_token'
twilio_trail_number = '+twilio_phone_number'
my_phone = 'my_phone_number'
seattle_coordinates = {
    'lat': 38.9072,
    'lon': 77.0369,
    'exlude': 'current,minutely,hourly',
    'appid': api_key
}

response = requests.get(OMN_Endpoint,  params=seattle_coordinates)
response.raise_for_status()
data = response.json()
# get hourly data from 0 to 12 index
hour_list = data['hourly'][:12]
# get weather data from hour_list
hour_weather_list = [x['weather'][0] for x in hour_list]
# print(hour_list)
# print(len(hour_list))
# print(hour_weather_list)
will_rain = False

for dict in hour_weather_list:
    if dict['id'] < 700:
        will_rain = True
        break


if will_rain:
    client = Client(twilio_id, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain!☂",
        from_=twilio_trail_number,
        to=my_phone
    )
    print(message.status)


