import re
import requests 
from bs4 import BeautifulSoup
url = 'https://www.amazon.com/'

headers = {'user-agent': 'kaveh'}

r = requests.get(url,headers=headers)
soup = BeautifulSoup(r.text,'lxml')
soup_Option = soup.select('#searchDropdownBox')

Soup_value = soup_Option[0].children

for items in Soup_value:
    # print(items[0].ge)
    print(items)
    
    # print(type(items))
    # x = re.findall('value="(.[^"]+)"',str(items))
    