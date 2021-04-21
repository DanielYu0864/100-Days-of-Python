# open() in python: https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
with open('my_file.txt') as file:  # with statement  https://www.geeksforgeeks.org/with-statement-in-python/
    contents = file.read()
    print(contents)
''' auto close when exist "with" statement '''

'''
# file = open('my_file.txt')  # https://docs.python.org/3/library/functions.html?highlight=open#open
# file.close()  # https://www.tutorialspoint.com/python/file_close.htm
'''
"""
character in open(filename, mode=)
'r' -> open for reading(default)
'w' -> open for writing, truncating the file first (create the if if it doesn't exists)
'a' -> open for writing, appending to the end of file if it exists
"""

with open('new_file.txt', mode='w') as file:  # change the mode to write to write the file (init 'r' as read only)
    file.write('Hello World!\nHow are you?')

with open('my_file.txt', mode='w') as file:  # change the mode to write to write the file (init 'r' as read only)
    file.write('Hello World!\nnew text 1')

with open('my_file.txt', mode='a') as file:
    file.write('\nnew text 2')
