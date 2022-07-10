from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.LINK_TEXT, 'View basket')
    USER_ICON = (By.CLASS_NAME, "icon-user")


class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    LOGIN_USERNAME = (By.ID, "id_login-username")
    LOGIN_PASSWORD = (By.ID, "id_login-password")
    BUTTON_LOGIN = (By.NAME, "login_submit")
    REGISTRATION_USERNAME = (By.ID, "id_registration-email")
    REGISTRATION_PASSWORD = (By.ID, "id_registration-password1")
    REGISTRATION_PASSWORD_CONFIRM = (By.ID, "id_registration-password2")
    BUTTON_REGISTRATION = (By.NAME, "registration_submit")


class ProductPageLocators:
    BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    NAME_PRODUCT = (By.TAG_NAME, "h1")
    PRICE_PRODUCT = (By.CSS_SELECTOR, ".product_main .price_color")
    MESSAGE_NAMES = (By.CSS_SELECTOR, ".alertinner strong")


class BasketPageLocators:
    PAGE_HEADER = (By.CLASS_NAME, "page-header")
    INNER_CONTENT = (By.ID, "content_inner")
    TABLE_PRICE = (By.CLASS_NAME, "table-condensed")
    MESSAGE = (By.ID, "messages")
    BASKET_ITEMS = (By.CLASS_NAME, "basket-items")
