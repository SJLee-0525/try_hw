import requests
from pprint import pprint

API_KEY = 'ttbsungjoon1111015001'
API_URL = 'http://www.aladin.co.kr/ttb/api/ItemList.aspx'

params = {
    'TTBKey': API_KEY,
    'QueryType': 'ItemNewSpecial',
    'MaxResults': '50',
    'start': '1',
    'SearchTarget': 'Book',
    'Version': '20131101',
    'Output': 'JS'
}
response = requests.get(API_URL, params = params).json()
items = response['item']
output = []
def print_bookinfo(its):
    info = {}
    info['국제 표준 도서 번호'] = its['isbn']
    info['저자'] = its['author']
    info['제목'] = its['title']
    info['출간일'] = its['pubDate']
    return info

for i in items:
    output.append(print_bookinfo(i))
pprint(output)