"""
# Error handling
    try: Something that might cause an exception
    except: Do this if there was an exception
    else: Do this if there were on exceptions
    finally: Do this no matter what happens
"""
try:
    file = open('a_file.txt')
    a_dict = {'key': 'value'}
    # print(a_dict['something not exist'])
except FileNotFoundError:  # The except clause(s) specify one or more exception handlers, never use except  without handler.
    file = open('a_file.txt', mode='w')  # create a file if doesn't exist
    file.write('Something')
except KeyError as error_massage:
    print(f'The key: {error_massage} does not exist.')
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print('File closed')

# usage of raise
height = float(input('Height: '))
weight = int(input('Weight: '))

if height > 3:
    raise ValueError('Human height should not be over 3 meters.')

bmi = weight / height ** 2
print(bmi)