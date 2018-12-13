from model.team import Team
from model.match import Match

team1 = Team('Fnatic')
team2 = Team('G2')

team1.score = 10
team2.score = -3

match = Match(team1, team2, 1337)
match.winner = team1

print('Fnatic: ' + str(match.reward(team1)))
print('G2: ' + str(match.reward(team2)))
