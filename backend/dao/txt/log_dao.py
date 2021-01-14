import datetime as datetime
from backend.helpers.write_file import *

root = 'backend/logs/logs.txt'


def save_log_txt(type_: str, file_name: str):
    with open(root, "a") as file:
        data = datetime.datetime.now()
        data_format = data.strftime("%d/%m/%Y %H:%M:%S")
        info = f"{type_};{data_format}=> Acesso a função: {file_name}\n"
        file.write(info)


def read_logs_txt():
    logs = []
    with open(root, 'r') as file:
        for line in file:
            line_by_space = line.strip().split(';')
            logs.append(line_by_space)
    return logs
