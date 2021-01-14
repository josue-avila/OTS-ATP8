from backend.helpers.connection_db import *


# Método de persistência de uma nova categoria no banco de dados
# product = objeto contendo os parâmetros identifier, description, price
from backend.models.product import Product


def save_product_db(product: Product) -> bool:
    try:
        cursor.execute(
            f"INSERT INTO produto(nome, descricao, preco) VALUES('{product.name}', '{product.description}', {product.price});")
        con.commit()
        return True
    except Exception as e:
        return False


# Método de consulta de todos os produtos
# gravadas no banco de dados
def read_products_db():
    cursor.execute('SELECT * FROM produto;')
    result = cursor.fetchall()
    list_products= []
    for tuple in result:
        product = Product(tuple[1], tuple[2], tuple[3], tuple[0])
        list_products.append(product)
    return list_products