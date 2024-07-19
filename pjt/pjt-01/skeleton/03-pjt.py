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

    # 요구사항에 맞도록 이곳의 코드를 수정합니다.
    response = requests.get(url).json()

    temp_result = {}
    temp_result['main'] = response['main']
    temp_result['weather_data'] = response['weather']

    mini_result = {}
    mini_result['기압'] = temp_result['main']['pressure']
    mini_result['습도'] = temp_result['main']['humidity']
    mini_result['온도'] = temp_result['main']['temp']
    mini_result['체감온도'] = temp_result['main']['feels_like']
    mini_result['최고온도'] = temp_result['main']['temp_max']
    mini_result['최저온도'] = temp_result['main']['temp_min']

    mini_result_2 = {}
    mini_result_2['요약'] = temp_result['weather_data'][0]['description']
    mini_result_2['아이콘'] = temp_result['weather_data'][0]['icon']
    mini_result_2['식별자'] = temp_result['weather_data'][0]['id']
    mini_result_2['핵심'] = temp_result['weather_data'][0]['main']

    temp_list = []
    temp_list.append(mini_result_2)

    result = {}
    result['기본'] = mini_result
    result['날씨'] = temp_list
    
    return result


# 아래 코드는 수정하지 않습니다.
if __name__ == '__main__':
    # 여러분의 OpenWeatherMap API 키를 설정하세요
    api_key = 'd041d5b2deed53c8decf301f3fbadcb3'

    result = get_weather(api_key)
    pprint(result)

# {'기본': {'기압': 1008,
#         '습도': 94,
#         '온도': 298.66,
#         '체감온도': 299.72,
#         '최고온도': 298.91,
#         '최저온도': 297.81},
#  '날씨': [{'식별자': 803, '아이콘': '04n', '요약': 'broken clouds', '핵심': 'Clouds'}]}