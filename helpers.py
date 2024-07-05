import secrets
import allure
from faker import Faker


@allure.step('Генерируем рандомный хэш для ингредиентов.')
def generate_random_hex_24():
    hex = secrets.token_hex(12)
    return hex


class RandomUserGeneration:
    @staticmethod
    def generate_user_data():
        fake = Faker(locale="ru_RU")
        payload = {
            "email": fake.email(),
            "password": fake.password(),
            "name": fake.name()
        }
        return payload
