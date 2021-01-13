from backend.helpers.write_file import *

root = 'backend/files/marketplaces.txt'


def read_marketplaces_txt() -> list:
    marketplaces = []
    with open(root, 'r') as file:
        for line in file:
            line_by_comas = line.strip().split(';')
            marketplaces.append(line_by_comas)
    return marketplaces


def save_marketplace_txt(name, description) -> None:
    line = f"{name};{description}"
    write_file(root, line)
