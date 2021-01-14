from backend.dao.db.product_dao import save_product_db, read_products_db
from backend.controllers.log_controller import save_log
from backend.models.product import Product

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
