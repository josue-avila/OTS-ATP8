from backend.helpers.connection_db import *
from backend.models.marketplace import Marketplace


def read_marketplace_db() -> list:
    cursor.execute('SELECT * FROM marketplace')
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