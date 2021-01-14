from backend.helpers.connection_db import *
from backend.models.marketplace import Marketplace


def read_marketplaces_db() -> list:
    with Connection() as con:
        cursor = con.cursor()
        cursor.execute('SELECT * FROM marketplace ORDER BY id')
        marketplaces = cursor.fetchall()
        list_marketplaces = []
        for tuple in marketplaces:
            marketplace = Marketplace(tuple[1],tuple[2],tuple[0])
            list_marketplaces.append(marketplace)
        return list_marketplaces


def save_marketplace_db(marketplace: Marketplace) -> None:
    try:
        with Connection() as con:
            cursor = con.cursor()
            cursor.execute(f"INSERT INTO marketplace (nome, descricao) values('{marketplace.name}','{marketplace.description}');")
            con.commit()
    except Exception as e:
        print(e)

    
def read_marketplace_db(id: int) -> Marketplace:
    with Connection() as con:
        cursor = con.cursor()
        cursor.execute(f"SELECT * FROM marketplace WHERE id = {id};")
        tuple = cursor.fetchall()[0]
        marketplace = Marketplace(tuple[1], tuple[2], tuple[0])
        return marketplace


def update_marketplace_db(marketplace: Marketplace) -> None:
    with Connection() as con:
        cursor = con.cursor()
        cursor.execute(f"UPDATE marketplace SET nome = '{marketplace.name}', descricao = '{marketplace.description}' WHERE id = {marketplace.id};")
        con.commit()

def delete_marketplace_db(id: int) -> None:
    with Connection() as con:
        cursor = con.cursor()
        cursor.execute(f"DELETE FROM marketplace WHERE id={id};")
        con.commit()
