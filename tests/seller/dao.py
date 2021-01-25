from backend.dao.db.base_dao import BaseDao
from backend.dao.db.seller_dao import SellerDao

seller_dao = SellerDao()

def test_compare_instance_seller_controller_to_basecontroller():
    assert isinstance(seller_dao, BaseDao)