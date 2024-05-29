from typing import Any

from src.hw_11_1 import my_filter, my_map, non_empty_truths, replicate_each

m: list[Any] = [[], [[], []], [[0]], [[0, ""], [False, None]], [[0, 1, 2], [], [], [False, True, 42]]]
for item in m:
    print(non_empty_truths(item))

print(list(my_map(lambda x: x + 2, [-1, 2, -3])))
print(list(my_filter(lambda x: x % 2 == 1, range(10))))
print(list(replicate_each(3, [1, "a"])))


# from src.addit_function import sales_statistics, sorting_products
#
# # тест функции sorting_product
# products = [
#     {"name": "Apple", "category": "fruit", "price": 120, "quantity": 10},
#     {"name": "Banana", "category": "fruit", "price": 90, "quantity": 15},
#     {"name": "Avocado", "category": "fruit", "price": 200, "quantity": 5},
#     {"name": "Tomato", "category": "veggie", "price": 100, "quantity": 20},
#     {"name": "Broccoli", "category": "veggie", "price": 300, "quantity": 8},
#     {"name": "Carrot", "category": "veggie", "price": 100, "quantity": 25},
#     {"name": "Cookie", "category": "sweets", "price": 200, "quantity": 12, "brand": "ABC"},
#     {"name": "Donut", "category": "sweets", "price": 300, "quantity": 7, "brand": "XYZ"},
#     {"name": "Cake", "category": "sweets", "price": 400, "quantity": 3, "brand": "DEF", "discount": 10},
#     {"name": "Orange", "category": "fruit", "price": 150, "quantity": 18},
#     {"name": "Lettuce", "category": "veggie", "price": 80, "quantity": 30, "organic": True},
#     {"name": "Chocolate", "category": "sweets", "price": 250, "quantity": 10, "brand": "GHI", "flavor": "Dark"},
# ]
#
# print(sorting_products(products, "veggie"))
# print(sorting_products(products, "banana"))
# print(sorting_products(products))
# # end this test
#
# # тест функции sales_statistics
# list1 = [
#     {
#         "id": 1,
#         "date": "01.01.2024",
#         "items": [
#             {"name": "tovar1", "price": 10.5, "quantity": 1},
#             {"name": "tovar3", "price": 10.6, "quantity": 1},
#             {"name": "tovar5", "price": 10.2, "quantity": 2},
#         ],
#     },
#     {
#         "id": 2,
#         "date": "01.02.2024",
#         "items": [{"name": "tovar2", "price": 10.5, "quantity": 2},
#         {"name": "tovar8", "price": 10.3, "quantity": 1}],
#     },
#     {"id": 3, "date": "01.03.2024", "items": [{"name": "tovar3", "price": 10.6, "quantity": 1}]},
#     {"id": 4, "date": "01.04.2024", "items": [{"name": "tovar1", "price": 10.5, "quantity": 3}]},
#     {"id": 5, "date": "01.05.2024", "items": [{"name": "tovar2", "price": 10.7, "quantity": 1}]},
#     {"id": 6, "date": "01.06.2024", "items": [{"name": "tovar1", "price": 10.5, "quantity": 1}]},
#     {
#         "id": 7,
#         "date": "01.07.2024",
#         "items": [{"name": "tovar5", "price": 10.2, "quantity": 2},
#         {"name": "tovar8", "price": 10.3, "quantity": 1}],
#     },
#     {"id": 8, "date": "01.08.2024", "items": [{"name": "tovar1", "price": 10.5, "quantity": 1}]},
#     {
#         "id": 9,
#         "date": "01.09.2024",
#         "items": [
#             {"name": "tovar8", "price": 10.3, "quantity": 1},
#             {"name": "tovar7", "price": 10.5, "quantity": 1},
#             {"name": "tovar15", "price": 10.5, "quantity": 2},
#         ],
#     },
#     {"id": 10, "date": "01.01.2024", "items": [{"name": "tovar1", "price": 10.5, "quantity": 1}]},
#     {
#         "id": 11,
#         "date": "01.02.2024",
#         "items": [{"name": "tovar1", "price": 10.4, "quantity": 2},
#         {"name": "tovar7", "price": 10.5, "quantity": 1}],
#     },
#     {"id": 12, "date": "01.03.2024", "items": [{"name": "tovar7", "price": 10.5, "quantity": 1}]},
#     {
#         "id": 13,
#         "date": "01.04.2024",
#         "items": [{"name": "tovar1", "price": 10.9, "quantity": 5},
#         {"name": "tovar15", "price": 10.5, "quantity": 2}],
#     },
#     {"id": 14, "date": "01.01.2024", "items": [{"name": "tovar11", "price": 10.8, "quantity": 1}]},
#     {
#         "id": 15,
#         "date": "01.09.2024",
#         "items": [
#             {"name": "tovar12", "price": 10.5, "quantity": 1},
#             {"name": "tovar12", "price": 10.5, "quantity": 1},
#         ],
#     },
#     {"id": 16, "date": "01.11.2024", "items": [{"name": "tovar7", "price": 10.6, "quantity": 5}]},
#     {"id": 17, "date": "01.12.2024", "items": [{"name": "tovar18", "price": 10.5, "quantity": 1}]},
#     {"id": 18, "date": "01.08.2024", "items": [{"name": "tovar1", "price": 10.7, "quantity": 1}]},
#     {"id": 19, "date": "01.07.2024", "items": [{"name": "tovar15", "price": 10.5, "quantity": 2}]},
#     {
#         "id": 20,
#         "date": "01.01.2024",
#         "items": [{"name": "tovar9", "price": 102, "quantity": 8},
#         {"name": "tovar12", "price": 10.5, "quantity": 1}],
#     },
#     {"id": 21, "date": "01.02.2024", "items": [{"name": "tovar8", "price": 10.1, "quantity": 1}]},
#     {"id": 22, "date": "01.03.2024", "items": [{"name": "tovar7", "price": 10.3, "quantity": 1}]},
#     {"id": 23, "date": "01.04.2024", "items": [{"name": "tovar11", "price": 10.2, "quantity": 2}]},
# ]
#
# print(sales_statistics(list1))
# # end this test
#
#
