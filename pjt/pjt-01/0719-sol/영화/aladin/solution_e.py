import json


def new_books(books):
    result = []
    for book in books:
        books_detail = json.load(
            open(f'data/books/{book["id"]}.json', encoding="utf-8")
        )
        if books_detail["pubDate"][:4] == "2023":
            result.append(books_detail["title"])
    return result


# 아래의 코드는 수정하지 않습니다.
if __name__ == "__main__":
    books_json = open("data/books.json", encoding="utf-8")
    books_list = json.load(books_json)

    print(new_books(books_list))
