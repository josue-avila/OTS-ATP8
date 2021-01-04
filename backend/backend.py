
def save_marketplces(name:str, description: str) -> None:
    file = open('backend/db/marketplaces.txt','a')
    file.write(f'{name};{description}\n')
    file.close()

def read_products() -> list:
    file = open('backend/db/products.txt', 'r')
    products = []
    for line in file:
        line_by_comas = line.split(';')
        products.append(line_by_comas)
        products[-1][-1] = products[-1][-1].rstrip('\n')
    file.close()
    return products