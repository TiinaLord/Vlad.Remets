from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
import time

class Product_page(Base):

    def __init__(self, driver_g):
        super().__init__(driver_g)
        self.driver_g = driver_g

    #locators
    change_color = '//*[@id="p-y7vu8"]'
    change_ssd = '//*[@id="p-z136o"]'
    change_engraving = '//*[@id="p-1ue5f"]'
    button_buy = '//*[@id="pc-2DXs"]/div[2]/div[8]/div[1]/button[2]'
    button_cart = '//*[@id="header-search"]/div/div[3]/div[1]/div/a/span[1]'
    #getters

    def get_change_color(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.change_color)))
    def get_change_ssd(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.change_ssd)))
    def get_change_engraving(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.change_engraving)))
    def get_button_buy(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_buy)))
    def get_button_cart(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_cart)))




    #actions

    def click_change_color(self):
        self.get_change_color().click()
        print("click change_color")
    def click_change_ssd(self):
        self.get_change_ssd().click()
        print("click change_ssd")

    def click_change_engraving(self):
        self.get_change_engraving().click()
        print("click change_engraving")
    def click_button_buy(self):
        self.get_button_buy().click()
        print("click button_buy")
    def click_button_cart(self):
        self.get_button_cart().click()
        print("click button_cart")


   #Methods
    def macbook_options(self):
        self.get_current_url()
        self.click_change_color()
        self.click_change_ssd()
        self.click_change_engraving()
        self.click_button_buy()
        self.click_button_cart()
        self.assert_url('https://www.dns-shop.ru/product/6d3d0ac103dded20/136-noutbuk-apple-macbook-air-seryj/')
        self.screenshot()
