"""
    팔로워가 5,000,000이상, 10,000,000미만인 아티스트들을 
    아티스트 이름과 팔로워를 목록으로 출력하기
"""

import json
from pprint import pprint


def get_popular():
    # 자료 불러오기
    artists_json = open('data/artists.json', encoding='utf-8')
    artists_list = json.load(artists_json)

    # 장르 id를 담은 리스트 생성
    # [178, 451, 116, 427, 832, 523, 325, 157, 724, 638, 318, 396, 962, 607, 604, 246, 208, 225, 720, 573]
    id_list = []
    for artist in artists_list:
        id_list.append(artist['id'])

    # id 리스트와 반복문을 활용해 파일을 엶
    influencer_list = []
    for id in id_list:
        artist_info_json = open(f'data/artists/{id}.json', encoding="utf-8")
        artist_info = json.load(artist_info_json)
        # 팔로워 수가 500만 이상 1000만 미만인 경우에 한해서 아티스트 이름과 팔로워 수를 튜플로 묶어 influencer_list에 담음
        if 5000000 < artist_info['followers']['total'] < 10000000:
            name_follow = artist_info['name'], artist_info['followers']['total']
            influencer_list.append(name_follow)
    # [('Jimin', 5901644), ('SEVENTEEN', 9571638), ('IU', 8041766), ('Jung Kook', 8000368), ('(G)I-DLE', 6278033), ('NCT DREAM', 6785638)]

    # 형식에 맞춰 dict를 만든 후 최종 리스트에 담음
    final_list = []
    for influencer in influencer_list:
        final_dict = {}
        final_dict['followers'] = influencer[1]
        final_dict['name'] = influencer[0]
        final_list.append(final_dict)

    return final_list


# 아래의 코드는 수정하지 않습니다.
if __name__ == "__main__":
    pprint(get_popular())
