import requests
from pprint import pprint

# 문제3. B번에서 얻는 결과를 활용하여, KEY 값들을 한글로 변경한 딕셔너리를 반환하도록 구성합니다.
# KEY 에 해당하는 한글 KEY 값들은 다음과 같습니다.
# feels_like : '체감온도',
# humidity : '습도',
# pressure : '기압',
# temp : '온도',
# temp_max : '최고온도',
# temp_min : '최저온도',
# description : '요약',
# icon : '아이콘',
# main : '핵심’
# id : ‘식별자’


def get_weather(api_key):
    city = "Seoul,KR"
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

    response = requests.get(url)
    data = response.json()

    # 내부 키 값 한글로 변경
    translated_keys = {
        'feels_like': '체감온도',
        'humidity': '습도',
        'pressure': '기압',
        'temp': '온도',
        'temp_max': '최고온도',
        'temp_min': '최저온도',
        'description': '요약',
        'icon': '아이콘',
        'main': '핵심',
        'id': '식별자',
    }

    # 기본 데이터 키 값 변경
    main_data = data.get('main')
    translated_main_data = {
        translated_keys.get(key): value for key, value in main_data.items()
    }

    # 날씨 데이터 키 값 변경
    weather_data = data.get('weather')
    translated_weather_data = [
        {translated_keys.get(key): value for key, value in item.items()}
        for item in weather_data
    ]

    result_dict = {
        '기본': translated_main_data,
        '날씨': translated_weather_data,
    }

    return result_dict


# 여러분의 OpenWeatherMap API 키를 설정하세요
api_key = '87246d75e1ce26e1392a087b3d1d88c5'

result = get_weather(api_key)
pprint(result)
