import requests
from pprint import pprint
from examples.spotify_config import getHeaders


def get_related_artists(name):
    # 여기에 코드를 작성합니다.
    URL = 'https://api.spotify.com/v1'
    headers = getHeaders()
    params = {
        'q': f'artist:{name}',
        'type': 'artist',
        'market': 'KR',
        'limit': 1,
    }

    # 아티스트 id 검색
    response = requests.get(f'{URL}/search', headers=headers, params=params)
    response = response.json()

    # 없는 아티스트인 경우 None반환
    if len(response['artists']['items']) == 0:
        return None

    # 연관 아티스트 검색
    artistId = response['artists']['items'][0]['id']
    params = {
        'id': artistId,
    }
    response = requests.get(
        f'{URL}/artists/{artistId}/related-artists',
        headers=headers,
        params=params,
    )
    response = response.json()
    artists = response['artists']

    results = []
    for artist in artists:
        results.append(artist['name'])

    return results


# 아래 코드는 수정하지 않습니다.
if __name__ == '__main__':
    pprint(get_related_artists('NewJeans'))
    pprint(get_related_artists('OldShirts'))
