from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
import time

class Items_page(Base):

    def __init__(self, driver_g):
        super().__init__(driver_g)
        self.driver_g = driver_g

    #locators
    rating_filter = '/html/body/div[2]/div/div[2]/div[1]/div/div[3]/div[1]/div[2]/label/span[2]'
    collapse_avail_bar = '/html/body/div[2]/div/div[2]/div[1]/div/div[3]/div[1]/div[1]/a/span'
    input_price_from = '/html/body/div[2]/div/div[2]/div[1]/div/div[3]/div[1]/div[4]/div/div/div[1]/input'
    input_price_to = '/html/body/div[2]/div/div[2]/div[1]/div/div[3]/div[1]/div[4]/div/div/div[2]/input'
    apple_filter = '/html/body/div[2]/div/div[2]/div[1]/div/div[3]/div[1]/div[6]/div/div/div[2]/label[3]/span[2]'
    confirm_button = '/html/body/div[2]/div/div[2]/div[1]/div/div[3]/div[2]/div/button[1]'
    product_page = '/html/body/div[2]/div/div[2]/div[2]/div[3]/div/div[2]/div[1]/a/span'
    #getters

    def get_rating_filter(self):
        return WebDriverWait(self.driver_g, 60).until(EC.element_to_be_clickable((By.XPATH, self.rating_filter)))
    def get_collapse_avail_bar(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.collapse_avail_bar)))
    def get_input_price_from(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.input_price_from)))
    def get_input_price_to(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.input_price_to)))
    def get_apple_filter(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.apple_filter)))
    def get_confirm_button(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.confirm_button)))
    def get_product_page(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_page)))




    #actions

    def click_rating_filter(self):
        self.get_rating_filter().click()
        print("click rating_filter")
    def click_collapse_avail_bar(self):
        self.get_collapse_avail_bar().click()
        print("click collapse_avail_bar")

    def click_input_price_from(self, input_price_from):
        self.get_input_price_from().send_keys(input_price_from)
        print("input_price_from")
    def click_input_price_to(self, input_price_to):
        self.get_input_price_to().send_keys(input_price_to)
        print("input_price_to")
    def scroll_to_apple(self):
        self.driver_g.execute_script("window.scrollTo(0, 1200)")
        print('scroll_to_apple')
    def click_apple_filter(self):
        self.get_apple_filter().click()
        print("click apple_filter")
    def scroll_to_confirm(self):
        self.driver_g.execute_script("window.scrollTo(0, 1700)")
        print('scroll_to_confirm')
    def click_confirm_button(self):
        self.get_confirm_button().click()
        print("click confirm_button")
    def scroll_to_first_item(self):
        self.driver_g.execute_script("window.scrollTo(0, -1700)")
        print('scroll_to_first_item')
    def click_product_page(self):
        self.get_product_page().click()
        print("click product_page")


   #Methods
    def filters(self):
        self.get_current_url()
        self.click_rating_filter()
        self.click_collapse_avail_bar()
        self.click_input_price_from("140000")
        self.click_input_price_to("250000")
        self.scroll_to_apple()
        self.click_apple_filter()
        self.scroll_to_confirm()
        self.click_confirm_button()
        self.scroll_to_first_item()
        time.sleep(5)
        self.click_product_page()
        self.assert_url('https://www.dns-shop.ru/catalog/17a892f816404e77/noutbuki/')
        self.screenshot()