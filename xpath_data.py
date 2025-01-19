class BasePagePaths:
    feed_button = ".//a/p[text()='Лента Заказов']" # кнопка лента заказов
    stellar_burgers_logo = ".//div[contains(@class, 'AppHeader_header__logo')]" # лого Stellar Burgers
    constructor_button = ".//a/p[text()='Лента Заказов']" # кнопка конструктор
    personal_button = ".//a/p[text() = 'Личный Кабинет']"  # кнопка личный кабинет


class LoginPagePaths:
    pass
    # login_header = ".//div[contains(@class, 'Auth_login')]//h2[text()='Вход']" # Заголовок страницы
    # lp_email_input = ".//label[text()='Email']/..//input[@name='name']" # Поле пароль на странице логина
    # lp_password_input = ".//label[text()='Пароль']/..//input[@name='Пароль']" # Поле пароль на странице логина
    # login_button = ".//form/button[text()='Войти']" # Кнопка «Войти»
    # registration_link = ".//p[1]/a[text()='Зарегистрироваться']" # Кнопка-ссылка "Зарегистрироваться"
    # password_recovery_link = ".//p[2]/a[text()='Восстановить пароль']"  # Кнопка-ссылка «Войти»


class RegistrationPagePaths:
    pass
    # rp_name_input = ".//label[text()='Имя']/..//input[@name='name']" # Поле имя на странице регистрации
    # rp_email_input = ".//label[text()='Email']/..//input[@name='name']" # Поле емейл на странице регистрации
    # rp_password_input = ".//label[text()='Пароль']/..//input[@name='Пароль']" # Поле пароль на странице регистрации
    # sign_up_button = ".//form/button[text()='Зарегистрироваться']" # Кнопка "Зарегистрироваться"
    # rp_login_link = ".//p/a[text()='Войти']" # Кнопка-ссылка «Войти»
    #
    # # сообщения об ошибках
    # error_message_existing_user = ".//p[text() = 'Такой пользователь уже существует']" # сообщение об ошибке 'Такой пользователь уже существует'
    # error_message_incorrect_password = ".// p[text() = 'Некорректный пароль']" # сообщение об ошибке 'Некорректный пароль'


class HomePagePaths:
    pass
    # go_to_account_button = ".//button[text()='Войти в аккаунт']" # Кнопка «Войти в аккаунт»
    # place_an_order_button = './/div/button[text()= "Оформить заказ"]' # Кнопка «Оформить заказ»

    # Секция "Соберите бургер"
    collect_a_burger_header= ".//h1[text()='Соберите бургер']"  # Заголовок «Соберите бургер»
    # bread_tab = ".//span[text() = 'Булки']" # меню булок
    # sauce_tab = ".//span[text() = 'Соусы']" # меню соусов
    # fillings_tab = ".//span[text() = 'Начинки']" # меню начинок
    # ingredients_section = ".//section[contains(@class, 'BurgerIngredients_ingredients')]" # секция ингридиентов для бургеров
    #
    first_bread_ingredient = ".//div[contains(@class, 'BurgerIngredients_ingredients__menu')]/ul[1]/a[1]" # первый по счету ингридиент в секции булок
    # breads_section_header = ".//div[contains(@class, 'BurgerIngredients_ingredients__menu')]/h2[text()='Булки']" # заголовок секции булок
    #
    first_sauce_ingredient = ".//div[contains(@class, 'BurgerIngredients_ingredients__menu')]/ul[1]/a[1]"  # первый по счету ингридиент в секции соусов
    # sauces_section_header = ".//div[contains(@class, 'BurgerIngredients_ingredients__menu')]/h2[text()='Соусы']"  # заголовок секции соусов
    #
    first_filling_ingredient = ".//div[contains(@class, 'BurgerIngredients_ingredients__menu')]/ul[1]/a[1]"  # первый по счету ингридиент в секции начинок
    # fillings_section_header = ".//div[contains(@class, 'BurgerIngredients_ingredients__menu')]/h2[text()='Начинки']"  # заголовок секции начинок

    ingredient_details_modal_header =  ".//div/h2[text()='Детали ингредиента']" # заголовок "Детали заказа" на модальном окне ингредиента
    close_details_button = ".//section[1]/div[1]/button[contains(@class, 'modal__close')]" # крестик на окне деталей ингредиента

    burger_basket_section = ".//section[2]/ul[contains( @class , 'BurgerConstructor_basket__list')]" # секция корзины
    total_counter = ".//div[contains(@class, 'BurgerConstructor_basket__totalContainer')]/p" # счетчик суммы в корзине


class ForgotPasswordPagePaths:
    pass
    # fp_login_link = ".//p/a[text()='Войти']" # Кнопка-ссылка «Войти»
    # fp_email_input = ".//form/fieldset/div/div/input" # Поле email на странице восстановления пароля
    # fp_recover_button = ".//div/form/button[text()='Восстановить']" # Кнопка «Восстановить»


class ResetPasswordPagePaths:
    pass
    # rp_page_header = ".//div[1]/div/main/div/h2[text()='Восстановление пароля']" # Заголовок «Восстановление пароля»
    # rp_eye_button = ".//form/fieldset[1]/div/div/div[contains(@class, 'icon-action')]" # Иконка глаза в поле password
    # rp_password_input = ".//form/fieldset[1]/div/div/input[@type='password']" # Поле пароль на странице сброса пароля


class PersonalAccountPagePaths:
    pass
    # profile_tab = ".//a[text()='Профиль']" # вкладка профиль
    # pa_email_input = ".//div/input[@name='Name']" # Поле емейл
    # logout_button = ".// button[text() = 'Выход']" # кнопка "Выход"

class FeedPagePaths:
    feed_header = ".//div/h1[text()='Лента заказов']" # хедер лента заказов