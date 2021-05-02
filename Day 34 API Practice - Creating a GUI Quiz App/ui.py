from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ('Arial', 15, 'italic')


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(bg=THEME_COLOR, padx=5, pady=5, width=340, height=700)
        # canvas
        self.canvas = Canvas(width=300, height=250, bg='White', highlightthickness=0)
        self.quiz_text = self.canvas.create_text(150, 125, text='a', width=280, fill=THEME_COLOR, font=FONT)
        self.canvas.grid(column=0, row=1, columnspan=2, padx=20, pady=20)
        # score board
        self.score_board = Label(text='Score: 0', font=FONT, bg=THEME_COLOR, fg='White')
        self.score_board.grid(column=1, row=0, padx=20, pady=20)
        # true button
        self.true_image = PhotoImage(file='images/true.png')
        self.true_btn = Button(image=self.true_image, highlightthickness=0, command=self.true_pressed)
        self.true_btn.grid(column=0, row=2, padx=10, pady=10)
        # false button
        self.false_image = PhotoImage(file='images/false.png')
        self.false_btn = Button(image=self.false_image, highlightthickness=0, command=self.false_pressed)
        self.false_btn.grid(column=1, row=2, padx=10, pady=10)
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.score_board.config(text=f'Score: {self.quiz.score}')
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.quiz_text, text=q_text, fill=THEME_COLOR)
        else:
            self.canvas.itemconfig(self.quiz_text, text=f'The Quiz end', fill=THEME_COLOR)
            self.true_btn.config(state='disabled')
            self.false_btn.config(state='disabled')

    def true_pressed(self):
        is_right = self.quiz.check_answer('True')
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer('False')
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='Green')
            self.canvas.itemconfig(self.quiz_text, fill='White')
        else:
            self.canvas.config(bg='Red')
            self.canvas.itemconfig(self.quiz_text, fill='White')

        self.window.after(1000, self.get_next_question)