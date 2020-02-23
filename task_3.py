"""
3. Создать два списка с различным количеством элементов. В первом должны
быть записаны ключи, во втором — значения. Необходимо написать функцию,
создающую из данных ключей и значений словарь. Если ключу не хватает
значения, в словаре для него должно сохраняться значение None. Значения,
которым не хватило ключей, необходимо отбросить.
"""


def create_dict(keys, values):
    """
    Создания словаря на основе списков
    :param keys: ключи
    :param values: значения
    :return: словарь
    """

    return {keys[i]: values[i] if i < len(
        values) else None for i in range(0, len(keys))}


if __name__ == '__main__':

    KEYS = ["key1", "key2", "key3", "key4", "key5", "key6", "key7", "key8"]
    VALUES = ["Value1", "Value2", "Value3"]

    print(f"Результат - {create_dict(KEYS,VALUES)}")

"""
Результат - {'key1': 'Value1', 'key2': 'Value2', 'key3': 'Value3', 'key4': None, 'key5': None, 'key6': None, 'key7': None, 'key8': None}
"""
