import requests
from pprint import pprint


def get_users_books(title):
    # 여기에 코드를 작성합니다.
    URL = 'http://www.aladin.co.kr/ttb/api/ItemSearch.aspx'
    api_key = '알라딘 api 키 입력'

    params = {
    'ttbkey': {api_key},
    'Query': {title},
    'QueryType': 'Title',
    'MaxResults': 1,
    'start': 1,
    'SearchTarget': 'Used',
    'output': 'js',
    'Version': '20131101',
    'OptResult': 'usedList'
    }

    response = requests.get(URL, params=params)
    response = response.json()
    
    # 도서의 검색 결과가 존재한다면 수행할 구문
    try:
        price_sale = response['item'][0]['priceSales'] # 새제품 가격
        used_list = response['item'][0]['subInfo']['usedList']

        used_list_key = list(used_list.keys()) # ['aladinUsed', 'userUsed', 'spaceUsed']

        # 위에서 할당받은 키 값을 이용해 used_list 순회
        used_sale_dict = {}
        for key in used_list_key:
            if used_list[key]['itemCount'] > 0:
                if key == 'aladinUsed':
                    used_sale_dict['알라딘'] = used_list[key]['minPrice'] 
                elif key == 'userUsed':
                    used_sale_dict['회원'] = used_list[key]['minPrice'] 
                elif key == 'spaceUsed':
                    used_sale_dict['광활한 우주점'] = used_list[key]['minPrice'] 

        # 만약 중고 재고가 없을 경우, 새제품 가격을 반환
        if len(used_sale_dict) == 0:
            return f'도서 "{title}"의 중고 재고가 없으며, 새 제품은 {price_sale}원에 판매 중입니다.'
        
        # 중고 재고가 있을 경우
        else:
            # dict 자료형을 튜플로 변환 후 value 값을 기준으로 오름차순 정렬 [('회원', 160), ('광활한 우주점', 5400), ('알라딘', 6700)]
            used_sale_list = sorted(used_sale_dict.items(), key=lambda item: item[1]) 

            # 가장 첫번째 값들을 할당
            offline_bookstore = used_sale_list[0][0]
            offline_price = used_sale_list[0][1]

            return f'도서 "{title}"의 가장 저렴한 중고는 {offline_bookstore}이 보유 중이며, {offline_price}원에 판매 중입니다.'

    # 검색 결과가 없는 경우 수행할 구문
    except IndexError:
        return None
    

# 아래 코드는 수정하지 않습니다.
if __name__ == '__main__':
    pprint(get_users_books('죄와 벌'))
    pprint(get_users_books('로미오와 줄리엣'))
    pprint(get_users_books('*'))

'''
'도서 "죄와 벌"의 가장 저렴한 중고는 회원이 보유 중이며, 5000원에 판매 중입니다.'
'도서 "로미오와 줄리엣"의 가장 저렴한 중고는 회원이 보유 중이며, 3000원에 판매 중입니다.'
None
'''
