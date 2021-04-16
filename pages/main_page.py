from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage):
    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK)

    def go_to_login_page(self):
        login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        login_link.click()
