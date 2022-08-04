from unicodedata import category


class Question:
    def __init__(self, text, answer, cat) -> None:
        self.text = text
        self.answer = answer
        self.category = cat