# Seller
from backend import write_file,create_log
import re

def save_seller(seller,path) -> None:
    if isinstance(seller.get('fullname'), str) and seller.get('phone').isdigit() and re.match(r"[^@]+@[^@]+\.[^@]+", seller.get('email')):
        line = f"{seller.get('fullname')};{seller.get('phone')};{seller.get('email')}"
        write_file(path,line)
        create_log("create_seller")
    else:
        raise Exception("Please verify the seller information and try again.")

def read_sellers() -> list:
    file = open('backend/db/sellers.txt', 'r')
    sellers = []
    for line in file:
        line_by_comas = line.split(';')
        sellers.append(line_by_comas)
        sellers[-1][-1] = sellers[-1][-1].rstrip('\n')
    file.close()
    create_log("read_sellers")
    return sellers