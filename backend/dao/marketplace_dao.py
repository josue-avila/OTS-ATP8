from backend.helpers.connection_db import *

def read_marketplace_db() -> list:
    cursor.execute('SELECT * FROM marketplace')

    marketplaces = cursor.fetchall()
    con.commit()

    return marketplaces

def save_marketplace_db(name: str, description: str) -> None:
    try:
        cursor.execute(f"INSERT INTO marketplace (nome, descricao) values('{name}','{description}');")
        con.commit()
        return True
    except Exception as e:
        return False