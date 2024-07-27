import requests
from pprint import pprint
from examples.spotify_config import getHeaders


def get_recommended_tracks(track, artist, genre):
    # 여기에 코드를 작성합니다.
    URL = 'https://api.spotify.com/v1'
    headers = getHeaders()

    # 📌 1. artist id 가져오기
    params = {
        'q': f'artist:{artist}',
        'type': 'artist',
        'market': 'KR',
        'limit': 1,
    }
    response = requests.get(f'{URL}/search', headers=headers, params=params)
    response = response.json()

    # 없는 아티스트인 경우 None반환
    if len(response['artists']['items']) == 0:
        return None

    artistId = response['artists']['items'][0]['id']

    # 📌 2. track id 가져오기
    params = {
        'q': f'track:{track}',
        'type': 'track',
        'market': 'KR',
        'limit': 1,
    }
    response = requests.get(f'{URL}/search', headers=headers, params=params)
    response = response.json()

    # 없는 트랙인 경우 None반환
    if len(response['tracks']['items']) == 0:
        return None

    trackId = response['tracks']['items'][0]['id']

    # 📌 3. recommendation 작성
    params = {
        'seed_artists': f'{artistId}',
        'seed_tracks': f'{trackId}',
        'seed_genres': f'{genre}',
        'market': 'KR',
        'limit': 5,
    }
    response = requests.get(
        f'{URL}/recommendations', headers=headers, params=params
    )
    response = response.json()
    tracks = response['tracks']

    results = []
    for track in tracks:
        ouput = {
            '트랙': track['name'],
            '아티스트': track['artists'][0]['name'],
        }
        results.append(ouput)

    return results


# 아래 코드는 수정하지 않습니다.
if __name__ == '__main__':
    pprint(get_recommended_tracks('HypeBoy', 'BTS', 'k-pop,acoustic'))
