import requests
import time

API_KEY = '입력하세요'  # OpenWeatherMap API 키를 입력하세요.
CITY = 'Seoul,KR'
LAT = 37.5665  # 서울의 위도
LON = 126.9780  # 서울의 경도

def get_current_weather(api_key, city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    response = requests.get(url)
    data = response.json()
    return data

def get_historical_weather(api_key, lat, lon, dt):
    url = f'http://api.openweathermap.org/data/2.5/onecall/timemachine?lat={lat}&lon={lon}&dt={dt}&appid={api_key}'
    response = requests.get(url)
    data = response.json()
    return data

def print_rain_info(data, time_period):
    if 'rain' in data:
        print(f"{time_period} Rain (1h): {data['rain'].get('1h', 'No data')} mm")
        print(f"{time_period} Rain (3h): {data['rain'].get('3h', 'No data')} mm")
    else:
        print(f"{time_period} Rain: No rain data available")

# 현재 날씨 데이터 가져오기
current_weather = get_current_weather(API_KEY, CITY)
print("Current Weather:")
print_rain_info(current_weather, "Current")

# 작년 이맘때의 Unix timestamp 계산하기
current_time = int(time.time())
one_year_ago = current_time - 365 * 24 * 60 * 60

# 작년 이맘때의 날씨 데이터 가져오기
historical_weather = get_historical_weather(API_KEY, LAT, LON, one_year_ago)
print(historical_weather)
print("\nHistorical Weather (One Year Ago):")
print_rain_info(historical_weather['current'], "Historical")
