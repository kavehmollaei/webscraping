
import requests 
from bs4 import BeautifulSoup
url = 'https://bama.ir/car/'
urll = 'https://www.digikala.com/product/dkp-80907/%DA%A9%D8%B1%D9%85-%D9%BE%D9%88%D8%AF%D8%B1-%D8%A2%DA%A9%D9%86%D9%87-%D9%85%D8%A7%DB%8C-%D9%85%D8%AF%D9%84-acneline-a02'
headers = {'user-agent': 'kaveh'}

r = requests.get(url,headers=headers)
print(r.status_code,end=",")

soup = BeautifulSoup(r.text,'lxml')

brand_soup = soup.select('#selectedTopBrand')
brand_soup_option = brand_soup[0].children
print(brand_soup_option)
f = open('out-test-mu.txt','w+')
for i in brand_soup_option:
    f.write(i.string)
    try:
        f.write(i['value'])
    except:
        print('no value')
f.close()