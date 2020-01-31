from  selenium import webdriver
import selenium
import datetime

urll = 'https://www.amazon.com/baby-reg/search-results/ref=s9_acss_bw_cg_navreg17_3b1_w?pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-2&pf_rd_r=M7HNRF0E5QZXMM51XRWV&pf_rd_t=101&pf_rd_p=ebc06864-bee1-4ca9-bcc0-e772ee0c61f4&pf_rd_i=16115931011'
url = 'https://www.amazon.com/'
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)
#ketab=Books
register_field = driver.find_element_by_css_selector('#nav-xshop .nav-a:nth-child(3)').click()
baby_register = driver.find_element_by_css_selector('.bxc-grid__row--light~ .bxc-grid__row--light+ .bxc-grid__row--light .bxc-grid__column--light+ .bxc-grid__column--light img').click()

driver.get(urll)
register_field = driver.find_element_by_css_selector('#nameOrEmailField')
register_field.send_keys('kavehmollaei')
city_field = driver.find_element_by_css_selector('#cityField')
city_field.send_keys('Arizona')



# add Month
x = datetime.datetime.now()
Month_Year = x.strftime('%B')
print(Month_Year)
# el = driver.find_element_by_xpath('//*[(@id = "a-autoid-2-announce")]//*[contains(concat( " ", @class, " " ), concat( " ", "a-dropdown-prompt", " " ))]/option[text()="%s"]' %Month_Year).click()
selector = driver.find_element_by_id('a-autoid-2-announce')
selector.click()
el=driver.find_element_by_id('eventDateMonthField_1')
el.click()


#add state
state_select = driver.find_element_by_id('stateField')
state_select.send_keys('Iran')
select_year = driver.find_element_by_css_selector('#a-autoid-3-announce .a-dropdown-prompt').click()


# add year
select_final = driver.find_element_by_id('eventDateYearField_2')
select_final.click()
'''
el = driver.find_element_by_css_selector('#a-autoid-2-announce')
el.click()
el.find_elements_by_id('eventDateMonthField_9').click()
'''





#el.find_elements_by_class_name("a-dropdown-link a-active")

# select_month = el.find_element_by_tag_name('li')
# print(select_month)
# for option in select_month:
    # option.click()



    # if option.text == 'May':
        # option.click()
        # break
            

'''

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
'''