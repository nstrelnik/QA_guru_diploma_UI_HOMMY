from selene import browser, have
import allure
from data.users import User


class Authorization:

    @allure.step('Открытие главной страницы')
    def open_browser(self):
        browser.open('')
        return self

    @allure.step('Открытие формы авторизации')
    def open_authorization_form(self):
        browser.element('//*[@class = "navigation-personal"]/li[3]').click()
        return self

    @allure.step('Заполнение поля Username')
    def fill_username(self, user: User):
        browser.element('#user-email').type(user.user_email)
        return self

    @allure.step('Заполнение поля Password')
    def fill_password(self, user: User):
        browser.element('#user-password').type(user.user_password)
        return self

    @allure.step('Нажатие на кнопку Login')
    def click_login(self):
        browser.element('//*[@name = "Login"]').click()
        return self

    @allure.step('Проверка успешной авторизации')
    def assert_successful_authorization(self):
        assert browser.element('.personal-data__title').should(have.text('Личные данные'))
        return self

    @allure.step('Проверка неуспешной авторизации')
    def assert_invalid_authorization(self):
        assert browser.element('.errortext').should(have.text('Неверный логин или пароль.'))
        return self

    @allure.step('Выход из аккаунта')
    def logout(self):
        browser.element('.login-info__logout-text').click()
        return self

    @allure.step('Проверка выхода из аккаунта')
    def asser_logout_successful(self):
        assert browser.driver.current_url == "https://myhommy.ru/auth/"
        return self


authorization = Authorization()
