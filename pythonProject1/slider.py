from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
g = Service('C:\\Users\\Влад\\PycharmProjects\\pythonProject1\\chromedriver.exe')
driver_g = webdriver.Chrome(options=options, service=g)
base_url = 'https://html5css.ru/howto/howto_js_rangeslider.php'
driver_g.get(base_url)
driver_g.maximize_window()

action = ActionChains(driver_g)

slider = driver_g.find_element(By.XPATH, '//*[@id="slidecontainer"]/input')
action.click_and_hold(slider).move_by_offset(20, 0).release().perform()
print("slider activated")

