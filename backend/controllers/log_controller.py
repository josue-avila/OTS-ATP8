from backend.dao.db.log_dao import save_log_db, read_logs_db
from backend.models.log import Log


def save_log(operation: str, description: str) -> None:
    log = Log(operation, description)
    save_log_db(log)


def read_logs() -> list:
    list_log = read_logs_db()
    return list_log
