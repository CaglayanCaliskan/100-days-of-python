import os
from tabnanny import check
from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
question_bank = []
for question in question_data:
    new_quest = Question(question["text"], question["answer"])
    question_bank.append(new_quest)

quiz = QuizBrain(question_bank)
os.system('cls')


while quiz.still_has_questions():
    answer = quiz.next_question()
quiz.final_score()
