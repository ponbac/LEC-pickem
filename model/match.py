class Match:
    def __init__(self, team_one, team_two, match_id):
        self.team_one = team_one
        self.team_two = team_two
        self.winner = None
        self.match_id = match_id

    @property
    def winner(self):
        return self.winner

    @winner.setter
    def winner(self, team):
        if team == self.team_one or team == self.team_two:
            self.winner = team
        else:
            raise ValueError('Winning team not part of match!')

