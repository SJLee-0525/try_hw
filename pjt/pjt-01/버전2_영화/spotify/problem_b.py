import json
from pprint import pprint


def artist_info(artist, genres):
    # 장르 id를 key로, name을 value로 하는 dict 생성
    genres_names_dict = {}
    for genre in genres:
        genres_names_dict[genre['id']] = genre['name']
    
    # 장르의 id 값을 name 값으로 바꾸기
    for i in range(len(artist['genres_ids'])):
        artist['genres_ids'][i] = genres_names_dict[artist['genres_ids'][i]]

    my_artist = {
        'id': artist.get('id'),
        'name': artist.get('name'),
        'genres_names': artist.get('genres_ids'),
        'images': artist.get('images'),
        'type': artist.get('type')
        }
    
    return my_artist

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    artist_json = open('data/artist.json', encoding='utf-8')
    artist_dict = json.load(artist_json)

    genres_json = open('data/genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    pprint(artist_info(artist_dict, genres_list))

# {'genres_names': ['punk-rock', 'anime'],
#  'id': 178,
#  'images': [{'height': 640,
#              'url': 'https://i.scdn.co/image/ab6761610000e5eb59f8cfc8e71dcaf8c6ec4bde',
#              'width': 640},
#             {'height': 320,
#              'url': 'https://i.scdn.co/image/ab6761610000517459f8cfc8e71dcaf8c6ec4bde',
#              'width': 320},
#             {'height': 160,
#              'url': 'https://i.scdn.co/image/ab6761610000f17859f8cfc8e71dcaf8c6ec4bde',
#              'width': 160}],
#  'name': 'Jimin',
#  'type': 'artist'}