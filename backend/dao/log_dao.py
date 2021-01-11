import datetime as datetime
import psycopg2

host = 'pgsql08-farm15.uni5.net'
user = 'topskills11'
password = 'olist123'
database = 'topskills11'

connection_string = f'host={host} user={user} dbname={database} password={password}'
con = psycopg2.connect(connection_string)
cursor = con.cursor()


def create_log_db(type_: str, file_name: str):
    try:
        data = datetime.datetime.now()
        data_format = data.strftime("%d/%m/%Y %H:%M:%S")
        info = f"{data_format}=> Acesso a função: {file_name}"
        cursor.execute(f"INSERT INTO logs (operacao, descricao) VALUES('{type_}','{info}');")
        con.commit()
        return True
    except Exception as e:
        return False


def read_logs_db():
    cursor.execute('SELECT * FROM logs;')
    result = cursor.fetchall()
    con.commit()
    return result
