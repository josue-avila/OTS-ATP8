from backend.controllers.base_controller import BaseController
from backend.dao.db.log_dao import LogDao


class LogController(BaseController):
    def __init__(self):
        self.__dao = LogDao()
        super().__init__(self.__dao)