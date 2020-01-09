import requests
from bs4 import BeautifulSoup


url = 'https://www.gajmarket.com/'
r = requests.get(url)

soup = BeautifulSoup(r.text,'html.parser')
title_soup = soup.find_all('.slick-slide')

print(title_soup)
