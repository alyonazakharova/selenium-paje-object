from pages.base_page import BasePage
from .locators import CartPageLocators


class CartPage(BasePage):
    def should_be_empty(self):
        message = self.browser.find_element(*CartPageLocators.NUMBER_OF_PRODUCTS_MESSAGE).text
        assert CartPageLocators.EMPTY_CART_MESSAGE in message
