from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

PATH = "./chromedriver"
driver = webdriver.Chrome(PATH)

driver.get("file:///home/artemiyz/Programming/School/FF2/MASH.html")
print("Connected to ", driver.title)

# driver.switch_to.new_window('tab')

try:

    hrefs = [i.get_attribute('href') for i in driver.find_elements(By.CSS_SELECTOR, '.form')]
    home = driver.current_window_handle

    cnt = 0
    for i in hrefs:
        driver.switch_to.new_window('tab')
        driver.get(i)
        inp = driver.find_element(By.CSS_SELECTOR, "input[type='text']")
        sub = driver.find_element(By.XPATH, '//span[contains(text(), "Отправить")]')
        inp.send_keys('dsfvfgfs')
        ActionChains(driver).click(sub).perform()
        time.sleep(0.5)
        print('Completed %d forms' % (cnt := cnt + 1))
        driver.close()
        driver.switch_to.window(home)
except:
    print('Terminated')

finally:
    driver.quit()