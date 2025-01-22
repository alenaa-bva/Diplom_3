from config import UrlLib
from data import LoginData
from pages.base_page.base_page import BasePage
from locators import ForgotPasswordPagePaths
from tests.conftest import driver


class ResetPasswordPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def move_on_the_reset_password_page(self, driver):
        driver.get(UrlLib.FORGOT_PASSWORD_PAGE_URL)

        self.fill_the_field(ForgotPasswordPagePaths.fp_email_input, LoginData.LOGIN_DATA["login"])
        self.click_on_the_element(ForgotPasswordPagePaths.fp_recover_button)

        return self.wait_element_to_be_visible(ForgotPasswordPagePaths.fp_password_input)

    def make_a_password_visible_by_eye_button(self, driver):
        driver.get(UrlLib.FORGOT_PASSWORD_PAGE_URL)

        self.fill_the_field(ForgotPasswordPagePaths.fp_email_input, LoginData.LOGIN_DATA["login"])
        self.click_on_the_element(ForgotPasswordPagePaths.fp_recover_button)
        self.fill_the_field(ForgotPasswordPagePaths.fp_password_input, LoginData.LOGIN_DATA["password"])
        self.click_on_the_element(ForgotPasswordPagePaths.fp_eye_button)

        return self.wait_element_to_be_visible(ForgotPasswordPagePaths.fp_password_field_shows_password)
