from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#needs a better algorithm that will buy better upgrades instead of just the most expensive

upgrade = time.perf_counter() + 5
counter = time.perf_counter() + 60*5


chrome_driver_path = "E:\\Development\\chromedriver\\100\\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("http://orteil.dashnet.org/experiments/cookie/")
cookie = driver.find_element(By.CSS_SELECTOR, value="#cookie")
upgrades = driver.find_elements(By.CSS_SELECTOR, value="#store div")
upgrade_ids = [upgrade.get_attribute("id") for upgrade in upgrades]
print(upgrade_ids)

def price_updater():
    global cookie_upgrades
    cookie_upgrades = {}
    prices = []
    prices_data = driver.find_elements(By.CSS_SELECTOR, value="#store b")
    for price in prices_data:
        element_text = price.text
        if element_text != "":
            price = element_text.split("-")[1].strip().replace(",", "")
            prices.append(price)
        for n in range(len(prices)):
            cookie_upgrades[int(prices[n])] = upgrade_ids[n]

while True:
    cookie.click()

    if time.perf_counter() > upgrade:
        price_updater()

        #get current money
        money = driver.find_element(By.CSS_SELECTOR, value="#money").text
        if "," in money:
           money =  money.strip().replace(",", "")
        money = int(money)

        #compare upgrade list
        possible_upgrades = {}
        for cost,id in cookie_upgrades.items():
            if money > int(cost):
                possible_upgrades[cost] = id

        if possible_upgrades:
            highest_value = max(possible_upgrades)
            to_purchase = possible_upgrades[highest_value]
            driver.find_element(By.ID, value=to_purchase).click()
        upgrade = time.perf_counter() + 5
        
    
    if time.perf_counter() > counter:
        print(driver.find_element(By.CSS_SELECTOR, value="#cps").text)
        counter = time.time() + 60*5
