import requests
from bs4 import BeautifulSoup
import xlsxwriter

url = 'https://www.gadgetsnow.com/mobile-phones'


r = requests.get(url)
out_put = r.text


soup = BeautifulSoup(out_put,'html.parser')
workbook = xlsxwriter.Workbook('result_mo.xlsx')
worksheet = workbook.add_worksheet()
title = soup.select('.gadName')
row = 0
for i in title:
    worksheet.write_string(row,0,i.get_text())
    row +=1


workbook.close()    