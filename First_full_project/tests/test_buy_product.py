import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.cart_page import Cart_page
from pages.client_information_page import Client_information_page
from pages.finish_page import Finish_page
from pages.login_page import Login_page
from pages.main_page import Main_page
from pages.payment_page import Payment_page

@pytest.mark.run(order=3)
def test_buy_product_1(set_up):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    g = Service('C:\\Users\\Влад\\PycharmProjects\\OOP_tests\\chromedriver.exe')
    driver_g = webdriver.Chrome(options=options, service=g)

    print("Test 1 is started")

    login = Login_page(driver_g)
    login.authorization()
    mp = Main_page(driver_g)
    mp.select_products_1()
    cp = Cart_page(driver_g)
    cp.click_checkout_button()

    cip = Client_information_page(driver_g)
    cip.input_information()

    p = Payment_page(driver_g)
    p.click_finish_button()

    f = Finish_page(driver_g)
    f.finish()
@pytest.mark.run(order=1)
def test_buy_product_2(set_group):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    g = Service('C:\\Users\\Влад\\PycharmProjects\\First_full_project\\chromedriver.exe')
    driver_g = webdriver.Chrome(options=options, service=g)

    print("Test 2 is started")

    login = Login_page(driver_g)
    login.authorization()
    mp = Main_page(driver_g)
    mp.select_products_2()
    cp = Cart_page(driver_g)
    cp.click_checkout_button()

@pytest.mark.run(order=2)
def test_buy_product_3():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    g = Service('C:\\Users\\Влад\\PycharmProjects\\First_full_project\\chromedriver.exe')
    driver_g = webdriver.Chrome(options=options, service=g)

    print("Test 3 is started")

    login = Login_page(driver_g)
    login.authorization()
    mp = Main_page(driver_g)
    mp.select_products_3()
    cp = Cart_page(driver_g)
    cp.click_checkout_button()