from bs4 import BeautifulSoup
import requests
from urllib.request import urlopen

url=requests.get("https://hlstats.panda-community.com/hlstats.php?game=tf53").text
soup = BeautifulSoup(url,'lxml')

player= soup.findAll(class_='game-table-cell')
print(player[4].text)