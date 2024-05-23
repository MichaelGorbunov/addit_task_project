# Проект дополнительных заданий к домашним работам



## Установка:

1. Клонируйте репозиторий:
```
git clone https://github.com/MichaelGorbunov/bank_app.git
```
2. Установите зависимости:
```
poetry install
```
## Реализованные функции:

1. **sales_statistics**  Функция возвращает словарь, содержащий информацию о средней стоимости заказа
    и количестве заказов за каждый месяц. Ключами словаря должны быть год и месяц в формате
    YYYY-MM , а значениями — словари, содержащие два поля:
    average_order_value — средняя стоимость заказа за месяц,
    order_count— количество заказов за месяц.
2. **sorting_products**  Функция возвращает список словарей, отсортированных по убыванию стоимости продукта,
    но только для продуктов из заданной категории.
    Если категория не задана, то сортировка производится для всех продуктов.


## Лицензия:

Этот проект можно использовать безвозмездно для любых, 
не противоречащих законодательству целей.