# coding=utf-8
import time
from selenium import webdriver
import os

driver = webdriver.Chrome("c:\\temp\\chromedriver.exe")
driver.get('https://buyme.co.il')
time.sleep(2)
driver.maximize_window()

# SIGN UP
# driver.find_element_by_class_name("seperator-link").click()
# driver.find_element_by_class_name("text-btn").click()
# driver.find_element_by_xpath("//input[@placeholder='שם פרטי']").send_keys("korkin")
# driver.find_element_by_xpath("//input[@placeholder='מייל']").send_keys("korkin@mail.net.il")
# driver.find_element_by_xpath("//input[@placeholder='סיסמה']").send_keys("Passw0rd")
# driver.find_element_by_xpath("//input[@placeholder='אימות סיסמה']").send_keys("Passw0rd")
# time.sleep(2)
# CHECK_BOX = driver.find_elements_by_xpath("//*[@type='checkbox']")
# CHECK_BOX[0].click()
# CHECK_BOX[1].click()

# SIGN IN
driver.find_element_by_class_name("seperator-link").click()
driver.find_element_by_xpath("//input[@placeholder='מייל']").send_keys("korkin@mail.net.il")
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
time.sleep(2)

driver.find_element_by_xpath("//input[@placeholder='מה הסכום?']").send_keys("150")
driver.find_element_by_xpath("//button[@type='submit']").click()
for CHOICE_LIST in driver.find_elements_by_class_name("text"):
    if CHOICE_LIST.text == "למישהו אחר":
        CHOICE_LIST.click()
        time.sleep(2)
        break
time.sleep(2)

driver.find_element_by_xpath("//a/span[contains(text(), 'לאיזה אירוע')]").click()
CAUSE = "//ul/li[contains(text(),'סתם')]"
driver.find_element_by_xpath(CAUSE).click()
driver.find_element_by_xpath("//*[contains(@placeholder,'מזל טוב')]").clear()
driver.find_element_by_xpath("//*[contains(@placeholder,'מזל טוב')]").send_keys("Happy 10Xgiving!")
WINNER = "//*[contains(@data-parsley-required-message,'מי הזוכה המאושר')]"
driver.find_element_by_xpath(WINNER).send_keys("BOBKA")
GIVER = "//*[contains(@data-parsley-required-message,'למי יגידו תודה')]"
driver.find_element_by_xpath(GIVER).clear()
driver.find_element_by_xpath(GIVER).send_keys("TSB")
driver.find_element_by_name("fileUpload").send_keys(os.path.join(os.getcwd(),"radio-button.png"))
driver.implicitly_wait(60)
driver.find_element_by_class_name("send-now").click()
driver.find_element_by_xpath("//*[contains(text(), 'ב-SMS')]").click()
driver.find_element_by_xpath("//*[contains(@placeholder,'ספרות בלבד')]").send_keys("0526626671")
driver.find_element_by_id("resendReciver").send_keys("0557654321")
driver.find_element_by_xpath("//*[contains(text(), 'שמירה')]").click()

time.sleep(5)
driver.close()
