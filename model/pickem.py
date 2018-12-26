from model.team import Team
from model.match import Match


class Pickem:
    teams = {}
    matches = []
    users = []

    def __init__(self):
        print('Pickem init...')

    # Get team from key, creates new if none exists
    @staticmethod
    def get_team(key):
        # Check if team already exists, if not create new
        try:
            Pickem.teams[key]
        except KeyError as e:
            new_team = Team(key)
            Pickem.teams[key] = new_team

        return Pickem.teams[key]

    # TODO Get user or create new one?
    def get_user(self, username):
        print('TODO!')
