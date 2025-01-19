from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data import LoginData
from xpath_data import HomePagePaths, RegistrationPagePaths, LoginPagePaths, ForgotPasswordPagePaths

# # вспомогательные функции
# def wait_element_to_be_clickable(driver, locator, timeout=5):
#     return WebDriverWait(driver, timeout).until(expected_conditions.element_to_be_clickable(locator))
#
# def wait_element_to_be_visible(driver, locator, timeout=5):
#     return WebDriverWait(driver, timeout).until(expected_conditions.visibility_of_element_located(locator))


#тесты
class TestLoginPage:

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

