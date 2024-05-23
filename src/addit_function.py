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
