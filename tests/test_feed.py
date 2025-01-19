import pytest

from data import BasePageData
from pages.feed_page import FeedPage
from pages.home_page import HomePage


class TestHomePage:

    #переход по клику на кнопку лента заказов
    @pytest.mark.parametrize("page", [
        # BasePageData.LOGIN_PAGE_URL
        # BasePageData.FEED_PAGE_URL,
         BasePageData.REGISTER_PAGE_URL,
        # BasePageData.RESET_PASSWORD_PAGE_URL,
        # BasePageData.FORGOT_PASSWORD_PAGE_URL
    ])
    def test_move_from_other_page_to_constructor_by_logo(
            self,
            driver,
            page
    ):
        feed_page_obj = FeedPage(driver)
        feed_header_text = feed_page_obj.move_to_order_feed_page(driver, page)

        assert feed_header_text == 'Лента заказов'

    def test_move_to_order_feed_page(self):
        pass

    def test_open_order_details_by_click_on_the_order(self):
        pass

    def test_get_orders_on_the_feed_from_history(self):
        pass

    def test_get_increased_counters_when_place_the_order(self):
        pass

