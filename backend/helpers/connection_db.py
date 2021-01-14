import psycopg2


class Connection:

    def __connection_string(self) -> str:
        host = 'pgsql08-farm15.uni5.net'
        user = 'topskills11'
        password = 'olist123'
        database = 'topskills11'
        return f'host={host} user={user} dbname={database} password={password}'

    def __enter__(self):
        self.__connection = psycopg2.connect(self.__connection_string())
        return self.__connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__connection.close()
