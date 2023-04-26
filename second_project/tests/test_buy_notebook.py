import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pages.cart_page import Cart_page
from pages.items_page import Items_page
from pages.main_page import Main_page
from pages.notebook_page import Notebook_page
from pages.order_page import Order_page
from pages.pc_page import Pc_page
from pages.product_page import Product_page

@pytest.mark.run(order=1)
def test_buy_macbook(set_up):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    g = Service('C:\\Users\\Влад\\PycharmProjects\\second_project\\chromedriver.exe')
    driver_g = webdriver.Chrome(options=options, service=g)
    driver_g.maximize_window()
    print("Test 1 is started")

    mp = Main_page(driver_g)
    mp.select_pc1()

    pc = Pc_page(driver_g)
    pc.select_notebook1()

    cn = Notebook_page(driver_g)
    cn.choose_notebook1()

    ip = Items_page(driver_g)
    ip.filters()

    pp = Product_page(driver_g)
    pp.macbook_options()

    cp = Cart_page(driver_g)
    cp.cart_to_order()

    op = Order_page(driver_g)
    op.confirm_order()
    print("Test 1 is finished")
