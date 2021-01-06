# Seller
from backend import write_file
import re

def save_seller(seller,path) -> None:
    print(str(isinstance(seller.get('fullname'), str)) + ";" + str(isinstance(seller.get('phone'), int)) + ";" + str(re.match(r"[^@]+@[^@]+\.[^@]+", seller.get('email'))))

    if isinstance(seller.get('fullname'), str) and seller.get('phone').isdigit() and re.match(r"[^@]+@[^@]+\.[^@]+", seller.get('email')):
        line = f"{seller.get('fullname')};{seller.get('phone')};{seller.get('email')}"
        write_file(path,line)
        create_log("save_seller")
    else:
        raise Exception("Please verify the seller information and try again.")
