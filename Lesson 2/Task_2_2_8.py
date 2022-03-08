import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/file_input.html")

browser.find_element(By.NAME, "firstname").send_keys("Misha")
browser.find_element(By.NAME, "lastname").send_keys("Ivanov")
browser.find_element(By.NAME, "email").send_keys("testik@mail.ru")

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'text.txt')
browser.find_element(By.ID, "file").send_keys(file_path)

browser.find_element(By.CSS_SELECTOR, "form > button[type='submit']").click()

time.sleep(15)
browser.quit()


