from selene import browser, have, be
import allure


class Cart:

    @allure.step('Переход на страницу корзины')
    def open_cart(self):
        browser.element('//*[@class = "navigation-personal"]/li[4]').click()
        return self

    @allure.step('Удаление товара из корзины')
    def delete_product_from_cart(self):
        browser.element('.ordered-products__product-delete').click()
        return self

    @allure.step('Проверка удаления товара из корзины')
    def assert_delete_product_from_cart(self):
        browser.element('.cart__empty-block-text').should(be.visible).should(have.text("В вашей корзине пока пусто"))
        return self


cart = Cart()
