import json
import pprint

def dec_artists(artists):
    # 장르 id를 담은 리스트 생성
    # [178, 451, 116, 427, 832, 523, 325, 157, 724, 638, 318, 396, 962, 607, 604, 246, 208, 225, 720, 573]
    id_list = []
    for artist in artists:
        id_list.append(artist['id'])

    # id 리스트와 반복문을 활용해 파일을 엶
    million_10_list = []
    for id in id_list:
        artist_info_json = open(f'data/artists/{id}.json', encoding="utf-8")
        artist_info = json.load(artist_info_json)
        # 팔로워 수가 1000만 이상인 경우에 한해서 아티스트 이름과 팔로워 수, uri-id를 튜플로 묶어 name_follow_list에 담음
        if artist_info['followers']['total'] >= 10000000:
            name_follow = artist_info['name'], artist_info['followers']['total'], artist_info['uri'][-22:]
            million_10_list.append(name_follow)
    # [('BTS', 66752935, '3Nrfpe0tUJi4K4DXYWgMUX'), ('BLACKPINK', 42654043, '41MozSoPIsD1dJM0CLPjZF'), ('Stray Kids', 11770970, '2dIgFjalVxs4ThymZ67YCE'), ('j-hope', 15150417, '0b1sIQumIAsNbqAoIClSpy')]

    # 형식에 맞춰 dict를 만든 후 최종 리스트에 담음
    final_list = []
    for million_10_artist in million_10_list:
        final_dict = {}
        final_dict['name'] = million_10_artist[0]
        final_dict['uri'] = million_10_artist[2]
        final_list.append(final_dict)

    return final_list

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    artists_json = open('data/artists.json', encoding='utf-8')
    artists_list = json.load(artists_json)

    pprint.pprint(dec_artists(artists_list))

# [{'name': 'BTS', 'uri': '3Nrfpe0tUJi4K4DXYWgMUX'},
#  {'name': 'BLACKPINK', 'uri': '41MozSoPIsD1dJM0CLPjZF'},
#  {'name': 'Stray Kids', 'uri': '2dIgFjalVxs4ThymZ67YCE'},
#  {'name': 'j-hope', 'uri': '0b1sIQumIAsNbqAoIClSpy'}]
