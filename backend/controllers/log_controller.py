import sys
sys.path.append('.')
from backend.dao.log_dao import *
from backend.dao_txt.log_dao_txt import *


def save_log(operation: str, description: str) -> None:
    log = Log(operation, description)
    save_log_db(log)


def read_logs() -> list:
    list_log = read_logs_db()
    return list_log
