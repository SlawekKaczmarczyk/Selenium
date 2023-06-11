from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

PATH ="C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://orteil.dashnet.org/cookieclicker/")

driver.implicitly_wait(5)

cookie = driver.find_element(By.ID, 'bigCookie')
cookie_count = driver.find_element(By.ID, 'cookies')
items = [driver.find_element(By.ID, 'productPrice' + str(i)) for i in range(1,-1,-1)] # most exprensive upgrade first

actions = ActionChains(driver)
actions.click(cookie)

for i in range(5000):
    actions.perform()