from data import BasePageData, LoginData
from pages.base_page import BasePage
from tests.conftest import driver
from xpath_data import LoginPagePaths, HomePagePaths, BasePagePaths, PersonalAccountPagePaths


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # def login(self, driver):
    #     driver.get(BasePageData.LOGIN_PAGE_URL)
    #
    #     self.fill_the_field(driver, LoginPagePaths.lp_email_input, LoginData.LOGIN_DATA["login"])
    #     self.fill_the_field(driver, LoginPagePaths.lp_password_input, LoginData.LOGIN_DATA["password"])
    #     self.click_on_the_element(driver, LoginPagePaths.login_button)
    #
    #     self.wait_element_to_be_visible(driver, HomePagePaths.collect_a_burger_header)

