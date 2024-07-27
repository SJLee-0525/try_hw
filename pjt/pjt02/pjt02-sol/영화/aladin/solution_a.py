import requests
from pprint import pprint


def get_author_books():
    # URL -> 내가 요청을 보내고자 하는 알라딘 주소
    # 알라딘에는 총 3가지 유형의 API가 있다. (상품 검색, 상품 리스트, 상품 조회)
    # 특정 작가, 도서, 출판사 등을 검색하기 위해선 '상품 검색' API를 사용한다.
    URL = 'http://www.aladin.co.kr/ttb/api/ItemSearch.aspx'

    # 예를들어 베스트셀러 도서 경우, 상품 리스트에서 조회할 수 있으며, 이때 TTBKey와 QueryType은 필수다.
    # 파울로 코엘료 작가 검색은 상품 검색에서 조회할 수 있으며, 이때 TTBKey와 Query가 필수다.

    #  `ttbkey`에는 알라딘 회원 가입 후 부여받은 TTBKey 값을 담아 보내야 한다.
    #  'Query'에는 저자이름을 담아 보낸다.
    #  1번 문제의 경우 저자의 도서 20권을 요청해야하므로,옵션 요청 변수 MaxResults 에 20을 담아 보낸다.
    #  output은 xml과 js중 선택할 수 있고, Version은 최신 버전인 20131101를 선택한다.
    #  그 밖의 옵션은 선택적으로 삽입가능하다.

    # 즉, 알라딘에서 파울로 코엘료의 작품 20권 정보를 받아오려면 주소창에
    # 도메인 + Query String Parameter 를 적절히 요청하면된다.
    # 완성된 주소형태
    # 'http://www.aladin.co.kr/ttb/api/ItemSearch.aspx?ttbkey=[부여받은 TTBKey]&Query=파울로 코엘료&QueryType=Author&MaxResults=20&start=1&SearchTarget=Book&output=js&Version=20131101'
    # 여기서 &를 사용해 각자 다른 요구사항을 삽입할 수 있다.

    # 그래서 위와 같이 완성된 주소 전체를 requests에 넘겨주어도 되고,
    # requests를 사용하는 또 다른 방법으로 2번째 인자에
    # params 키워드 인자에 내가 직접 딕셔너리 형태로 요구사항을 작성한 뒤 요청을 보낼 수도 있다.

    # 주의할 점은 여기서도 key 값은 반드시 API 제공 사이트에서 제시하는 이름 그대로 작성할 것
    # ex) 알라딘 공식 문서 의 요청 파라미터 ttbkey와 다른 TTBKey: TTB_Key: 와 같은 형태면 안된다.
    params = {
        'ttbkey': '부여받은 TTBKey',
        'Query': '파울로 코엘료',
        'QueryType': 'Author',
        'MaxResults': 20,
        'start': 1,
        'SearchTarget': 'Book',
        'output': 'js',
        'Version': '20131101',
    }

    # 그렇게 요청 보내 받아온 결과는 requests 타입의 데이터이고, # 파이썬에서 바로 쓸 수 없으며
    response = requests.get(URL, params=params)  # <response [200]>

    # 파이썬에서 쓸 수 있도록 하기 위해 json() 메서드를 사용해
    # json 타입의 데이터를 파이썬의 자료형으로 변환한다.
    response = response.json()
    # 받아온 응답을 보면 item에 파울로 코엘료의 도서 20권에 대한 정보가 담겨있다.
    book_list = response['item']

    # 이 작품 리스트에 있는 도서 정보에서 책 이름을 result에 담아 출력한다.
    result = []

    for book in book_list:
        result.append(book['title'])
    return result


# 아래 코드는 수정하지 않습니다.
if __name__ == '__main__':
    pprint(get_author_books())
