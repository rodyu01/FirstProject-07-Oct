import time
from selenium import webdriver

#Constants
USER_NAME = "Anna"
USER_PASSWORD = "Anna080677"
USER_MAIL = "bas0793@gmail.com"
CHROME_DRIVER = "C://Users//Anna//Downloads//chromedriver_win32//chromedriver.exe"
REGISTRATION = "seperator-link"
FOR_REGISTRATION = "text-btn"
FILE_WITH_SITE_NAME = "C:/Users/CaField/Downloads/site_name.txt"
REGISTRATION_CONDITIONS = "fa"
REGISTRATION_ON_BUYME = "//*[contains(text(), 'הרשמה ל-BUYME')]"
LOGIN_ON_BUYME = "//*[contains(text(), 'כניסה ל-BUYME')]"
FIND_GIFT = "ui-btn"
BUSINESS_PRICE = "//span[@class='card-price' and contains(text(), '280')]"
FOR_SOMEONE_ELSE = "//*[contains(text(), 'למישהו אחר')]"
RECEIVER_BUTTON = "//*[contains(@data-parsley-required-message,'מי הזוכה המאושר')]"
RECEIVER_NAME = "Julia"
SENDER_BUTTON = "//*[contains(@data-parsley-required-message,'למי יגידו תודה')]"
SENDER_NAME = "Friends"
EVENT = "//a/span[contains(text(), 'לאיזה אירוע')]"
BIRTHDAY = "//ul/li[contains(text(), 'יום הולדת')]"
SPA_NAVE_ZEDEK = "ספא נווה צדק"
BLESSING_BUTTON = "//*[contains(@placeholder,'מזל טוב')]"
BLESSING = "Dear Julia! Happy Birthday"
IMAGE_TO_UPLOAD = "D:/Python/HappyBirthday.jpg"
IMMEDIATELY_AFTER_PAYMENT = "send-now"
SMS_OPTION = "//*[contains(text(), 'ב-SMS')]"
SENDER_PHONE = "0527959979"
SENDER_PHONE_BUTTON = "//*[contains(@placeholder,'ספרות בלבד')]"
RECEIVER_PHONE = "0544716254"
RECEIVER_PHONE_BUTTON = "//*[@id='resendReciver']"
SAVE_BUTTON = "//*[contains(text(), 'שמירה')]"
UPLOAD_PICTURE_BUTTON = "fileUpload"
MAIL_BUTTON = "//*[contains(@placeholder,'מייל')]"
PASSWORD_BUTTON = "//*[contains(@placeholder,'סיסמה')]"
NAME_BUTTON = "//*[contains(@placeholder,'שם פרטי')]"
PASSWORD_AGAIN_BUTTON = "//*[contains(@placeholder,'אימות סיסמה')]"
AMOUNT_BUTTON = "//a/span[contains(text(), 'סכום')]"
LOCATION_BUTTON = "//a/span[contains(text(), 'אזור')]"
CATEGORY_BUTTON = "//a/span[contains(text(), 'קטגוריה')]"
CENTER = "//ul/li[contains(text(), 'מרכז')]"
GIFT_CARD_SPA = "//ul/li[contains(text(), 'גיפט קארד לבתי ספא')]"
PRICE_200_299 = "//ul/li[contains(text(), '200-299')]"
SUBMIT_BUTTON = "//button[text()='תשלום']"

#Try to read site from external text file and put it in SITE_NAME variable for next use
try:
    site_file = open(FILE_WITH_SITE_NAME, 'r', encoding='utf-8')
    SITE_NAME = site_file.read()
except IOError:
    print ("Error: can't find file or read data")
site_file.close()

#Open chrome driver
#driver = webdriver.Chrome(executable_path=CHROME_DRIVER)
driver = webdriver.Chrome("c:\\temp\\chromedriver.exe")

# Opening chrome browser on a desired page
driver.get(SITE_NAME)
# Maximize window
driver.maximize_window()
# Waiting for 2 seconds
time.sleep(2)

# press on button כניסה/הרשמה
driver.find_element_by_class_name(REGISTRATION).click()

# # REGISTRATION PAGE - START
# # press on button להרשמה
# driver.find_element_by_class_name(FOR_REGISTRATION).click()
#
# # Fill name
# driver.find_element_by_xpath(NAME_BUTTON).clear()
# driver.find_element_by_xpath(NAME_BUTTON).send_keys(USER_NAME)
# # Fill mail
# driver.find_element_by_xpath(MAIL_BUTTON).clear()
# driver.find_element_by_xpath(MAIL_BUTTON).send_keys(USER_MAIL)
# # Fill password
# driver.find_element_by_xpath(PASSWORD_BUTTON).clear()
# driver.find_element_by_xpath(PASSWORD_BUTTON).send_keys(USER_PASSWORD)
# # Fill password again
# driver.find_element_by_xpath(PASSWORD_AGAIN_BUTTON).clear()
# driver.find_element_by_xpath(PASSWORD_AGAIN_BUTTON).send_keys(USER_PASSWORD)
#
# elements = driver.find_elements_by_class_name(REGISTRATION_CONDITIONS)
# # Click on agreement
# elements[0].click()
# # Don't approve to receive mails
# elements[1].click()
#
# # Click on registration on buyme
# driver.find_element_by_xpath(REGISTRATION_ON_BUYME).click()
# # REGISTRATION PAGE - END

# LOGIN PAGE - START
# Fill mail
driver.find_element_by_xpath(MAIL_BUTTON).send_keys(USER_MAIL)
# Fill password
driver.find_element_by_xpath(PASSWORD_BUTTON).send_keys(USER_PASSWORD)
# Click on login to buyme
driver.find_element_by_xpath(LOGIN_ON_BUYME).click()

# LOGIN PAGE - END

# HOME SCREEN - START
time.sleep(2)
# Click on סכום
driver.find_element_by_xpath(AMOUNT_BUTTON).click()
# Click on 100-199 שח
driver.find_element_by_xpath(PRICE_200_299).click()

# Click on אזור
driver.find_element_by_xpath(LOCATION_BUTTON).click()

# Click on מרכז
driver.find_element_by_xpath(CENTER).click()

# Click on קטגוריה
driver.find_element_by_xpath(CATEGORY_BUTTON).click()

# Click on גיפט קארד לבתי ספא
driver.find_element_by_xpath(GIFT_CARD_SPA).click()

# Click on תמצאו לי מתנה
driver.find_element_by_class_name(FIND_GIFT).click()
# HOME SCREEN - END

# BUSINESS SCREEN - START
time.sleep(2)
# Pick a business
driver.find_element_by_partial_link_text(SPA_NAVE_ZEDEK).click()
time.sleep(2)
# Type a price
driver.find_element_by_xpath(BUSINESS_PRICE).click()
# BUSINESS SCREEN - END

# SENDER/RECEIVER INFORMATION SCREEN - START
time.sleep(2)
# Press button "למישהו אחר"
driver.find_element_by_xpath(FOR_SOMEONE_ELSE).click()
# Enter receiver name
driver.find_element_by_xpath(RECEIVER_BUTTON).clear()
driver.find_element_by_xpath(RECEIVER_BUTTON).send_keys(RECEIVER_NAME)
# Enter sender name
driver.find_element_by_xpath(SENDER_BUTTON).clear()
driver.find_element_by_xpath(SENDER_BUTTON).send_keys(SENDER_NAME)
# Pick element
driver.find_element_by_xpath(EVENT).click()
# Pick יום הולדת
driver.find_element_by_xpath(BIRTHDAY).click()
# Enter a blessing
driver.find_element_by_xpath(BLESSING_BUTTON).clear()
driver.find_element_by_xpath(BLESSING_BUTTON).send_keys(BLESSING)
# Scroll down
driver.execute_script("window.scrollTo(0, 500)")
# Upload a picture
driver.find_element_by_name(UPLOAD_PICTURE_BUTTON).send_keys(IMAGE_TO_UPLOAD)
# Press button "מיד אחרי התשלום"
driver.find_element_by_class_name(IMMEDIATELY_AFTER_PAYMENT).click()
# Pick sms option
driver.find_element_by_xpath(SMS_OPTION).click()
# Enter טלפון שלי
driver.find_element_by_xpath(SENDER_PHONE_BUTTON).clear()
driver.find_element_by_xpath(SENDER_PHONE_BUTTON).send_keys(SENDER_PHONE)
# Enter טלפון המקבל
driver.find_element_by_xpath(RECEIVER_PHONE_BUTTON).clear()
driver.find_element_by_xpath(RECEIVER_PHONE_BUTTON).send_keys(RECEIVER_PHONE)
# Click on שמירה
driver.find_element_by_xpath(SAVE_BUTTON).click()
# Click on תשלום
driver.find_element_by_xpath(SUBMIT_BUTTON).click()
# SENDER/RECEIVER INFORMATION SCREEN - END
