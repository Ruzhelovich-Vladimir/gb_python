"""
2. Написать программу, которая запрашивает у пользователя ввод числа.
На введенное число она отвечает сообщением, целое оно или дробное.
Если дробное — необходимо далее выполнить сравнение чисел до и после
запятой. Если они совпадают, программа должна возвращать значение True,
иначе False.

В этой задачи работаю только со строками, не преобразовывая в числовой формат, т.к. для
больших чисел преобразование работает не корректно.
Например:
self.is_int = float(number) == int(float(number)) - не работает на больших числах
"""


class Number:
    """
    Класс работы с числами
    """
    __slots__ = [
        "number_str",
        "is_number",
        "is_float",
        "is_int",
        "is_float_mirror"]

    def __init__(self, number):
        """
        Инициалищируем свойства класса файл
        :param file_name: Имя файла
        """
        # на всякий случай заменяем "," на ".", если пользователь ввёл через
        # разделить ","
        number = number.replace(
            ",", ".")

        self.is_number = self.is_int = self.is_float_mirror = False
        # Преобразовываем в случае, если параметр будет не строка, убираем
        # лишние пробелы
        self.number_str = str(number).strip()

        if self.str_is_float():
            # Убираем из строки лишние символы, делаем двоёное преобразование
            # (лишние пробелы и нули)
            #self.number_str = str(self.number)
            self.is_number = True

            # Есть в числе есть разлелить дробной части, то если после удаление все лидир. нулей
            # нулей что-то осталось, то число дробное, в противном случае целое
            self.is_int = len(
                self.number_str.split('.')[1].strip("0")) == 0 \
                if len(self.number_str.split('.')) > 1 else True
            # Разбиваем целую и дробную часть,
            # убераем лидирующие нули у целой части, у дробной части только справа
            # т.к. для дробной части они безполезны например 10.10
            # сравниваем эти две строки
            self.is_float_mirror = (self.number_str.split(".")[0].strip(
                "0") == self.number_str.split(".")[1].rstrip("0")) if not self.is_int else False

    def str_is_float(self):
        """
        Проверяет строка является число типа float
        :return: True - строка является лислом, в противном случае False
        """
        try:
            float(self.number_str)
        except ValueError:
            self.is_float = False
        else:
            self.is_float = True

        return self.is_float

    @property
    def get_info_num(self):
        """
        Возращает словарь свойств
        :return:
        """
        return {
            "is_number": self.is_number,
            "is_int": self.is_int,
            "is_float_mirror": self.is_float_mirror}


if __name__ == '__main__':

    INFO = Number(input("Введите число:")).get_info_num
    if not INFO["is_number"]:
        print("Строка не является числом")
    elif INFO["is_int"]:
        print("Строка является целым числом")
    elif INFO["is_float_mirror"]:
        print("Строка является зеркальной десятичной дробью")
    else:
        print("Строка не является зеркальной десятичной дробью")

"""
Результаты работы скрипта:

Введите число:123456780000000000000000000000000000000000000.1234567800000
Строка является зеркальной десятичной дробью

Введите число:23948792384.0
Строка является целым числом

Введите число:число один
Строка не является числом

Введите число:123456.0123456
Строка не является зеркальной десятичной дробью

Введите число:123456,0123456
Строка не является зеркальной десятичной дробью

"""
