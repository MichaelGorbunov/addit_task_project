from typing import Any


def non_empty_truths(val: list[Any]) -> list[Any]:
    """функция очищает список от пустых,нулеых, и false значений"""
    if not isinstance(val, list):
        return val

    return [x for x in map(non_empty_truths, val) if x]


#
# y=(lambda x: x + 2, [-1, 2, -3])
# def my_map(f:str, xs:list):
#     return list(map(f, xs))
#
# my_map("lambda x: x + 2", [-1, 2, -3])
