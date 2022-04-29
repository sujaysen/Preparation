# Selenium is an open-source automation testing tools.
# pip install selenium
from selenium import webdriver
import time  
from selenium.webdriver.common.keys import Keys  

driver = webdriver.Chrome()
driver.maximize_window()  
driver.get("https://google.co.in")
driver.find_element_by_name("q").send_keys("selenium test")  
time.sleep(3)  
driver.find_element_by_name("btnK").send_keys(Keys.ENTER)  
time.sleep(3)  
driver.close()  

