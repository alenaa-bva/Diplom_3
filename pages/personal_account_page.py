from data import BasePageData
from pages.base_page import BasePage
from tests.conftest import driver
from xpath_data import LoginPagePaths, HomePagePaths, BasePagePaths, PersonalAccountPagePaths


class PersonalAccountPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def move_to_the_personal_account_by_authorized_user(self, driver) -> bool:
        self.login(driver)
        self.click_on_the_element(driver, BasePagePaths.personal_button)

        return self.wait_element_to_be_visible(driver, PersonalAccountPagePaths.profile_tab).text

    def move_to_the_personal_account_by_unauthorized_user(self, driver) -> str:
        driver.get(BasePageData.BASE_PAGE_URL)
        self.click_on_the_element(driver, BasePagePaths.personal_button)

        return self.wait_element_to_be_visible(driver, LoginPagePaths.login_header).text

    def user_order_is_displayed_in_the_history_tab_when_the_order_placed(self, driver, home_page_obj) -> dict:
        home_page_order_number = home_page_obj.place_an_order_by_authorized_user(driver)
        self.click_on_the_element(driver, HomePagePaths.close_order_button)
        self.click_on_the_element(driver, BasePagePaths.personal_button)
        self.click_on_the_element(driver, PersonalAccountPagePaths.history_tab)
        self.scroll_to_element(driver, PersonalAccountPagePaths.last_order_number)

        history_tab_order_number = self.wait_element_to_be_visible(driver,
                                                                   PersonalAccountPagePaths.last_order_number).text

        order_number = {
            "home_page_order_number": f"#0{home_page_order_number}",
            "history_tab_order_number": history_tab_order_number
        }

        return order_number

    def logout(self, driver):
        self.login(driver)
        self.click_on_the_element(driver, BasePagePaths.personal_button)
        self.click_on_the_element(driver, PersonalAccountPagePaths.logout_button)

        return self.wait_element_to_be_visible(driver, LoginPagePaths.login_header).text
