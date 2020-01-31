import requests
from bs4 import BeautifulSoup
import xlsxwriter

url = 'https://www.gadgetsnow.com/mobile-phones'


r = requests.get(url)
out_put = r.text


soup = BeautifulSoup(out_put,'html.parser')
#workbook = xlsxwriter.workbook('result_mo.xlsx')
#worksheet = workbook.add_worksheet()

title_t = soup.select('img')
row = 0
for i in title_t:
    title_url = i['src']
    print(title_url)
    
    
    
  