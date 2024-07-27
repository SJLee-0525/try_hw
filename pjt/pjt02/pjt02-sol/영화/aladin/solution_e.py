import requests
from pprint import pprint


def get_users_books(title):
    URL = 'http://www.aladin.co.kr/ttb/api/ItemSearch.aspx'
    params = {
        'ttbkey': '부여받은 TTBKey',
        'Query': {title},
        'QueryType': 'Title',
        'MaxResults': 1,
        'start': 1,
        'SearchTarget': 'Book',
        'output': 'js',
        'Version': '20131101',
        'OptResult': 'usedList',  # 중고서적 조회
    }
    response = requests.get(URL, params=params).json()

    # 검색 결과가 없는 도서는 None 리턴
    if len(response['item']) == 0:
        return

    price = response['item'][0]['priceSales']
    used_list = response['item'][0]['subInfo']['usedList']

    result_place = ''
    result_price = 0
    for _ in used_list:
        if (
            used_list.get('aladinUsed')
            and used_list.get('aladinUsed').get('itemCount') > 0
        ):
            if result_price < used_list['aladinUsed']['minPrice']:
                result_price = used_list['aladinUsed']['minPrice']
                result_place = '알라딘'
        if (
            used_list.get('userUsed')
            and used_list.get('userUsed').get('itemCount') > 0
        ):
            if result_price < used_list['userUsed']['minPrice']:
                result_price = used_list['userUsed']['minPrice']
                result_place = '회원'
        if (
            used_list.get('spaceUsed')
            and used_list.get('spaceUsed').get('itemCount') > 0
        ):
            if result_price < used_list['spaceUsed']['minPrice']:
                result_price = used_list['spaceUsed']['minPrice']
                result_place = '광활한 우주점'
        if result_price == 0:
            result_price = price
            return f'도서 "{title}"의 중고 재고가 없으며, 새 제품은 {result_price}원에 판매 중입니다.'
    return f'도서 "{title}"의 가장 저렴한 중고는 {result_place}이 보유 중이며, {result_price}원에 판매 중입니다.'


# 아래 코드는 수정하지 않습니다.
if __name__ == '__main__':
    pprint(get_users_books('죄와 벌'))
    pprint(get_users_books('로미오와 줄리엣'))
    pprint(get_users_books('*'))
