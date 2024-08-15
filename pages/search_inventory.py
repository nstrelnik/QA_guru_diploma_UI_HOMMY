from selene import browser, have
import allure


class Search:

    @allure.step('Поиск товара в каталоге через строку поиска')
    def open_search(self):
        browser.element('//*[@class = "navigation-personal"]/li[1]').click()
        return self

    @allure.step('Ввод поискового запроса')
    def search_query_enter(self, value):
        browser.element('.header-search__input').type(value).press_enter()
        return self

    @allure.step('Проверка найденного товара')
    def search_query_successful(self, value):
        assert browser.all('.card-product__title').element_by(have.exact_text(value))
        return self


search = Search()
