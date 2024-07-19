import json


def best_new_books(books):
    best_review_book = ""
    best_review = 0
    for book in books:
        books_detail = json.load(
            open(f'data/books/{book["id"]}.json', encoding="utf-8")
        )
        if (
            books_detail["pubDate"][:4] == "2023"
            and best_review < books_detail["customerReviewRank"]
        ):
            best_review = books_detail["customerReviewRank"]
            best_review_book = books_detail["title"]

    return best_review_book


# 아래의 코드는 수정하지 않습니다.
if __name__ == "__main__":
    books_json = open("data/books.json", encoding="utf-8")
    books_list = json.load(books_json)

    print(best_new_books(books_list))
