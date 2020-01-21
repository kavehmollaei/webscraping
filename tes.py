

from  selenium import webdriver
import selenium
import datetime

url = 'https://www.amazon.com/'

driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)
#ketab=Books
select_field = driver.find_element_by_css_selector('#nav-search .nav-left').click()
select_Books = driver.find_element_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "nav-focus", " " ))]').click()
el = driver.find_element_by_id('searchDropdownBox')
for option in el.find_elements_by_tag_name('option'):
    if option.text == 'Books':
        option.click() # select() in earlier versions of webdriver
        break

select_text = driver.find_element_by_css_selector('#twotabsearchtextbox')

searching_text = input('Pls Enter Serach text:')
select_text.send_keys(searching_text)

#push_button = driver.find_element_by_class_name('nav-input')
push_button = driver.find_element_by_css_selector('.nav-sprite .nav-input')
push_button.click()

