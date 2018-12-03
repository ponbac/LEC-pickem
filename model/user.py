class User:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def get_score(self):
        return self.score

    def set_score(self, new_score):
        self.score = new_score
