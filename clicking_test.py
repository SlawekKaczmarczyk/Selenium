from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH ="C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)



driver.get("https://github.com")
print(driver.title)
driver.maximize_window() # without this, it cannot see search field

link = driver.find_element(By.LINK_TEXT, 'Pricing').click()
time.sleep(5)
driver.close()