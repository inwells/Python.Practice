import pickle
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from os.path import exists
import json
from time import sleep
from random import randint

with open("api.key") as key:
        LOGIN = json.load(key)

chrome_driver_path = "E:\\Development\\chromedriver\\100\\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.tinder.com")

# if exists("cookies.pkl"):
#     cookies = pickle.load(open("cookies.pkl", "rb"))
#     for cookie in cookies:
#         driver.add_cookie(cookie)
# else:

cookies = pickle.load(open("cookies.pkl", "rb"))
for cookie in cookies:
    driver.add_cookie(cookie)
    
sleep(5)

cookies = driver.find_element(By.XPATH, value='//*[@id="q939012387"]/div/div[2]/div/div/div[1]/div[1]/button/span')
cookies.click()

login = driver.find_element(By.CLASS_NAME, value="button")
login.click()

sleep(2)

fb_login = driver.find_element(By.XPATH, value='//*[@id="q-789368689"]/div/div/div[1]/div/div/div[3]/span/div[2]/button')
fb_login.click()

sleep(2)

driver.switch_to.window(driver.window_handles[1])

fb_user = driver.find_element(By.ID, value="email")
fb_user.send_keys(LOGIN["username"])

fb_pass = driver.find_element(By.ID, value="pass")
fb_pass.send_keys(LOGIN["pass"])

fb_btn = driver.find_element(By.NAME, value="login")
fb_btn.click()

sleep(60)
driver.switch_to.window(driver.window_handles[0])
pickle.dump( driver.get_cookies() , open("cookies.pkl","wb"))

loc_allow = driver.find_element(By.XPATH, value='//*[@id="q-789368689"]/div/div/div/div/div[3]/button[1]')
loc_allow.click()
sleep(1)

no_not = driver.find_element(By.XPATH, value='//*[@id="q-789368689"]/div/div/div/div/div[3]/button[2]/span')
no_not.click()
sleep(1)


while True:
    sleep(randint(2,5))
    try:
        next = driver.find_element(By.XPATH,value='//*[@id="q939012387"]/div/div[1]/div/div/main/div/div/div[1]/div/div[5]/div/div[4]/button')
        next.click()
    except:
        try:
            back = driver.find_element(By.XPATH, value='//*[@id="q1269383588"]/div/div/div[1]/div/div[4]/button')
            back.click()
        except:
            pass
        
    
        
    
    