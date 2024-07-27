import requests
from pprint import pprint
from examples.spotify_config import getHeaders


def get_artists():
    # 여기에 코드를 작성합니다.
    URL = 'https://api.spotify.com/v1'
    headers = getHeaders()
    genre = 'k-pop'
    params = {
        'q': f'genre:{genre}',
        'type': 'artist',
        'market': 'KR',
        'limit': 20,
    }

    response = requests.get(f'{URL}/search', headers=headers, params=params)
    response = response.json()

    results = []
    artists = response['artists']['items']
    for item in artists:
        results.append(item['name'])

    return results


# 아래 코드는 수정하지 않습니다.
if __name__ == '__main__':
    pprint(get_artists())
