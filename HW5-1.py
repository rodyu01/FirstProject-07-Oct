import selenium
from selenium import webdriver

driver = webdriver.Chrome(executable_path="c:\\temp\\chromedriver.exe")
driver.get('http://github.com')
driver.find_element_by_class_name("js-site-search-form").send_keys("selenium")


# driver.find_element_by_id('source').send_keys("כיסא")
# id_var = driver.find_element_by_id('gt-submit')
# class_var = driver.find_element_by_class_name('jfk-button')
# xpath_var = driver.find_element_by_xpath("//input[@type='submit']")
# print(id_var)
# print(class_var)
# print(xpath_var)
