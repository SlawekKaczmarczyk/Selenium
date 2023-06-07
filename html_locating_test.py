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

search = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/header/div/div[2]/div/div/div[1]/div/div/form/label/input[1]")
search.send_keys("test")
search.send_keys(Keys.RETURN)

try:
    main = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[4]/main/div/div[3]/div"))).click()
    main = driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/main/div/div[3]/div/ul/li[1]")
    print(main.text)
    
finally:
    time.sleep(5)
    driver.close()
