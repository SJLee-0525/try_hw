import requests
from pprint import pprint as print

black_list = [
    'Hoeger LLC',
    'Keebler LLC',
    'Yost and Sons',
    'Johns Group',
    'Romaguera-Crona',
]

def create_user(receive_data_list):
    censored_user_list = {}
    for receive_data in receive_data_list:
        if censorship(receive_data) == True:
            value_list = []
            value_list.append(receive_data['name'])
            censored_user_list[receive_data['company']] = value_list
    return censored_user_list

def censorship(receive_data):
    if receive_data['company'] in black_list:
        print(f'{receive_data["company"]} 소속의 {receive_data["name"]} 은/는 등록할 수 없습니다.')
        return False
    else:
        print(f'이상 없습니다.')
        return True

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

result = create_user(dummy_data)
print(result)