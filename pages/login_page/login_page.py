from data import UrlLib
from locators import LoginPagePaths, HomePagePaths
from pages.base_page.base_page import BasePage
from pages.registration_page.registration_page import RegistrationPage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def login(self):

        register_page = RegistrationPage(self.driver)
        register_data = register_page.register()

        self.driver.get(UrlLib.LOGIN_PAGE_URL)

        self.fill_the_field(LoginPagePaths.lp_email_input, register_data["login"])
        self.fill_the_field(LoginPagePaths.lp_password_input, register_data["password"])
        self.click_on_the_element(LoginPagePaths.login_button)

        self.wait_element_to_be_visible(HomePagePaths.collect_a_burger_header)
