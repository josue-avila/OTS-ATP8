from backend.helpers.connection_db import *

def read_sellers_db() -> list:

    cursor.execute('select * from seller')
    sellers = cursor.fetchall()
    con.commit()

    return sellers

def save_seller_db(name: str, phone: str, email: str) -> None:
    try:
        cursor.execute(f"INSERT INTO seller (nome, telefone, email) values('{name}','{phone}','{email}');")
        con.commit()
        return True
    except Exception as e:
        return False