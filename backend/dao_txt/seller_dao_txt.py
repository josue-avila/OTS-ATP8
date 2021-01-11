import sys
sys.path.append('.')

from backend.helpers.write_file import *

root = './backend/db/sellers.txt'

def read_sellers_txt() -> list:
    file = open(root, 'r')
    sellers = []
    for line in file:
        line_by_comas = line.strip().split(';')
        sellers.append(line_by_comas)
    file.close()
    return sellers

def save_seller_txt(name, phone, email) -> None:
    line = f"{name};{phone};{email}"
    write_file(root, line)