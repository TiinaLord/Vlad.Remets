import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from login_page import Login_page


class Test_1():
    def test_select_product(self):

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

        select_product_1 = WebDriverWait(driver_g, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]')))
        select_product_1.click()
        print("Product 1 is selected")

        cart = WebDriverWait(driver_g, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]')))
        cart.click()
        print("Entered in cart")

test = Test_1()
test.test_select_product()