import json


def best_new_books(books):
    ''' 상세 json 파일의 이름이 id이므로 books의 id 값들만 리스트에 담음 '''
    books_id_list = []
    for book in books:
        books_id_list.append(book.get('id'))

    # id 리스트와 반복문을 활용해 파일을 열고, 책 제목과 출판 연도, 평점을 담은 tuple을 리스트에 담음
    # [('오만과 편견', '2003', 9.3), ('노인과 바다', '2012', 9.1), ... ('클린 코드 Clean Code - 애자일 소프트웨어 장인 정신', '2013', 8.3)]
    title_pubdate_review_list = []
    for id in books_id_list:
        detailed_info_json = open(f'data/books/{id}.json', encoding='utf-8')
        detailed_info = json.load(detailed_info_json)
        title_pubdate = detailed_info['title'], detailed_info['pubDate'][:4], detailed_info['customerReviewRank']
        title_pubdate_review_list.append(title_pubdate)

    # 출판 연도를 key로, 해당되는 책 제목과 평점을 value로 하는 dict 생성
    # {'2003': [('오만과 편견', 9.3), ('서양미술사', 8.2)], '2012': [('노인과 바다', 9.1)], ... '2013': [('클린 코드 Clean Code - 애자일 소프트웨어 장인 정신', 8.3)]}
    date_title_dict = {}
    for title_pubdate in title_pubdate_review_list:
        title, pubdate, review = title_pubdate
        if pubdate in date_title_dict:
            date_title_dict[pubdate].append((title, review)) # 만약 해당 연도 key가 있을 경우 해당 key에 value 추가
        elif pubdate not in date_title_dict:
            date_title_dict[pubdate] = [(title, review)] # key가 없을 경우, 해당 연도 key를 만들고 value에 책 이름 값 추가
    
    # 찾는 년도의 책 목록을 불러온 후, 평점이 좋은 순으로 정렬
    # [('사피엔스 - 유인원에서 사이보그까지, 인간 역사의 대담하고 위대한 질문', 9.6), ('회복탄력성의 힘 - 쉽게 포기하지 않고 결국 해내는 아이의 비밀', 8.8)]
    find_book_list = date_title_dict['2023']
    find_book_list.sort(key = lambda x:x[1], reverse=True)
    
    return find_book_list[0][0]


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    books_json = open('data/books.json', encoding='utf-8')
    books_list = json.load(books_json)

    print(best_new_books(books_list))

# 사피엔스 - 유인원에서 사이보그까지, 인간 역사의 대담하고 위대한 질문