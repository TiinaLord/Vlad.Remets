import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from login_page import Login_page


class Test_1():
    def test_login_first_user(self):

        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        g = Service('C:\\Users\\Влад\\PycharmProjects\\OOP_tests\\chromedriver.exe')
        driver_g = webdriver.Chrome(options=options, service=g)
        base_url = 'https://www.saucedemo.com/'
        driver_g.get(base_url)
        driver_g.maximize_window()
        time.sleep(1)

        print("Test is started")
        login = Login_page(driver_g)
        login.authorization(login_name="standard_user", login_password="secret_sauce")
        print("User 1 is logged")

        time.sleep(1)
        driver_g.back()

        time.sleep(1)
        login.authorization(login_name="locked_out_user", login_password="secret_sauce")
        print("User 2 is not logged")
        time.sleep(1)

        reset_button = WebDriverWait(driver_g, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]/h3/button')))
        reset_button.click()

        clear_name = WebDriverWait(driver_g, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="user-name"]')))
        clear_name.click()
        time.sleep(2)
        clear_name.send_keys(Keys.CONTROL + "a")
        clear_name.send_keys(Keys.BACKSPACE)

        clear_password = WebDriverWait(driver_g, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="password"]')))
        clear_password.click()
        time.sleep(2)
        clear_password.send_keys(Keys.CONTROL + "a")
        clear_password.send_keys(Keys.BACKSPACE)

        time.sleep(2)
        login.authorization(login_name="problem_user", login_password="secret_sauce")
        print("User 3 is logged")
        time.sleep(1)
        driver_g.back()

        login.authorization(login_name="performance_glitch_user", login_password="secret_sauce")
        time.sleep(5)

        button_login = WebDriverWait(driver_g, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="login-button"]')))
        button_login.click()



test = Test_1()
test.test_login_first_user()




