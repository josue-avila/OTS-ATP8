from backend.dao.db.log_dao import LogDao
from backend.dao.db.base_dao import BaseDao


def test_log_dao_instance():
    log_dao = LogDao()

    assert isinstance(log_dao, BaseDao)
    assert isinstance(log_dao, LogDao)

