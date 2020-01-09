import requests
from bs4 import BeautifulSoup

url = 'https://www.amazon.com/s?k=j+j+ballard&dc&ref=a9_sc_1'
#headers={'User-Agent':'my app.0.0.1','Accept-Language'
#:'en-En, en,q=.5'}
r = requests.get(url)


soup = BeautifulSoup(r.text,'html.parser')
#print(soup)
title_soup = soup.select('.s-image')
print(title_soup)

for i in title_soup:
    print(i.get_text())



#soup = BeautifulSoup(r.text,'html.parser')
#print(soup)
#my_soup = soup('span',{'class':'a-size-small a-color-base aok-align-center aok-inline-block'})
#print(my_soup)
#for i in my_soup:
#    print(i.get_text())
#my_soup_list = my_soup[2].get_text()
#print(my_soup_list)

