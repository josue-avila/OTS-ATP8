from backend.dao.db.base_dao import BaseDao
from backend.dao.db.category_dao import CategoryDao


def test_category_dao_instance():
    category_dao = CategoryDao()

    assert isinstance(category_dao, BaseDao)
    assert isinstance(category_dao, CategoryDao)
