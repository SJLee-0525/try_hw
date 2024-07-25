import json
from pprint import pprint


def book_info(book, categories):
    categories_names = []
    categoryIds = book["categoryId"]
    for category_id in categoryIds:
        for category in categories:
            if category["id"] == category_id:
                categories_names.append(category["name"])

    result = {
        "id": book["id"],
        "title": book["title"],
        "author": book["author"],
        "priceSales": book["priceSales"],
        "description": book["description"],
        "cover": book["cover"],
        "categoryName": categories_names,
    }
    return result


# 아래의 코드는 수정하지 않습니다.
if __name__ == "__main__":
    book_json = open("data/book.json", encoding="utf-8")
    book = json.load(book_json)

    categories_json = open("data/categories.json", encoding="utf-8")
    categories_list = json.load(categories_json)

    pprint(book_info(book, categories_list))
