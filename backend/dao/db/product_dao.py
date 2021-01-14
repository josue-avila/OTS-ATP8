from backend.helpers.connection_db import *


# Método de persistência de uma nova categoria no banco de dados
# product = objeto contendo os parâmetros identifier, description, price
from backend.models.product import Product


def save_product_db(product: Product) -> None:
    try:
        with Connection() as con:
            cursor = con.cursor()
            cursor.execute(
                f"INSERT INTO produto(nome, descricao, preco) VALUES('{product.name}', '{product.description}', {product.price});")
            con.commit()
    except Exception as e:
        print(e)


# Método de consulta de todos os produtos
# gravadas no banco de dados
def read_products_db():
    with Connection() as con:
        cursor = con.cursor()
        cursor.execute('SELECT * FROM produto ORDER BY id;')
        result = cursor.fetchall()
        list_products= []
        for tuple in result:
            product = Product(tuple[1], tuple[2], tuple[3], tuple[0])
            list_products.append(product)
        return list_products


def read_product_db(id: int) -> Product:
    with Connection() as con:
        cursor = con.cursor()
        cursor.execute(f"SELECT * FROM produto WHERE id = {id};")
        tuple = cursor.fetchall()[0]
        product = Product(tuple[1], tuple[2], tuple[3], tuple[0])
        return product


def update_product_db(product: Product) -> None:
    with Connection() as con:
        cursor = con.cursor()
        cursor.execute(f"UPDATE produto SET nome = '{product.name}', descricao = '{product.description}', preco = '{product.price}' WHERE id = {product.id};")
        con.commit()

def delete_product_db(id: int) -> None:
    with Connection() as con:
        cursor = con.cursor()
        cursor.execute(f"DELETE FROM produto WHERE id={id};")
        con.commit()