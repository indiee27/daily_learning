# script for importing shifts from co_op website
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_argument("--disable-infobars")
options.add_argument("--disable-extensions")
options.add_argument("--disable-popup-blocking")
options.add_argument("--user-data-dir=C:\\Users\\indie\\AppData\\Local\\Google\\Chrome\\User Data")

options.add_experimental_option("useAutomationExtension", False)
options.add_experimental_option("excludeSwitches", ['enable-automation'])


driver = webdriver.Chrome(options=options)
driver.get("https://accounts.google.com/")

#driver.find_element(by.name("Co-op")).send_keys(keys.RETURN)

driver.switch_to_frame("backgroundImage")