class Match:
    def __init__(self, team_one, team_two):
        self.team_one = team_one
        self.team_two = team_two
        self.winner = None

    def get_winner(self):
        return self.winner

    def set_winner(self, winner):
        self.winner = winner
