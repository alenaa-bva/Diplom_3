import pytest

from data import BasePageData
from pages.home_page import HomePage
from pages.login_page import LoginPage
from xpath_data import HomePagePaths, LoginPagePaths


class TestHomePage:

    #переход по клику на конструктор
    @pytest.mark.parametrize("page", [
        #BasePageData.LOGIN_PAGE_URL
        #BasePageData.FEED_PAGE_URL,
         BasePageData.REGISTER_PAGE_URL,
        # BasePageData.RESET_PASSWORD_PAGE_URL,
        # BasePageData.FORGOT_PASSWORD_PAGE_URL
    ])
    def test_move_from_other_page_to_constructor_by_logo(
            self,
            driver,
            page
    ):
        home_page_obj = HomePage(driver)
        collect_a_burger_header_text = home_page_obj.move_from_other_page_to_constructor_by_logo(driver, page)

        assert collect_a_burger_header_text == 'Соберите бургер'

    #
    #
    # def test_move_to_bread_section(
    #         self,
    #         driver
    # ):
    #
    #     driver.get("https://stellarburgers.nomoreparties.site")
    #
    #     wait_element_to_be_visible(driver, HomePagePaths.first_bread_ingredient)
    #
    #     header = driver.find_element(*HomePagePaths.breads_section_header).text
    #
    #     assert header == 'Булки'
    #
    #
    # def test_move_to_sauce_section(
    #         self,
    #         driver
    # ):
    #
    #     driver.get("https://stellarburgers.nomoreparties.site")
    #
    #     wait_element_to_be_visible(driver, HomePagePaths.ingredients_section)
    #
    #     driver.find_element(*HomePagePaths.sauce_tab).click()
    #
    #     wait_element_to_be_visible(driver, HomePagePaths.first_sauce_ingredient)
    #
    #     header = driver.find_element(*HomePagePaths.sauces_section_header).text
    #
    #     assert header == 'Соусы'
    #
    #
    # def test_move_to_fillings_section(
    #         self,
    #         driver
    # ):
    #
    #     driver.get("https://stellarburgers.nomoreparties.site")
    #
    #     wait_element_to_be_visible(driver, HomePagePaths.ingredients_section)
    #
    #     driver.find_element(*HomePagePaths.fillings_tab).click()
    #
    #     wait_element_to_be_visible(driver, HomePagePaths.first_filling_ingredient)
    #
    #     header = driver.find_element(*HomePagePaths.fillings_section_header).text
    #
    #     assert header == 'Начинки'



    @pytest.mark.parametrize("ingredient", [
        #HomePagePaths.first_bread_ingredient,
        # HomePagePaths.first_sauce_ingredient,
        HomePagePaths.first_filling_ingredient
    ])
    def test_open_ingredient_details_by_click_on_the_ingredient(
            self,
            driver,
            ingredient
    ):
        home_page_obj = HomePage(driver)
        ingredient_details_modal_header_text = home_page_obj.open_ingredient_details_by_click_on_the_ingredient(driver, ingredient)

        assert ingredient_details_modal_header_text == 'Детали ингредиента', (
        f"Ошибка: Ожидался текст заголовка 'Детали ингредиента', но получен '{ingredient_details_modal_header_text}'")

    @pytest.mark.parametrize("ingredient", [
        # HomePagePaths.first_bread_ingredient,
        # HomePagePaths.first_sauce_ingredient,
        HomePagePaths.first_filling_ingredient
    ])
    def test_close_ingredient_details_by_click_on_the_cross(
            self,
            driver,
            ingredient
    ):
        home_page_obj = HomePage(driver)
        is_modal_closed = home_page_obj.close_ingredient_details_by_click_on_the_cross(driver,ingredient)

        assert is_modal_closed, "Модальное окно не закрылось после клика на крестик"

    @pytest.mark.parametrize("ingredient", [
        # HomePagePaths.first_bread_ingredient,
        # HomePagePaths.first_sauce_ingredient,
        HomePagePaths.first_filling_ingredient
    ])
    def test_add_ingredients_by_type_to_the_basket(
            self,
            driver,
            ingredient
    ):
        home_page_obj = HomePage(driver)
        is_sum_more_than_zero = home_page_obj.add_ingredients_to_the_order_by_move_to_the_basket(driver, ingredient)

        assert is_sum_more_than_zero, "Сумма в корзине не стала больше нуля после добавления ингредиента"


    def test_place_an_order_by_authorized_user(self, driver):

        home_page_obj = HomePage(driver)
        order_number = home_page_obj.place_an_order_by_authorized_user(driver)

        assert order_number is not None, "Заказ не оформлен, номер заказа не найден"

    def test_place_an_order_by_unauthorized_user(self):
        pass




