import time
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


def test_link_about():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    g = Service('C:\\Users\\Влад\\PycharmProjects\\First_full_project\\chromedriver.exe')
    driver_g = webdriver.Chrome(options=options, service=g)

    print("Test is started")

    login = Login_page(driver_g)
    login.authorization()

    mp = Main_page(driver_g)
    mp.select_menu_about()

    print("finish test")


