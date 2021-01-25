from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class Session:
    def __init__(self) -> None:
        host = 'pgsql08-farm15.uni5.net'
        user = 'topskills11'
        password = 'olist123'
        database = 'topskills11'
        self.__connection_string = f'postgresql://{user}:{password}@{host}:5432/{database}'

    def __enter__(self):
        self.__engine = create_engine(self.__connection_string)
        S = sessionmaker(self.__engine)
        self.__session = S()
        return self.__session

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__session.close()
        self.__engine.dispose()
