from backend.dao.db.base_dao import BaseDao
from backend.models.seller import Seller


class SellerDao(BaseDao):
    def create(self, model: Seller) -> None:
        query = f"""INSERT INTO seller(nome, telefone, email) VALUES('{model.fullname}','{model.phone}','{model.email}');"""
        super().execute(query)


    def read_all(self) -> list:
        query = 'SELECT * FROM seller ORDER BY id;'
        result_list = super().read(query)
        sellers = []
        for result in result_list:
            seller = Seller(result[1], result[2], result[3], result[0])
            sellers.append(seller)
        return sellers


    def read_by_id(self, id: int) -> Seller:
        query = f"SELECT * FROM seller WHERE id = {id};"
        result = super().read(query)[0]
        seller = Seller(result[1], result[2], result[3], result[0])
        return seller


    def update(self, model: Seller)-> None:
        query = f"UPDATE seller SET nome = '{model.fullname}', telefone = '{model.phone}', email = '{model.email}' WHERE id = {model.id};"
        super().execute(query)


    def delete(self, id: int) -> None:
        query = f"DELETE FROM seller WHERE id={id};"
        super().execute(query)
