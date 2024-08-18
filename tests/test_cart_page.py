from pages.authorization_page import authorization
import allure
from pages.inventory_page import inventory
from pages.cart_page import cart


@allure.story('Удаление товара из корзины')
def test_delete_from_cart():
    product_name = "Ваза VERDA S"

    authorization.open_browser()

    inventory.open_catalog()
    inventory.open_product_page(product_name)
    inventory.add_product_to_cart()

    cart.open_cart()
    cart.delete_product_from_cart()
    cart.assert_delete_product_from_cart()


