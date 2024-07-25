import requests
from pprint import pprint

# 문제1. 날씨 데이터의 응답을 json 형태로 변환하여 key 값만 출력하시오.
# 공식문서의 요청변수와 예제 요청결과(JSON) 부분을 참고합니다.


def get_weather(api_key):
    city = "Seoul,KR"
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

    response = requests.get(url)
    data = response.json()

    return data.keys()


# 여러분의 OpenWeatherMap API 키를 설정하세요
api_key = '87246d75e1ce26e1392a087b3d1d88c5'

result = get_weather(api_key)
pprint(result)
