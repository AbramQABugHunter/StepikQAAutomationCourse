from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')


class ProductPageLocators:
    ADD_TO_BASCET_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form > button")
    MESSAGE_ABOUT_ADDING = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, "#content_inner  div.col-sm-6.product_main > h1")
    MESSAGE_BASKET_TOTAL = (By.CSS_SELECTOR, "#messages  div > p:nth-child(1) > strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "#content_inner  div.col-sm-6.product_main > p.price_color")
    SUCCES_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div")
