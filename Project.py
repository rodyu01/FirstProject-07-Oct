# coding=utf-8
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome("c:\\temp\\chromedriver.exe")
driver.get('https://buyme.co.il')
driver.maximize_window()
time.sleep(5)
driver.find_element_by_class_name("seperator-link").click()
driver.find_element_by_class_name("text-btn").click()
driver.find_element_by_xpath("//input[@placeholder='שם פרטי']").send_keys("korkin")
driver.find_element_by_xpath("//input[@placeholder='מייל']").send_keys("korkin@012.net.il")
driver.find_element_by_xpath("//input[@placeholder='סיסמה']").send_keys("Passw0rd")
driver.find_element_by_xpath("//input[@placeholder='אימות סיסמה']").send_keys("Passw0rd")
check_box = driver.find_elements_by_class_name("fa")
check_box[0].click()
check_box[1].click()
driver.find_element_by_xpath("//button[@type='submit']").click()
