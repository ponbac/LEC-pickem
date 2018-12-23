import requests
from bs4 import BeautifulSoup

# Get page and pass it to bs4
url = 'https://lol.gamepedia.com/EU_LCS/2018_Season/Summer_Season'
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")

# Find relevant data
schedule_table = soup.find('div', attrs={'class': 'tabs-dynamic'})
weeks = schedule_table.find('div', attrs={'class': 'tabs-content'})
week1 = weeks.find('div', attrs={'class': 'content1'})
matches = week1.find_all('tr')[2:]

[type(item) for item in weeks]

# print(matches.text)

i = 0
for x in matches:
    teams = x.find_all('td')[1].find_all('div')[0].text
    result = x.find_all('td')[2].text.replace('\n', '')

    i += 1
    print(str(i) + ":" + teams + " Score: " + result)
