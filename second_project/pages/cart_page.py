from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
import time

class Cart_page(Base):

    def __init__(self, driver_g):
        super().__init__(driver_g)
        self.driver_g = driver_g

    #locators
    change_quantity = '//*[@id="cart-page-new"]/div[1]/div[2]/div/div/div[1]/div/div/div/div/div[1]/div[1]/div[2]/div/button[2]/i'
    add_guarantee = '//*[@id="cart-page-new"]/div[1]/div[2]/div/div/div[1]/div/div/div/div/div[1]/div[3]/div[2]/div/div/div/div[3]/div'
    add_service = '//*[@id="cart-page-new"]/div[1]/div[2]/div/div/div[1]/div/div/div/div/div[2]/div[1]/div[1]/div[2]/div[1]/div/div/div[1]/label/span[1]'
    add_accessory = '//*[@id="cart-page-new"]/div[1]/div[2]/div/div/div[1]/div/div/div/div/div[2]/div[2]/div/div[2]/div/div/div/div/div[1]/div/div[1]/button'
    button_order = '//*[@id="buy-btn-main"]'
    #getters

    def get_change_quantity(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.change_quantity)))
    def get_add_guarantee(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_guarantee)))
    def get_add_service(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_service)))
    def get_add_accessory(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_accessory)))
    def get_button_order(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_order)))
    #actions

    def click_change_quantity(self):
        self.get_change_quantity().click()
        print("click change_quantity")
    def click_add_guarantee(self):
        self.get_add_guarantee().click()
        print("click add_guarantee")

    def click_add_service(self):
        self.get_add_service().click()
        print("click add_service")
    def click_add_accessory(self):
        self.get_add_accessory().click()
        print("click add_accessory")
    def click_button_order(self):
        self.get_button_order().click()
        print("click button_order")


   #Methods
    def cart_to_order(self):
        self.get_current_url()
        self.click_change_quantity()
        self.click_add_guarantee()
        self.click_add_service()
        self.click_add_accessory()
        self.click_button_order()
        self.assert_url('https://www.dns-shop.ru/cart/?activeTabId=1')
