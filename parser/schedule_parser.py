import requests
from bs4 import BeautifulSoup
from model.match import Match


class ScheduleParser:
    def __init__(self, week_as_int):
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
        i = 0
        for x in self.week:
            i += 1

            teams = x.find_all('td')[1].find_all('div')[0].text
            team1 = teams[:4].strip()
            team2 = teams[-5:].strip()
            result = x.find_all('td')[2].text.replace('\n', '')

            match = Match(team1, team2, i)

            if result[0] == '1':
                print(team1 + " won!")
            elif result[-1:] == '1':
                print(team2 + ' won!')




sp = ScheduleParser(1)
sp.get_matches()
