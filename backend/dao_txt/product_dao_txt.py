root = 'backend/db/products.txt'


# Método de persistência de um novo produto no arquivo txt
# product = objeto contendo os parâmetros identifier, description, price
def save_product_txt(product):
    file = open(root, 'a')
    file.write(
        f"{product.get('identifier')};{product.get('description')};{product.get('price')}\n")
    file.close()


# Método de consulta de todos os produtos
# gravadas no arquivo products.txt
def read_products_txt() -> list:
    file = open(root, 'r')
    products = []
    for line in file:
        line_by_comas = line.strip().split(';')
        products.append(line_by_comas)
    file.close()
    return products
