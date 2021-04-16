from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Expected 'login' in URL"

    def should_be_login_form(self):
        email_input_exists = self.is_element_present(*LoginPageLocators.LOGIN_FORM_EMAIL)
        password_input_exists = self.is_element_present(*LoginPageLocators.LOGIN_FORM_PASSWORD)
        assert email_input_exists and password_input_exists, "Email or/and password input doesn't exists in login form"

    def should_be_register_form(self):
        email_input_exists = self.is_element_present(*LoginPageLocators.REGISTER_FORM_EMAIL)
        password1_input_exists = self.is_element_present(*LoginPageLocators.REGISTER_FORM_PASSWORD)
        password2_input_exists = self.is_element_present(*LoginPageLocators.REGISTER_FORM_REPEAT_PASSWORD)
        assert email_input_exists and password1_input_exists and password2_input_exists, "Email or/and password input doesn't exists in login form"

    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_EMAIL)
        email_field.send_keys(email)
        pwd1_field = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_PASSWORD)
        pwd1_field.send_keys(password)
        pwd2_field = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_REPEAT_PASSWORD)
        pwd2_field.send_keys(password)
        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        register_button.click()
