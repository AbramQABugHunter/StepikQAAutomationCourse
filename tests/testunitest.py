from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import time

class TestUnitest(unittest.TestCase):
    def test_Unitest1(self):
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/registration1.html")

        browser.find_element(By.CSS_SELECTOR, "div.first_block .first").send_keys("Ivan")
        browser.find_element(By.CSS_SELECTOR, "div.first_block .second").send_keys("Petrov")
        browser.find_element(By.CSS_SELECTOR, "div.first_block .third").send_keys("petrov@mail.ru")
        browser.find_element(By.CSS_SELECTOR, "div.second_block .first").send_keys("1111")
        browser.find_element(By.CSS_SELECTOR, "div.second_block .second").send_keys("address")
        browser.find_element(By.CSS_SELECTOR, "button.btn").click()
        time.sleep(1)
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, 'текст не совпадает')

    def test_un2(self):
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/registration2.html")

        browser.find_element(By.CSS_SELECTOR, "div.first_block .first").send_keys("Ivan")
        browser.find_element(By.CSS_SELECTOR, "div.first_block .second").send_keys("Petrov")
        browser.find_element(By.CSS_SELECTOR, "div.first_block .third").send_keys("petrov@mail.ru")
        browser.find_element(By.CSS_SELECTOR, "div.second_block .first").send_keys("1111")
        browser.find_element(By.CSS_SELECTOR, "div.second_block .second").send_keys("address")
        browser.find_element(By.CSS_SELECTOR, "button.btn").click()
        time.sleep(1)
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, 'текст не совпадает')

if __name__ == "__main__":
    unittest.main()