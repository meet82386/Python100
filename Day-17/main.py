from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

questions = [Question(i["question"], i["correct_answer"]) for i in question_data]

quiz_brain = QuizBrain(questions)

while quiz_brain.still_has_questions():
    quiz_brain.next_question()

