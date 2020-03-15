"""
Решил скопировать данный модуль, немного его модифицировал,
что бы исспользовал модель

Репозиторий (скрипт управления хранилищем данных)
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import models

PATH_DB = 'database.sqlite3'


class Repository:
    """Репозиторий"""

    def __init__(self, path_db, base):
        """
        Инициализируем базу
        :param path_db: относительный пусть и имя базы данных базы данных
        """
        self.engine = create_engine(
            f'sqlite:///{path_db}?check_same_thread=False')
        self.create_base(base)  # Создаём базу
        self.session = self.get_session()

    def create_base(self, base):
        """Создаем БД"""
        #base = declarative_base()
        base.metadata.create_all(self.engine)

    def get_session(self):
        """Создаем объект сессии"""
        session = sessionmaker(bind=self.engine)
        session = session()
        return session


if __name__ == '__main__':
    REP = Repository(PATH_DB, models.BASE)
