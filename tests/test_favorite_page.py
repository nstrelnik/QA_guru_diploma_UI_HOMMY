from pages.authorization_page import authorization
import allure
from pages.inventory_page import inventory
from pages.favorite_page import favorite


@allure.story('Удаление товара из Избранного')
def test_delete_product_from_favorite():
    product_name = "Ваза VERDA S"
    authorization.open_browser()
    inventory.open_catalog()
    (favorite.open_page_product_for_favorite(
        product_name).add_product_to_favorites().open_page_favorite().delete_product_from_favorite().
     assert_delete_product_from_favorite())
