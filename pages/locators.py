from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    CART_LINK = (By.XPATH, "//span/a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class LoginPageLocators:
    LOGIN_FORM_EMAIL = (By.CSS_SELECTOR, "input[name='login-username']")
    LOGIN_FORM_PASSWORD = (By.CSS_SELECTOR, "input[name='login-password']")
    REGISTER_FORM_EMAIL = (By.CSS_SELECTOR, "input[name='registration-email']")
    REGISTER_FORM_PASSWORD = (By.CSS_SELECTOR, "input[name='registration-password1']")
    REGISTER_FORM_REPEAT_PASSWORD = (By.CSS_SELECTOR, "input[name='registration-password2']")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "button[name='registration_submit']")


class ProductPageLocators:
    ADD_TO_CART_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    PRODUCT_NAME = (By.TAG_NAME, "h1")
    ADDED_PRODUCT_NAME = (By.XPATH, "//div[@class='alertinner ']/strong")
    PRODUCT_PRICE = (By.XPATH, "//div[contains(@class, 'product_main')]/p[@class='price_color']")
    ADDED_PRODUCT_PRICE = (By.XPATH, "//div[@class='alertinner ']/p/strong")
    SUCCESS_MESSAGE = (By.XPATH, "//div[@class='alertinner ']")


class CartPageLocators:
    NUMBER_OF_PRODUCTS_MESSAGE = (By.CSS_SELECTOR, "#content_inner p")
    EMPTY_CART_MESSAGE = "empty"
