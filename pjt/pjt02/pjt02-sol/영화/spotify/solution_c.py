import requests
from pprint import pprint
from examples.spotify_config import getHeaders


def get_recently_tracks():
    # 여기에 코드를 작성합니다.
    URL = 'https://api.spotify.com/v1'
    headers = getHeaders()
    params = {
        'q': 'genre:classical',
        'type': 'track',
        'market': 'KR',
        'limit': 10,
    }

    response = requests.get(f'{URL}/search', headers=headers, params=params)
    response = response.json()
    tracks = response['tracks']['items']

    sorted_tracks = sorted(
        tracks, key=lambda track: track['album']['release_date'], reverse=True
    )

    results = []
    for index, track in enumerate(sorted_tracks):
        if index == 5:
            break
        album = {
            '앨범명': track['album']['name'],
            '아티스트': track['album']['artists'][0]['name'],
            '발매일': track['album']['release_date'],
        }
        results.append(album)

    return results


# 아래 코드는 수정하지 않습니다.
if __name__ == '__main__':
    pprint(get_recently_tracks())
