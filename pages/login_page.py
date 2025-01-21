from data import BasePageData
from helpers import generate_register_data
from pages.base_page import BasePage
from locators import RegistrationPagePaths, HomePagePaths, LoginPagePaths


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def login(self):

        register_data = self.register()

        self.driver.get(BasePageData.LOGIN_PAGE_URL)

        self.fill_the_field(self.driver, LoginPagePaths.lp_email_input, register_data["login"])
        self.fill_the_field(self.driver, LoginPagePaths.lp_password_input, register_data["password"])
        self.click_on_the_element(self.driver, LoginPagePaths.login_button)

        self.wait_element_to_be_visible(HomePagePaths.collect_a_burger_header)


    def register(self) -> dict:
        register_data = generate_register_data()

        self.driver.get(BasePageData.REGISTER_PAGE_URL)

        self.fill_the_field(self.driver, RegistrationPagePaths.rp_name_input, register_data["name"])
        self.fill_the_field(self.driver, RegistrationPagePaths.rp_email_input, register_data["login"])
        self.fill_the_field(self.driver, RegistrationPagePaths.rp_password_input, register_data["password"])
        self.click_on_the_element(self.driver, RegistrationPagePaths.sign_up_button)

        return register_data