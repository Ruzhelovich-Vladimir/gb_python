"""
Модель базы данных склодского учёта
"""

from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.ext.declarative import declarative_base

BASE = declarative_base()


class OwnershipForm(BASE):
    """
    Таблица форм собственности
    """
    __tablename__ = 'ownership_form'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)

    def __init__(self, name):
        """
        :param name: Наименование
        """
        self.name = name

    def __repr__(self):
        """
        :return: Наименование
        """
        return self.name


class Categories(BASE):
    """
    Таблица категорий товаров
    """
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    description = Column(String(100), nullable=False)

    def __init__(self, name, description):
        """
        :param name: Наименовани
        :param description: Описание
        """
        self.name = name
        self.description = description

    def __repr__(self):
        """
        :return: Наименование
        """
        return self.name


class Units(BASE):
    """
    Таблица едениц измерений товаров
    """
    __tablename__ = 'units'

    id = Column(Integer, primary_key=True)
    name = Column(String(15), nullable=False)
    description = Column(String(50), nullable=False)

    def __init__(self, name, description):
        """
        :param name: Наименование
        :param description: Описание
        """
        self.name = name
        self.description = description

    def __repr__(self):
        """
        :return: Наименование
        """
        return self.name


class Positions(BASE):
    """
    Таблица должностей
    """
    __tablename__ = 'positions'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)

    def __init__(self, name):
        """
        :param name: Наименование
        :param description: Описание
        """
        self.name = name

    def __repr__(self):
        """
        :return: Наименование
        """
        return self.name


class Goods(BASE):
    """
    Таблица Товаров
    """
    __tablename__ = 'goods'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    unit_id = Column(Integer, ForeignKey('units.id'))
    category_id = Column(Integer, ForeignKey('categories.id'))

    def __init__(self, name):
        """
        :param name: Ноименование
        """
        self.name = name

    def __repr__(self):
        """
        :return: Наименование
        """
        return self.name


class Employees(BASE):
    """
    Таблица сотрудников
    """

    __tablename__ = 'employees'

    id = Column(Integer, primary_key=True)
    surname = Column(String(50), nullable=False)                # Фамилия
    first_name = Column(String(50), nullable=False)             # Имя
    patronymic = Column(String(50), nullable=False)             # Отчество
    position_id = Column(Integer, ForeignKey('positions.id'))

    def __init__(self, surname, first_name, patronymic):
        """
        :param surname: Фамилия
        :param first_name: Имя
        :param patronymic: Отчество
        """
        self.surname = surname
        self.first_name = first_name
        self.patronymic = patronymic

    def __repr__(self):
        """
        :return: ФИО
        """
        return f"{self.surname} {self.first_name} {self.patronymic}"


class Vendors(BASE):
    """
    Поставщики
    """
    __tablename__ = 'vendors'

    id = Column(Integer, primary_key=True)
    name = Column(String(150), nullable=False)
    ownership_form_id = Column(Integer, ForeignKey('ownership_form.id'))
    address = Column(String(150))
    phone = Column(String(20))
    email = Column(String(50))

    def __init__(self, name, address, phone, email):
        """
        :param name: Наименование
        """
        self.name = name
        self.address = address
        self.phone = phone
        self.email = email

    def __repr__(self):
        """
        :return: Наименнование
        """
        return self.name
