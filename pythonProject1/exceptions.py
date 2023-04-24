from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
g = Service('C:\\Users\\Влад\\PycharmProjects\\pythonProject1\\chromedriver.exe')
driver_g = webdriver.Chrome(options=options, service=g)
# base_url = 'https://demoqa.com/dynamic-properties'
base_url = 'https://demoqa.com/radio-button'
driver_g.get(base_url)
driver_g.maximize_window()


# try:
   # visible_button = driver_g.find_element(By.XPATH, '//*[@id="visibleAfter"]')
   # visible_button.click()
# except NoSuchElementException as exception:
    # print("No such element exception")
    # time.sleep(5)
    # visible_button = driver_g.find_element(By.XPATH, '//*[@id="visibleAfter"]')
   # visible_button.click()
   # print("Click visible button")

yes_button = driver_g.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div[2]/label')
yes_button.click()
try:
    message =  driver_g.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div[2]/label')
    value_message = message.text
    print(value_message)
    assert value_message == "No"
except AssertionError as exception:
    driver_g.refresh()
    yes_button = driver_g.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div[2]/label')
    yes_button.click()
    message = driver_g.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div[2]/label')
    value_message = message.text
    print(value_message)
    assert value_message == "Yes"
    print("The message is Yes")
print("Test done")