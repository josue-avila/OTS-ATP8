import sys
sys.path.append('')

from backend.helpers.write_file import *

root = 'backend/files/marketplaces.txt'

def read_marketplaces_txt() -> list:
    file = open(root, 'r')
    marketplaces = []
    for line in file:
        line_by_comas = line.strip().split(';')
        marketplaces.append(line_by_comas)
    file.close()
    return marketplaces

def save_marketplace_txt(name, description) -> None:
    line = f"{name};{description}"
    write_file(root, line)