"""
Advanced Python Arguments
*Args
**Kwargs

# Arguments with Default Values:
def my_function(a=1,b=2,c=3):
    #Do this with a
    #Then do this with b
    #Finally do this with c

my_function()

"""
"""
Graphical User Interface (GUI)

By use Tkinter: https://docs.python.org/3/library/tkinter.html#the-packer
"""
"""
*args: Many Positional Arguments
more: https://realpython.com/python-kwargs-and-args/

# Unlimited Arguments:
def add(*args): 
    for n in args: -> turn input into tuple
        print(n)

add(1, 2, 3, 4, 5)
# type(args) == tuple
"""
"""
**kwargs: Many  Keyworded Arguments:
more: https://realpython.com/python-kwargs-and-args/

def calculate(**kwargs): -> kwargs == keyword argument
    print(kwargs) -> turn input into dictionary

calculate(add=3, multiply=5)
type(kwargs) == dictionary

"""
from tkinter import *

window = Tk()
window.title('My First GUI Program')
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)  # padding_x and padding_y

def button_clicked():
    new_label = user_input.get()
    my_label.config(text=new_label)

# Label in tkinter

my_label = Label(text='I am a Label', font=('Arial', 20, 'bold'))

my_label['text'] = 'new text'  # or my_label.config(text='new text')
my_label.grid(column=0, row=0)
my_label.config(padx=20, pady=20)


# Button in tkinter: https://www.tutorialspoint.com/python/tk_button.htm
button = Button(text='Click me', command=button_clicked)
button.grid(column=1, row=1)
new_button = Button(text='New click me', command=button_clicked)
new_button.grid(column=2, row=0)

# Entry

user_input = Entry(width=10)
user_input.grid(column=3, row=2)



# ** grid() and pack() can not use together




window.mainloop()  # keep window open

"""
Other method in tkinter
"""
# from tkinter import *
#
# # Creating a new window and configurations
# window = Tk()
# window.title("Widget Examples")
# window.minsize(width=500, height=500)
#
# # Labels
# label = Label(text="This is old text")
# label.config(text="This is new text")
# label.pack()
#
#
# # Buttons
# def action():
#     print("Do something")
#
#
# # calls action() when pressed
# button = Button(text="Click Me", command=action)
# button.pack()
#
# # Entries
# entry = Entry(width=30)
# # Add some text to begin with
# entry.insert(END, string="Some text to begin with.")
# # Gets text in entry
# print(entry.get())
# entry.pack()
#
# # Text
# text = Text(height=5, width=30)
# # Puts cursor in textbox.
# text.focus()
# # Adds some text to begin with.
# text.insert(END, "Example of multi-line text entry.")
# # Get's current value in textbox at line 1, character 0
# print(text.get("1.0", END))
# text.pack()
#
#
# # Spinbox
# def spinbox_used():
#     # gets the current value in spinbox.
#     print(spinbox.get())
#
#
# spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
# spinbox.pack()
#
#
# # Scale
# # Called with current scale value.
# def scale_used(value):
#     print(value)
#
#
# scale = Scale(from_=0, to=100, command=scale_used)
# scale.pack()
#
#
# # Checkbutton
# def checkbutton_used():
#     # Prints 1 if On button checked, otherwise 0.
#     print(checked_state.get())
#
#
# # variable to hold on to checked state, 0 is off, 1 is on.
# checked_state = IntVar()
# checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
# checked_state.get()
# checkbutton.pack()
#
#
# # Radiobutton
# def radio_used():
#     print(radio_state.get())
#
#
# # Variable to hold on to which radio button value is checked.
# radio_state = IntVar()
# radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
# radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
# radiobutton1.pack()
# radiobutton2.pack()
#
#
# # Listbox
# def listbox_used(event):
#     # Gets current selection from listbox
#     print(listbox.get(listbox.curselection()))
#
#
# listbox = Listbox(height=4)
# fruits = ["Apple", "Pear", "Orange", "Banana"]
# for item in fruits:
#     listbox.insert(fruits.index(item), item)
# listbox.bind("<<ListboxSelect>>", listbox_used)
# listbox.pack()
# window.mainloop()
