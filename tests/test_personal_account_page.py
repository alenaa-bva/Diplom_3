from pages.personal_account_page import PersonalAccountPage

from pages.home_page import HomePage
from tests.conftest import driver


class TestPersonalAccountPage:

    def test_move_to_the_personal_account_by_authorized_user(self, driver):
        personal_page_obj = PersonalAccountPage(driver)
        personal_page_profile_tab_text = personal_page_obj.move_to_the_personal_account_by_authorized_user(driver)

        assert personal_page_profile_tab_text == 'Профиль', f"Переход в ЛК не совершен, вкладка - {personal_page_profile_tab_text} не найдена"

    def test_move_to_the_personal_account_by_unauthorized_user(self, driver):
        personal_page_obj = PersonalAccountPage(driver)
        login_page_header_text = personal_page_obj.move_to_the_personal_account_by_unauthorized_user(driver)

        assert login_page_header_text == 'Вход', f"Переход на страницу логина не совершен, заголовок - {login_page_header_text} не найден"

    def test_user_order_is_displayed_in_the_history_tab_when_the_order_placed(self, driver):
        home_page_obj = HomePage(driver)
        personal_page_obj = PersonalAccountPage(driver)
        order_number = personal_page_obj.user_order_is_displayed_in_the_history_tab_when_the_order_placed(driver,
                                                                                                          home_page_obj)

        assert order_number["home_page_order_number"] == order_number["history_tab_order_number"], \
            (f"В истории заказов ожидается последний заказ с номером - {order_number['home_page_order_number']}. "
             f"Фактический номер - {order_number['history_tab_order_number']}")

    def test_logout(self, driver):
        personal_page_obj = PersonalAccountPage(driver)
        login_page_header_text = personal_page_obj.logout(driver)

        assert login_page_header_text == 'Вход'
