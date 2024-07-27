import requests
from pprint import pprint


def get_author_other_books(title):
    URL = 'http://www.aladin.co.kr/ttb/api/ItemSearch.aspx'
    params = {
        'ttbkey': '부여받은 TTBKey',
        'Query': {title},
        'QueryType': 'Title',
        'MaxResults': 1,  # 첫 번쩨 도서
        'start': 1,
        'SearchTarget': 'Book',
        'output': 'js',
        'Version': '20131101',
    }
    response = requests.get(URL, params=params).json()
    # print(response)
    """
        response['item'] = 
            [
                {
                    'title': '베니스의 상인', 
                    'link': 'http://www.aladin.co.kr/shop/wproduct.aspx?ItemId=315176143&amp;partner=openAPI&amp;start=api', 
                    'author':  윌리엄 셰익스피어 (지은이), 최종철 (옮긴이)',
                    'pubDate': '2010-12-28', 
                    'description': '민음사 세계문학전집' 262권. 셰익스피어가 32세 무렵이던 1596~1597년에 쓴 비교적 초기 작품으로, 주인공인 '베니스의 상인' 외에도 유대인 샤일록과 지혜로운 여성 포셔까지 모든 인물들의 개성이 돋보이는 희비극이다. 1605년에 초연된 후 지금까지 수없이 공연되었으며, 각각의 인물의 시건으로 다양한 해석이 이루어졌다.'
                    'isbn': '8937462621', 
                    'isbn13': '9788937462627', 
                    'itemId': 8579428, 
                    'priceSales': 8100, 
                    'priceStandard': 9000, 
                    ...
                    'subInfo': {}
                }
            ]
    """

    # 검색 결과가 없는 도서는 None 리턴
    if len(response['item']) == 0:
        return

    # 검색한 도서의 저자 및 isbn
    author = response['item'][0]['author']
    author_name = author.split('(지은이)')[0].strip()
    isbn = response['item'][0]['isbn']

    # 지은이의 다른 작품 검색
    params = {
        'ttbkey': 'ttbsmileever431637001',
        'Query': {author_name},
        'QueryType': 'Author',
        'MaxResults': 10,
        'start': 1,
        'SearchTarget': 'Book',
        'output': 'js',
        'Version': '20131101',
    }
    response = requests.get(URL, params=params).json()

    author_books = response['item']

    # 지은이의 다른 작품 중 검색한 도서를 제외한 도서 제목을 result에 담아 출력
    result = []
    for author_book in author_books:
        if author_book['isbn'] != isbn:
            result.append(author_book['title'])

        if len(result) == 5:
            break

    ouput = {
        f'"{title}"의 저자 "{author_name}"의 다른 도서 목록': result,
    }
    return ouput


# 아래 코드는 수정하지 않습니다.
if __name__ == '__main__':
    pprint(get_author_other_books('베니스의 상인'), width=120)
    pprint(get_author_other_books('죄와 벌'), width=120)
    pprint(get_author_other_books('*'), width=120)
