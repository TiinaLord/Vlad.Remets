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
new_date.send_keys(Keys.CONTROL + "a")
new_date.send_keys(Keys.BACKSPACE) #Чистим строку
time.sleep(2)

adding_datetime = datetime.datetime.today() + datetime.timedelta(days=10) # Текущая дата + добавляем 10 дней
print(adding_datetime)
added_time = adding_datetime.strftime("%m/%d/%Y") #Меняем формат записываемой даты
print(added_time)
new_date.send_keys(added_time)



