from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import requests

import os
import time
import json
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By

dir_current = os.getcwd()
path__ = "https://free-proxy-list.net"

driverLocation = dir_current + "\chromedriver.exe"
chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(driverLocation, chrome_options=chrome_options)
driver.set_window_size(1440, 900)

data_text = driver.get(path__)
driver.implicitly_wait(3)

proxy_data = []
proxy_data_element_ = {}

num_page_loaded = 6

def check_proxy(px):
    https_ = 'https' if px['https'] == 'yes' else 'http'
    
    try:
        requests.get("https://www.google.com/", proxies = {https_: https_ + "://" + px['ip']}, timeout = 3)
    except Exception as x:
        print('--'+px['ip'] + ' is dead :`(')
        return False
    else:
        print('--'+px['ip'] + ' is doing :)')
    return True

while num_page_loaded:
    dataTable = None
    # buttonNextElem = None
    dataTable = driver.find_elements(By.CSS_SELECTOR, '.dataTable tbody tr')
    # dataTable = WebDriverWait(driver, 5).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.dataTable tbody tr')))
    # driver.find_elements(By.XPATH, '//button')
    
    for dataRow in dataTable:
        textRow = dataRow.text.split(maxsplit=8)
    
        proxy_data_element_['ip'] = textRow[0]
        proxy_data_element_['https'] = True if textRow[6] == 'yes' else False
        
        check_ip = check_proxy(proxy_data_element_)
        
        if check_ip:        
            proxy_data_element_['port'] = textRow[1]
            proxy_data_element_['code'] = textRow[2]
            proxy_data.append(proxy_data_element_)
        
        proxy_data_element_ = {}
            
    num_page_loaded-=1
    
    if num_page_loaded:
       buttonNextElem = driver.find_element(By.CSS_SELECTOR, '.pagination li.next a')
       buttonNextElem.click() 
       driver.implicitly_wait(3)
       
     


struct_time_ = time.localtime()
time_string = time.strftime("%H-%M-%S__%m-%d-%Y", struct_time_)

with open(f"proxy_list({time_string}).json", "w") as write_file:
    json.dump(proxy_data, write_file)
    
print('work done!!!')   


class ProxyGrabber():
    def __init__(self, driver_, grab_path, **kwargs):
        self.grab_path = grab_path if grab_path else 'https://free-proxy-list.net'
        self.pages_num = kwargs.get('pages_num') if 'pages_num' in kwargs.keys() else '5'
        self.proxy_data = []
        
    def check_proxy(px):
        https_ = 'https' if px['https'] == 'yes' else 'http'
        
        try:
            requests.get("https://www.google.com/", proxies = {https_: https_ + "://" + px['ip']}, timeout = 3)
        except Exception as x:
            print('--'+px['ip'] + ' is dead :`(')
            return False
        else:
            print('--'+px['ip'] + ' is doing :)')
        return True
    
    def get_proxy_list():
        

         