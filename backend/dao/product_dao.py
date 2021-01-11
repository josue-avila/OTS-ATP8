from backend.helpers.connection_db import *


# Método de persistência de uma nova categoria no banco de dados
# product = objeto contendo os parâmetros identifier, description, price
def save_product_db(product) -> bool:
    try:
        cursor.execute(
            f"INSERT INTO produto(nome, descricao, preco) VALUES('{product.get('identifier')}', '{product.get('description')}', '{product.get('price')}');")
        con.commit()
        return True
    except Exception as e:
        return False


# Método de consulta de todos os produtos
# gravadas no banco de dados
def read_products_db():
    cursor.execute('SELECT * FROM produto;')
    result = cursor.fetchall()
    con.commit()
    return result