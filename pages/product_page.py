from .base_page import BasePage
from locators import ProductPageLocators


class ProductPage(BasePage):
    def is_review_button_presented_in_page(self):
        assert self.is_element_present(*ProductPageLocators.REVIEW_BUTTON), "There is no review button in the page"

    def add_to_card(self):
        card = self.browser.find_element(*ProductPageLocators.ADD_TO_CARD_BUTTON)
        card.click()

    def is_item_added_to_card(self):
        self.is_basket_equal_to_item_price()
        self.is_this_product_added_to_basket()

    def is_basket_equal_to_item_price(self):
        basket_price = self.browser.find_element(*ProductPageLocators.TOTAL_BASKET_PRICE).text
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        assert basket_price == product_price, "Price in basket is not equal to the product's price"

    def is_this_product_added_to_basket(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_name_message = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_MESSAGE).text
        assert product_name == product_name_message, "Name of the product in the page is not the same as in the notification message"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_success_message_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but it should disappeared"

