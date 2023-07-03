import json
from datetime import datetime


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
    """
    Конвертируем дату в формат ДД.ММ.ГГГГ
    """
    data = datetime.strptime(str_date, '%Y-%m-%dT%H:%M:%S.%f')
    return datetime.strftime(data, '%d.%m.%Y')


def convert_num(str_data: str) -> str:
    """
    Шифруем номер карты или счета
    """
    lst = str_data.split(' ')
    if len(lst[-1]) == 16:
        a = lst[-1][:4]
        b = lst[-1][4:6]
        c = lst[-1][-4:]
        return f"{lst[0]} {a} {b}** **** {c}"
    else:
        return f"{lst[0]} **{lst[-1][-4:]}"


def get_amount(operation_amount: dict) -> str:
    """
    Возвращает сумму перевода в нужной валюте
    """
    return f"{operation_amount['operationAmount']['amount']} {operation_amount['operationAmount']['currency']['name']}"


def output_info(ops_list: list[dict]) -> str:
    """
    Выводим информацию на экран
    """
    info_list = []
    for i in range(len(ops_list)):
        date = convert_date(ops_list[i]['date'])
        desc = ops_list[i]['description']
        to_info = convert_num(ops_list[i].get('to'))
        if ops_list[i].get('from') is not None:
            from_info = convert_num(ops_list[i].get('from'))
            info_list.append(f"{date} {desc} \n{from_info} -> {to_info} \n{get_amount(ops_list[i])}")
        else:
            info_list.append(f"{date} {desc} \n-> {to_info} \n{get_amount(ops_list[i])}")
    return '\n\n'.join(info_list)
