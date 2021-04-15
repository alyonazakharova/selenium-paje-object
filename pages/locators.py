from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM_EMAIL = (By.CSS_SELECTOR, "input[name='login-username']")
    LOGIN_FORM_PASSWORD = (By.CSS_SELECTOR, "input[name='login-password']")
    REGISTER_FORM_EMAIL = (By.CSS_SELECTOR, "input[name='registration-email']")
    REGISTER_FORM_PASSWORD = (By.CSS_SELECTOR, "input[name='registration-password1']")
    REGISTER_FORM_REPEAT_PASSWORD = (By.CSS_SELECTOR, "input[name='registration-password2']")


