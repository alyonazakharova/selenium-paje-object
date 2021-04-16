import pytest

from pages.product_page import ProductPage
import time

# link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"


# def test_guest_should_see_add_to_cart_button(browser):
#     link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
#     page = ProductPage(browser, link)
#     page.open()
#     page.should_be_add_to_cart_button()


links = ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
         # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
         # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
         # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
         # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
         # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
         # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
         pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                      marks=pytest.mark.xfail),
         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
         # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"
         ]


@pytest.mark.parametrize('link', links)
def test_guest_can_add_product_to_cart(browser, link):
    # link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{offerN}"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()
    page.solve_quiz_and_get_code()
    page.should_be_correct_name()
    page.should_be_correct_price()
