from backend.dao.db.base_dao import BaseDao
from backend.dao.db.log_dao import LogDao
from backend.models.log import Log

class BaseController:
    def __init__(self, dao, model_type):
        self.__dao = dao
        self.__logdao = LogDao()
        self.__model_type = model_type

    def create(self, model: object) -> None:
        log = Log('set', self.__model_type)
        self.__logdao.create(log)
        return self.__dao.create(model)

    def read_by_id(self, id: int) -> object:
        log = Log('get', self.__model_type)
        self.__logdao.create(log)
        return self.__dao.read_by_id(id)

    def read_all(self) -> list:
        log = Log('get', f'all {self.__model_type}')
        self.__logdao.create(log)
        return self.__dao.read_all()

    def delete(self, id: int) -> None:
        log = Log('delete', self.__model_type)
        self.__logdao.create(log)
        self.__dao.delete(id)

    def update(self, model: object) -> None:
        log = Log('update', self.__model_type)
        self.__logdao.create(log)
        self.__dao.update(model)
