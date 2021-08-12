from logging import exception
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC


import os
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
import modules.proxy_grab as pg



dir_current = os.getcwd()
path__ = "https://katfile.com/nlqzor5jlt44/nida_chenagtsang_tonkaia_anatomiia_v_tibetskoi_meditsine_iog.rar.html"

driverLocation = dir_current + "\chromedriver.exe"
chrome_options = Options()
# chrome_options.add_argument("--headless")
driver = webdriver.Chrome(driverLocation, chrome_options=chrome_options)
data_text = driver.get(path__)
driver.implicitly_wait(5)

# driver.find_element(By.CLASS_NAME, 'recaptcha-checkbox-checkmark').click()
driver.find_element(By.ID, 'fbtn1').click()
driver.implicitly_wait(3)
driver.find_element(By.ID, 'fbtn1').click()

driver.implicitly_wait(5)

if len(driver.window_handles) > 1:
    driver.switch_to.window(driver.window_handles[0]) 
    
# WebDriverWait(driver, 40).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="_mform"]/div[2]/div/div/div/div/button[2]')))
# driver.find_element(By.XPATH, '//*[@id="_mform"]/div[2]/div/div/div/div/button[2]').click()

# if len(driver.window_handles) > 1:
#     driver.switch_to.window(driver.window_handles[0]) 

# driver.implicitly_wait(33)   
time.sleep(33)    
# element_ = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "downloadbtn")))
# WebDriverWait(driver, 35).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.downloadbtn')))
check_box = driver.find_element(By.ID, 'recaptchaAnchor')
check_box.click()

# finally:
#     driver.implicitly_wait(100)
    # driver.quit()
# try:
#     
# finally:
#     driver.quit()








a = 1

# actions = ActionChains(driver)
# driver.get(path_)

# turbo_button1 = driver.find_element_by_id("nopay-btn")
# actions.click(turbo_button1)

# actions = ActionChains(driver)


# actions.perform()

# driver.implicitly_wait(10)


# print(driver.current_url)


# driver.close()
