from typing import Any


def non_empty_truths(val: list[Any]) -> list[Any]:
    """функция очищает список от пустых,нулевых, и false значений"""
    if not isinstance(val, list):
        return val

    return [x for x in map(non_empty_truths, val) if x]


def my_map(func, value_list):
    """упрощенная map"""
    return map(func, value_list)


def my_filter(func, range_value):
    """упрощенный фильтр"""
    return filter(func, range_value)


def replicate_each(number, value_list):
    """умножитель списков"""
    return value_list * number
