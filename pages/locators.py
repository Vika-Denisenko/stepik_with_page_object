from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class LoginPageLocators:
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTER_FORM = (By.ID, 'register_form')


class ProductPageLocators:
    BUTTON = (By.CLASS_NAME, 'btn-add-to-basket')
    NAME_PRODUCT = (By.TAG_NAME, 'h1')
    PRICE_PRODUCT = (By.CSS_SELECTOR, '.product_main .price_color')
    MESSAGE_NAMES = (By.CSS_SELECTOR, '.alertinner strong')
