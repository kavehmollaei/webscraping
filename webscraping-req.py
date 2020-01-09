import requests
from bs4 import BeautifulSoup


url = 'https://en.wikipedia.org/wiki/George_Orwell'
r = requests.get(url)
#print(r.text)
soup = BeautifulSoup(r.text,'html.parser')
title_soup = soup('h1',{'id':'firstHeading'})
#print(title[0].get_text())
title_text=title_soup[0].string



informational_books = {}
informational_books['title'] = title_text
print(informational_books)
info_soup = soup('div',{'id':'mw-content-text'})
#for i in info_soup:
#    print(i.get_text())

text_all =info_soup[0].get_text()
text_all_list=text_all.split('\n')
#print(text_all_list)
description = '' 
for i in text_all_list[1:4]:
    description +=i
informational_books['description'] = description
print(informational_books)