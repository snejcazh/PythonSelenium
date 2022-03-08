import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/selects1.html")

x = int(browser.find_element(By.ID, "num1").text)
y = int(browser.find_element(By.ID, "num2").text)

select = Select(browser.find_element(By.ID, "dropdown"))
select.select_by_value(str(x + y))

browser.find_element(By.XPATH, "//form/button[@type='submit']").click()

time.sleep(12)
browser.quit()