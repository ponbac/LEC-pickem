import requests
from bs4 import BeautifulSoup

# Get page and pass it to bs4
url = 'https://lol.gamepedia.com/EU_LCS/2018_Season/Summer_Season'
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")

# Find relevant data
schedule_table = soup.find_all('div', attrs={'style': 'width:280px;display:table;table-layout:fixed;'})

[type(item) for item in schedule_table]

i = 0
for x in schedule_table:
    i += 1
    print(str(i) + ": " + x.text)
