import time

import pytest

from pages.cart_page import CartPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage


@pytest.mark.user
class TestUserAddToCartFromProductPage:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        page = LoginPage(browser, "http://selenium1py.pythonanywhere.com/ru/accounts/login/")
        page.open()
        email = str(time.time()) + "@fakemail.org"
        password = "pwdqweqwe"
        page.register_new_user(email, password)
        time.sleep(2)
        page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_cart(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        page = ProductPage(browser, link)
        page.open()
        page.add_to_cart()
        page.solve_quiz_and_get_code()
        page.should_be_correct_name()
        page.should_be_correct_price()

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()


def test_guest_should_see_add_to_cart_button(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_to_cart_button()


links = ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
         # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
         # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
         # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
         # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
         # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
         # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
         pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                      marks=pytest.mark.xfail),
         # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
         # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"
         ]


@pytest.mark.need_review
@pytest.mark.parametrize('link', links)
def test_guest_can_add_product_to_cart(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()
    page.solve_quiz_and_get_code()
    page.should_be_correct_name()
    page.should_be_correct_price()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_cart(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_cart(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()
    page.should_message_disappear()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_cart_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_cart_page()
    cart_page = CartPage(browser, browser.current_url)
    cart_page.should_be_empty()
