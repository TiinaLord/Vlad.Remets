from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Login_page():
    def __init__(self, driver_g):
        self.driver_g = driver_g

    def authorization(self, login_name, login_password):

        user_name = WebDriverWait(self.driver_g, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="user-name"]')))  # XPATH
        user_name.send_keys(login_name)
        print("Input login")

        user_password = WebDriverWait(self.driver_g, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="password"]')))  # CSS_SELECTOR
        user_password.send_keys(login_password)
        print("Input password")

        button_login = WebDriverWait(self.driver_g, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="login-button"]')))
        button_login.click()
        print("Click the login button")