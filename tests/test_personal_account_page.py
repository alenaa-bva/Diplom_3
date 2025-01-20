from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data import LoginData
from pages.personal_account_page import PersonalAccountPage
from xpath_data import HomePagePaths, LoginPagePaths, PersonalAccountPagePaths

# # вспомогательные функции
# def wait_element_to_be_clickable(driver, locator, timeout=5):
#     return WebDriverWait(driver, timeout).until(expected_conditions.element_to_be_clickable(locator))
#
# def wait_element_to_be_visible(driver, locator, timeout=5):
#     return WebDriverWait(driver, timeout).until(expected_conditions.visibility_of_element_located(locator))


#тесты
# class TestPAPage:
#     pass

    # def test_open_personal_account(
    #         self,
    #         driver
    # ):
    #     driver.get("https://stellarburgers.nomoreparties.site")
    #
    #     # переход на форму логина через кнопку войти в аккаунт
    #     wait_element_to_be_clickable(driver, HomePagePaths.go_to_account_button).click()
    #
    #     # логин
    #     driver.find_element(*LoginPagePaths.lp_email_input).send_keys(LoginData.LOGIN)
    #     driver.find_element(*LoginPagePaths.lp_password_input).send_keys(LoginData.PASSWORD)
    #     driver.find_element(*LoginPagePaths.login_button).click()
    #
    #     order_button = wait_element_to_be_visible(driver, HomePagePaths.place_an_order_button).text
    #
    #     assert order_button == 'Оформить заказ', "Авторизация не прошла"
    #
    #     # переход в личный кабинет
    #     driver.find_element(*HomePagePaths.personal_account_button).click()
    #
    #     email_input = wait_element_to_be_visible(driver, PersonalAccountPagePaths.pa_email_input).get_attribute("value")
    #
    #     assert '/account/profile' in driver.current_url and email_input is not None
    #
    #
    # def test_logout(
    #         self,
    #         driver
    # ):
    #     driver.get("https://stellarburgers.nomoreparties.site")
    #
    #
    #     # переход на форму логина через кнопку войти в аккаунт
    #     wait_element_to_be_clickable(driver, HomePagePaths.go_to_account_button).click()
    #
    #     # логин
    #     driver.find_element(*LoginPagePaths.lp_email_input).send_keys(LoginData.LOGIN)
    #     driver.find_element(*LoginPagePaths.lp_password_input).send_keys(LoginData.PASSWORD)
    #     driver.find_element(*LoginPagePaths.login_button).click()
    #
    #     order_button = wait_element_to_be_visible(driver, HomePagePaths.place_an_order_button).text
    #
    #     assert order_button == 'Оформить заказ', "Авторизация не прошла"
    #
    #     # переход в личный кабинет
    #     driver.find_element(*HomePagePaths.personal_account_button).click()
    #
    #     wait_element_to_be_visible(driver, PersonalAccountPagePaths.pa_email_input)
    #
    #     assert '/account/profile' in driver.current_url
    #
    #     # выход из аккаунта
    #     driver.find_element(*PersonalAccountPagePaths.logout_button).click()
    #
    #     wait_element_to_be_visible(driver, LoginPagePaths.login_header)
    #
    #     assert '/login' in driver.current_url


from pages.home_page import HomePage
from pages.login_page import LoginPage
from tests.conftest import driver


class TestPersonalAccountPage:

    # переход по клику на конструктор

    def test_move_to_the_personal_account_by_authorized_user(self, driver):

        login_page_obj = LoginPage(driver)
        personal_page_obj = PersonalAccountPage(driver)
        personal_page_profile_tab_text = personal_page_obj.move_to_the_personal_account_by_authorized_user(driver, login_page_obj)

        assert personal_page_profile_tab_text == 'Профиль', f"Переход в ЛК не совершен, вкладка - {personal_page_profile_tab_text} не найдена"

    def test_move_to_the_personal_account_by_unauthorized_user(self, driver):

        personal_page_obj = PersonalAccountPage(driver)
        login_page_header_text = personal_page_obj.move_to_the_personal_account_by_unauthorized_user(driver)

        assert login_page_header_text == 'Вход', f"Переход на страницу логина не совершен, заголовок - {login_page_header_text} не найден"

    def test_user_order_is_displayed_in_the_history_tab_when_the_order_placed(self, driver):

        home_page_obj = HomePage(driver)
        personal_page_obj = PersonalAccountPage(driver)
        order_number = personal_page_obj.user_order_is_displayed_in_the_history_tab_when_the_order_placed(driver, home_page_obj)

        assert order_number["home_page_order_number"] == order_number["history_tab_order_number"], \
            (f"В истории заказов ожидается последний заказ с номером - {order_number['home_page_order_number']}. "
             f"Фактический номер - {order_number['history_tab_order_number']}")

    def test_logout(self, driver):

        personal_page_obj = PersonalAccountPage(driver)
        login_page_header_text = personal_page_obj.logout(driver)

        assert login_page_header_text == 'Вход'


        # def test_login_from_go_to_account_button(
        #         self,
        #         driver
        # ):
        #     driver.get("https://stellarburgers.nomoreparties.site")
        #
        #     # переход на форму логина через кнопку войти в аккаунт
        #     wait_element_to_be_clickable(driver, HomePagePaths.go_to_account_button).click()
        #
        #     # логин
        #     driver.find_element(*LoginPagePaths.lp_email_input).send_keys(LoginData.LOGIN)
        #     driver.find_element(*LoginPagePaths.lp_password_input).send_keys(LoginData.PASSWORD)
        #     driver.find_element(*LoginPagePaths.login_button).click()
        #
        #     order_button = wait_element_to_be_visible(driver, HomePagePaths.place_an_order_button).text
        #
        #     assert order_button == 'Оформить заказ', "Авторизация не прошла"
        #
        #
        # def test_login_from_personal_account_button(
        #         self,
        #         driver
        # ):
        #     driver.get("https://stellarburgers.nomoreparties.site")
        #
        #     wait_element_to_be_clickable(driver, HomePagePaths.go_to_account_button)
        #
        #     # переход на форму логина через кнопку личный кабинет
        #     driver.find_element(*HomePagePaths.personal_account_button).click()
        #
        #     # логин
        #     driver.find_element(*LoginPagePaths.lp_email_input).send_keys(LoginData.LOGIN)
        #     driver.find_element(*LoginPagePaths.lp_password_input).send_keys(LoginData.PASSWORD)
        #     driver.find_element(*LoginPagePaths.login_button).click()
        #
        #     order_button = wait_element_to_be_visible(driver, HomePagePaths.place_an_order_button).text
        #
        #     assert order_button == 'Оформить заказ', "Авторизация не прошла"
        #
        #
        #
        # def test_login_from_registration_form(
        #         self,
        #         driver
        # ):
        #     driver.get("https://stellarburgers.nomoreparties.site/register")
        #
        #     # Переход на форму логина из формы регистрации
        #     wait_element_to_be_clickable(driver, RegistrationPagePaths.rp_login_link).click()
        #
        #     # логин
        #     driver.find_element(*LoginPagePaths.lp_email_input).send_keys(LoginData.LOGIN)
        #     driver.find_element(*LoginPagePaths.lp_password_input).send_keys(LoginData.PASSWORD)
        #     driver.find_element(*LoginPagePaths.login_button).click()
        #
        #     order_button = wait_element_to_be_visible(driver, HomePagePaths.place_an_order_button).text
        #
        #     assert order_button == 'Оформить заказ', "Авторизация не прошла"
        #
        #
        # def test_login_from_password_recovering_form(
        #         self,
        #         driver
        # ):
        #     driver.get("https://stellarburgers.nomoreparties.site/forgot-password")
        #
        #     # Переход на форму логина из формы восстановления пароля
        #     wait_element_to_be_clickable(driver, ForgotPasswordPagePaths.fp_login_link).click()
        #
        #     # логин
        #     driver.find_element(*LoginPagePaths.lp_email_input).send_keys(LoginData.LOGIN)
        #     driver.find_element(*LoginPagePaths.lp_password_input).send_keys(LoginData.PASSWORD)
        #     driver.find_element(*LoginPagePaths.login_button).click()
        #
        #     order_button = wait_element_to_be_visible(driver, HomePagePaths.place_an_order_button).text
        #
        #     assert order_button == 'Оформить заказ', "Авторизация не прошла"
        #
        #
        # def test_move_to_password_recovering_form_by_password_recovering_button(self):
        pass









