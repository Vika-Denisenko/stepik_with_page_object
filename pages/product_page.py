from selenium.webdriver.support.expected_conditions import visibility_of
from selenium.webdriver.support.wait import WebDriverWait

from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.BUTTON)
        button.click()



    def get_alert_message_name(self):
        alert_message_name = self.browser.find_elements(*ProductPageLocators.MESSAGE_NAMES)[0].text
        assert self.get_name_product() in alert_message_name, 'Name is not in message'

    def get_alert_message_price(self):
        alert_message_price = self.browser.find_elements(*ProductPageLocators.MESSAGE_NAMES)[-1]
        WebDriverWait(self.browser, 5).until(visibility_of(alert_message_price))
        assert self.get_price_product() in alert_message_price.text, f'{self.get_price_product()} != {alert_message_price.text}'

    def get_name_product(self):
        name_product = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT).text
        return name_product

    def get_price_product(self):
        price_product = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT).text
        return price_product

    def should_be_button_add_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.BUTTON), 'Button is not present on the page'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.MESSAGE_NAMES), \
            "Success message is presented, but should not be"

    def success_message_is_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.MESSAGE_NAMES), \
            "Success message is not disappeared, but should not be"
