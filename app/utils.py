import json
from settings import OPERATIONS_PATH


def get_operations(path) -> list[dict]:
    """
    Читаем файл и возвращаем содержимое в виде списка.
    """
    with open(path, encoding='utf-8') as file:
        return json.load(file)


def get_executed_ops(ops_lst: list[dict]) -> list[dict]:
    executed_list = [dictionary for dictionary in ops_lst if dictionary.get('state') == 'EXECUTED']
    return executed_list


def sort_list(ops_lst: list[dict]) -> list[dict]:
    return sorted(ops_lst, key=lambda operation: operation['date'], reverse=True)

"""a = get_operations(OPERATIONS_PATH)
print(sort_list(get_executed_ops(a))[0:5])"""
