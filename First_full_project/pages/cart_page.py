from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Cart_page(Base):

    def __init__(self, driver_g):
        super().__init__(driver_g)
        self.driver_g = driver_g

    #locators
    checkout_button = '//*[@id="checkout"]'

    #getters

    def get_checkout_button(self):
        return WebDriverWait(self.driver_g, 10).until(EC.element_to_be_clickable((By.XPATH, self.checkout_button)))

    #actions

    def click_checkout_button(self):
        self.get_checkout_button().click()
        print("click checkout_button")

   #Methods
    def product_confirmation(self):
        self.get_current_url()
        self.click_checkout_button()


