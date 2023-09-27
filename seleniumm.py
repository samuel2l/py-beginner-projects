from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
#driver.get("https://www.amazon.com")

#driver.quit() closes entire window
#driver.close() only closes the current tab

#web scraping with selenium
driver.get('https://www.python.org/')
#we copy the xpath from the dev tools
data = driver.find_element(by=By.NAME,value="q")
data.send_keys("History")
data.send_keys(Keys.ENTER)
#Keys class has all non alphabet keys
# print(data.text)
# data.click()

# event_list=data.text.split('\n')
# event_dict={}
# times_list=[]
# event_names=[]
# for i in range(0,len(event_list),2):
#     times_list.append(event_list[i])
# for i in range(1,len(event_list),2):
#     event_names.append(event_list[i])

# print(times_list)
# print(event_names)
# for  n in range(len(times_list)):
#     event_dict[n]={
#         "time": times_list[n],
#         "name": event_names[n]
#     }
#print(event_dict)
#print(data.text)
#other ways to scrape:
# print(data.get_attribute("href"))
#data = driver.find_element(by=By.CSS_SELECTOR,value=".lightbox-target img")

