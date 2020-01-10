from  selenium import webdriver
import selenium
import datetime



driver = webdriver.Chrome()
driver.maximize_window()


url = 'https://www.seleniumeasy.com/test/basic-first-form-demo.html'
# get url
driver.get(url)

username_field = driver.find_element_by_id('user-message')
username_field.clear() 
username_field.send_keys('kavehmollaei@gmail.com')

push_button = driver.find_element_by_class_name('btn-default')
push_button.click()

input_field1 = driver.find_element_by_id('sum1')
input_field1.send_keys('2')


input_field2 = driver.find_element_by_id('sum2')
input_field2.send_keys('3')
push_button2 = driver.find_element_by_xpath('//*[(@id = "gettotal")]//*[contains(concat( " ", @class, " " ), concat( " ", "btn-default", " " ))]')
push_button2.click()

url_url = 'https://www.seleniumeasy.com/test/basic-select-dropdown-demo.html'
url_url_url = 'http://demo.guru99.com/test/newtours/register.php'
driver.get(url_url)

# get Date on x
x = datetime.datetime.now()
# get day of week in notaion
day_hafteh = x.strftime('%A')


#select date
select_dropdownbox = driver.find_element_by_xpath("//*[(@id = 'select-demo')]/option[text()='%s']" %day_hafteh).click() 

driver.close()

