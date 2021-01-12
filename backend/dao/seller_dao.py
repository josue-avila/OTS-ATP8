from backend.helpers.connection_db import *
from backend.models.seller import Seller


def read_sellers_db() -> list:

    cursor.execute('select * from seller')
    sellers = cursor.fetchall()
    list_sellers = []
    for tuple in sellers:
        seller = Seller(tuple[1], tuple[2], tuple[3], tuple[0])
        list_sellers.append(seller)
    return list_sellers

def save_seller_db(seller: Seller) -> None:
    try:
        cursor.execute(f"INSERT INTO seller (nome, telefone, email) values('{seller.fullname}','{seller.phone}','{seller.email}');")
        con.commit()
        print("save seller")
        return True
    except Exception as e:
        return False