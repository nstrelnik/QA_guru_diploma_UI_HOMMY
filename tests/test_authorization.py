from pages.authorization_page import authorization
from data.users import User
import allure


@allure.story('Успешная авторизация')
def test_successful_authorization():
    user = User(
        user_email='testtest@mail.ru',
        user_password='testtest@mail.ru'
    )
    authorization.open_browser().open_authorization_form().fill_username(user).fill_password(
        user).click_login().assert_successful_authorization()


@allure.story('Неуспешная авторизация')
def test_invalid_authorization():
    user = User(
        user_email='test@mail.ru',
        user_password='test@mail.ru'
    )
    authorization.open_browser().open_authorization_form().fill_username(user).fill_password(
        user).click_login().assert_invalid_authorization()


@allure.story('Выход из аккаунта')
def test_logout():
    user = User(
        user_email='testtest@mail.ru',
        user_password='testtest@mail.ru'
    )
    authorization.open_browser().open_authorization_form().fill_username(user).fill_password(
        user).click_login().assert_successful_authorization().logout().asser_logout_successful()
