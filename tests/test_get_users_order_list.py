import allure
from stellar_burgers_api import OrderMethods


@allure.story('Ручка /api/orders')
@allure.description('Получить заказы конкретного пользователя')
class TestGetUsersOrderList:
    @allure.description('Проверка получения списка заказов авторизованным пользователем. '
                        'Получаем код 200 и тело ответа в котором есть: "success":true')
    def test_get_users_order_list_with_auth_success(self, login_user):
        token = login_user[2]
        order_list_response = OrderMethods.get_users_order_list(token_user=token)
        assert (
                order_list_response.status_code == 200
                and order_list_response.json()['success'] is True
        )

    @allure.description('Проверка невозможности получения списка заказов, если пользователь не авторизован.'
                        'Получаем код 401')
    def test_get_users_order_list_with_auth_success(self):
        order_list_response = OrderMethods.get_users_order_list(token_user='')
        assert (
                order_list_response.status_code == 401
                and order_list_response.text == '{"success":false,"message":"You should be authorised"}'
        )
