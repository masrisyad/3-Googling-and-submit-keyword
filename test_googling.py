from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('https://google.co.id')
driver.find_element_by_name('q').send_keys(
    'Risyad Abdala Ramadhan' + Keys.ENTER)
assert 'Risyad Abdala Ramadhan' in driver.find_element_by_css_selector(
    'h3').text
assert 'Risyad Abdala Ramadhan' in driver.title
driver.quit()
