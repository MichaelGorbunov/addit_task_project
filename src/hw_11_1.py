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
# print(lambda x: x + 2, [-1, 2, -3])
# list(my_map(lambda x: x + 2, [-1, 2, -3]))  # [1, 4, -1]
# list(my_filter(lambda x: x % 2 == 1, range(10)))  # [1, 3, 5, 7, 9]
# list(replicate_each(1, [1, 'a']))  # [1, 'a']
# list(replicate_each(3, [1, 'a']))  # [1, 1, 1, 'a', 'a', 'a']
# list(replicate_each(0, [1, 'a']))  # []