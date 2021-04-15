class QuizBrain:

    def __init__(self, q_input):
        self.user_score = 0
        self.question_number = 0
        self.question_list = q_input

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_q = self.question_list[self.question_number]
        self.question_number += 1
        user_input = input(f"Q.{self.question_number} : {current_q.text} (True/False): ")
        self.check_answer(user_answer=user_input, correct_answer=current_q.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.user_score += 1
            print('You got it right!')
        else:
            print('You got it wrong.')
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.user_score}/{self.question_number}")
        print("\n")

    def final_score(self):
        if self.question_number == len(self.question_list):
            print("You've completed the quiz!")
            print(f"Your final score was: {self.user_score}/{self.question_number}")

# todo: asking the questions ☑️
# todo: checking if the answer was correct ☑️
# todo: checking if we're the end of the quiz ☑️



