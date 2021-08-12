from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC


import os
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
 


dir_current = os.getcwd()
path__ = "https://trubobit.com/h2ssmx949ohb.html"

driverLocation = dir_current + "\chromedriver.exe"
chrome_options = Options()
# chrome_options.add_argument("--headless")
driver = webdriver.Chrome(driverLocation, chrome_options=chrome_options)
# data_text = driver.get(path__)
# driver.implicitly_wait(3)
# driver.find_element(By.ID, 'nopay-btn').click()
# driver.implicitly_wait(5)
# driver.find_element(By.PARTIAL_LINK_TEXT, 'продолжить скачивание в текущем браузере').click()
# driver.implicitly_wait(5)
# # driver.find_element(By.CLASS_NAME, 'recaptcha-checkbox-checkmark').click()

# идем по адресу
data_text = driver.get(path__)
driver.implicitly_wait(3)

# нажимаем на кнопку скачать
# ждем 3 сек
driver.find_element(By.ID, 'nopay-btn').click()
driver.implicitly_wait(3)

# проверяем сколько окон
    #если окон несколько закрываем остальные и  переходим в нужное
driver.find_element(By.CLASS_NAME, 'nopay-btn').click()
driver.implicitly_wait(6)
    
# нажимаем на ссылку продолжить скачивание в текущем окне

is_time_limit = driver.find_element(By.ID, 'timeout-limit-header')

if is_time_limit:
    print('Лимит времени исчерпан')
    
    
driver.find_element(By.ID, '#checkbox').click()
driver.implicitly_wait(3)


    
# проверяем сколько окон
    #если окон несколько закрываем остальные и  переходим в нужное
    
# ждем 1 мин
# жмем на скачать
# проверяем сколько окон    
    #если окон несколько закрываем остальные и  переходим в нужное
    
# жмем на скачать
# проверяем сколько окон    
    #если окон несколько закрываем остальные и  переходим в нужное

try:
    element_ = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.ID, "recaptcha-anchor")))
    element_.click()
finally:
    driver.quit()








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
