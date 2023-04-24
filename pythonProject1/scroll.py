
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
base_url = 'https://www.saucedemo.com/' # Указываем нужный юрл
driver_g.get(base_url)
driver_g.maximize_window()
time.sleep(1)


login, password = "standard_user", "secret_sauce"

user_name = driver_g.find_element(By.XPATH,'//*[@id="user-name"]') # XPATH
user_name.send_keys(login)
print("Input login")

user_password = driver_g.find_element(By.CSS_SELECTOR,"#password") # CSS_SELECTOR
user_password.send_keys(password)
print("Input password")

button_login = driver_g.find_element(By.XPATH,'//*[@id="login-button"]')
button_login.click()
print("Click the login button")

# time.sleep(1)
# driver_g.execute_script("window.scrollTo(0, 200)") # (X, Y)- где X - смещение влево/вправо, Y - Вверх/вниз
time.sleep(2)

#Способ 2
action = ActionChains(driver_g) #Показываем системе, что хотим управлять конкретным драйвером
add_to_cart = driver_g.find_element(By.XPATH, '//*[@id="add-to-cart-test.allthethings()-t-shirt-(red)"]')
action.move_to_element(add_to_cart).perform()



current_time = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
name_screen = "sceenshot" + current_time + ".png"
driver_g.save_screenshot('C:\\Users\\Влад\\PycharmProjects\\pythonProject1\\screens\\' + name_screen)