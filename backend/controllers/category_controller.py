import sys
sys.path.append('.')
from backend.controllers.log_controller import *
from backend.dao.category_dao import *
from backend.dao_txt.category_dao_txt import *
from backend.models.category import Category


# Método responsável por validar os parâmentros / retornos
# e invocar o método de persistência de uma nova categoria
def add_new_category(category: Category) -> None:
    if isinstance(category.name, str) and isinstance(category.description, str):
        add_new_category_db(category)
    create_log('set', 'category')


# Método responsável por validar os parâmentros / retornos
# e invocar o método de consulta de todas as categorias cadastradas
def read_categories() -> list:
    categories = read_categories_db()
    create_log('get', 'categories')
    return categories
