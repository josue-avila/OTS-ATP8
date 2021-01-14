from backend.helpers.connection_db import *
from backend.models.seller import Seller


def read_sellers_db() -> list:
    with Connection() as con:
        cursor = con.cursor()
        cursor.execute('SELECT * FROM seller ORDER BY id')
        sellers = cursor.fetchall()
        list_sellers = []
        for tuple in sellers:
            seller = Seller(tuple[1], tuple[2], tuple[3], tuple[0])
            list_sellers.append(seller)
        return list_sellers


def save_seller_db(seller: Seller) -> None:
    try:
        with Connection() as con:
            cursor = con.cursor()
            cursor.execute(f"INSERT INTO seller (nome, telefone, email) values('{seller.fullname}','{seller.phone}','{seller.email}');")
            con.commit()
    except Exception as e:
        print(e)


def read_seller_db(id: int) -> Seller:
    with Connection() as con:
        cursor = con.cursor()
        cursor.execute(f"SELECT * FROM seller WHERE id = {id};")
        tuple = cursor.fetchall()[0]
        seller = Seller(tuple[1], tuple[2], tuple[3], tuple[0])
        return seller


def update_seller_db(seller: Seller) -> None:
    with Connection() as con:
        cursor = con.cursor()
        cursor.execute(f"UPDATE seller SET nome = '{seller.fullname}', telefone = '{seller.phone}', email = '{seller.email}' WHERE id = {seller.id};")
        con.commit()


def delete_seller_db(id: int) -> None:
    with Connection() as con:
        cursor = con.cursor()
        cursor.execute(f"DELETE FROM seller WHERE id={id};")
        con.commit()
