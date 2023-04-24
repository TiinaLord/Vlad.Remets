from base.base_class import Base
class Finish_page(Base):

    def __init__(self, driver_g):
        super().__init__(driver_g)
        self.driver_g = driver_g

    #locators
    #getters
    #actions
    #Methods
    def finish(self):
        self.get_current_url()
        self.assert_url('https://www.saucedemo.com/checkout-complete.html')
        self.screenshot()

