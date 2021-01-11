import psycopg2

host = 'pgsql08-farm15.uni5.net'
user = 'topskills11'
password = 'olist123'
database = 'topskills11'

connection_string = f'host={host} user={user} dbname={database} password={password}'

con = psycopg2.connect(connection_string)

cursor = con.cursor()

def read_marketplace_db() -> list:
    cursor.execute('SELECT * FROM marketplace')

    marketplaces = cursor.fetchall()
    con.commit()

    return marketplaces

def save_marketplace_db(name: str, description: str) -> None:
    try:
        cursor.execute(f"INSERT INTO marketplace (nome, descricao) values('{name}','{description}');")
        con.commit()
        return True
    except Exception as e:
        return False