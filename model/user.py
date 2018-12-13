class User:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.current_matches = []

    def place_bet(self, match):
        unique = True

        for m in self.current_matches:
            if match.match_id == m.match_id:
                unique = False
                break

        if unique:
            self.current_matches.append(match)
        else:
            raise ValueError('Match already exists in users matches!')

    def increase_score(self, points_to_add):
        if points_to_add > 0:
            self.score += points_to_add
        else:
            raise ValueError('Invalid amount of points to add!')
