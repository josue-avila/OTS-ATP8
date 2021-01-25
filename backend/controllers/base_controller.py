from backend.controllers.log_controller import LogController
from backend.dao.db.base_dao import BaseDao
from backend.models.base_model import BaseModel
from backend.models.log import Log


class BaseController:
    def __init__(self, dao: BaseDao, domain_name: str) -> None:
        self.__dao = dao
        self.__log_controller = LogController()
        self.__domain_name = domain_name

    def create(self, model: BaseModel) -> None:
        self.__dao.save(model)
        log = Log('set', self.__domain_name)
        self.__log_controller.save(log)

    def read_by_id(self, id: int) -> BaseModel:
        result = self.__dao.read_by_id(id)
        log = Log('get', self.__domain_name)
        self.__log_controller.save(log)
        return result

    def read_all(self) -> list:
        result = self.__dao.read_all()
        log = Log('get', f'all {self.__domain_name}')
        self.__log_controller.save(log)
        return result

    def delete(self, id: int) -> None:
        item = self.read_by_id(id)
        self.__dao.delete(item)
        log = Log('delete', self.__domain_name)
        self.__log_controller.save(log)

    def update(self, model: BaseModel) -> None:
        self.__dao.save(model)
        log = Log('update', self.__domain_name)
        self.__log_controller.save(log)

