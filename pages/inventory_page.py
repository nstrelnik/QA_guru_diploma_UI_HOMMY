from selene import browser, have, be
import allure


class Inventory:

    @allure.step('Открытие страницы каталога')
    def open_catalog(self):
        browser.element('//*[@class = "navigation-main__list"]/li[2]').click()
        browser.element('//*[@class = "main-category__list"]/li[1]').click()
        return self

    @allure.step('Переход на страницу товара')
    def open_product_page(self, value):
        browser.all('.card-product__title').element_by(have.exact_text(value)).click()
        return self

    @allure.step('Добавление товара в корзину')
    def add_product_to_cart(self):
        browser.element('.card-product__button').click()
        return self

    @allure.step('Проверка добавления товара в корзину')
    def assert_product_to_cart_successful(self):
        browser.element('.value--add').should(be.visible)
        return self


inventory = Inventory()
