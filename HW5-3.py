import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="c:\\temp\\chromedriver.exe")
driver.get('http://facebook.com')
driver.find_element_by_id('email').send_keys("user@mail.com")
driver.find_element_by_id('pass').send_keys("password")
driver.find_element_by_id('loginbutton').send_keys(Keys.ENTER)
