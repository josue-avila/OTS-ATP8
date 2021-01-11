from backend.helpers.write_file import *
cat_file = "backend/db/categories.txt"


# Método de persistência de uma nova categoria no arquivo txt
# name = nome da nova categoria cadastrada
# desc = descrição da nova categoria cadastrada
def add_new_category_txt(name: str, desc: str) -> bool:
    try:
        linha = f'{name};{desc}'
        write_file(cat_file, linha)
        return True
    except Exception as e:
        return False


# Método de consulta de todas as categorias
# gravadas no arquivo categories.txt
def read_categories_txt() -> list:
    file = open('backend/db/categories.txt', 'r')
    categories = []
    for line in file:
        line_by_comas = line.strip().split(';')
        categories.append(line_by_comas)
    file.close()
    return categories


# Método de consulta de um categoria especifica
def search_category_txt(name: str, desc: str):
    categories_list = read_categories_txt()
    categories_names = []
    for cat in categories_list:
        categories_names.append(cat[0])
    if not name in categories_names:
        add_new_category_txt(name, desc)
