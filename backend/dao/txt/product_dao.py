root = 'backend/files/products.txt'


# Método de persistência de um novo produto no arquivo txt
# product = objeto contendo os parâmetros identifier, description, price
def save_product_txt(product):
    with open(root, 'a') as file:
        file.write(
            f"{product.get('identifier')};{product.get('description')};{product.get('price')}\n"
        )


# Método de consulta de todos os produtos
# gravadas no arquivo products.txt
def read_products_txt() -> list:
    products = []
    with open(root, 'r') as file:
        for line in file:
            line_by_comas = line.strip().split(';')
            products.append(line_by_comas)
    return products
