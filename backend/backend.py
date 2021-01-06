from datetime import datetime

def save_marketplaces(marketplace) -> None:
    file = open('backend/db/marketplaces.txt','a')
    file.write(f'{marketplace.get("name")};{marketplace.get("description")}\n')
    file.close()
    create_log("save_marketplaces")
    

def read_products() -> list:
    file = open('backend/db/products.txt', 'r')
    products = []
    for line in file:
        line_by_comas = line.split(';')
        products.append(line_by_comas)
        products[-1][-1] = products[-1][-1].rstrip('\n')
    file.close()
    create_log("read_products")
    return products

def save_product(product) -> None:
    file = open('backend/db/products.txt','a')
    file.write(f"{product.get('identifier')};{product.get('description')};{product.get('price')}\n")
    file.close()
    create_log("save_product")

def read_marketplaces() -> list:
    file = open('backend/db/marketplaces.txt', 'r')
    mktplaces= []
    for line in file:
        line_by_comas = line.split(';')
        mktplaces.append(line_by_comas)
        mktplaces[-1][-1] = mktplaces[-1][-1].rstrip('\n')
    file.close()
    create_log("read_marketplaces")
    return mktplaces

def create_log(file_name) -> None:
    file = open('backend/logs/logs.txt', "a")
    info = str(datetime.now()) + ' Foi consultado ' + file_name + '\n'
    file.write(info)
    file.close()

def search_mktplace(marketplace):
    marketplaces_list = read_marketplaces()
    marketplaces_names=[]
    for mkt in marketplaces_list:
        marketplaces_names.append(mkt[0])
    if not marketplace.get("name") in marketplaces_names:
        save_marketplaces(marketplace)

#included by Ana - 05/01/2021
def write_file(path: str, line: str) -> None:
    if isinstance(line, str):
        archive = open(path, 'a')
        archive.write(f'{line}\n')
        archive.close()
    else:
        raise Exception("incorrect value")
