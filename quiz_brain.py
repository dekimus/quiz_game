
class QuizBrain:
    def __init__(self, lista) -> None:
        self.question_number = 0
        self.question_list = lista
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def nextQuestion(self):
        question = self.question_list[self.question_number]
        self.question_number += 1
        print(question.category)
        answer = input(f"Q{self.question_number}. {question.text}?: (True/False) ")
        self.check_answer(answer, question.answer)
    
    def check_answer(self, ans, correct):
        if ans.lower() == correct.lower():
            self.score += 1
            print("You are right.")
        else:
            print("Thats wrong.")
        print(f"The correct answer was: {correct}.")
        print(f"Your current score is {self.score}/{self.question_number}.\n")
