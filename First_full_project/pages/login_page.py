from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Login_page(Base):

    url = 'https://www.saucedemo.com/'

    def __init__(self, driver_g):
        super().__init__(driver_g)
        self.driver_g = driver_g

    #locators
    user_name = '//*[@id="user-name"]'
    password = '//*[@id="password"]'
    login_button = '//*[@id="login-button"]'
    main_word = '//*[@id="header_container"]/div[2]/span'

    #getters

    def get_user_name(self):
        return WebDriverWait(self.driver_g, 10).until(EC.element_to_be_clickable((By.XPATH, self.user_name)))
    def get_password(self):
        return WebDriverWait(self.driver_g, 10).until(EC.element_to_be_clickable((By.XPATH, self.password)))
    def get_login_button(self):
        return WebDriverWait(self.driver_g, 10).until(EC.element_to_be_clickable((By.XPATH, self.login_button)))

    def get_main_word(self):
        return WebDriverWait(self.driver_g, 10).until(EC.element_to_be_clickable((By.XPATH, self.main_word)))

    #actions

    def input_user_name(self, user_name):
        self.get_user_name().send_keys(user_name)
        print("input user_name")

    def input_password(self, password):
        self.get_password().send_keys(password)
        print("input password")

    def click_login_button(self):
        self.get_login_button().click()
        print("click login_button")
   #Methods
    def authorization(self):
        self.driver_g.get(self.url)
        self.driver_g.maximize_window()
        self.get_current_url()
        self.input_user_name("standard_user")
        self.input_password("secret_sauce")
        self.click_login_button()
        self.assert_word(self.get_main_word(), 'Products')

