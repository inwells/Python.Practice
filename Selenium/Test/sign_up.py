from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path = "E:\\Development\\chromedriver\\100\\chromedriver.exe"
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options,executable_path=chrome_driver_path)

driver.get("http://secure-retreat-92358.herokuapp.com/")

fname = driver.find_element(By.NAME, value="fName")
fname.send_keys("Big")
lname = driver.find_element(By.NAME, value="lName")
lname.send_keys("dong")
email = driver.find_element(By.NAME, value="email")
email.send_keys("bigdong@littledong.com")
button = driver.find_element(By.CSS_SELECTOR, value=".btn-primary") #or form button

button.click()
