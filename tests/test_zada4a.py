import time
import math
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('Links',
                         ["236895/step/1",
                          "236896/step/1",
                          "236897/step/1",
                          "236898/step/1",
                          "236899/step/1",
                          "236903/step/1",
                          "236904/step/1",
                          "236905/step/1"])
def test_mark(browser, Links):
    link = f"https://stepik.org/lesson/{Links}/"
    browser.get(link)
    browser.implicitly_wait(20)
    answer = math.log(int(time.time()))
    browser.find_element(By.CLASS_NAME, "ember-text-area").send_keys(str(answer))
    browser.find_element(By.CLASS_NAME, "submit-submission").click()
    response = browser.find_element(By.CLASS_NAME, "smart-hints__hint")
    assert "Correct" in response.text, print(response.text)
