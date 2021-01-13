from backend.controllers.log_controller import save_log
from backend.dao.db.category_dao import save_category_db, read_categories_db, read_category_db, update_category_db
from backend.models.category import Category


# Método responsável por validar os parâmentros / retornos
# e invocar o método de persistência de uma nova categoria
def save_category(category: Category) -> None:
    if isinstance(category.name, str) and isinstance(category.description, str):
        save_category_db(category)
    save_log('set', 'category')


# Método responsável por validar os parâmentros / retornos
# e invocar o método de consulta de todas as categorias cadastradas
def read_categories() -> list:
    categories = read_categories_db()
    save_log('get', 'categories')
    return categories


def read_category(id: int) -> Category:
    category = read_category_db(id)
    save_log('read', 'category')
    return category


def update_category(category: Category) -> None:
    new_category = read_category(category.id)
    new_category.name = category.name
    new_category.description = category.description
    update_category_db(new_category)
    save_log('update', 'category')

