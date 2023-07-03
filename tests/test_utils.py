from settings import OPERATIONS_PATH
from app.utils import convert_date, get_operations, get_executed_ops, sort_list_of_5, convert_num


def test_convert_date():
    assert convert_date("2019-08-26T10:50:58.294041") == "26.08.2019"


def test_get_operations():
    assert isinstance(get_operations(OPERATIONS_PATH), list)


def test_get_executed_ops(operations):
    assert(get_executed_ops(operations)) == operations[1:]


def test_sort_list_of_5(operations):
    assert(sort_list_of_5(operations)) == operations[5:]

def test_convert_num():
    assert(convert_num('Visa Platinum 1246377376343588')) == 'Visa Platinum 1246 37** **** 3588'
    assert(convert_num("Счет 14211924144426031657")) == 'Счет **1657'
