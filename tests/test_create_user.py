import allure
import pytest
from helpers import RandomUserGeneration
from stellar_burgers_api import UserMethods


@allure.story('Ручка /api/auth/register')
@allure.description('Создание/регистрация пользователя')
class TestCreateUser:
    @allure.description('Создание пользователя с корректными данными. '
                        'Получаем код 200 и тело ответа в котором есть: "success":true')
    def test_create_uniq_user_success(self, create_user, delete_user):
        response = create_user[1]
        assert (response.status_code == 200 and
                response.json()['success'] is True)

    @allure.description('Проверка невозможности создании пользователя, когда он уже зарегистрирован.'
                        'Получаем ошибку 403')
    def test_create_double_user_return_status_code_403(self, create_user):
        data = create_user[0]
        response = UserMethods.create_user(data)
        assert (response.status_code == 403 and
                response.json()['message'] == 'User already exists')

    @allure.description('Проверка невозможности создании пользователя, когда одно из полей незаполненно.'
                        'Получаем ошибку 403')
    @pytest.mark.parametrize('field', ['email', 'password'])
    def test_create_user_with_empty_field_error(self, field):
        user_data = RandomUserGeneration.generate_user_data()
        payload = user_data
        payload.pop(field)
        response = UserMethods.create_user(payload)
        assert response.status_code == 403
        assert response.json()['message'] == 'Email, password and name are required fields'

