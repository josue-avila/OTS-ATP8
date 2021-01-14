import datetime as datetime
from backend.helpers.connection_db import *
from backend.models.log import Log


def save_log_db(log: Log) -> None:
    try:
        with Connection() as con:
            cursor = con.cursor()
            cursor.execute(
                f"INSERT INTO logs (timestamp, operacao, descricao) VALUES('{log.timestamp}','{log.operation}', '{log.description}');")
            con.commit()
    except Exception as e:
        print(e)


def read_logs_db() -> list:
    with Connection() as con:
        cursor = con.cursor()
        cursor.execute('SELECT * FROM logs ORDER BY id;')
        result = cursor.fetchall()
        list_logs = []
        for tuple in result:
            log = Log(tuple[2], tuple[3], tuple[0], tuple[1])
            list_logs.append(log)
        return result
