import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(executable_path="c:\\temp\\chromedriver.exe")
driver.get('http://youtube.com')
driver.find_element_by_id('search').send_keys("orphaned land")
driver.find_element_by_id('search').send_keys(Keys.ENTER)

# driver.find_element_by_id('search-icon-legacy').send_keys(Keys.ENTER)

