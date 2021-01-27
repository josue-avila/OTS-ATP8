from backend.dao.db.log_dao import LogDao


class LogController:
    def __init__(self):
        self.__dao = LogDao()

    def save(self, model: object) -> int:
        return self.__dao.save(model)

    def read_all(self) -> list:
        list_all = self.__dao.read_all()
        return list_all
