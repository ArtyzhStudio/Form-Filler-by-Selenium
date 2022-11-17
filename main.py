from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

PATH = "/home/artemiyz/Programming/chromedriver"
driver = webdriver.Chrome(PATH)

driver.get("https://docs.google.com/forms/d/e/1FAIpQLSflKyNIuB323TF_5OWhFOwuxu_y_Ig-EXZJaYxDixZ6ZlDcKA/viewform")
print("Connected to ", driver.title)

# driver.switch_to.new_window('tab')

for i in range(20):
    driver.refresh()
    inp = driver.find_element(By.CSS_SELECTOR, "input[type='text']")
    sub = driver.find_element(By.XPATH, '//span[contains(text(), "Отправить")]')
    inp.send_keys('dsfvfgfs')
    ActionChains(driver).click(sub).perform()
    time.sleep(0.5)

driver.quit()