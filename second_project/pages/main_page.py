from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base

class Main_page(Base):

    url = 'https://www.dns-shop.ru/'

    def __init__(self, driver_g):
        super().__init__(driver_g)
        self.driver_g = driver_g

    #locators
    select_pc = '//*[@id="catalog"]/div[1]/div[5]/a/a'


    #getters

    def get_select_pc(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_pc)))
    #actions

    def click_select_pc(self):
        self.get_select_pc().click()
        print("click selected pc group")
   #Methods
    def select_pc1(self):
        self.driver_g.get(self.url)
        self.get_current_url()
        self.click_select_pc()
