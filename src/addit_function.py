import datetime


def sorting_products(products: list[dict], category: str = "all") -> list[dict] | None:
    """Функция возвращает список словарей, отсортированных по убыванию стоимости продукта,
    но только для продуктов из заданной категории.
    Если категория не задана, то сортировка производится для всех продуктов."""
    sorting_product = []
    # if len(products) == 0:
    #     return None
    if category == "all":
        sorting_product = products
    else:
        category_list = []
        for item in products:
            if item.get("category") not in category_list:
                category_list.append(item.get("category"))
        if category not in category_list:
            return None
        else:
            for item_product in products:
                if item_product["category"] == category:
                    sorting_product.append(item_product)
    return sorted(sorting_product, key=lambda x: x["price"], reverse=True)


def summ_price(sales: list, date_order: str) -> dict:
    """функция суммирует значения в заказах,возвращает среднее значение,
    и количество вхождений."""
    # sales_list = {}
    summ_orders = 0
    count = 0
    for item in sales:
        if item["date"] == date_order:
            # print(item)
            summ_orders += item["sum_orders"]
            count += 1
    avg_price = round(summ_orders / count, 2)
    return dict({"average_order_value": avg_price, "order_count": count})


def sales_statistics(sales: list[dict]) -> dict:
    """Функция должна возвращает словарь, содержащий информацию о средней стоимости заказа
    и количестве заказов за каждый месяц. Ключами словаря должны быть год и месяц в формате
    YYYY-MM , а значениями — словари, содержащие два поля:
    average_order_value — средняя стоимость заказа за месяц,
    order_count— количество заказов за месяц."""
    sales_list: list[dict] = []
    for item in sales:  # фомируем список со словарем вида дата:сумма товаров в заказе
        date_as_mont = (datetime.datetime.strptime(item["date"], "%d.%m.%Y")).strftime("%Y-%m")

        sum_orders = 0
        for order in item["items"]:
            sum_orders = sum_orders + order["price"] * order["quantity"]
        sales_list.append(dict({"date": date_as_mont, "sum_orders": sum_orders}))
        sales_list = sorted(sales_list, key=lambda x: x["date"])

    sales_stat_dic = {}
    date_group_list: list[str] = []  # формируем список месяцев
    for item in sales_list:
        if not item["date"] in date_group_list:
            date_group_list.append(item["date"])

    for dates in date_group_list:
        sales_stat_dic[dates] = summ_price(sales_list, dates)

    return sales_stat_dic
