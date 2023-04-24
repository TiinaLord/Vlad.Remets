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
base_url = 'https://demoqa.com/date-picker'
driver_g.get(base_url)
driver_g.maximize_window()

new_date = driver_g.find_element(By.XPATH, '//*[@id="datePickerMonthYearInput"]')
new_date.click()
time.sleep(2)
#now_date = datetime.datetime.utcnow().srtftime('%d')
#print(now_date)
#date = int(now_date) + 1
#locator = '//*[@id="datePickerMonthYear"]/div[2]/div[2]/div/div/div[2]/div[2]/div[4]/div[5]' + str(date) + "th, 2023"
#print(locator)

pick_date = driver_g.find_element(By.XPATH, '//*[@id="datePickerMonthYear"]/div[2]/div[2]/div/div/div[2]/div[2]/div[4]/div[5]')
pick_date.click()
new_date.send_keys(Keys.CONTROL + "a")
new_date.send_keys(Keys.BACKSPACE)
time.sleep(2)
new_date.send_keys("30/04/2023")
time.sleep(1)
new_date.send_keys(Keys.RETURN)