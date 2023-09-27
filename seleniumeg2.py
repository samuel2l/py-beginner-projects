from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome()
driver.get('http://secure-retreat-92358.herokuapp.com/')

first= driver.find_element(by=By.NAME , value="fName")
first.send_keys("Samuel")
first.send_keys(Keys.ENTER)
last= driver.find_element(by=By.NAME , value="lName")
last.send_keys("Adams")
last.send_keys(Keys.ENTER)
email= driver.find_element(by=By.NAME , value="email")
email.send_keys("sama29571@gmail.com")
email.send_keys(Keys.ENTER)
time.sleep(5)
driver.close()

