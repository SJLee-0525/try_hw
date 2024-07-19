import json
from pprint import pprint


def books_info(books, categories):
    result = []
    for book in books:
        categories_name = []
        categoryIds = book["categoryId"]
        for categoryId in categoryIds:
            for category in categories:
                if category["id"] == categoryId:
                    categories_name.append(category["name"])

        tmp = {
            "id": book["id"],
            "title": book["title"],
            "author": book["author"],
            "priceSales": book["priceSales"],
            "description": book["description"],
            "cover": book["cover"],
            "categoryName": categories_name,
        }
        result.append(tmp)
    return result


# 아래의 코드는 수정하지 않습니다.
if __name__ == "__main__":
    books_json = open("data/books.json", encoding="utf-8")
    books = json.load(books_json)

    categories_json = open("data/categories.json", encoding="utf-8")
    categories_list = json.load(categories_json)

    pprint(books_info(books, categories_list))
