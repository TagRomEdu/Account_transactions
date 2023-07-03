import json
from datetime import datetime
from settings import OPERATIONS_PATH


def get_operations(path) -> list[dict]:
    """
    Читаем файл и возвращаем содержимое в виде списка.
    """
    with open(path, encoding='utf-8') as file:
        return json.load(file)


def get_executed_ops(ops_lst: list[dict]) -> list[dict]:
    """
    Исключаем из списка операций те, что не прошли.
    """
    executed_list = [dictionary for dictionary in ops_lst if dictionary.get('state') == 'EXECUTED']
    return executed_list


def sort_list_of_5(ops_lst: list[dict]) -> list[dict]:
    """
    Сортируем наш список операций по дате от последней и возвращаем первые 5 позиций
    """
    return sorted(ops_lst, key=lambda operation: operation['date'], reverse=True)[:5]


def convert_date(str_date: str) -> str:
    data = datetime.strptime(str_date, '%Y-%m-%dT%H:%M:%S.%f')
    return datetime.strftime(data, '%d.%m.%Y')


def convert_num(str_data: str) -> str:
    lst = str_data.split(' ')
    if len(lst[-1]) == 16:
        a = lst[-1][:4]
        b = lst[-1][4:6]
        c = lst[-1][-4:]
        return f"{a} {b}** **** {c}"
    else:
        return f"**{lst[-1][-4:]}"


print(convert_num(a))

