from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from xpath_data import BasePagePaths, FeedPagePaths


class FeedPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def move_to_order_feed_page(self, driver, page):

        driver.get(page)  # здесь передаем страницы через параметризацию

        # нажимаем на лого
        self.click_on_the_element(BasePagePaths.feed_button)

        # возвращаем текст хедера страницы
        return self.wait_element_to_be_visible(driver, (By.XPATH, FeedPagePaths.feed_header)).text
