import pytest

from config import UrlLib
from pages.feed_page.feed_page import FeedPage
from pages.home_page.home_page import HomePage


class TestFeedPage:

    # переход по клику на кнопку лента заказов
    @pytest.mark.parametrize("page", [
        UrlLib.LOGIN_PAGE_URL,
        UrlLib.FEED_PAGE_URL,
        UrlLib.REGISTER_PAGE_URL,
        UrlLib.FORGOT_PASSWORD_PAGE_URL
    ])
    def test_move_to_order_feed_page(
            self,
            driver,
            page
    ):
        feed_page_obj = FeedPage(driver)
        feed_header_text = feed_page_obj.move_to_order_feed_page(page)

        assert feed_header_text == 'Лента заказов'

    def test_open_order_details_by_click_on_the_order_box(self, driver):
        feed_page_obj = FeedPage(driver)
        order_elements = feed_page_obj.open_order_details_by_click_on_the_order_box()

        assert (order_elements["order_ingredients"] and order_elements[
            "order_price"]), "Ингридиенты и сумма заказа не найдены"

    def test_get_order_on_the_feed_from_history(self, driver):
        feed_page_obj = FeedPage(driver)
        home_page_obj = HomePage(driver)
        results = feed_page_obj.get_order_on_the_feed_from_history(home_page_obj)

        assert results['history_tab_order_number_text'] == results[
            'order_number_on_the_feed_text'], "Номер заказа не найден в ленте заказов"

    def test_get_increased_counter_today_when_place_the_order(self, driver):
        feed_page_obj = FeedPage(driver)
        home_page_obj = HomePage(driver)
        results = feed_page_obj.get_increased_counter_today_when_place_the_order(home_page_obj)

        assert int(results['today_orders_after']) > int(results['today_orders_before'])

    def test_get_increased_counter_all_time_when_place_the_order(self, driver):
        feed_page_obj = FeedPage(driver)
        home_page_obj = HomePage(driver)
        results = feed_page_obj.get_increased_counter_all_time_when_place_the_order(home_page_obj)

        assert int(results['all_time_orders_after']) > int(results['all_time_orders_before'])

    def test_show_new_order_in_work_section(self, driver):
        feed_page_obj = FeedPage(driver)
        home_page_obj = HomePage(driver)
        results = feed_page_obj.show_new_order_in_work_section(home_page_obj)

        assert results['constructor_page_order_number_text'] == results[
            'order_number_in_work_text'], "Номер заказа не найден в разделе 'В работе'"
