class User:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.current_matches = []

    def place_bet(self, match):
        for m in self.current_matches:
            if match.match_id == m.match_id:
                break

        self.current_matches.append(match)
