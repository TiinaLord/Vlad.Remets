import datetime
import time
from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
g = Service('C:\\Users\\Влад\\PycharmProjects\\pythonProject1\\chromedriver.exe')
driver_g = webdriver.Chrome(options=options, service=g)
base_url = 'https://demoqa.com/checkbox'
driver_g.get(base_url)
driver_g.maximize_window()
time.sleep(1)


check_box = driver_g.find_element(By.XPATH,'//*[@id="tree-node"]/ol/li/span/label')
check_box.click()

# radio_button = driver_g.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div[2]/label')
# radio_button.click()


button_list = driver_g.find_element(By.XPATH,'//*[@id="tree-node"]/ol/li/span/button/svg')
button_list.click()
