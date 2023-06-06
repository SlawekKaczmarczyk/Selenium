from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

PATH ="C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)



driver.get("https://github.com")
print(driver.title)
driver.maximize_window() # without this, it cannot see search field

search = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/header/div/div[2]/div/div/div[1]/div/div/form/label/input[1]")
search.send_keys("test")
search.send_keys(Keys.RETURN)
time.sleep(5)
driver.close()
