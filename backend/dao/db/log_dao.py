from backend.dao.db.base_dao import BaseDao
from backend.models.log import Log


class LogDao(BaseDao):
    def __init__(self):
        super().__init__(Log)