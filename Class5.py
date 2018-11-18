import time

import selenium

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="c:\\temp\\chromedriver.exe")
driver.implicitly_wait(10)
driver.get('https://translate.google.co.il/?hl=iw')
print(driver.current_url)
print(driver.title)
# print(driver.page_source)
driver.refresh()
driver.find_element_by_id("source").send_keys("my name is")
# driver.quit()
button_element =  driver.find_element_by_id("gt-submit").send_keys(Keys.ENTER)
# button_element.click()
time.sleep(3)
driver.find_element_by_id("source").clear()
driver.find_element_by_id("gt-swap").click()
driver.find_element_by_id("source").send_keys(" הוא")

# drop = driver.find_element_by_xpath("//input[@id='gt-sl-gms']")
# if drop.is_displayed():
#     print("displayed")

# x = driver.find_elements_by_id("gt-submit")
# x[0].click()

