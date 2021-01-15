from backend.dao.db.base_dao import BaseDao
from backend.models.category import Category


class CategoryDao(BaseDao):
    def create(self, model: Category) -> None:
        query = f"""INSERT INTO categoria(nome, descricao) VALUES('{model.name}','{model.description}');"""
        super().execute(query)

    def read_all(self) -> list:
        query = 'SELECT * FROM categoria ORDER BY id;'
        result_list = super().read(query)
        categories = []
        for result in result_list:
            category = Category(result[1], result[2], result[0])
            categories.append(category)
        return categories

    def read_by_id(self, id: int) -> Category:
        query = f"SELECT * FROM categoria WHERE id = {id};"
        result = super().read(query)[0]
        category = Category(result[1], result[2], result[0])
        return category

    def update(self, model: Category) -> None:
        query = f"UPDATE categoria SET nome = '{model.name}', descricao = '{model.description}' WHERE id = {model.id};"
        super().execute(query)

    def delete(self, id: int) -> None:
        query = f"DELETE FROM categoria WHERE id={id};"
        super().execute(query)
