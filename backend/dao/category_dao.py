from backend.helpers.connection_db import *

# Método de persistência de uma nova categoria no banco de dados
# name = nome da nova categoria cadastrada
# desc = descrição da nova categoria cadastrada
def add_new_category_db(name: str, desc: str) -> bool:
    try:
        cursor.execute(
            f"INSERT INTO categoria(nome, descricao) VALUES('{name}','{desc}');")
        con.commit()
        return True
    except Exception as e:
        return False


# Método de consulta de todas as categorias
# gravadas no banco de dados
def read_categories_db() -> list:
    cursor.execute('SELECT * FROM categoria;')
    categories = cursor.fetchall()
    con.commit()
    return categories


# Método de consulta de um categoria especifica
def search_category_db(name: str, desc: str):
    pass
