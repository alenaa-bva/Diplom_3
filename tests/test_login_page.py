from pages.home_page import HomePage
from pages.login_page import LoginPage
from tests.conftest import driver


class TestLoginPage:

    #переход по клику на конструктор



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

