import json


def sorted_cs_books_by_price(books, categories):
    # 카테고리 id를 key로, name을 value로 하는 dict 생성
    # {'과학': 31916, '에세이 / 수필': 31908, '자기계발': 151138, ... 컴퓨터 공학': 2721}
    categories_info = {}
    for category in categories:
        categories_info[category['name']] = category['id']

    # ''' 상세 json 파일의 이름이 id이므로 books의 id 값들만 리스트에 담음 '''
    books_id_list = []
    for book in books:
        books_id_list.append(book.get('id'))

    # id 리스트와 반복문을 활용해 파일을 열고, 책 제목과 카테고리 id, 판매 가격을 담은 tuple을 리스트에 담음
    # [('오만과 편견', [151128, 50919], 11700), ('노인과 바다', [151128, 50919], 7200), ('달과 6펜스', [50919], 9000), ... ('클린 코드 Clean Code - 애자일 소프트웨어 장인 정신', [2721], 29700)]
    title_id_price_list = []
    for id in books_id_list:
        detailed_info_json = open(f'data/books/{id}.json', encoding='utf-8')
        detailed_info = json.load(detailed_info_json)
        # 만약 categoryId가 길이가 없는 int일 경우, 리스트에 넣어줌
        if type(detailed_info['categoryId']) is int:
            category_id = [detailed_info['categoryId']]
        else:
            category_id = detailed_info['categoryId']
        title_pubdate = detailed_info['title'], category_id, detailed_info['priceSales']
        title_id_price_list.append(title_pubdate)

    # 찾고자 하는 카테고리의 id값을 가져옴
    target_id = categories_info['컴퓨터 공학']
    
    # tartet_list의 요소 각각의 id값에 찾는 id가 있는지 확인하고, 있으면 target_list에 제목을 담음
    target_list = []
    for title_id_price in title_id_price_list:
        if target_id in title_id_price[1]:
            target_list.append(title_id_price[0])

    return target_list

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    books_json = open('data/books.json', encoding='utf-8')
    books = json.load(books_json)

    categories_json = open('data/categories.json', encoding='utf-8')
    categories_list = json.load(categories_json)

    print(sorted_cs_books_by_price(books, categories_list))


# ['한 권으로 읽는 컴퓨터 구조와 프로그래밍 - 더 나은 소프트웨어 개발을 위한 하드웨어,
# 자료구조, 필수 알고리즘 등 프로그래머의 비밀 노트',
# '클린 코드 Clean Code - 애자일 소프트웨어 장인 정신']
