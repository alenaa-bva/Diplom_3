from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from data import BasePageData, HomePageData
from pages.base_page import BasePage
from xpath_data import LoginPagePaths, HomePagePaths, BasePagePaths


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def move_from_other_page_to_constructor_by_logo(self, driver, page):

        driver.get(page)

        # нажимаем на лого
        self.click_on_the_element(BasePagePaths.stellar_burgers_logo)

        # возвращаем текст хедера страницы
        return self.wait_element_to_be_visible(driver, (By.XPATH, HomePagePaths.collect_a_burger_header)).text


    def open_ingredient_details_by_click_on_the_ingredient(self, driver, ingredient):

        driver.get(BasePageData.BASE_PAGE_URL)

        # кликнуть на ингредиент
        self.click_on_the_element(ingredient)

        # возвращаем заголовок Детали ингридиента
        return self.wait_element_to_be_visible(driver, (By.XPATH, HomePagePaths.ingredient_details_modal_header)).text


    def close_ingredient_details_by_click_on_the_cross(self, driver, ingredient):

        driver.get(BasePageData.BASE_PAGE_URL)

        # кликнуть на ингредиент
        self.click_on_the_element(ingredient)

        # кликнуть на крестик
        self.click_on_the_element(HomePagePaths.close_details_button)

        # ждем закрытия модалки и возвращаем результат True или False
        return self.wait_element_not_visible(driver, (By.XPATH, HomePagePaths.ingredient_details_modal_header))


    def add_ingredients_to_the_order_by_move_to_the_basket(self, driver, ingredient):

        driver.get(BasePageData.BASE_PAGE_URL)

        # перетащить ингредиент
        self.drag_and_drop_element((By.XPATH, ingredient), (By.XPATH, HomePagePaths.burger_basket_section), driver)

        # ждем пока итоговая сумма не станет > 0
        return WebDriverWait(driver, timeout = 5).until(lambda driver: int(driver.find_element(By.XPATH, HomePagePaths.total_counter).text) > 0)








