import allure
from helpers import generate_random_hex_24
from stellar_burgers_api import OrderMethods


@allure.story('Ручка /api/orders')
@allure.description('Создание заказа')
class TestCreateOrder:
    @allure.title('Проверка создания заказа c ингредиентами авторизованным пользователем. '
                        'Получаем код 200 и тело ответа в котором есть: "success":true')
    def test_create_order_with_auth_with_ingredients_success(self, login_user):
        ingredients = OrderMethods.get_ingredients()
        token = login_user[2]
        order_response = OrderMethods.create_order(token_user=token, ids=ingredients)
        assert (
                order_response.status_code == 200
                and order_response.json()['success'] is True
        )

    @allure.title('Проверка создания заказа c ингредиентами не авторизованным пользователем. '
                        'Получаем код 200 и тело ответа в котором есть: "success":true')
    def test_create_order_without_auth_with_ingredients_success(self):
        ingredients = OrderMethods.get_ingredients()
        order_response = OrderMethods.create_order(token_user='', ids=ingredients)
        assert (
                order_response.status_code == 200
                and order_response.json()['success'] is True
        )

    @allure.title('Проверка создания заказа без ингредиентов авторизованным пользователем. '
                        'Получаем код 400 и тело ответа в котором есть: \'success\':false')
    def test_create_order_with_auth_without_ingredients_error(self, login_user):
        token = login_user[2]
        order_response = OrderMethods.create_order(token_user=token, ids='')
        assert (
                order_response.status_code == 400 and
                order_response.text == '{"success":false,"message":"Ingredient ids must be provided"}'
        )

    @allure.title('Проверка создания заказа без ингредиентов не авторизованным пользователем. '
                        'Получаем код 400 и тело ответа в котором есть: \'success\':false')
    def test_create_order_without_auth_without_ingredients_error(self):
        order_response = OrderMethods.create_order(token_user='', ids='')
        assert (
                order_response.status_code == 400 and
                order_response.text == '{"success":false,"message":"Ingredient ids must be provided"}'
        )

    @allure.title('Проверка создания заказа с неверным хешем ингредиентов. '
                        'Получаем код 400')
    def test_create_order_with_incorrect_hex_error_400(self):
        ingredients = generate_random_hex_24()
        order_response = OrderMethods.create_order(token_user='', ids=ingredients)
        assert (
                order_response.status_code == 400 and
                order_response.text == '{"success":false,"message":"One or more ids provided are incorrect"}'
        )
