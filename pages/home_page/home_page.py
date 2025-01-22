from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from data import BasePageData
from pages.base_page.base_page import BasePage
from tests.conftest import driver
from locators import HomePagePaths, BasePagePaths


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def move_from_other_page_to_constructor_by_logo(self, page):
        self.driver.get(page)

        # нажимаем на лого
        self.click_on_the_element(BasePagePaths.stellar_burgers_logo)

        # возвращаем текст хедера страницы
        return self.wait_element_to_be_visible(HomePagePaths.collect_a_burger_header).text

    def open_ingredient_details_by_click_on_the_ingredient(self, driver, ingredient):
        driver.get(BasePageData.BASE_PAGE_URL)

        # кликнуть на ингредиент
        self.click_on_the_element(ingredient)

        # возвращаем заголовок Детали ингридиента
        return self.wait_element_to_be_visible(HomePagePaths.ingredient_details_modal_header).text

    def close_ingredient_details_by_click_on_the_cross(self, driver, ingredient):
        driver.get(BasePageData.BASE_PAGE_URL)

        # кликнуть на ингредиент
        self.click_on_the_element(ingredient)

        # кликнуть на крестик
        self.click_on_the_element(HomePagePaths.close_details_button)

        # ждем закрытия модалки и возвращаем результат True или False
        return self.wait_element_not_visible(HomePagePaths.ingredient_details_modal_header)

    def add_ingredients_to_the_order_by_move_to_the_basket(self, driver, ingredient):
        driver.get(BasePageData.BASE_PAGE_URL)

        # перетащить ингредиент
        self.drag_and_drop_element(ingredient, HomePagePaths.burger_basket_section)

        # ждем пока итоговая сумма не станет > 0
        return WebDriverWait(driver, timeout=5).until(
            lambda driver: int(driver.find_element(By.XPATH, HomePagePaths.total_counter).text) > 0)

    def place_an_order_by_authorized_user(self, driver):
        # логинимся
        self.login(driver)

        ingredients = [
            HomePagePaths.first_bread_ingredient,
            HomePagePaths.first_filling_ingredient,
            HomePagePaths.first_sauce_ingredient
        ]

        # добавляем ингредиенты ка заказу
        for ingredient in ingredients:
            self.drag_and_drop_element(ingredient, HomePagePaths.burger_basket_section)

        # размещаем заказ
        self.click_on_the_element(HomePagePaths.place_an_order_button)
        # ждем, пока на модалке пропадет номер 9999
        self.wait_element_not_visible(HomePagePaths.order_number_9999)

        # возвращаем номер заказа
        return self.wait_element_to_be_visible(HomePagePaths.order_number).text
