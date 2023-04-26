from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
import time

class Order_page(Base):

    def __init__(self, driver_g):
        super().__init__(driver_g)
        self.driver_g = driver_g

    #locators
    tel_number = '//*[@id="ir-5xj1j"]'
    email = '//*[@id="ir-445j5o"]'
    change_store_button = '//*[@id="checkout"]/div/div[1]/div[2]/div[2]/div[1]/div[3]/div[2]/div/div/button'
    choose_store_button = '//*[@id="vue-avails-85288243-b7ee-4a66-9497-c1823e5d49ab"]/div/div/div[2]/div[1]/div[2]/div/div[2]/button'
    payment_method_button ='//*[@id="checkout"]/div/div[1]/div[2]/div[2]/div[2]/div[2]/div[1]/div/div[2]'
    choose_payment_radio_button = '//*[@id="checkout"]/div/div[1]/div[2]/div[2]/div[2]/div[2]/div[3]/div[2]/div/div[2]/div/div[1]'
    confirm_order_button = '//*[@id="checkout"]/div/div[1]/div[2]/div[2]/div[3]/div[1]/button'

    def get_tel_number(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.tel_number)))
    def get_email(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.email)))
    def get_change_store_button(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.change_store_button)))
    def get_choose_store_button(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.choose_store_button)))
    def get_confirm_order_button(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.confirm_order_button)))
    #actions

    def input_tel_number(self):
        self.get_tel_number().click()
        print("input tel_number")
    def input_email(self):
        self.get_email().click()
        print("input email")

    def click_change_store_button(self):
        self.get_change_store_button().click()
        print("click change_store_button")
    def click_choose_store_button(self):
        self.get_choose_store_button().click()
        print("click choose_store_button")
    def click_confirm_order_button(self):
        self.get_confirm_order_button().click()
        print("click confirm_order_button")


   #Methods
    def confirm_order(self):
        self.get_current_url()
        self.input_tel_number()
        self.input_email()
        self.click_change_store_button()
        self.click_choose_store_button()
        self.click_confirm_order_button()
        self.assert_url('https://www.dns-shop.ru/checkout-main/')
        self.screenshot()