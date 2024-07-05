import allure
import requests
from urls import Urls


class UserMethods:
    @staticmethod
    @allure.step('Создание нового пользователя в системе')
    def create_user(payload):
        response = requests.post(Urls.URL_MAIN + Urls.URL_CREATE_USER, data=payload)
        return response

    @staticmethod
    @allure.step('Логин пользователя в системе')
    def login_user(payload):
        response = requests.post(Urls.URL_MAIN + Urls.URL_LOGIN_USER, data=payload)
        return response

    @staticmethod
    @allure.step('Обновление данных о пользователе')
    def update_user(token_user, payload):
        headers = {'Authorization': token_user}
        response = requests.patch(Urls.URL_MAIN + Urls.URL_UPDATE_USER, headers=headers, data=payload)
        return response

    @staticmethod
    @allure.step('Удаление пользователя')
    def delete_user(token_user):
        headers = {'Authorization': token_user}
        response = requests.delete(Urls.URL_MAIN + Urls.URL_DELETE_USER, headers=headers)
        return response


class OrderMethods:
    @staticmethod
    @allure.step('Создание заказа')
    def create_order(token_user, ids):
        headers = {'Authorization': token_user}
        payload = {'ingredients': ids}
        response = requests.post(Urls.URL_MAIN + Urls.URL_CREATE_ORDER, headers=headers, json=payload)
        return response

    @staticmethod
    @allure.step('Получение списка ингредиентов')
    def get_ingredients():
        response = requests.get(Urls.URL_MAIN + Urls.URL_GET_INGREDIENTS)
        ingredients = []
        for i in response.json()['data']:
            ingredients.append(i['_id'])
            return ingredients

    @staticmethod
    @allure.step('Получение списка заказов пользователя')
    def get_users_order_list(token_user):
        headers = {'Authorization': token_user}
        response = requests.get(Urls.URL_MAIN + Urls.URL_GET_USER_ORDERS, headers=headers)
        return response
