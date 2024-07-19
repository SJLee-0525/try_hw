import requests
from pprint import pprint as print

# 무작위 유저 정보 요청 경로


dummy_data = []
# API 요청
for s in range(1, 11):
    API_URL = 'https://jsonplaceholder.typicode.com/users/' + str(s)
    response = requests.get(API_URL)

    # JSON -> dict 데이터 변환
    parsed_data = response.json()
    dummy_data.append(parsed_data['name'])

print(dummy_data)