from backend.helpers.connection_db import *


# Método de persistência de uma nova categoria no banco de dados
# name = nome da nova categoria cadastrada
# desc = descrição da nova categoria cadastrada
from backend.models.category import Category


def save_category_db(category: Category) -> bool:
    try:
        cursor.execute(
            f"INSERT INTO categoria(nome, descricao) VALUES('{category.name}','{category.description}');")
        con.commit()
        # cursor.close()
        # con.close()
        return True
    except Exception as e:
        return False


# Método de consulta de todas as categorias
# gravadas no banco de dados
def read_categories_db() -> list:
    cursor.execute('SELECT * FROM categoria;')
    categories = cursor.fetchall()
    list_categories = []
    for tuple in categories:
        category = Category(tuple[1],tuple[2],tuple[0])
        list_categories.append(category)
    # cursor.close()
    # con.close()
    return list_categories
