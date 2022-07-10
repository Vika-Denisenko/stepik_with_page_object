from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_basket_url(self):
        # реализуйте проверку на корректный url адрес
        current_url = self.browser.current_url
        assert "basket" in current_url, f"{current_url} hasn`t str 'basket'"

    def should_be_page_header(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*BasketPageLocators.PAGE_HEADER), "Page header is not presented"

    def should_be_basket_content(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*BasketPageLocators.INNER_CONTENT), "Content is not presented"

    def should_be_basket_page(self):
        self.should_be_basket_url()
        self.should_be_page_header()
        self.should_be_basket_content()

    def should_message_basket_is_empty(self):
        assert "Your basket is empty." in self.browser.find_element(
            *BasketPageLocators.INNER_CONTENT).text, "Message didnt " \
                                                     "present on page "

    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
            "Basket is not empty, but should be empty"

    def should_not_be_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_ITEMS), \
            "Basket is empty, but should not be empty"
