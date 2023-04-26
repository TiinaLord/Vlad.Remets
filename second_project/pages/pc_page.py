from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base

class Pc_page(Base):

    def __init__(self, driver_g):
        super().__init__(driver_g)
        self.driver_g = driver_g

    #locators
    select_notebook = '/html/body/div[2]/div[1]/div[2]/a[1]/div[1]/span'


    #getters

    def get_select_notebook(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_notebook)))
    #actions

    def click_select_notebook(self):
        self.get_select_notebook().click()
        print("click select_notebook group")
   #Methods
    def select_notebook1(self):
        self.get_current_url()
        self.click_select_notebook()
