from backend.dao.db.base_dao import BaseDao
from backend.dao.db.product_dao import ProductDao


def test_product_dao_instance():
    product_dao = ProductDao()

    assert isinstance(product_dao, BaseDao)
    assert isinstance(product_dao, ProductDao)
    assert issubclass(ProductDao, BaseDao)
