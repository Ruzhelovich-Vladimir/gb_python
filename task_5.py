"""
5. Усовершенствовать первую функцию из предыдущего примера. Необходимо во
втором списке часть строковых значений заменить на значения типа example345
(строка+число). Далее — усовершенствовать вторую функцию из предыдущего
примера (функцию извлечения данных). Дополнительно реализовать поиск
определенных подстрок в файле по следующим условиям вывод первого вхождения,
вывод всех вхождений. Реализовать замену всех найденных подстрок на новое
значение и вывод всех подстрок, состоящих из букв и цифр и имеющих пробелы
только в начале и конце — например, example345.

Комментарий:
1.
Концовку задания не совсем понял, по моему она не совсем согласуется
с вышесказанным, сделал отдельную функцию
'
....и вывод всех подстрок, состоящих из букв и цифр и имеющих пробелы
только в начале и конце — например, example345.
'
2.
Для замены и поиска подстраки исспользовал  методы str, т.к. они быстрее,
чеме регулярное выражение.
"""

import os
import random as r
import re


def regular_from_file(file_name, re_str=None, mode="all"):
    """
Вывод    Вывод строк по регулярному выражению
    :param file_name: имя файла
    :param re_str: Строка регулярного выражения
    :param mode: all - применять для всех строк, first - применять для  первой строки
    """
    if mode not in ("all", "first"):
        print("Ошибка.Не корректный параметр mode [all,first]")
        return

    with open(file_name, 'r', encoding='utf-8') as file:
        for file_str in file.readlines():
            # Флаг демонстрациии
            show_flag = re.match(re_str, file_str) is not None
            # Флаг прерывания вывода на экран
            stop_flag = show_flag and mode == "first"
            # Заменяю строку, если задана строка поиска и замены
            if show_flag:
                print(file_str)
            if stop_flag:
                break


def find_from_file(file_name, find_str=None, mode="all", replace_str=None):
    """
    Вывод файла на экран
    :param file_name: имя файла
    :param find_str: - строка поиска
    :param mode: all - применять для всех строк, first - применять для  первой строки
    :param replace_str: значение для замены
    """
    if mode not in ("all", "first"):
        print("Ошибка.Не корректный параметр mode [all,first]")
        return

    with open(file_name, 'r', encoding='utf-8') as file:
        for file_str in file.readlines():
            # Флаг демонстрациии
            show_flag = (file_str.find(find_str) >=
                         0 if find_str is not None else True)
            # Флаг прерывания вывода на экран
            stop_flag = show_flag and mode == "first"
            # Заменяю строку, если задана строка поиска и замены
            if show_flag:
                print((file_str.replace(find_str, replace_str)
                       if len(find_str) > 0 else file_str))
            if stop_flag:
                break


def create_file(
        file_name,
        find_str=None,
        mode="all",
        replace_str=None,
        re_str=None):
    """
    Создание файла
    :param file_name: имя файла
    :param find_str: строка поиска для замены
    :param mode:  all - применять для всех строк, first - применять для  первой строки
    :param replace_str: значение для замены
    :param re_str: регулярное выражение для поиска
   """

    if not os.path.isfile(file_name):

        length = r.randint(1, 20)  # Размер списка
        max_int_random = 10000  # Максимальное случайное целое число

        number_list = [r.randint(0, max_int_random) for i in range(0, length)]

        random_separator = (lambda: ' ' if r.randint(0, 1) == 1
                            else '\t')  # случай разделитель
        # Случайным образом добавляем в текстовое значение число из первого
        # списка
        text_list = [
            f"example{(str(number_list[i]) if r.randint(0, 1) == 1 else '')}"
            f"{random_separator()}" for i in range(0, length)]

        cortege = zip(text_list, number_list)

        # Запись в файл
        with open(file_name, 'w', encoding='utf-8') as file:
            file.writelines(f"{elem[0]}{str(elem[1])}\n" for elem in cortege)
    else:
        print(f"Файл - {file_name} уже существует")

    print("Поиск и замена:")
    find_from_file(file_name, find_str, mode, replace_str)
    print("Поиск по регулярному выражению")
    regular_from_file(file_name, re_str, mode)


if __name__ == '__main__':

    # r"^\s.+\s$" - выдаёт пустой список

    print("*" * 50)
    print("mode=all")
    create_file("my.txt", "1", "all", "*", r"^.+ \d+$")
    print("*" * 50)
    print("mode=first")
    create_file("my.txt", "1", "first", "*", r"^.+ \d+$")

"""
**************************************************
mode=all
Поиск и замена:
example943*	943*
example4*08	4*08
Поиск по регулярному выражению
example9356 9356
example 6545
example3839 3839
example2305 2305
**************************************************
mode=first
Файл - my.txt уже существует
Поиск и замена:
example943*	943*
Поиск по регулярному выражению
example9356 9356
"""
