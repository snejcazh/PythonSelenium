import time
from selenium import  webdriver
from selenium.webdriver.common.by import By

from Functions import calc

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/redirect_accept.html")

browser.find_element(By.CSS_SELECTOR, ".trollface.btn-primary").click()

new_window = browser.window_handles[1]
browser.switch_to.window(new_window)

x = browser.find_element(By.ID, "input_value").text
y = calc(x)

browser.find_element(By.ID, "answer").send_keys(y)

browser.find_element(By.XPATH, "//button[@class='btn btn-primary' and @type='submit']").click()

time.sleep(10)
browser.quit()
