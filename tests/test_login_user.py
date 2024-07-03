import copy
import allure
import pytest
from helpers import RandomUserGeneration
from stellar_burgers_api import UserMethods


@allure.story('Ручка /api/auth/login')
@allure.description('Авторизация пользователя')
class TestLoginUser:
    @allure.title('Проверка успешного логина пользователя. '
                        'Получаем статус 200 и тело ответа в котором есть: "success":true')
    def test_login_user_success(self, login_user):
        response = login_user[1]
        assert (response.status_code == 200 and
                response.json()['success'] is True)

    @allure.title('Проверка невозможности логина пользователя с неверным логином и паролем.'
                        'Получаем ошибку 401')
    def test_login_user_with_incorrect_login_and_password(self):
        data = RandomUserGeneration.generate_user_data()
        response = UserMethods.login_user(data)
        assert (response.status_code == 401 and
                response.json()['message'] == 'email or password are incorrect')

    @allure.title('Проверка невозможности логина пользователя, когда логин или пароль не переданы.'
                        'Получаем ошибку 401')
    @pytest.mark.parametrize('field', ['email', 'password'])
    def test_login_user_with_empty_field_error(self, field, create_user):
        payload = copy.deepcopy(create_user[0])
        UserMethods.create_user(payload)
        payload.pop(field)
        response = UserMethods.login_user(payload)
        assert response.status_code == 401
        assert response.json()['message'] == 'email or password are incorrect'
