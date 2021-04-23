
"""
# For Loop
numbers = [1, 2, 3]
new_list = []
for n in number:
    add_1 = n + 1
    new_list.append(add_1)

# List Comprehension: work on list, string
1. new_list = [new_item for item in list]
2. Condition: The condition is like a filter that only accepts the items that valuate to True.
EX: new_list = [expression for item in iterable if condition == True]
3. Iterable: The iterable can be any iterable object, like a list, tuple, set etc. 
EX: new_list = [x for x in range(10)]
more: https://www.w3schools.com/python/python_lists_comprehension.asp
EX: 1.
    numbers = [1, 2, 3]
    new_list = [n + 1 for n in numbers]
    2. turn string into list
    name = "Angela"
    new_name_list = [letter for letter in name] // ['A', 'n', 'g', 'e', 'l', 'a']

Python Sequences: list, range, string, tuple
"""
"""
Dictionary Comprehension:  {key: value for (key, value) in iterable}
more: https://www.geeksforgeeks.org/python-dictionary-comprehension/
EX:
    1. new_dict = {new_key:new_value for item in list}
    2. new_dict = {new_key:new_value for (key,value) in dict.items()}
    3. new_dict = {new_key:new_value for (key,value) in dict.items() if test}
"""
"""
# Pandas DataFrame with Dict Comprehension
EX:
    data = pandas.DataFrame(dict)
    # loop through a data frame 
    for (key, value) in data.items():
        print(key)
    # loop through rows of a data frame: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.iterrows.html?highlight=iterrows#pandas.DataFrame.iterrows
    for (index, row) in data.iterrows(): 
        print(row)
"""