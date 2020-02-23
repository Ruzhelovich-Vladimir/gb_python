"""
1. Написать программу, которая будет содержать функцию для получения
имени файла из полного пути до него. При вызове функции в качестве
аргумента должно передаваться имя файла с расширением. В функции
необходимо реализовать поиск полного пути по имени файла, а затем
«выделение» из этого пути имени файла (без расширения).

На входе программы пользователь должен указать  параметры имя файла
и каталог поиска
"""

import os
import sys


class File:
    """
    Класс работы с файломи
    """
    __slots__ = ["file_name"]

    def __init__(self, file_name):
        """
        Инициалищируем свойства класса файл
        :param file_name: Имя файла
        """
        self.file_name = file_name

    def find(self, find_dir):
        """
        Поиска файла по пути, вывод имени файла без расширения
        :param find_dir: каталог поиска
        """
        flag_stop = False

        for root, dirs, files in os.walk(find_dir):
            for file in files:
                if self.file_name.upper() == file.upper():
                    filename, file_extension = os.path.splitext(file)
                    print(
                        f"Файл {filename} расположен '{root}' c расширением {file_extension}")
                    flag_stop = True  # Флаг прекращения поиска
                    break
            if flag_stop:
                break

        if not flag_stop:
            print(f"Файл {self.file_name} в каталоге {find_dir} не был найден.")


if __name__ == '__main__':
    # Если есть ключ помощи
    if u"/?" in sys.argv or u"/h " in sys.argv:
        print("Поиск файла python task_1.py ИМЯ_ФАЙЛА КАТАЛОГ_ПОИСКА")
    elif len(sys.argv) > 2:
        # Если параметров больше 2, то запускаем поиск
        File(sys.argv[1]).find(sys.argv[2])
    else:
        print("Ошибка. Введит имя фала и каталог поиска или python task_1.py /h или /?")
