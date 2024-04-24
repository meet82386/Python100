class QuizBrain:
    """Logic of quiz application"""

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        """Displays next question."""
        question = self.question_list[self.question_number]
        answer = input(f"Q. {self.question_number + 1}>  {question.question}  ")

        status = "Wrong"
        if answer.lower().strip() == question.answer.lower():
            self.score += 1
            status = "Correct"

        print(f"{status}. Score is {self.score}/{len(self.question_list)}")
        print()
        self.question_number += 1

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

