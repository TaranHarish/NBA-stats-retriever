# NBA Web Scraping Project

from urllib.request import urlopen
from pandas import DataFrame
from pyparsing import results
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import requests

url = "https://www.basketball-reference.com/leagues/NBA_2021_totals.html"
html = urlopen(url)
soup = BeautifulSoup(html, "html.parser")

response = requests.get(url)
web_page = response.text
soup = BeautifulSoup(web_page, "html.parser")
site_title = soup.title.string
print(f"\nFrom {site_title}\n")

soup.findAll('tr', limit=2)
headers = [th.getText() for th in soup.findAll('tr', limit=2)[0].findAll('th')]
headers = headers[1:]

rows = soup.findAll('tr')[1:]
player_stats = [[td.getText() for td in rows[i].findAll('td')]
                for i in range(len(rows))]

stats = pd.DataFrame(player_stats, columns=headers)
stats.head(10)
print(stats)

# header = soup.find(class_="thead")
# column_title = [header.text for item in header][0]
# print(column_title)

# column_title_C = column_title.replace("\n",",").split(",")[2:-1]

# table = soup.find_all(class_="full_table")
# print(table)

# players = []
# for i in range(len(table)):

# player_ = []

# for td in table[i].find_all("td"):
# player_.append(td.text)

# players.append(player_)

# df = pd.DataFrame(players, columns=column_title_C).set_index("Players")
