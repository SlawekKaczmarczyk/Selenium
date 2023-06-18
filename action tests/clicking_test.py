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

try:
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, 'Features')))
    element.click()
    time.sleep(0.5) # added for visual purposes
    driver.back()
    time.sleep(0.5)
    driver.forward()
    time.sleep(0.5)
    element.clear()

except:
    time.sleep(1)
    driver.close()