import requests
from bs4 import BeautifulSoup


url =  'https://en.wikipedia.org/wiki/Nineteen_Eighty-Four'


r = requests.get(url)
out_put=r.text
# f = open('out-test.txt','w+')
# for i in out_put:


   # f.write(i)


#f.close()
## estekhraj matn ba request
soup = BeautifulSoup(out_put,'html.parser')
title = soup('h1',{'id':'firstHeading'})
title_book = title[0].get_text()
informational_book = {}
informational_book['title']=title_book
description_soup = soup('div',{'id':'mw-content-text'})
des_all=description_soup[0].get_text()
des_all_list = des_all.split('\n')
description=''
for i in des_all_list[:3]:
    description +=i

informational_book['description']= description

print(informational_book)


#استخراج به کمک requestکتابخانه

