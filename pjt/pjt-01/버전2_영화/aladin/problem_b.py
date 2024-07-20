import json
from pprint import pprint


def book_info(book, categories):
    # 카테고리 id를 key로, name을 value로 하는 dict 생성
    categories_info = {}
    for category in categories:
        categories_info[category['id']] = category['name']
    # {31916: '과학', 31908: '에세이 / 수필', 151138: '자기계발', ... 51449: '윤리학', 2721: '컴퓨터 공학'}

    # categoryId의 id 값을 name 값으로 바꾸기
    for i in range(len(book['categoryId'])):
        book['categoryId'][i] = categories_info[book['categoryId'][i]]

    new_book_info = {
        'id': book.get('id'),
        'title': book.get('title'),
        'author': book.get('author'),
        'priceSales':  book.get('priceSales'),
        'description': book.get('description'),
        'cover': book.get('cover'),
        'categoryName': book.get('categoryId'),
    }
    
    return new_book_info


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    book_json = open('data/book.json', encoding='utf-8')
    book = json.load(book_json)

    categories_json = open('data/categories.json', encoding='utf-8')
    categories_list = json.load(categories_json)

    pprint(book_info(book, categories_list))

# {'author': '어니스트 헤밍웨이 (지은이), 김욱동 (옮긴이)',
#  'categoryName': ['문학', '영미소설'],
#  'cover': 'https://image.aladin.co.kr/product/1452/24/coversum/8937462788_2.jpg',
#  'description': '노벨 문학상, 퓰리처상 수상 작가, 20세기 미국 문학을 개척한 작가 어니스트 헤밍웨이의 대표작. 미국 현대 '
#                 "문학의 개척자라 불리는 헤밍웨이는 제1차 세계대전 후 삶의 좌표를 잃어버린 '길 잃은 세대'를 대표하는 "
#                 "작가이다. '민음사 세계문학전집' 278권으로 출간된 &lt;노인과 바다&gt;는 헤밍웨이의 마지막 소설로, "
#                 '작가 고유의 소설 수법과 실존 철학이 짧은 분량 안에 집약되어 있다.',
#  'id': 14522431,
#  'priceSales': 7200,
#  'title': '노인과 바다'}