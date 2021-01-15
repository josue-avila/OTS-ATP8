import datetime as datetime
from backend.dao.db.base_dao import BaseDao
from backend.models.log import Log


class LogDao(BaseDao):
    def create(self, model: Log) -> None:
        query = f"""INSERT INTO logs (timestamp, operacao, descricao) VALUES('{model.timestamp}','{model.operation}', '{model.description}'); """
        super().execute(query)

    def read_all(self) -> list:
        query = 'SELECT * FROM logs ORDER BY id;'
        result_list = super().read(query)
        logs = []
        for result in result_list:
            log = Log(result[2], result[3], result[0], result[1])
            logs.append(log)
        return logs
