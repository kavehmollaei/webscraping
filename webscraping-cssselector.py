import requests
from bs4 import BeautifulSoup


url = 'https://en.wikipedia.org/wiki/Nineteen_Eighty-Four'
r = requests.get(url)
css_selector = '.searchaux+ .navigation-not-searchable'


soup = BeautifulSoup(r.text,'html.parser')
#title_soup = soup.find_all('.slick-slide')

title_soup = soup.select(css_selector)
print(title_soup[0].get_text())



#استخراج به کمک css_selector