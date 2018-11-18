import selenium
from selenium import webdriver

driver = webdriver.Firefox(executable_path="c:\\temp\\geckodriver.exe")
driver.get('http://www.ynet.co.il')

driver = webdriver.Chrome(executable_path="c:\\temp\\chromedriver.exe")
driver.get('http://walla.co.il')
site_name = driver.current_url
driver.refresh()
print(site_name)
print(driver.current_url)

if site_name == driver.current_url:
    print('same')
else:
    print('different')

