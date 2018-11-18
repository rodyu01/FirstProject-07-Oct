# coding=utf-8
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
driver = webdriver.Chrome("c:\\temp\\chromedriver.exe")
driver.get('https://buyme.co.il')
driver.maximize_window()
time.sleep(2)
driver.find_element_by_class_name("seperator-link").click()
driver.find_element_by_xpath("//input[@placeholder='מייל']").send_keys("korkin@012.net.il")
driver.find_element_by_xpath("//input[@placeholder='סיסמה']").send_keys("Passw0rd")
driver.find_element_by_xpath("//button[@type='submit']").click()
time.sleep(2)
driver.find_element_by_xpath("//div/a/span").click()
driver.find_element_by_xpath("//ul/li[contains(text(),'100-199')]").click()
driver.find_element_by_xpath("//div[2]/a").click()
driver.find_element_by_xpath("//ul/li[contains(text(),'מרכז')]").click()
driver.find_element_by_xpath("//div[3]/a").click()
driver.find_element_by_xpath("//ul/li[contains(text(),'גיפט קארד למסעדות שף')]").click()
driver.find_element_by_xpath("//form/a").click()
time.sleep(2)
for BIZ_LIST in driver.find_elements_by_class_name("label"):
    if BIZ_LIST.text == "טאיזו":
        BIZ_LIST.click()
        time.sleep(2)
        break
driver.find_element_by_xpath("//input[@placeholder='מה הסכום?']").send_keys("150")
driver.find_element_by_xpath("//button[@type='submit']").click()
