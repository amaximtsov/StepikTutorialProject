from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini > span > a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")
    EMPTY_BASKET_TEXT = (By.CSS_SELECTOR, "#content_inner > p")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL = (By.CSS_SELECTOR, "input[name='registration-email']")
    REGISTER_PASSWORD = (By.CSS_SELECTOR, "input[name='registration-password1']")
    REGISTER_PASSWORD1 = (By.CSS_SELECTOR, "input[name='registration-password2']")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "button[name='registration_submit']")


class ProductPageLocators:
    ADD_TO_BASKET_BTN = (By.CSS_SELECTOR, '.btn-add-to-basket')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main h1')
    PRODUCT_NAME_IN_ALERT = (By.CSS_SELECTOR, '.alert-success:first-child strong')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main .price_color')
    PRODUCT_PRICE_IN_ALERT = (By.CSS_SELECTOR, '.alertinner p strong')
    PRODUCT_SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.alert-success:first-child')
