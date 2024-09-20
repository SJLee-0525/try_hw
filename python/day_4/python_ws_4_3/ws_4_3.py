import requests
from pprint import pprint as print

dummy_data = []
# API 요청
for s in range(1, 11):
    API_URL = 'https://jsonplaceholder.typicode.com/users/' + str(s)
    response = requests.get(API_URL)

    # JSON -> dict 데이터 변환
    parsed_data = response.json()
    if -80 < float(parsed_data['address']['geo']['lat']) < 80 and -80 < float(parsed_data['address']['geo']['lng']) < 80:
        dummy_dict = {'company':parsed_data['company']['name'],
                      'lat':parsed_data['address']['geo']['lat'],
                      'lng':parsed_data['address']['geo']['lng'],
                      'name':parsed_data['name']
                      }
        dummy_data.append(dummy_dict)

print(dummy_data)