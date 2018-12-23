import requests
from bs4 import BeautifulSoup
from model.match import Match
from model.pickem import Pickem


class ScheduleParser:
    match_counter = 0

    def __init__(self, week_as_int):
        # Create pickem instance
        self.pickem = Pickem()

        # Get page and pass it to bs4
        self.url = 'https://lol.gamepedia.com/EU_LCS/2018_Season/Summer_Season'
        self.page = requests.get(self.url)
        self.soup = BeautifulSoup(self.page.content, "html.parser")

        # Find relevant data
        self.schedule_table = self.soup.find('div', attrs={'class': 'tabs-dynamic'})
        self.weeks = self.schedule_table.find('div', attrs={'class': 'tabs-content'})
        self.week = self.weeks.find('div', attrs={'class': 'content' + str(week_as_int)}).find_all('tr')[2:]

    # Print given week
    def print_week(self):
        i = 0
        for x in self.week:
            teams = x.find_all('td')[1].find_all('div')[0].text
            result = x.find_all('td')[2].text.replace('\n', '')

            i += 1
            print(str(i) + ":" + teams + " Score: " + result)

    # Get matches as match-objects
    def get_matches(self):
        for x in self.week:
            ScheduleParser.match_counter += 1

            teams = x.find_all('td')[1].find_all('div')[0].text
            team1 = self.pickem.get_team(teams[:4].strip())
            team2 = self.pickem.get_team(teams[-5:].strip())
            result = x.find_all('td')[2].text.replace('\n', '')

            match = Match(team1, team2, self.match_counter)

            # Check winner
            if int(result[0]) > int(result[-1:]):
                match.winner = team1
                print(str(ScheduleParser.match_counter) + ': ' + team1.name + ' won! Score: ' + str(team1.score))
            elif int(result[0]) < int(result[-1:]):
                match.winner = team2
                print(str(ScheduleParser.match_counter) + ': ' + team2.name + ' won! Score: ' + str(team2.score))
            else:
                print('No winner yet!')


for x in range(1, 10):
    sp = ScheduleParser(x)
    sp.get_matches()
