from .pages.product_page import ProductPage
import pytest


links = ['http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0',
         'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1',
         'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2',
         'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3',
         'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4',
         'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5',
         'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6',
         'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7',
         'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8',
         'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9']


# @pytest.mark.parametrize('link', (*links[0:7], pytest.param(links[7], marks=pytest.mark.xfail), *links[8:10]))
# def test_guest_can_add_product_to_basket(browser, link):
#     current_link = link
#     page = ProductPage(browser, current_link)
#     page.open()
#     page.add_to_basket()
#     page.solve_quiz_and_get_code()
#     page.should_be_equal_product_name()
#     page.should_be_equal_product_price()


@pytest.mark.negative
@pytest.mark.xfail(reason="Will be fixed later")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.negative
@pytest.mark.xfail(reason="Will be fixed later")
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_disappeared_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
