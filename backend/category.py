from backend import create_log, write_file
cat_file = "backend/db/categories.txt"

def add_new_category(name:str, desc:str)->None:  
    if isinstance(name, str) and isinstance(desc, str): 
        linha = f'{name};{desc}'
        write_file(cat_file,linha)
    create_log('create_category')    

def read_categories() -> list:
    file = open('backend/db/categories.txt', 'r')
    categories = []
    for line in file:
        line_by_comas = line.split(';')
        categories.append(line_by_comas)
        categories[-1][-1] = categories[-1][-1].rstrip('\n')
    file.close()
    create_log("read_categories")
    return categories


def search_category(name:str, desc:str):
    categories_list = read_categories()
    categories_names=[]
    for cat in categories_list:
        categories_names.append(cat[0])
    if not name in categories_names:
        add_new_category(name, desc)
