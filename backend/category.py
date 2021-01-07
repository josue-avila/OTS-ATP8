from backend import create_log
cat_file = "backend/db/categories.txt"


def salvar_arquivo(caminho:str,linha:str) -> None:
    arquivo = open(caminho,'a')
    arquivo.write(f'{linha}\n')
    arquivo.close()


def add_new_category(name:str, desc:str)->None:  
    if isinstance(name, str) and isinstance(desc, str): 
        linha = f'{name};{desc}'
        salvar_arquivo(cat_file,linha)
    create_log('Cadastrar Categoria')    