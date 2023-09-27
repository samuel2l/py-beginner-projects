from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('http://orteil.dashnet.org/experiments/cookie/')

cookie_click = driver.find_element(by=By.ID, value="cookie")

store = driver.find_elements(by=By.CSS_SELECTOR, value="#store b")
ids = driver.find_elements(by=By.CSS_SELECTOR, value="#store div")
id_list = []

for _id in ids:
    id_list.append(_id.get_attribute("id"))

product_costs = []
product_items = []

for product in store:
    try:
        # getting the costs but for some reason an empty list is being printed at the end hence the reason for error handling
        product_costs.append(int(product.text.split('-')[1].replace(",", "")))
    except IndexError:
        continue

timeout = time.time() + 7
five_min = time.time() + 60 * 5  # 5minutes

while True:
    cookie_click.click()
    if time.time() > timeout:
        user_money = driver.find_element(by=By.ID, value="money")

        money = int(user_money.text.replace(",", ""))
        possible_purchases = []

        for i in product_costs:
            if money < i:
                continue
            else:
                possible_purchases.append(i)
        try:
            purchase = max(possible_purchases)
            purchase_index = possible_purchases.index(purchase)
            get_id = driver.find_element(by=By.ID, value=f"{id_list[purchase_index]}")
        except ValueError:
            continue
        else:
            get_id.click()

        # Add another 5 seconds until the next check
        timeout = time.time() + 7
    if timeout > five_min:
        cookie_per_second = driver.find_element(by=By.ID, value="cps")
        print(cookie_per_second.text)
        break
