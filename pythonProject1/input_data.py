#Авторизация + позитивная проверка значения
import time
from selenium import webdriver
from selenium.webdriver import Keys
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

user_name = driver_g.find_element(By.XPATH,'//*[@id="user-name"]') # XPATH
user_name.send_keys(login) # Отправляем данные в поле ввода
print("Input login")
# time.sleep(1)
# user_name.send_keys((Keys. BACKSPACE)) #Убираем последнюю букву
# user_name.clear() #для очистки полей ввода

user_password = driver_g.find_element(By.CSS_SELECTOR,"#password") # CSS_SELECTOR
user_password.send_keys(password)
print("Input password")
# password.send_keys(Keys.ENTER)  # пропуск команды


button_login = driver_g.find_element(By.XPATH,'//*[@id="login-button"]')
button_login.click()
print("Click the login button")


filter = driver_g.find_elements(By.XPATH,'//select[@data-test="product_sort_container"]')
time.sleep(2)
filter.click()

filter.send_keys(Keys.PAGE_DOWN) # Спускаемся в листе на нижний пункт
time.sleep(2)
filter.send_keys(Keys.RETURN) # Применяем фильтрацию

