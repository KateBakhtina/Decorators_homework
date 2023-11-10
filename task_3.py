import csv
import os
import re

from main import parametrized_logger

path = f"{os.getcwd()}\\task_3.log"


@parametrized_logger(path)
def make_cook_book():
    with open(r"data_for_task_3\recipes.txt", encoding="utf-8") as file:
        cook_book = {}
        for dish in file.read().split("\n\n"):
            dish, _, *ingredients = dish.split("\n")
            cook_book.setdefault(dish, [])
            for raw in ingredients:
                ingredient, quantity, measure = raw.split("|")
                cook_book[dish].append(
                    {
                        "ingredient_name": ingredient,
                        "quantity": int(quantity),
                        "measure": measure,
                    }
                )
    return cook_book


@parametrized_logger(path)
def get_shop_list_by_dishes(dishes, person):
    dishes_filter = dict(
        filter(lambda item: item[0] in dishes, make_cook_book().items())
    )
    result = {}
    for value in dishes_filter.values():
        for element in value:
            key, quantity, measure = element.values()
            result.setdefault(key, {"measure": measure, "quantity": 0})
            result[key]["quantity"] += quantity * person
    return result


if __name__ == "__main__":
    get_shop_list_by_dishes(["Запеченный картофель", "Омлет"], 2)
