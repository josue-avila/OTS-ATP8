import sys
sys.path.append('.')
from backend.dao.log_dao import *
from backend.dao_txt.log_dao_txt import *


def create_log(type_: str, file_name: str) -> None:
    create_log_db(type_, file_name)


def read_logs() -> list:
    list_log = read_logs_db()
    return list_log
