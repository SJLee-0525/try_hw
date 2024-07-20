import json


def best_book(books):
    ''' 상세 json 파일의 이름이 id이므로 books의 id 값들만 리스트에 담음 '''
    books_id_list = []
    for book in books:
        books_id_list.append(book.get('id'))

    ''' id 리스트와 반복문을 활용해 파일을 열고, 책 제목을 key로, 평점을 value로 하는 tuple 요소를 담는 리스트 생성
    [('오만과 편견', 9.3), ('노인과 바다', 9.1), ('달과 6펜스', 8.5), ... ('클린 코드 Clean Code - 애자일 소프트웨어 장인 정신', 8.3)] '''
    books_title_review_list = []
    for id in books_id_list:
        detailed_info_json = open(f'data/books/{id}.json', encoding='utf-8')
        detailed_info = json.load(detailed_info_json)
        title_review = detailed_info['title'], detailed_info['customerReviewRank']
        books_title_review_list.append(title_review)

    # id 리스트와 반복문을 활용해 파일을 열고, 책 제목을 key로, 평점을 value로 하는 dict 생성
    # {'오만과 편견': 9.3, '노인과 바다': 9.1, '달과 6펜스': 8.5, ... '클린 코드 Clean Code - 애자일 소프트웨어 장인 정신': 8.3}
    # review_rank = {}
    # for id in books_id_list:
    #     detailed_info_json = open(f'data/books/{id}.json', encoding='utf-8')
    #     detailed_info = json.load(detailed_info_json)
    #     review_rank[detailed_info['title']] = detailed_info['customerReviewRank']
    

    ''' books_title_review_list 내부 튜플의 2번째 요소를 기준으로 정렬
    # [('멋진 신세계', 9.9), ('이방인', 9.7), ('정의란 무엇인가', 9.7), ... ('고도를 기다리며', 8.1)] '''
    books_title_review_list.sort(key = lambda x:x[1], reverse=True)
    
    most_populer_book = books_title_review_list[0][0]
    
    return most_populer_book


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    books_json = open('data/books.json', encoding='utf-8')
    books_list = json.load(books_json)

    print(best_book(books_list))
