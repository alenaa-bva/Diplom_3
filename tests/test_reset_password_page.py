from pages.reset_password_page.reset_password_page import ResetPasswordPage


class TestResetPasswordPage:

    def test_move_on_the_reset_password_page(self, driver):
        reset_password_page_obj = ResetPasswordPage(driver)
        is_password_field = reset_password_page_obj.move_on_the_reset_password_page(driver)

        assert is_password_field, "Не найдено поле для ввода пароля"

    def test_make_a_password_visible_by_eye_button(self, driver):
        reset_password_page_obj = ResetPasswordPage(driver)
        is_password_field_active = reset_password_page_obj.make_a_password_visible_by_eye_button(driver)

        assert is_password_field_active, "Не удалось показать пароль"
