from selenium import webdriver

chrome_driver_path = "E:\\Development\\chromedriver\\100\\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.amazon.com")

# price = driver.find_element_by_id("priceblock_ourprice")

# search_bar = driver.find_element_by_name("q")
# print(search_bar.get_attribute("placeholder"))

# logo = driver.find_element_by_class_name("nav-logo-link")

# documentation_link = driver.find_element_by_css_selector(".documentation-widget a")

### inspect > copy > copy xpatth ###
### https://www.w3schools.com/xml/xpath_intro.asp ###

# privacy_link = driver.find_element_by_xpath('//*[@id="navFooter"]/div[5]/ul/li[2]/a')
# print(privacy_link.text)