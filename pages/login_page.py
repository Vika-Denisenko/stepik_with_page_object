from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        current_url = self.browser.current_url
        assert "login" in current_url, f"{current_url} hasn`t str 'login'"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def register_new_user(self, email, password):
        user_name = self.browser.find_element(*LoginPageLocators.REGISTRATION_USERNAME)
        user_name.send_keys(email)
        password_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD)
        password_field.send_keys(password)
        password_confirm = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_CONFIRM)
        password_confirm.send_keys(password)
        button_login = self.browser.find_element(*LoginPageLocators.BUTTON_REGISTRATION)
        button_login.click()
