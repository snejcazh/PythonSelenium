import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from Functions import calc

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/get_attribute.html")

image = browser.find_element(By.ID, 'treasure')
x = image.get_attribute("valuex")
y = calc(x)

textarea = browser.find_element(By.ID, "answer")
textarea.send_keys(y)

checkbox = browser.find_element(By.ID, "robotCheckbox")
checkbox.click()

radiobutton = browser.find_element(By.ID, "robotsRule")
radiobutton.click()

submit = browser.find_element(By.XPATH, "//form//button[@type='submit']")
submit.click()

time.sleep(15)
browser.quit()
