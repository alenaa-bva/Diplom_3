class BasePagePaths:
    feed_button = ".//a/p[text()='Лента Заказов']"  # кнопка лента заказов
    stellar_burgers_logo = ".//div[contains(@class, 'AppHeader_header__logo')]"  # лого Stellar Burgers
    constructor_button = ".//a/p[text()='Лента Заказов']"  # кнопка конструктор
    personal_button = ".//a/p[text() = 'Личный Кабинет']"  # кнопка личный кабинет


class LoginPagePaths:
    login_header = ".//div[contains(@class, 'Auth_login')]//h2[text()='Вход']"  # Заголовок страницы
    lp_email_input = ".//fieldset[1]/div/div/input[@name='name']"  # Поле email на странице логина
    lp_password_input = ".//fieldset[2]/div/div/input[@name='Пароль']"  # Поле пароль на странице логина
    login_button = ".//form/button[text()='Войти']"  # Кнопка «Войти»


class RegistrationPagePaths:
    rp_name_input = ".//label[text()='Имя']/..//input[@name='name']"  # Поле имя на странице регистрации
    rp_email_input = ".//label[text()='Email']/..//input[@name='name']"  # Поле емейл на странице регистрации
    rp_password_input = ".//label[text()='Пароль']/..//input[@name='Пароль']"  # Поле пароль на странице регистрации
    sign_up_button = ".//form/button[text()='Зарегистрироваться']"  # Кнопка "Зарегистрироваться"


class HomePagePaths:
    place_an_order_button = './/div/button[text()= "Оформить заказ"]'  # Кнопка «Оформить заказ»

    # Секция "Соберите бургер"
    collect_a_burger_header = ".//h1[text()='Соберите бургер']"  # Заголовок «Соберите бургер»
    first_bread_ingredient = ".//div[contains(@class, 'BurgerIngredients_ingredients__menu')]/ul[1]/a[1]"  # первый по счету ингридиент в секции булок

    first_sauce_ingredient = ".//div[contains(@class, 'BurgerIngredients_ingredients__menu')]/ul[2]/a[1]"  # первый по счету ингридиент в секции соусов
    first_filling_ingredient = ".//div[contains(@class, 'BurgerIngredients_ingredients__menu')]/ul[3]/a[1]"  # первый по счету ингридиент в секции начинок

    ingredient_details_modal_header = ".//div/h2[text()='Детали ингредиента']"  # заголовок "Детали заказа" на модальном окне ингредиента
    close_details_button = ".//section[1]/div[1]/button[contains(@class, 'modal__close')]"  # крестик на окне деталей ингредиента

    burger_basket_section = ".//section[2]/ul[contains( @class , 'BurgerConstructor_basket__list')]"  # секция корзины
    total_counter = ".//div[contains(@class, 'BurgerConstructor_basket__totalContainer')]/p"  # счетчик суммы в корзине
    order_number_9999 = ".//div[1]/div/h2[text()='9999']"  # Номер заказа 9999 на всплывашке при оформлении заказа, после которого появится настоящий номер заказа
    close_order_button = ".//section[1]/div[1]/button[contains(@class, 'modal__close')]"  # крестик на модалке заказа
    order_number = ".//div[1]/div/h2"  # Номер заказа на всплывашке при оформлении заказа
    extra_modal_1 = ".//div[2][@class='Modal_modal_overlay__x2ZCr']"  # перекрывающая модалка
    extra_modal_2 = ".//div[1][@class='Modal_modal_overlay__x2ZCr']"  # перекрывающая модалка


class ForgotPasswordPagePaths:
    fp_email_input = ".//form/fieldset/div/div/input"  # Поле email на странице восстановления пароля
    fp_recover_button = ".//div/form/button[text()='Восстановить']"  # Кнопка «Восстановить»
    fp_page_header = ".//div/h2[text()='Восстановление пароля']"  # Заголовок «Восстановление пароля»
    fp_eye_button = ".//form/fieldset[1]/div/div/div[contains(@class, 'icon-action')]"  # Иконка глаза в поле password
    fp_password_field_shows_password = ".//div/div/label[contains(@class, 'input__placeholder-focused')]"  # Поле для ввода пароля в активном статусе
    fp_password_input = ".//form/fieldset[1]/div/div/input[@type='password']"  # Поле пароль на странице сброса пароля


class PersonalAccountPagePaths:
    profile_tab = ".//a[text()='Профиль']"  # вкладка профиль
    history_tab = ".//a[text()='История заказов']"  # вкладка История заказов
    logout_button = ".//li[3]/button[text()='Выход']"  # кнопка "Выход"
    last_order_number = ".//li[last()]/a/div[1][contains(@class, 'OrderHistory_textBox')]/p[1]"  # номер последнего оформленного заказа


class FeedPagePaths:
    feed_header = ".//div/h1[text()='Лента заказов']"  # хедер лента заказов
    order_box = ".//div[1]/div/main/div/div/ul/li[1]"  # плашка заказа в ленте
    order_ingredients = ".//section[2]/div[1]/div/ul"  # секция с составом
    order_price = ".//section[2]/div[1]/div/div/div"  # секция с суммой
    in_work_order_number = ".//div[1]/ul[2]/li"  # номер заказа в работе
    in_work_description = ".//div[1]/ul[2]/li[text()='Все текущие заказы готовы!']"  # элемент который отображается несколько секунд до номера заказа
    orders_completed_all_the_time = ".//div[1]/div/main/div/div/div/div[2]/p[2]"  # заказы за все время
    orders_completed_today = ".//div[1]/div/main/div/div/div/div[3]/p[2]"  # заказы за сегодня
