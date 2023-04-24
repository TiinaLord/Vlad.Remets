
import time
from selenium import webdriver
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

            #Input the number
print("Hello, welcome to the market, choose 1 of these 6 items")
pick_product = input()
print("You picked the ", pick_product, "let's make the order for you")


            # Info product_1
if pick_product == 1:
    product_1 = driver_g.find_element(By.XPATH, '//*[@id="item_4_title_link"]/div')
    value_product_1 = product_1.text
    print(value_product_1)

    price_product_1 = driver_g.find_element(By.XPATH, '//*[@id="inventory_container"]/div/div[1]/div[2]/div[2]/div')
    value_price_product_1 = price_product_1.text
    print(value_price_product_1)

    import time
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.common.by import By

    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    g = Service('C:\\Users\\Влад\\PycharmProjects\\pythonProject1\\chromedriver.exe')
    driver_g = webdriver.Chrome(options=options, service=g)
    base_url = 'https://www.saucedemo.com/'  # Указываем нужный юрл
    driver_g.get(base_url)
    driver_g.maximize_window()
    time.sleep(1)

    login, password = "standard_user", "secret_sauce"

    user_name = driver_g.find_element(By.XPATH, '//*[@id="user-name"]')  # XPATH
    user_name.send_keys(login)
    print("Input login")

    user_password = driver_g.find_element(By.CSS_SELECTOR, "#password")  # CSS_SELECTOR
    user_password.send_keys(password)
    print("Input password")

    button_login = driver_g.find_element(By.XPATH, '//*[@id="login-button"]')
    button_login.click()
    print("Click the login button")

    # Info product_1
    list_pick_product = ['//*[@id="item_4_title_link"]/div', '//*[@id="item_0_title_link"]/div',
                         '//*[@id="item_1_title_link"]/div', '//*[@id="item_5_title_link"]/div',
                         '//*[@id="item_2_title_link"]/div', '//*[@id="item_3_title_link"]/div']
    list_pick_value_product = ['//*[@id="inventory_container"]/div/div[1]/div[2]/div[2]/div',
                               '//*[@id="inventory_container"]/div/div[2]/div[2]/div[2]/div',
                               '//*[@id="inventory_container"]/div/div[3]/div[2]/div[2]/div',
                               '//*[@id="inventory_container"]/div/div[4]/div[2]/div[2]/div',
                               '//*[@id="inventory_container"]/div/div[5]/div[2]/div[2]/div',
                               '//*[@id="inventory_container"]/div/div[6]/div[2]/div[2]/div']
    list_pick_add_product = ['//*[@id="add-to-cart-sauce-labs-backpack"]',
                             '//*[@id="add-to-cart-sauce-labs-bike-light"]',
                             '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]',
                             '//*[@id="add-to-cart-sauce-labs-fleece-jacket"]',
                             '//*[@id="add-to-cart-sauce-labs-onesie"]',
                             '//*[@id="add-to-cart-test.allthethings()-t-shirt-(red)"]']
    list_cart_product = ['//*[@id="item_4_title_link"]/div', '//*[@id="item_0_title_link"]/div',
                         '//*[@id="item_1_title_link"]/div', '//*[@id="item_5_title_link"]/div',
                         '//*[@id="item_2_title_link"]/div', '//*[@id="item_3_title_link"]/div']
    list_cart_price = ['//*[@id="cart_contents_container"]/div/div[1]/div[3]/div[2]/div[2]/div',
                       '//*[@id="cart_contents_container"]/div/div[1]/div[3]/div[2]/div[2]/div',
                       '//*[@id="cart_contents_container"]/div/div[1]/div[3]/div[2]/div[2]/div',
                       '//*[@id="cart_contents_container"]/div/div[1]/div[3]/div[2]/div[2]/div',
                       '//*[@id="cart_contents_container"]/div/div[1]/div[3]/div[2]/div[2]/div',
                       '//*[@id="cart_contents_container"]/div/div[1]/div[3]/div[2]/div[2]/div']
    list_finish_value = ['//*[@id="item_4_title_link"]/div', '//*[@id="item_0_title_link"]/div',
                         '//*[@id="item_1_title_link"]/div', '//*[@id="item_5_title_link"]/div',
                         '//*[@id="item_2_title_link"]/div', '//*[@id="item_3_title_link"]/div']
    list_finish_price = ['//*[@id="checkout_summary_container"]/div/div[1]/div[3]/div[2]/div[2]/div',
                         '//*[@id="checkout_summary_container"]/div/div[1]/div[3]/div[2]/div[2]/div',
                         '//*[@id="checkout_summary_container"]/div/div[1]/div[3]/div[2]/div[2]/div',
                         '//*[@id="checkout_summary_container"]/div/div[1]/div[3]/div[2]/div[2]/div',
                         '//*[@id="checkout_summary_container"]/div/div[1]/div[3]/div[2]/div[2]/div',
                         '//*[@id="checkout_summary_container"]/div/div[1]/div[3]/div[2]/div[2]/div']

    print("Hello, welcome to the market, choose 1 of these 6 items")
    pick_product = int(input())
    print("You picked the ", pick_product, "let's make the order for you")
    if pick_product == 1:  # вызываем нужные локаторы на каждом этапе из списка с помощью if else
        x, y, z, a, b, q, w = list_pick_product[0], list_pick_value_product[0], list_pick_add_product[0], \
        list_cart_product[0], list_cart_price[0], list_finish_value[0], list_finish_price[0]
    elif pick_product == 2:
        x, y, z, a, b, q, w = list_pick_product[1], list_pick_value_product[1], list_pick_add_product[1], \
        list_cart_product[1], list_cart_price[1], list_finish_value[1], list_finish_price[1]
    elif pick_product == 3:
        x, y, z, a, b, q, w = list_pick_product[2], list_pick_value_product[2], list_pick_add_product[2], \
        list_cart_product[2], list_cart_price[2], list_finish_value[2], list_finish_price[2]
    elif pick_product == 4:
        x, y, z, a, b, q, w = list_pick_product[3], list_pick_value_product[3], list_pick_add_product[3], \
        list_cart_product[3], list_cart_price[3], list_finish_value[3], list_finish_price[3]
    elif pick_product == 5:
        x, y, z, a, b, q, w = list_pick_product[4], list_pick_value_product[4], list_pick_add_product[4], \
        list_cart_product[4], list_cart_price[4], list_finish_value[4], list_finish_price[4]
    elif pick_product == 6:
        x, y, z, a, b, q, w = list_pick_product[5], list_pick_value_product[5], list_pick_add_product[5], \
        list_cart_product[5], list_cart_price[5], list_finish_value[5], list_finish_price[5]
    elif pick_product > 6 or pick_product < 1:
        print("You can only pick 1-6 items, please try again")

    product_1 = driver_g.find_element(By.XPATH, x)
    value_product_1 = product_1.text
    print(value_product_1)

    price_product_1 = driver_g.find_element(By.XPATH, y)
    value_price_product_1 = price_product_1.text
    print(value_price_product_1)

    select_product_1 = driver_g.find_element(By.XPATH, z)
    select_product_1.click()
    print("Product 1 is selected")

    cart = driver_g.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a')
    cart.click()
    print("Enter in cart")

    # Info product_1 in cart
    cart_product_1 = driver_g.find_element(By.XPATH, a)
    value_cart_product_1 = cart_product_1.text
    print(value_cart_product_1)

    assert value_product_1 == value_cart_product_1
    print("Passed")

    cart_price_product_1 = driver_g.find_element(By.XPATH, b)
    value_cart_price_product_1 = cart_price_product_1.text
    print(value_cart_price_product_1)

    assert value_cart_price_product_1 == value_price_product_1
    print("Passed")

    checkout = driver_g.find_element(By.XPATH, '//*[@id="checkout"]')
    checkout.click()
    print("Click Checkout")

    # input user info
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

    # Compare name and price
    finish_product_1 = driver_g.find_element(By.XPATH, q)
    value_finish_product_1 = finish_product_1.text
    print(value_finish_product_1)

    assert value_product_1 == value_finish_product_1
    print("INFO Passed")

    finish_price_product_1 = driver_g.find_element(By.XPATH, w)
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


