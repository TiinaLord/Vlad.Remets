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
base_url = 'https://demoqa.com/buttons'
driver_g.get(base_url)
driver_g.maximize_window()

action = ActionChains(driver_g)
double = driver_g.find_element(By.XPATH, '//*[@id="doubleClickBtn"]')
action.double_click(double).perform()

right_click = driver_g.find_element(By.XPATH, '//*[@id="rightClickBtn"]')
action.context_click(right_click).perform()