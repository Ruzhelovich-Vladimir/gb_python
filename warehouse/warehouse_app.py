"""
Модуль работы c Базой данных "Склад"
"""

import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import qApp
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QFileDialog
from PyQt5 import QtSql
from PyQt5.QtSql import QSqlTableModel
from PyQt5.QtSql import QSqlRelationalTableModel
from PyQt5.QtSql import QSqlRelationalDelegate
from PyQt5.QtSql import QSqlRelation


class Window(QWidget):
    """
    Класс приложения
    """

    def __init__(self, parent=None):
        """
        метод инициализации
        :param parent:
        """
        QWidget.__init__(self, parent)
        uic.loadUi('warehouse_windows_form.ui', self)   # Загрузить форму
        self.btn_quit.clicked.connect(qApp.quit)        # Сигнал выхода
        self.db_path = r'database.sqlite3'              # Путь по умолчанию

        # Назначение кнопки на смену источника данных
        self.db_path_select.clicked.connect(self.get_dialog_file_name)
        self.db_connect(self.db_path)                   # Подключение к базе

        self.tbl_list.itemClicked.connect(
            self.show_tables)  # Изменение таблицы

        self.table_model = QSqlRelationalTableModel()
        self.con = None
        self.edit_flag = False  # Флаг редактирования

        self.add_buttom.clicked.connect(self.add_row_action)
        self.del_buttom.clicked.connect(self.del_row_action)

    def db_connect(self, filename):
        """
        Подключение к источнику данных
        :param filename: Имя файла базы данных
        """
        self.form_db_path.setText(filename)
        self.con = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        self.con.setDatabaseName(self.db_path)

        self.con.open()
        self.show_tbl_list()

    def show_tbl_list(self):
        """Отображение списка таблиц"""

        self.tbl_list.clear()

        for table_name in self.con.tables():
            self.tbl_list.addItem(table_name)

    def show_tables(self):
        """Отображение значений таблицы"""

        self.save_change_db()
        table = self.tbl_list.currentItem().text()  # Наименование таблицы

        if table == 'goods':
            self.show_goods()
        elif table == 'employees':
            self.show_employees()
        elif table == 'vendors':
            self.show_vendors()
        else:
            self.table_model.setTable(table)
            self.table_model.select()
        self.table_model.setEditStrategy(QSqlTableModel.OnManualSubmit)
        view = self.tableView
        view.setModel(self.table_model)
        view.setItemDelegate(QSqlRelationalDelegate(view))

    def show_goods(self):
        """Показать товары"""
        self.table_model.setTable('goods')
        self.table_model.setRelation(2, QSqlRelation('units', 'id', 'name'))
        self.table_model.setRelation(
            3, QSqlRelation(
                'categories', 'id', 'name'))
        self.table_model.select()

    def show_employees(self):
        """Показать сотрудников"""
        self.table_model.setTable('employees')
        self.table_model.setRelation(
            4, QSqlRelation(
                'positions', 'id', 'name'))
        self.table_model.select()

    def show_vendors(self):
        """Показать поставщиков"""
        self.table_model.setTable('vendors')
        self.table_model.setRelation(
            2, QSqlRelation(
                'ownership_form', 'id', 'name'))
        self.table_model.select()


    def add_row_action(self):
        """Добавить строку"""
        self.edit_flag = True
        self.table_model.insertRows(self.table_model.rowCount(), 1)

    def del_row_action(self):
        """Удалит строку"""
        self.edit_flag = True
        rows_for_remove = list(map(lambda x: x.row(), self.tableView.selectedIndexes()))
        for i in rows_for_remove:
            self.table_model.removeRows(i, 1)

    def get_dialog_file_name(self):
        """
        Диалог выбора файла
        :return:
        """
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name, _ = QFileDialog.getOpenFileName(
            self, "QFileDialog.getOpenFileName()", "", "SQLite3 DB (*.sqlite3)", options=options)

        if file_name:
            self.db_connect(file_name)

    def save_change_db(self):
        """Сохранение базы данных"""
        self.table_model.submitAll()


if __name__ == '__main__':
    APP = QApplication(sys.argv)
    WIN = Window()
    WIN.show()
    sys.exit(APP.exec_())
