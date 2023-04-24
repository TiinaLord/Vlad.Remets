from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
g = Service('C:\\Users\\Влад\\PycharmProjects\\pythonProject1\\chromedriver.exe')
driver_g = webdriver.Chrome(options=options, service=g)
base_url = 'https://demoqa.com/dynamic-properties'
driver_g.get(base_url)
driver_g.maximize_window()
# driver_g.implicitly_wait(10) #Неявное ожидание для каждого действия

print("Test is started")
# visible_button = driver_g.find_element(By.XPATH, '//*[@id="visibleAfter"]')
# visible_button.click()
visible_button = WebDriverWait(driver_g, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="visibleAfter"]')))
visible_button.click()
print("Test is finished")
