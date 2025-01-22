from data import UrlLib
from helpers import generate_register_data
from locators import RegistrationPagePaths
from pages.base_page.base_page import BasePage


class RegistrationPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def register(self) -> dict:

        register_data = generate_register_data()

        self.driver.get(UrlLib.REGISTER_PAGE_URL)

        self.fill_the_field(RegistrationPagePaths.rp_name_input, register_data["name"])
        self.fill_the_field(RegistrationPagePaths.rp_email_input, register_data["login"])
        self.fill_the_field(RegistrationPagePaths.rp_password_input, register_data["password"])
        self.click_on_the_element(RegistrationPagePaths.sign_up_button)

        return register_data