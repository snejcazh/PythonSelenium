import time
import math

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



list_url = ["https://stepik.org/lesson/236895/step/1",
            "https://stepik.org/lesson/236896/step/1",
            "https://stepik.org/lesson/236897/step/1",
            "https://stepik.org/lesson/236898/step/1",
            "https://stepik.org/lesson/236899/step/1",
            "https://stepik.org/lesson/236903/step/1",
            "https://stepik.org/lesson/236904/step/1",
            "https://stepik.org/lesson/236905/step/1"]

# list_url = ["https://stepik.org/lesson/236895/step/1"]

@pytest.fixture()
def browser():
    print("\nstart browser")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser")
    browser.quit()


@pytest.mark.parametrize("link", list_url)
def test_answer(browser, link):
    browser.get(link)

    WebDriverWait(browser, 15).until(
         EC.presence_of_element_located((By.CLASS_NAME, "string-quiz__textarea")))

    answer = math.log(int(time.time()))
    browser.find_element(By.CSS_SELECTOR,
                         ".string-quiz__textarea").send_keys(answer)
    browser.find_element(By.CSS_SELECTOR, ".submit-submission").click()

    WebDriverWait(browser, 12).until(
        EC.presence_of_element_located((By.CLASS_NAME, "smart-hints__hint")))

    text_hint = browser.find_element(By.CLASS_NAME, "smart-hints__hint").text
    assert text_hint == "Correct!", f"text is {text_hint}"


  #  time.sleep(8)
