from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 15
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text='00:00')
    timer_label.config(text='Timer', fg=GREEN)
    checked_mark_label.config(text='')
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    reps += 1
    if reps % 8 == 0:  # if it's the 8th rep:
        timer_label.config(text='Break', fg=RED)
        count_down(long_break_sec)
    elif reps % 2 == 0:  # if it's the 2nd/4th/6th:
        timer_label.config(text='Break', fg=PINK)
        count_down(short_break_sec)
    else:  # if it's the 1st/3rd/5th/7 rep:
        timer_label.config(text='Work', fg=GREEN)
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f'0{count_sec}'
    if count_min < 10:
        count_min = f'0{count_min}'

    canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')
    if count > 0:
        timer = window.after(1000, count_down, count - 1)  # count down every 1.0 sec
    else:
        start_timer()
        checked_marks = ''
        work_sessions = math.floor(reps / 2)

        for _ in range(work_sessions):
            checked_marks += '✔️'
            checked_mark_label.config(text=checked_marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Tomato Timer')
window.config(padx=100, pady=50, bg=YELLOW)

"""
tkinter canvas widget: https://www.tutorialspoint.com/python/tk_canvas.htm
tkinter .after(): http://tcl.tk/man/tcl8.6/TclCmd/after.htm
dynamic typing in python -> python can change the data type variable after assign
more about python dynamic typing: https://stackoverflow.com/questions/11328920/is-python-strongly-typed
"""
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)

# image
tomato_image = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(106, 130, text="00:00", fill='white', font=(FONT_NAME, 30, 'bold'))
canvas.grid(column=1, row=1)

# label
timer_label = Label(text='Timer', font=(FONT_NAME, 35, 'bold'), padx=150, pady=20, bg=YELLOW, fg=GREEN)
timer_label.grid(column=1, row=0)

checked_mark_label = Label(text='', font=(FONT_NAME, 15, 'bold'), padx=15, pady=15, bg=YELLOW, fg=GREEN)
checked_mark_label.grid(column=1, row=3)

# button
start_btn = Button(text='Start', font=(FONT_NAME, 10, 'bold'), bg=YELLOW, highlightthickness=0, command=start_timer)
start_btn.grid(column=0, row=2)

reset_btn = Button(text='Reset', font=(FONT_NAME, 10, 'bold'), bg=YELLOW, highlightthickness=0, command=reset_timer)
reset_btn.grid(column=2, row=2)

window.mainloop()
