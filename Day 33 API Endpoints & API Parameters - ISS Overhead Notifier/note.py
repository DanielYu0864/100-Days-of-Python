"""
API (application programming interface) in python
"""
"""
Working with responses: HTTP Codes, Exceptions & JSON Data
1XX: Hold on
2XX: Here you go
3XX: Go Away
4XX: You fuck up
5XX: I as a server, fuck up
"""
import requests
from datetime import datetime

# # use requests package to get api info
# iss_response = requests.get('http://api.open-notify.org/iss-now.json')
# # to get error code if status code != 200
# iss_response.raise_for_status()
# # to get status code
# print(iss_response.status_code)
# # requests.json() to get json data
# print(iss_response.json())
# data = iss_response.json()['iss_position']
# print(data)
# longitude = data['longitude']
# latitude = data['latitude']
# iss_position = (latitude, longitude)
# print(iss_position)
#
#
#
# # get iss sunset info from https://sunrise-sunset.org/api
# sunset_response = requests.get(f'https://api.sunrise-sunset.org/json?lat={latitude}&lng={longitude}&formatted=0')
# sunset_response.raise_for_status()
# data = sunset_response.json()
# sunrise = data['results']['sunrise']
# sunset = data['results']['sunset']
# print(sunset, sunrise)
#



# get seattle sunset info
seattle_position = {
    'lat': 47.606209,
    'lng': -122.332069,
    'formatted': 0
}
seattle_sunset_api = requests.get('https://api.sunrise-sunset.org/json', params=seattle_position)
seattle_sunset_api.raise_for_status()
data = seattle_sunset_api.json()
sunrise = data['results']['sunrise']
sunset = data['results']['sunset']

sunrise_hour = sunrise.split('T')[1].split(':')[0]
sunset_hour = sunset.split('T')[1].split(':')[0]

time_now = datetime.now()

print(time_now)

