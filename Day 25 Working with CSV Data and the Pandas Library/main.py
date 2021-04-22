import turtle
import pandas

screen = turtle.Screen()
screen.title('U.S. States Game')
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)
states_data = pandas.read_csv('50_states.csv')
states_list = states_data.state

guess_list = []
num_right = 0
game_on = True


def check_answer(user_quess):
    for state in states_list:
        if state.lower() == user_quess:
            return True


def add_state(x, y, state):
    new_state = turtle.Turtle()
    new_state.hideturtle()
    new_state.penup()
    new_state.goto(x, y)
    new_state.write(f'{state.title()}', align='center', font=("Courier", 8, "normal"))


while game_on:
    answer_state = (
        screen.textinput(title=f'{num_right}/50 State Correct', prompt="What's another state's name?")).lower()

    if answer_state == "exit":
        missing_states = []
        for state in states_list:
            if state not in guess_list:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv('missing_states_to_learn.csv')
        break

    if check_answer(answer_state) and (answer_state.title() not in guess_list):
        guess_list.append(answer_state.title())
        num_right += 1
        state_pos = states_data[states_list == answer_state.title()]
        add_state(int(state_pos.x), int(state_pos.y), answer_state)

    if num_right == 50:
        game_on = False
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.write("You've got every state correct!", align='center', font=("Courier", 30, "normal"))

# states_to_learn.csv




def get_mouse_click_coor(x, y):
    print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()  # https://realpython.com/python-gui-tkinter/#:~:text=mainloop()%20tells%20Python%20to,prompt%20displayed%20in%20the%20shell.
