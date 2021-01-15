from backend.dao.db.base_dao import BaseDao
from backend.models.marketplace import Marketplace


class MarketplaceDao(BaseDao):
    def create(self, model: Marketplace) -> None:
        query = f"""INSERT INTO marketplace(nome, descricao) VALUES('{model.name}','{model.description}');"""
        super().execute(query)

    def read_all(self) -> list:
        query = 'SELECT * FROM marketplace ORDER BY id;'
        result_list = super().read(query)
        marketplaces = []
        for result in result_list:
            marketplace = Marketplace(result[1], result[2], result[0])
            marketplaces.append(marketplace)
        return marketplaces

    def read_by_id(self, id: int) -> Marketplace:
        query = f"SELECT * FROM marketplace WHERE id = {id};"
        result = super().read(query)[0]
        marketplace = Marketplace(result[1], result[2], result[0])
        return marketplace

    def update(self, model: Marketplace) -> None:
        query = f"UPDATE marketplace SET nome = '{model.name}', descricao = '{model.description}' WHERE id = {model.id};"
        super().execute(query)

    def delete(self, id: int) -> None:
        query = f"DELETE FROM marketplace WHERE id={id};"
        super().execute(query)
