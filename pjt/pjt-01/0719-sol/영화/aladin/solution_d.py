import json


def best_book(books):
    result = ""
    customerReviewRank = 0
    for book in books:
        books_detail = json.load(
            open(f'data/books/{book["id"]}.json', encoding="utf-8")
        )
        if customerReviewRank <= books_detail["customerReviewRank"]:
            customerReviewRank = books_detail["customerReviewRank"]
            result = books_detail["title"]
    return result


# 아래의 코드는 수정하지 않습니다.
if __name__ == "__main__":
    books_json = open("data/books.json", encoding="utf-8")
    books_list = json.load(books_json)

    print(best_book(books_list))
