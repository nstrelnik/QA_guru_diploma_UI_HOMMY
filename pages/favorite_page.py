from selene import browser, have, be
import allure


class Favorite:

    @allure.step('Переход на страницу товара')
    def open_page_product_for_favorite(self, value):
        browser.all('.card-product__title').element_by(have.exact_text(value)).click()
        return self

    @allure.step('Добавление товара в Избранное')
    def add_product_to_favorites(self):
        browser.element('.card-product__favorite').click()
        return self

    @allure.step('Переход на страницу Избранного')
    def open_page_favorite(self):
        browser.element('//*[@class = "navigation-personal"]/li[2]').click()
        return self

    @allure.step('Проверка добавления товара в Избранное')
    def assert_product_to_favorites_successful(self, value):
        assert browser.all('.card-product__title').element_by(have.exact_text(value))
        return self

    @allure.step('Удаление товара из избранного')
    def delete_product_from_favorite(self):
        browser.element('.card-product-delete').click()
        return self

    @allure.step('Проверка удаления товара из избранного')
    def assert_delete_product_from_favorite(self):
        browser.element('.card-product__return').should(be.visible)


favorite = Favorite()
