from backend.controllers.log_controller import save_log
from backend.dao.db.category_dao import save_category_db, read_categories_db
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
