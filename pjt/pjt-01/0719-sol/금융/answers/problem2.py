import requests
from pprint import pprint

# 문제2. 날씨 데이터 중 다음 조건에 해당하는 값만 딕셔너리 형태로 반환하는 함수를 구성합니다.
#   KEY 값이“main” 인 데이터
#   KEY 값이 “weather” 인 데이터
# 함수에서 두 데이터를 새로운 dictionary 에 담아서 return 합니다.


def get_weather(api_key):
    city = "Seoul,KR"
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

    response = requests.get(url)
    data = response.json()

    result_dict = {'main': data.get('main'), 'weather': data.get('weather')}

    return result_dict


# 여러분의 OpenWeatherMap API 키를 설정하세요
api_key = '87246d75e1ce26e1392a087b3d1d88c5'

result = get_weather(api_key)
pprint(result)
