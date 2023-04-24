from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Main_page(Base):

    def __init__(self, driver_g):
        super().__init__(driver_g)
        self.driver_g = driver_g

    #locators
    select_product_1 = '//*[@id="add-to-cart-sauce-labs-backpack"]'
    select_product_2 = '//*[@id="add-to-cart-sauce-labs-bike-light"]'
    select_product_3 = '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]'
    cart = '//*[@id="shopping_cart_container"]/a'
    menu = '//*[@id="react-burger-menu-btn"]'
    link_about = '//*[@id="about_sidebar_link"]'

    #getters

    def get_product_1(self):
        return WebDriverWait(self.driver_g, 10).until(EC.element_to_be_clickable((By.XPATH, self.select_product_1)))
    def get_product_2(self):
        return WebDriverWait(self.driver_g, 10).until(EC.element_to_be_clickable((By.XPATH, self.select_product_2)))
    def get_product_3(self):
        return WebDriverWait(self.driver_g, 10).until(EC.element_to_be_clickable((By.XPATH, self.select_product_3)))
    def get_cart(self):
        return WebDriverWait(self.driver_g, 10).until(EC.element_to_be_clickable((By.XPATH, self.cart)))
    def get_menu(self):
        return WebDriverWait(self.driver_g, 10).until(EC.element_to_be_clickable((By.XPATH, self.menu)))
    def get_link_about(self):
        return WebDriverWait(self.driver_g, 10).until(EC.element_to_be_clickable((By.XPATH, self.link_about)))


    #actions

    def click_select_product_1(self):
        self.get_product_1().click()
        print("click selected product 1")
    def click_select_product_2(self):
        self.get_product_2().click()
        print("click selected product 2")
    def click_select_product_3(self):
        self.get_product_3().click()
        print("click selected product 3")
    def click_cart(self):
        self.get_cart().click()
        print("click to cart")
    def click_menu(self):
        self.get_menu().click()
        print("click to menu")
    def click_link_about(self):
        self.get_link_about().click()
        print("click to link_about")
   #Methods
    def select_products_1(self):
        self.get_current_url()
        self.click_select_product_1()
        self.click_cart()
    def select_products_2(self):
        self.get_current_url()
        self.click_select_product_2()
        self.click_cart()
    def select_products_3(self):
        self.get_current_url()
        self.click_select_product_3()
        self.click_cart()

    def select_menu_about(self):
        self.get_current_url()
        self.click_menu()
        self.click_link_about()
        self.assert_url("https://saucelabs.com/")