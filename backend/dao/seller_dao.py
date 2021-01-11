import psycopg2

host = 'pgsql08-farm15.uni5.net'
user = 'topskills11'
password = 'olist123'
database = 'topskills11'

connection_string = f'host={host} user={user} dbname={database} password={password}'

con = psycopg2.connect(connection_string)

cursor = con.cursor()

def read_sellers_db() -> list:

    cursor.execute('select * from seller')
    sellers = cursor.fetchall()
    con.commit()

    return sellers

def save_seller_db(name: str, phone: str, email: str) -> None:
    try:
        cursor.execute(f"INSERT INTO seller (nome, telefone, email) values('{name}','{phone}','{email}');")
        con.commit()
        return True
    except Exception as e:
        return False