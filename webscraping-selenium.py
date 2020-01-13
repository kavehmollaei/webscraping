from  selenium import webdriver
import selenium



driver = webdriver.Chrome()
driver.maximize_window()


url = 'https://www.gajmarket.com/login?'

driver.get(url)
#driver.get(url)
username_field = driver.find_element_by_name('Username')
username_field.clear() 
username_field.send_keys('kavehmollaei@gmail.com')
pass_field = driver.find_element_by_id('Password')
pass_field.clear()
pass_field.send_keys('rezareza')

login_button = driver.find_element_by_class_name('btn-primary')
login_button.click()
#driver.close()


print('---------------------------')
# print(driver.get_log('server'))

# print(driver.get_log('client'))

print(driver.get_log('driver'))