from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base

class Notebook_page(Base):

    def __init__(self, driver_g):
        super().__init__(driver_g)
        self.driver_g = driver_g

    #locators
    choose_notebook = '/html/body/div[2]/div[1]/div/a[1]/div[1]'

    #getters

    def get_choose_notebook(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.choose_notebook)))
    #actions

    def click_choose_notebook(self):
        self.get_choose_notebook().click()
        print("click choose_notebook group")
   #Methods
    def choose_notebook1(self):
        self.get_current_url()
        self.click_choose_notebook()