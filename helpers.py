import random

def generate_register_data():

    base_login = "alenaibragimova1"
    three_random_digits = random.randint(100, 999)
    login = f"{base_login}{three_random_digits}@yandex.ru"
    password = f"123456{three_random_digits}"
    name = "Alena"

    register_data = {
        "name" : name,
        "login": login,
        "password": password
    }
    return register_data


