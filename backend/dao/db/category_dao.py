from backend.helpers.connection_db import *
from backend.models.category import Category


# Método de persistência de uma nova categoria no banco de dados
def save_category_db(category: Category) -> bool:
    try:
        cursor.execute(
            f"INSERT INTO categoria(nome, descricao) VALUES('{category.name}','{category.description}');")
        con.commit()
        return True
    except Exception as e:
        return False


# Método de consulta de todas as categorias
# gravadas no banco de dados
def read_categories_db() -> list:
    cursor.execute('SELECT * FROM categoria ORDER BY id;')
    categories = cursor.fetchall()
    list_categories = []
    for tuple in categories:
        category = Category(tuple[1],tuple[2],tuple[0])
        list_categories.append(category)
    return list_categories


def read_category_db(id: int) -> Category:
    cursor.execute(f"SELECT * FROM categoria WHERE id = {id};")
    tuple = cursor.fetchall()[0]
    category = Category(tuple[1], tuple[2], tuple[0])
    return category


def update_category_db(category: Category) -> None:
    cursor.execute(f"UPDATE categoria SET nome = '{category.name}', descricao = '{category.description}' WHERE id = {category.id};")
