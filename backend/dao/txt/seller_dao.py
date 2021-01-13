from backend.helpers.write_file import *

root = './backend/files/sellers.txt'


def read_sellers_txt() -> list:
    sellers = []
    with open(root, 'r') as file:
        for line in file:
            line_by_comas = line.strip().split(';')
            sellers.append(line_by_comas)
    return sellers


def save_seller_txt(name, phone, email) -> None:
    line = f"{name};{phone};{email}"
    write_file(root, line)
