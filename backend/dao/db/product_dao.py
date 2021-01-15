from backend.dao.db.base_dao import BaseDao
from backend.models.product import Product


class ProductDao(BaseDao):
    def create(self, model: Product) -> None:
        query = f"""INSERT INTO produto(nome, descricao, preco) VALUES('{model.name}','{model.description}',{model.price});"""
        super().execute(query)


    def read_all(self) -> list:
        query = 'SELECT * FROM produto ORDER BY id;'
        result_list = super().read(query)
        products = []
        for result in result_list:
            product = Product(result[1], result[2], result[3], result[0])
            products.append(product)
        return products


    def read_by_id(self, id: int) -> Product:
        query = f"SELECT * FROM produto WHERE id = {id};"
        result = super().read(query)[0]
        product = Product(result[1], result[2], result[3], result[0])
        return product


    def update(self, model: Product)-> None:
        query = f"UPDATE produto SET nome = '{model.name}', descricao = '{model.description}', preco = '{model.price}' WHERE id = {model.id};"
        super().execute(query)


    def delete(self, id: int) -> None:
        query = f"DELETE FROM produto WHERE id={id};"
        super().execute(query)
