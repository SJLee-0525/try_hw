import json


def new_books(books):
    ''' 상세 json 파일의 이름이 id이므로 books의 id 값들만 리스트에 담음 '''
    books_id_list = []
    for book in books:
        books_id_list.append(book.get('id'))

    # id 리스트와 반복문을 활용해 파일을 열고, 책 제목과 출판 연도를 담은 tuple을 리스트에 담음
    # [('오만과 편견', '2003'), ('노인과 바다', '2012'), ('달과 6펜스', '2000'), ... ('클린 코드 Clean Code - 애자일 소프트웨어 장인 정신', '2013')]
    books_title_pubdate_list = []
    for id in books_id_list:
        detailed_info_json = open(f'data/books/{id}.json', encoding='utf-8')
        detailed_info = json.load(detailed_info_json)
        title_pubdate = detailed_info['title'], detailed_info['pubDate'][:4]
        books_title_pubdate_list.append(title_pubdate)

    # 출판 연도를 key로, 해당되는 책 제목을 value로 하는 dict 생성
    # {'2003': '서양미술사', '2012': '노인과 바다', '2000': '고도를 기다리며', ... '2013': '클린 코드 Clean Code - 애자일 소프트웨어 장인 정신'}
    date_title_dict = {}
    for title_pubdate in books_title_pubdate_list:
        title, pubdate = title_pubdate
        if pubdate in date_title_dict:
            date_title_dict[pubdate].append(title) # 만약 해당 연도 key가 있을 경우 해당 key에 value 추가
        elif pubdate not in date_title_dict:
            date_title_dict[pubdate] = [title] # key가 없을 경우, 해당 연도 key를 만들고 value에 책 이름 값 추가
 
    return date_title_dict['2023']


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    books_json = open('data/books.json', encoding='utf-8')
    books_list = json.load(books_json)

    print(new_books(books_list))

# ['회복탄력성의 힘 - 쉽게 포기하지 않고 결국 해내는 아이의 비밀', '사피엔스 - 유인원에서 사이보그까지, 인간 역사의 대담하고 위대한 질문']