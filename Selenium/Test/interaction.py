from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

chrome_driver_path = "E:\\Development\\chromedriver\\100\\chromedriver.exe"
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(chrome_options=options,executable_path=chrome_driver_path)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

#article_count = driver.find_element_by_xpath('//*[@id="articlecount"]/a[1]')
#or

article_count = driver.find_element(By.CSS_SELECTOR, value="#mp-topbanner #articlecount a")
#article_count.click()

comm_portal = driver.find_element(By.LINK_TEXT, value="Community portal")
#comm_portal.click()

search = driver.find_element(By.NAME, value="search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)
