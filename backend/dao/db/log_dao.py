import datetime as datetime
from backend.helpers.connection_db import *
from backend.models.log import Log


def save_log_db(log: Log):
    try:
        cursor.execute(f"INSERT INTO logs (timestamp, operacao, descricao) VALUES('{log.timestamp}','{log.operation}', '{log.description}');")
        con.commit()
        return True
    except Exception as e:
        return False


def read_logs_db():
    cursor.execute('SELECT * FROM logs;')
    result = cursor.fetchall()
    list_logs = []
    for tuple in result:
        log = Log(tuple[2], tuple[3], tuple[0], tuple[1])
        list_logs.append(log)
    return result
