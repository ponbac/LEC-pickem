class Team:
    def __init__(self, name):
        self.name = name
        self.logo = None
        self.score = 0

    def add_loss(self):
        self.score -= 1

    def add_win(self):
        self.score += 1
