from data import question_data


class Question:
    """Model for question"""

    def __init__(self, question, answer):
        self.question = question
        self.answer = answer
