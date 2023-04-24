#Авторизация + позитивная проверка значения
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
g = Service('C:\\Users\\Влад\\PycharmProjects\\pythonProject1\\chromedriver.exe')
driver_g = webdriver.Chrome(options=options, service=g)
base_url = 'https://www.saucedemo.com/' # Указываем нужный юрл
driver_g.get(base_url) # Переходим по url
driver_g.maximize_window() # Открываем окно на полный экран
time.sleep(3) # Задержка на указанное количество секунд


login, password = "standard_user", "secret_sauce"

#user_name = driver_g.find_element(By.ID,"user-name")  Находим нужный элемент через id
#user_name = driver_g.find_element(By.NAME,"user-name") через NAME
user_name = driver_g.find_element(By.XPATH,'//*[@id="user-name"]') #XPATH
user_name.send_keys(login) # Отправляем данные в поле ввода
print("Input login")
user_password = driver_g.find_element(By.CSS_SELECTOR,"#password") #CSS_SELECTOR
user_password.send_keys(password)
print("Input password")
button_login = driver_g.find_element(By.XPATH,'//*[@id="login-button"]')
button_login.click() #клики по кнопкам
print("Click the login button")


text_products = driver_g.find_element(By.XPATH,'//*[@id="header_container"]/div[2]/span')
value_text_products = text_products.text #считывание значения и выводим
print(value_text_products)
assert value_text_products == "Products" #Позитивная проверка значения в конкретном элементе
print(" Value in title is Passed")

url_inventory = "https://www.saucedemo.com/inventory.html"
get_url_inventory = driver_g.current_url
print(get_url_inventory)
assert url_inventory == get_url_inventory
print("url_inventory Passed")

time.sleep(1)
driver_g.refresh()