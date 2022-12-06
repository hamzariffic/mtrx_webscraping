# Python program to scrape Jumia
# and save data from website
import requests
from bs4 import BeautifulSoup
import csv

URL = "https://www.pinterest.com/carlostorres18/hardcore-quotes/"
r = requests.get(URL)

soup = BeautifulSoup(r.content, 'html5lib')

quotes = []  # a list to store quotes

table = soup.find('div', attrs={'id': 'all_quotes'})

for row in table.findAll('div',
                         attrs={'class': 'col-6 col-lg-3 text-center margin-30px-bottom sm-margin-30px-top'}):
    quote = {'theme': row.h5.text, 'url': row.a['href'], 'img': row.img['src'], 'lines': row.img['alt'].split(" #")[0],
             'author': row.img['alt'].split(" #")[1]}
    quotes.append(quote)

filename = 'hardcore_quotes.csv'
with open(filename, 'w', newline='') as f:
    w = csv.DictWriter(f, ['theme', 'url', 'img', 'lines', 'author'])
    w.writeheader()
    for quote in quotes:
        w.writerow(quote)
