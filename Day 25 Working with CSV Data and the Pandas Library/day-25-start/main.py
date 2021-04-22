"""
CSV: Comma Separated Values -> each data separated by comma
Pandas library
"""
# with open('weather_data.csv') as data_file:
#     data = data_file.readlines()

# import csv  # https://docs.python.org/3/library/csv.html
#
# with open('weather_data.csv') as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1].isdigit():
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas  # https://pandas.pydata.org/

data = pandas.read_csv('weather_data.csv')
# print(type(data))
# print(data['temp'])  # pandas take first row to be the name of each column

data_dict = data.to_dict()  # https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_dict.html?highlight=to_dict#pandas.DataFrame.to_dict
# print(data_dict)

temp_list = data['temp'].to_list()  # https://pandas.pydata.org/docs/reference/api/pandas.Series.to_list.html?highlight=to_list#pandas.Series.to_list
# print(temp_list)
average_temp = data['temp'].mean()  # https://pandas.pydata.org/docs/reference/api/pandas.Series.mean.html?highlight=mean#pandas.Series.mean
# print(average_temp)
max_temp = data['temp'].max()  # https://pandas.pydata.org/docs/reference/api/pandas.Series.max.html?highlight=series%20max#pandas.Series.max
# print(max_temp)

""" Get Data in Columns
# data['col_name'] == data.col_name
"""
# print(data.condition)

""" Get Data in Row
# data[data.col_name] == 'row_name/filter_condition_name'
"""
# print(data[data.day == 'Monday'])
# print(data[data.temp == max_temp])

monday = data[data.day == 'Monday']
# print(monday.condition)
monday_temp_celsius = monday.temp
monday_temp_fahrenheit = (monday_temp_celsius * 9/5) + 32
# print(monday_temp_fahrenheit)

""" Create a dataframe from scratch
"""
student_dict = {
    'students': ['Amy', 'James', 'Angela'],
    'scores': [76, 56, 65]
}
student_data = pandas.DataFrame(student_dict)
# student_data.to_csv('new_data.csv')  # https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html?highlight=to_csv#pandas.DataFrame.to_csv

"""
create a csv file: squirrel_count -> col: Primary Fur Color: Gray, Cinnamon, Black
Fur Color, Count
gray, int
red, int
black, int
"""
squirrel_data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
squirrel_color_list = squirrel_data['Primary Fur Color']
gray_squirrels = squirrel_data[squirrel_color_list == 'Gray']
red_squirrels = squirrel_data[squirrel_color_list == 'Cinnamon']
black_squirrels = squirrel_data[squirrel_color_list == 'Black']
squirrel_color_count = {
    'Fur Color': ['Gray', 'Cinnamon', 'Black'],
    'Count': [len(gray_squirrels), len(red_squirrels), len(black_squirrels)]
}
# print(squirrel_color_count)
color_data_dict = pandas.DataFrame(squirrel_color_count)
color_data_dict.to_csv('squirrel_count.csv')

