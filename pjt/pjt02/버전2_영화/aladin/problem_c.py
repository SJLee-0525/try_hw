import requests
from pprint import pprint


def get_bestseller_books(api_key):
    # 여기에 코드를 작성합니다.
    URL = 'http://www.aladin.co.kr/ttb/api/ItemSearch.aspx'

    params = {
    'ttbkey': {api_key},
    'Query': '파울로 코엘료',
    'QueryType': 'Author',
    'MaxResults': 20,
    'start': 1,
    'SearchTarget': 'Book',
    'output': 'js',
    'Version': '20131101',
    }

    response = requests.get(URL, params=params)
    response = response.json()

    # 보기 쉽게 제목과 판매지수를 key로 하는 dict를 먼저 생성
    title_salespoint_list = []
    for response_i in range(len(response['item'])):
        title_salespoint_list.append({'제목': response['item'][response_i]['title'],
                                      '판매지수': response['item'][response_i]['salesPoint']
                                      })
    
    # 판매지수의 value 값을 이용해서 내림차순 정렬
    sorted_title_salespoint_list = sorted(title_salespoint_list, key=lambda title_salespoint_list: (title_salespoint_list['판매지수']), reverse=True)
    
    # 상위 5개만 return
    return sorted_title_salespoint_list[:5]


# 아래 코드는 수정하지 않습니다.
if __name__ == '__main__':
    api_key = 'ttbyts02751555001'
    pprint(get_bestseller_books(api_key))

'''
[{'제목': '연금술사', '판매지수': 83158},
 {'제목': '11분', '판매지수': 10434},
 {'제목': '브리다', '판매지수': 10372},
 {'제목': '흐르는 강물처럼', '판매지수': 10107},
 {'제목': '포르토벨로의 마녀', '판매지수': 8404}]
'''
