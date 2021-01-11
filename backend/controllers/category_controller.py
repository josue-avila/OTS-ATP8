import sys
sys.path.append('.')
from backend.controllers.log_controller import *
from backend.dao.category_dao import *
from backend.dao_txt.category_dao_txt import *


# Método responsável por validar os parâmentros / retornos
# e invocar o método de persistência de uma nova categoria
def add_new_category(name: str, desc: str) -> None:
    if isinstance(name, str) and isinstance(desc, str):
        add_new_category_db(name, desc)
    create_log('set', 'add_new_category')


# Método responsável por validar os parâmentros / retornos
# e invocar o método de consulta de todas as categorias cadastradas
def read_categories() -> list:
    categories = read_categories_db()
    create_log('get', 'read_categories')
    return categories
