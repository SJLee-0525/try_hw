"""
    장르에 acoustic이 포함된 아티스트 이름 목록 출력하기
"""

import json
from pprint import pprint


def acoustic_artists():
    artist_json = open('data/artists.json', encoding='utf-8')
    artist_list = json.load(artist_json)

    genres_json = open('data/genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)
    
    # 장르 namedmf key로, id를 value로 하는 dict 생성
    # {'acoustic': 339, 'afrobeat': 745, 'alt-rock': 364, 'alternative': 94, ...  'work-out': 674, 'world-music': 98}
    genres_names_dict = {}
    for genre in genres_list:
        genres_names_dict[genre['name']] = genre['id']

    # 찾고자 하는 장르를 id 값으로 변환
    target_id = genres_names_dict['acoustic']
    
    # 장르 id가 포함된 아티스트 이름을 target_artist_list에 담음
    target_artist_list = []
    for artist in artist_list:
        if target_id in artist['genres_ids']:
            target_artist_list.append(artist['name'])

    return target_artist_list

# 아래의 코드는 수정하지 않습니다.
if __name__ == "__main__":
    pprint(acoustic_artists())

# ['BTS']