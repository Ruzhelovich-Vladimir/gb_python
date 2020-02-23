"""
4. Написать программу, в которой реализовать две функции. В первой должен
создаваться простой текстовый файл. Если файл с таким именем уже существует,
выводим соответствующее сообщение. Необходимо открыть файл и подготовить два
списка с текстовой и числовой информацией. Для создания списков использовать
генераторы. Применить к спискам функцию zip(). Результат выполнения этой
функции должен должен быть обработан и записан в файл таким образом, чтобы
каждая строка файла содержала текстовое и числовое значение. Вызвать вторую
функцию. В нее должна передаваться ссылка на созданный файл. Во второй
функции необходимо реализовать открытие файла и простой построчный вывод
содержимого. Вся программа должна запускаться по вызову первой функции.
"""

import os
import random as r


def show_file(file_name):
    """
    Вывод файла на экран
    :param file_name: имя файла
    """

    with open(file_name, 'r', encoding='utf-8') as file:
        for file_str in file.readlines():
            print(file_str)


def create_file(file_name):
    """
    Создание файла
    :param file_name: имя файла
    :return: Имя файла или None
    """

    if os.path.isfile(file_name):
        print(f"Файл - {file_name} уже существует")
        os.remove(file_name)
        return

    length = r.randint(1, 10000)  # Размер списка
    max_int_random = 10000  # Максимальное случайное целое число

    text_list = ["example" for i in range(0, length)]
    number_list = [r.randint(0, max_int_random) for i in range(0, length)]

    cortege = zip(text_list, number_list)

    # Запись в файл
    with open(file_name, 'w', encoding='utf-8') as file:
        file.writelines(f"{elem[0]}\t{str(elem[1])}\n" for elem in cortege)

    show_file(file_name)


if __name__ == '__main__':

    create_file("my.txt")
