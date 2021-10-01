from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")

class ProductPageLocators():
    ADD_TO_CARD_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    REVIEW_BUTTON = (By.ID, "write_review")
    TOTAL_BASKET_PRICE = (By.CSS_SELECTOR, 'div.alertinner  > p > strong')
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.col-sm-6 > h1")
    PRODUCT_NAME_MESSAGE = (By.CSS_SELECTOR, "div#messages > :nth-child(1) > div > strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div#messages > :nth-child(1)")

