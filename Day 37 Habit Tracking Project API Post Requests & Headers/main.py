import requests
from datetime import datetime
# pixela: https://pixe.la/
# pixela api doc: https://docs.pixe.la

pixela_endpoint = 'https://pixe.la/v1/users'
pixela_profile = 'https://pixe.la/@kukuyu74'

TOKEN = 'token'
USERNAME = 'username'
GRAPH_ID = 'graph1'
user_params = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}
################################# Create user ###########################################
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

################################ Create graphs ###########################################
# graph_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs'
#
# graph_config = {
#     'id': GRAPH_ID,
#     'name': 'Coding Graph',
#     'unit': 'minutes',
#     'type': 'int',
#     'color': 'kuro'
# }
#
# headers = {
#     'X-USER-TOKEN': TOKEN
# }
#
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
#
# print(response.text)

####################################### post pixel #######################################
# graph_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}'
#
# # use datetime module to get current date: use strftime() method to format the date: https://www.w3schools.com/python/python_datetime.asp
# yesterday = datetime(2021, 5, 4) # https://www.w3schools.com/python/python_datetime.asp
# today = datetime.now()
#
# request_body = {
#     'date': today.strftime('%Y%m%d'),  # 'yyyymmdd'
#     'quantity': '300'
# }
#
# headers = {
#     'X-USER-TOKEN': TOKEN
# }
#
#
# response = requests.post(url=graph_endpoint, json=request_body, headers=headers)
# print(response.text)

########################### update pixel ######################################
# yesterday = datetime(year=2021, month=5, day=4).strftime('%Y%m%d')
#
# graph_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{yesterday}'
#
# request_body = {
#     'quantity': '300'
# }
#
# headers = {
#     'X-USER-TOKEN': TOKEN
# }
#
# response = requests.put(url=graph_endpoint, json=request_body, headers=headers)
# print(response.text)

################################# Delete graph #######################################
# yesterday = datetime(year=2021, month=5, day=4).strftime('%Y%m%d')
# graph_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{yesterday}'
#
# headers = {
#     'X-USER-TOKEN': TOKEN
# }
#
# response = requests.delete(url=graph_endpoint, headers=headers)
# print(response.text)

