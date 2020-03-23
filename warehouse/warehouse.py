#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Импорт модулей
import sys
from PyQt5.QtWidgets import QMainWindow, QAction, QApplication

class CatalogMainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)

        # Структура главного окна
        # Создаем меню
        self.menu_bar = self.menuBar()

        # Создаем блоки меню
        # Блок меню 'Учет движения товаров'
        self.gma_menu = self.menu_bar.addMenu('Учет движения товаров')
        self.ro_open_btn = QAction(self)
        self.ro_open_btn.setText('Приходный ордер')
        self.wo_open_btn = QAction(self)
        self.wo_open_btn.setText('Расходный ордер')
        self.gma_menu.addAction(self.ro_open_btn)
        self.gma_menu.addAction(self.wo_open_btn)

# Отобразить главное окно
if __name__ == "__main__":
    app = QApplication(sys.argv)
    CMW = CatalogMainWindow()
    CMW.setWindowTitle('Складской учет')
    CMW.setFixedSize(1200, 800)
    CMW.show()
    sys.exit(app.exec_())
