import requests
from pprint import pprint


def get_users_books(title):
    # 여기에 코드를 작성합니다.
    URL = 'http://www.aladin.co.kr/ttb/api/ItemSearch.aspx'
    api_key = 'ttbyts02751555001'

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

    used_response = requests.get(URL, params=params)
    used_response = used_response.json()
    return used_response

    # try:
    #     ISBN = used_response['item'][0]['isbn']
    #     Used_URL = f'http://www.aladin.co.kr/ttb/api/ItemOffStoreList.aspx?ttbkey={api_key}&itemIdType=ISBN&ItemId={ISBN}&output=xml'
        
    #     try:
    #         find_used_response = requests.get(Used_URL)
    #         find_used_response = find_used_response.json()

    #         return find_used_response
        
    #     except requests.exceptions.JSONDecodeError:
    #         return '왜 안 돼'
    
    # except IndexError:
    #     return None





# 아래 코드는 수정하지 않습니다.
if __name__ == '__main__':
    pprint(get_users_books('죄와 벌'))
    pprint(get_users_books('로미오와 줄리엣'))
    pprint(get_users_books('*'))
