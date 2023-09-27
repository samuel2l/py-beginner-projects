from quiz_oop_brain import *
from quiz_oop_data import *


class Question:
    def __init__(self, qu, ans):
        self.qu = qu
        self.ans = ans


# q1= Question("my question","answer")
question_bank = []
for i in question_data:
    text = i["question"]
    answer = i["correct_answer"]
    qu_x_ans = Question(text, answer)
    question_bank.append(qu_x_ans)

print(question_bank)

quiz = QuizBrain(question_bank)


quiz.next_qu()
