
import datetime
import time
from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
g = Service('C:\\Users\\Влад\\PycharmProjects\\pythonProject1\\chromedriver.exe')
driver_g = webdriver.Chrome(options=options, service=g)
base_url = 'https://www.saucedemo.com/' # Указываем нужный юрл
driver_g.get(base_url)
driver_g.maximize_window()
time.sleep(1)


login, password = "standard_user", "secret_sauce"

user_name = driver_g.find_element(By.XPATH, '//*[@id="user-name"]') # XPATH
user_name.send_keys(login)
print("Input login")

user_password = driver_g.find_element(By.CSS_SELECTOR, "#password") # CSS_SELECTOR
user_password.send_keys(password)
print("Input password")

button_login = driver_g.find_element(By.XPATH, '//*[@id="login-button"]')
button_login.click()
print("Click the login button")

            #Info product_1
product_1 = driver_g.find_element(By.XPATH, '//*[@id="item_4_title_link"]/div')
value_product_1 = product_1.text
print(value_product_1)

price_product_1 = driver_g.find_element(By.XPATH, '//*[@id="inventory_container"]/div/div[1]/div[2]/div[2]/div')
value_price_product_1 = price_product_1.text
print(value_price_product_1)

select_product_1 = driver_g.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]')
select_product_1.click()
print("Product is selected")

cart = driver_g.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a')
cart.click()
print("Enter in cart")

            #Info product_1 in cart
cart_product_1 = driver_g.find_element(By.XPATH, '//*[@id="item_4_title_link"]/div')
value_cart_product_1 = cart_product_1.text
print(value_cart_product_1)

assert value_product_1 == value_cart_product_1
print("Passed")

cart_price_product_1 = driver_g.find_element(By.XPATH, '//*[@id="cart_contents_container"]/div/div[1]/div[3]/div[2]/div[2]/div')
value_cart_price_product_1 = cart_price_product_1.text
print(value_cart_price_product_1)

assert value_cart_price_product_1 == value_price_product_1
print("Passed")

checkout = driver_g.find_element(By.XPATH, '//*[@id="checkout"]')
checkout.click()
print("Click Checkout")

            #input user info
first_name = driver_g.find_element(By.XPATH, '//*[@id="first-name"]')
first_name.send_keys("Alfred")
print("Input first name")

last_name = driver_g.find_element(By.XPATH, '//*[@id="last-name"]')
last_name.send_keys("Manson")
print("Input last name")

postal_code = driver_g.find_element(By.XPATH, '//*[@id="postal-code"]')
postal_code.send_keys(174357)
print("Input postal code")


but_continue = driver_g.find_element(By.XPATH, '//*[@id="continue"]')
but_continue.click()
print("Click button continue")

#Compare name and price
finish_product_1 = driver_g.find_element(By.XPATH, '//*[@id="item_4_title_link"]/div')
value_finish_product_1 = finish_product_1.text
print(value_finish_product_1)

assert value_product_1 == value_finish_product_1
print("INFO Passed")

finish_price_product_1 = driver_g.find_element(By.XPATH, '//*[@id="checkout_summary_container"]/div/div[1]/div[3]/div[2]/div[2]/div')
value_finish_price_product_1 = finish_price_product_1.text
print(value_finish_price_product_1)

assert value_finish_price_product_1 == value_price_product_1
print("INFO Passed")

sum_price = driver_g.find_element(By.XPATH, '//*[@id="checkout_summary_container"]/div/div[2]/div[6]')
value_sum_price = sum_price.text
print(value_sum_price)

item_total = "Item total: " + value_finish_price_product_1
print(item_total)

assert value_sum_price == item_total
print("Total price passed")

