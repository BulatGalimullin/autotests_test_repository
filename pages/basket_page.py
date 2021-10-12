from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.CHECKOUT_LINK), \
            "Checkout link is in the page, but it should not"

    def should_be_empty_basket_message(self):
        empty_basket_message = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_MESSAGE).text

        browser_language = self.browser.execute_script(
            "return window.navigator.userLanguage || window.navigator.language")

        languages = {
            "ar": "سلة التسوق فارغة",
            "ca": "La seva cistella està buida",
            "cs": "Váš košík je prázdný",
            "da": "Din indkøbskurv er tom",
            "de": "Ihr Warenkorb ist leer",
            "en": "Your basket is empty",
            "el": "Το καλάθι σας είναι άδειο",
            "es": "Tu carrito esta vacío",
            "fi": "Korisi on tyhjä",
            "fr": "Votre panier est vide",
            "it": "Il tuo carrello è vuoto",
            "ko": "장바구니가 비었습니다",
            "nl": "Je winkelmand is leeg",
            "pl": "Twój koszyk jest pusty",
            "pt": "O carrinho está vazio",
            "pt-br": "Sua cesta está vazia",
            "ro": "Cosul tau este gol",
            "ru-RU": "Ваша корзина пуста",
            "sk": "Váš košík je prázdny",
            "uk": "Ваш кошик пустий",
            "zh-cn": "Your basket is empty",
        }

        if browser_language in languages.keys():
            card_is_empty_message_should_be = (languages[browser_language])

        assert card_is_empty_message_should_be in empty_basket_message, "Empty card text messages do not match"
