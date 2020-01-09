from  selenium import webdriver
import selenium



driver = webdriver.Chrome()
driver.maximize_window()


url = 'https://www.seleniumeasy.com/test/basic-first-form-demo.html'

driver.get(url)
#driver.get(url)
username_field = driver.find_element_by_id('user-message')
username_field.clear() 
username_field.send_keys('kavehmollaei@gmail.com')

push_button = driver.find_element_by_class_name('btn-default')
push_button.click()

input_field1 = driver.find_element_by_id('sum1')
input_field1.send_keys('2')


input_field2 = driver.find_element_by_id('sum2')
input_field2.send_keys('3')
push_button2 = driver.find_element_
push_button2.click()
#driver.close()

