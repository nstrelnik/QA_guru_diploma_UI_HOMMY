from pages.authorization_page import authorization
from pages.inventory_page import inventory
from pages.search_inventory import search
from pages.favorite_page import favorite
from data.users import User
from pages.cart_page import cart
import allure


@allure.story('Добавление товара в корзину пользователя')
def test_add_product_to_cart():
    user = User(
        user_email='testtest@mail.ru',
        user_password='testtest@mail.ru'
    )
    product_name = "Ваза VERDA S"
    authorization.open_browser().open_authorization_form().fill_username(user).fill_password(
        user).click_login().assert_successful_authorization()
    inventory.open_catalog().open_product_page(product_name).add_product_to_cart().assert_product_to_cart_successful()
    cart.open_cart().delete_product_from_cart()


@allure.story('Добавление товара в Избранное пользователя')
def test_add_product_to_favorite():
    user = User(
        user_email='testtest@mail.ru',
        user_password='testtest@mail.ru'
    )
    product_name = "Ваза VERDA S"
    authorization.open_browser().open_authorization_form().fill_username(user).fill_password(
        user).click_login().assert_successful_authorization()
    inventory.open_catalog()
    (favorite.open_page_product_for_favorite(product_name).add_product_to_favorites().open_page_favorite().
     assert_product_to_favorites_successful(product_name).delete_product_from_favorite())


@allure.story('Поиск товара в каталоге через строку поиска')
def test_search():
    product_name = "Часы настольные STELE"
    authorization.open_browser()
    search.open_search().search_query_enter(product_name).search_query_successful(product_name)
