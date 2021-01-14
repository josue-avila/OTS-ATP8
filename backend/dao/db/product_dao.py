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
    cursor.execute('SELECT * FROM produto ORDER BY id;')
    result = cursor.fetchall()
    list_products= []
    for tuple in result:
        product = Product(tuple[1], tuple[2], tuple[3], tuple[0])
        list_products.append(product)
    return list_products


def read_product_db(id: int) -> Product:
    cursor.execute(f"SELECT * FROM produto WHERE id = {id};")
    tuple = cursor.fetchone()
    product = Product(tuple[1], tuple[2], tuple[3], tuple[0])
    return product


def update_product_db(product: Product) -> None:
    cursor.execute(f"UPDATE produto SET nome = '{product.name}', descricao = '{product.description}', preco = '{product.price}' WHERE id = {product.id};")


def delete_product_db(id: int) -> None:
    cursor.execute(f"DELETE FROM produto WHERE id={id};")