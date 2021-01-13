from backend.helpers.connection_db import *
from backend.models.marketplace import Marketplace


def read_marketplaces_db() -> list:
    cursor.execute('SELECT * FROM marketplace ORDER BY id')
    marketplaces = cursor.fetchall()
    list_marketplaces = []
    for tuple in marketplaces:
        marketplace = Marketplace(tuple[1],tuple[2],tuple[0])
        list_marketplaces.append(marketplace)
    return list_marketplaces

def save_marketplace_db(marketplace: Marketplace) -> None:
    try:
        cursor.execute(f"INSERT INTO marketplace (nome, descricao) values('{marketplace.name}','{marketplace.description}');")
        con.commit()
        return True
    except Exception as e:
        return False

    
def read_marketplace_db(id: int) -> Marketplace:
    cursor.execute(f"SELECT * FROM marketplace WHERE id = {id};")
    tuple = cursor.fetchall()[0]
    marketplace = Marketplace(tuple[1], tuple[2], tuple[0])
    return marketplace


def update_marketplace_db(marketplace: Marketplace) -> None:
    cursor.execute(f"UPDATE marketplace SET nome = '{marketplace.name}', descricao = '{marketplace.description}' WHERE id = {marketplace.id};")
