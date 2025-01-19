import pytest

from data import BasePageData
from pages.home_page import HomePage
from xpath_data import HomePagePaths


class ForgotPasswordPage:
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def move_to_recover_password_page_by_click_on_recover_button(self, driver):

        driver.get(BasePageData.BASE_PAGE_URL)

        # кликнуть на ингредиент
        self.click_on_the_element(ingredient)

        # возвращаем заголовок Детали ингридиента
        return self.wait_element_to_be_visible(driver, (By.XPATH, HomePagePaths.ingredient_details_modal_header)).text
