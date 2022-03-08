import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from Functions import calc

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/alert_accept.html")

browser.find_element(By.CSS_SELECTOR, ".btn-primary[type='submit']").click()

confirm = browser.switch_to.alert
confirm.accept()

x = browser.find_element(By.ID, "input_value").text
y = calc(x)

browser.find_element(By.ID, "answer").send_keys(y)

browser.find_element(By.CSS_SELECTOR, "button.btn-primary[type='submit']").click()

time.sleep(10)
browser.quit()
