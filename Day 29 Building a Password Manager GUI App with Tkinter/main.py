from tkinter import *
from tkinter import messagebox  # messagebox is variable not class
from random import randint, choice, shuffle
import pyperclip  # https://pypi.org/project/pyperclip/


FONT = ("Courier", 13, 'bold')
INIT_EMAIL = 'adam741963@gmail.com'


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
def generator_password():
    # random.choice(list), random.randint(str, end)
    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(1, 5))]
    password_list += [choice(numbers) for _ in range(randint(3, 6))]

    shuffle(password_list)

    random_password = ''.join([str(ele) for ele in password_list])

    print(f"Your password is: {random_password}")
    password_entry.delete(0, END)
    password_entry.insert(END, random_password)
    pyperclip.copy(random_password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def data_save():
    website = website_entry.get()
    email = username_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="You fucking moron piece of shit", message="Don't leave any empty")
        return
    # message box .askokcancel() => return boolean
    is_ok_to_save = messagebox.askokcancel(title=website, message=f'These are the details entered: \nEmail: {email} \n Password: {password} \nIs it ok to save?')

    if is_ok_to_save:
        with open('password_file.txt', mode='a') as file:
            file.write(f'{website} | {email} | {password}\n')

        # clear all input
        website_entry.delete(0, END)
        password_entry.delete(0, END)
        # reset email to initial email
        username_entry.delete(0, END)
        username_entry.insert(END, INIT_EMAIL)


# ---------------------------- UI SETUP ------------------------------- #
# grid = 3 col *5 row
window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)

# image
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100, 120, image=logo_img)
canvas.grid(column=1, row=0)

# label
website_label = Label(text='Website: ', font=FONT, pady=10)
website_label.grid(column=0, row=1)

username_label = Label(text='Email/Username: ', font=FONT, pady=10)
username_label.grid(column=0, row=2)

password_label = Label(text='Password: ', font=FONT, pady=10)
password_label.grid(column=0, row=3)

# entries
website_entry = Entry(width=64)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

username_entry = Entry(width=64)
username_entry.insert(END, INIT_EMAIL)
username_entry.grid(column=1, row=2, columnspan=2)

password_entry = Entry(width=33)
password_entry.grid(column=1, row=3)

# button
generate_p_btn = Button(text='Generate Password', font=FONT, highlightthickness=0, command=generator_password)
generate_p_btn.grid(column=2, row=3)

add_btn = Button(text='Add', font=FONT, command=data_save)
add_btn.config(width=38)
add_btn.grid(column=1, row=4, columnspan=2)

window.mainloop()
