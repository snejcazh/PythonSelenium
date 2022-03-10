import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from Functions import calc

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/execute_script.html")

x = browser.find_element(By.ID, "input_value").text
y = calc(x)

browser.execute_script("window.scrollBy(0, 100);")

browser.find_element(By.ID, "answer").send_keys(y)

browser.find_element(By.ID, "robotCheckbox").click()

browser.find_element(By.ID, "robotsRule").click()

browser.find_element(By.CSS_SELECTOR, "form > button[type='submit']").click()

time.sleep(15)
browser.quit()







