import json


def get_operations(path):
    """
    Читаем файл и возвращаем содержимое в виде списка.
    """
    with open(path, encoding='utf-8') as file:
        return json.load(file)
