"""
Flash Card Program: for study new language
Use Frequency Dictionary
"""
from tkinter import *
import pandas
from random import choice

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

try:
    word_data = pandas.read_csv('data/words_to_learn.csv')
    # read data from .csv file
except FileNotFoundError:
    og_word_data = pandas.read_csv('data/french_words.csv')
    to_learn = og_word_data.to_dict(orient='records')
else:
    to_learn = word_data.to_dict(orient='records')


# generator new word
def card_generator():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = choice(to_learn)
    canvas.itemconfig(card_title_text, text='French', fill='black')
    canvas.itemconfig(card_word_text, text=current_card['French'], fill='black')
    canvas.itemconfig(current_bg, image=card_front_bg)
    flip_timer = window.after(3000, flip_card)


# delay function
def flip_card():
    if current_card:
        canvas.itemconfig(card_title_text, text='English', fill='white')
        canvas.itemconfig(card_word_text, text=current_card['English'], fill='white')
        canvas.itemconfig(current_bg, image=card_back_bg)


def remove_card():
    to_learn.remove(current_card)
    new_dict = pandas.DataFrame(to_learn)
    new_dict.to_csv(path_or_buf='data/words_to_learn.csv', index=False)


# UI SETUP
window = Tk()
window.title('Flashy')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

# Canvas
canvas = Canvas(height=526, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_bg = PhotoImage(file='images/card_front.png')
card_back_bg = PhotoImage(file='images/card_back.png')
current_bg = canvas.create_image(400, 263, image=card_front_bg)
card_title_text = canvas.create_text(400, 150, text='Title', font=('Ariel', 40, 'italic'))
card_word_text = canvas.create_text(400, 263, text='Word', font=('Ariel', 60, 'bold'))
canvas.grid(row=0, column=0, columnspan=2)

# Button
right_img = PhotoImage(file='images/right.png')
right_btn = Button(image=right_img, pady=10, highlightthickness=0, command=lambda: [card_generator(), remove_card()])
right_btn.grid(row=1, column=1)

wrong_img = PhotoImage(file='images/wrong.png')
wrong_btn = Button(image=wrong_img, pady=10, highlightthickness=0, command=card_generator)
wrong_btn.grid(row=1, column=0)

window.mainloop()
