from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

PATH ="C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://orteil.dashnet.org/cookieclicker/")

consent = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[2]/div[1]/div[2]/div[2]/button[1]/p"))).click()

language = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="langSelect-EN"]'))).click()


driver.implicitly_wait(50)

cookie = driver.find_element(By.ID, 'bigCookie')
cookie_count = driver.find_element(By.ID, 'cookies')
items = [driver.find_element(By.ID, 'productPrice' + str(i)) for i in range(1,-1,-1)] # most exprensive upgrade first

actions = ActionChains(driver)
actions.click(cookie)

for i in range(5000):
    actions.perform()

    