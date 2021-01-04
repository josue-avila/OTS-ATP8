
def save_marketplces(name:str, description: str) -> None:
    file = open('backend/db/marketplaces.txt','a')
    file.write(f'{name};{description}\n')
    file.close()
