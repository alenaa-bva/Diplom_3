from config import UrlLib
from pages.base_page.base_page import BasePage
from locators import BasePagePaths, FeedPagePaths, HomePagePaths, PersonalAccountPagePaths


class FeedPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def move_to_order_feed_page(self, page):
        self.driver.get(page)

        # нажимаем на лого
        self.click_on_the_element(BasePagePaths.feed_button)

        # возвращаем текст хедера страницы
        return self.wait_element_to_be_visible(FeedPagePaths.feed_header).text

    # если кликнуть на заказ, откроется всплывающее окно с деталями
    def open_order_details_by_click_on_the_order_box(self):
        self.driver.get(UrlLib.FEED_PAGE_URL)

        # нажимаем на плашку заказа
        self.click_on_the_element(FeedPagePaths.order_box)

        elements_on_the_order_modal = {
            "order_ingredients": self.wait_element_to_be_visible(FeedPagePaths.order_ingredients),
            "order_price": self.wait_element_to_be_visible(FeedPagePaths.order_ingredients)
        }

        # возвращаем elements_on_the_order_modal
        return elements_on_the_order_modal

    # заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»,

    def get_order_on_the_feed_from_history(self, home_page_obj):
        # создаем заказ и копируем номер заказа из истории заказов в личном кабинете

        home_page_obj.place_an_order_by_authorized_user()
        self.click_on_the_element(HomePagePaths.close_order_button)
        self.click_on_the_element(BasePagePaths.personal_button)
        self.click_on_the_element(PersonalAccountPagePaths.history_tab)
        self.scroll_to_element(PersonalAccountPagePaths.last_order_number)

        # забираем номер заказа из истории заказов
        history_tab_order_number_text = self.wait_element_to_be_visible(PersonalAccountPagePaths.last_order_number).text

        # перемещаемся на ленту заказов
        self.move_to_order_feed_page(UrlLib.BASE_PAGE_URL)

        # забираем номер заказа из плашки заказа
        order_number_on_the_feed = f".//ul/li/a/div[1]/p[1][text()='{history_tab_order_number_text}']"  # номера заказов в ленте
        self.scroll_to_element( order_number_on_the_feed)
        order_number_on_the_feed_text = self.wait_element_to_be_visible(order_number_on_the_feed).text

        result = {
            'history_tab_order_number_text': history_tab_order_number_text,
            'order_number_on_the_feed_text': order_number_on_the_feed_text
        }

        # возвращаем результат
        return result

    def show_new_order_in_work_section(self, home_page_obj):
        # создаем заказ и копируем номер заказа
        constructor_page_order_number_text = home_page_obj.place_an_order_by_authorized_user()
        self.click_on_the_element(HomePagePaths.close_order_button)

        # перемещаемся на ленту заказов
        self.driver.get(UrlLib.FEED_PAGE_URL)

        # забираем номер заказа из плашки заказа
        self.scroll_to_element(FeedPagePaths.in_work_order_number)

        # ждем, пока пропадет лишний текст
        self.wait_element_not_visible(self.driver, FeedPagePaths.in_work_description)
        order_number_in_work_text = self.wait_element_to_be_visible(FeedPagePaths.in_work_order_number).text

        result = {
            'constructor_page_order_number_text': f'0{constructor_page_order_number_text}',
            'order_number_in_work_text': order_number_in_work_text
        }

        # возвращаем результат
        return result

    def get_increased_counter_today_when_place_the_order(self, home_page_obj):
        self.driver.get(UrlLib.FEED_PAGE_URL)
        self.scroll_to_element(FeedPagePaths.orders_completed_today)
        today_orders_before = self.wait_element_to_be_visible(FeedPagePaths.orders_completed_today).text

        home_page_obj.place_an_order_by_authorized_user()
        self.driver.get(UrlLib.FEED_PAGE_URL)
        today_orders_after = self.wait_element_to_be_visible(FeedPagePaths.orders_completed_today).text

        result = {
            'today_orders_before': today_orders_before,
            'today_orders_after': today_orders_after
        }

        return result

    def get_increased_counter_all_time_when_place_the_order(self, home_page_obj):
        self.driver.get(UrlLib.FEED_PAGE_URL)
        self.scroll_to_element(FeedPagePaths.orders_completed_all_the_time)
        all_time_orders_before = self.wait_element_to_be_visible(FeedPagePaths.orders_completed_all_the_time).text

        home_page_obj.place_an_order_by_authorized_user()
        self.driver.get(UrlLib.FEED_PAGE_URL)
        all_time_orders_after = self.wait_element_to_be_visible(FeedPagePaths.orders_completed_all_the_time).text

        result = {
            'all_time_orders_before': all_time_orders_before,
            'all_time_orders_after': all_time_orders_after
        }

        return result
