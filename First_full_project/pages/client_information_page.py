from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Client_information_page(Base):

    def __init__(self, driver_g):
        super().__init__(driver_g)
        self.driver_g = driver_g

    #locators
    first_name = '//*[@id="first-name"]'
    last_name = '//*[@id="last-name"]'
    postal_code = '//*[@id="postal-code"]'
    continue_button = '//*[@id="continue"]'

    #getters

    def get_first_name(self):
        return WebDriverWait(self.driver_g, 10).until(EC.element_to_be_clickable((By.XPATH, self.first_name)))
    def get_last_name(self):
        return WebDriverWait(self.driver_g, 10).until(EC.element_to_be_clickable((By.XPATH, self.last_name)))
    def get_postal_code(self):
        return WebDriverWait(self.driver_g, 10).until(EC.element_to_be_clickable((By.XPATH, self.postal_code)))
    def get_continue_button(self):
        return WebDriverWait(self.driver_g, 10).until(EC.element_to_be_clickable((By.XPATH, self.continue_button)))

    #actions

    def input_first_name(self, first_name):
        self.get_first_name().send_keys(first_name)
        print("input user_name")

    def input_last_name(self, last_name):
        self.get_last_name().send_keys(last_name)
        print("input last_name")

    def input_postal_code(self, postal_code):
        self.get_postal_code().send_keys(postal_code)
        print("input postal_code")
    def click_continue_button(self):
        self.get_continue_button().click()
        print("click continue_button")
   #Methods
    def input_information(self):
        self.get_current_url()
        self.input_first_name("Joshua")
        self.input_last_name("Phoebes")
        self.input_postal_code("173599")
        self.click_continue_button()


