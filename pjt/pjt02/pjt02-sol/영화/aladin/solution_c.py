import requests
from pprint import pprint


def get_bestseller_books():
    URL = 'http://www.aladin.co.kr/ttb/api/ItemSearch.aspx'
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

    response = requests.get(URL, params=params).json()
    result = []
    book_list = response['item']
    book_list.sort(key=lambda x: x['salesPoint'], reverse=True)
    """
    - sorted() 함수를 사용하여 정렬할 수도 있다.
    sorted_book_list = sorted(book_list, key=lambda x: x['salesPoint'], reverse=True)
    result = sorted_book_list[:5]
    """

    for best_Book in book_list[:5]:
        ouput = {
            '제목': best_Book['title'],
            '판매지수': best_Book['salesPoint'],
        }
        result.append(ouput)

    return result


# 아래 코드는 수정하지 않습니다.
if __name__ == '__main__':
    pprint(get_bestseller_books())
