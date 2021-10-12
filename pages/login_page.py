from .base_page import BasePage
from .locators import LoginPageLocators
import string
import random


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, 'It is not a login page'
        assert True

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented in the page"    # реализуйте проверку, что есть форма логина
        assert True

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented in the page"
        assert True

    def register_new_user(self, email, password):
        email_register_form = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL)
        email_register_form.send_keys(email)
        password_register_form = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD)
        password_register_form.send_keys(password)
        password_confirm_register_form = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_CONFIRM)
        password_confirm_register_form.send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON).click()


    def password_generator(self, length):

        length = int(length)
        # define data
        lower = string.ascii_lowercase
        upper = string.ascii_uppercase
        num = string.digits
        symbols = string.punctuation

        # combine data
        all = lower + upper + num + symbols

        # use random
        temp = random.sample(all, length)

        # create password
        password = "".join(temp)
        return password


