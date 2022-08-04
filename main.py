from unicodedata import category
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for dic in question_data:
    text = dic["question"]
    answer = dic["correct_answer"]
    cat = dic["category"]
    q = Question(text, answer, cat)
    question_bank.append(q)
    

q = QuizBrain(question_bank)

while q.still_has_questions():
    q.nextQuestion()

print("You have completed the quest.")
print(f"Your final score is {q.score}/{q.question_number}.")