import requests
from pprint import pprint

# 문제4. C번의 데이터를 활용하여, 섭씨 온도 데이터를 추가합니다.


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

    # 온도를 섭씨로 변환하여 추가
    translated_main_data['온도(섭씨)'] = round(
        translated_main_data['온도'] - 273.15, 2
    )
    translated_main_data['최고온도(섭씨)'] = round(
        translated_main_data['최고온도'] - 273.15, 2
    )
    translated_main_data['최저온도(섭씨)'] = round(
        translated_main_data['최저온도'] - 273.15, 2
    )
    translated_main_data['체감온도(섭씨)'] = round(
        translated_main_data['체감온도'] - 273.15, 2
    )

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
