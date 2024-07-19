import json


def sorted_cs_books_by_price(books, categories):
    result = []

    cs_id = 0
    for category in categories:
        if category["name"] == "컴퓨터 공학":
            cs_id = category["id"]

    cs_books = []
    for book in books:
        categoryIds = book["categoryId"]
        if cs_id in categoryIds:
            cs_books.append(book)

    cs_books.sort(key=lambda book: book["priceSales"], reverse=True)

    for book in cs_books:
        result.append(book["title"])

    return result


# 아래의 코드는 수정하지 않습니다.
if __name__ == "__main__":
    books_json = open("data/books.json", encoding="utf-8")
    books = json.load(books_json)

    categories_json = open("data/categories.json", encoding="utf-8")
    categories_list = json.load(categories_json)

    print(sorted_cs_books_by_price(books, categories_list))
