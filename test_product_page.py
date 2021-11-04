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


@pytest.mark.parametrize('link', (*links[0:7], pytest.param(links[7], marks=pytest.mark.xfail), *links[8:10]))
def test_guest_can_add_product_to_basket(browser, link):
    current_link = link
    page = ProductPage(browser, current_link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_equal_product_name()
    page.should_be_equal_product_price()
