import sys

sys.path.append('.')

from backend.dao.product_dao import *
from backend.dao_txt.product_dao_txt import *
from backend.controllers.log_controller import *


# Método responsável por invocar o método
# de consulta de todas os produtos cadastrados
def read_products() -> list:
    products = read_products_db()
    save_log('get', 'products')
    return products


# Método responsável invocar o método de
# persistência de um novo produto
def save_product(product: Product) -> None:
    if (isinstance(product.name, str) and isinstance(product.description, str)
            and isinstance(product.price, str)):
        save_product_db(product)
        save_log('set', 'product')
