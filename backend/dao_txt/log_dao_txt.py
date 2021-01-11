import datetime as datetime
from backend.helpers.write_file import *

root = 'backend/logs/logs.txt'


def create_log_txt(type_: str, file_name: str):
    file = open(root, "a")
    data = datetime.datetime.now()
    data_format = data.strftime("%d/%m/%Y %H:%M:%S")
    info = f"{type_};{data_format}=> Acesso a função: {file_name}\n"
    file.write(info)
    file.close()


def read_logs_txt():
    file = open(root, 'r')
    logs = []
    for line in file:
        line_by_space = line.strip().split(';')
        logs.append(line_by_space)
    file.close()
    return logs
