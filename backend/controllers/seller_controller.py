from backend.dao.db.seller_dao import save_seller_db, read_sellers_db, read_seller_db, update_seller_db
from backend.controllers.log_controller import save_log
from backend.models.seller import Seller


def save_seller(seller: Seller) -> None:
    if isinstance(seller.fullname, str) and isinstance(seller.phone, str) and isinstance(seller.email, str):
        save_seller_db(seller)
    save_log('set', 'seller')


def read_sellers() -> list:
    sellers = read_sellers_db()
    save_log('get', 'sellers')
    return sellers


def read_seller(id: int) -> Seller:
    seller = read_seller_db(id)
    save_log('read', 'seller')
    return seller


def update_seller(seller: Seller) -> None:
    new_seller = read_seller(seller.id)
    new_seller.fullname = seller.fullname
    new_seller.phone = seller.phone
    new_seller.email = seller.email
    update_seller_db(new_seller)
    save_log('update', 'seller')
