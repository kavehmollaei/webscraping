import requests
from bs4 import BeautifulSoup
import xlsxwriter

workbook = xlsxwriter.Workbook('result.xlsx')
worksheet = workbook.add_worksheet()

url = 'https://www.amazon.com/s?k=jj+balard&ref=nb_sb_noss'
headers={'User-Agent':'my app.0.0.1','Accept-Language':'en-Us ,en,q=.5'}
r = requests.get(url,headers=headers)

out_put = r.text
soup = BeautifulSoup(out_put,'html.parser')

title_soup = soup.select('.a-color-base.a-text-normal')
row = 0
for i in title_soup:
    print(i.get_text())
    worksheet.write_string(row,0,i.get_text())
    row +=1
workbook.close()
