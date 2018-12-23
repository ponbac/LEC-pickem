import math


class Match:
    def __init__(self, team_one, team_two, match_id):
        self.team_one = team_one
        self.team_two = team_two
        self.winner = None
        self.team_difference = abs(team_one.score - team_two.score)
        self.favorite = team_one if team_one.score >= team_two.score else team_two
        self.match_id = match_id

    @property
    def winner(self):
        return self._winner

    @winner.setter
    def winner(self, team):
        if team == self.team_one or team == self.team_two:
            self._winner = team
        else:
            if team is not None:
                raise ValueError('Winning team not part of match!')

    def reward(self, picked_team):
        if self.winner is None:
            raise SystemError('Match does not have a winner!')

        if picked_team == self.winner:
            r = self.team_difference / 4

            if r > 1 and picked_team != self.favorite:
                return math.ceil(r)
            else:
                return 1
        else:
            return 0
