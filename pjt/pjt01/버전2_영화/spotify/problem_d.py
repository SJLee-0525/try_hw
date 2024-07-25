import json


def max_polularity(artists):
    # 장르 id를 담은 리스트 생성
    # [178, 451, 116, 427, 832, 523, 325, 157, 724, 638, 318, 396, 962, 607, 604, 246, 208, 225, 720, 573]
    id_list = []
    for artist in artists:
        id_list.append(artist['id'])

    # id 리스트와 반복문을 활용해 파일을 열고, 아티스트 이름과 인기도를 튜플로 묶어 name_pop_list에 담음
    # [('Jimin', 73), ('BTS', 79), ('NewJeans', 98), ('LE SSERAFIM', 77), ... ('TAEYEON', 91), ('FIFTY FIFTY', 89)]
    name_pop_list = []
    for id in id_list:
        artist_info_json = open(f'data/artists/{id}.json', encoding="utf-8")
        artist_info = json.load(artist_info_json)
        name_pop = artist_info['name'], artist_info['popularity']
        name_pop_list.append(name_pop)
    
    # 인기도 순으로 정렬
    # [('NewJeans', 98), ('Jay Park', 97), ('j-hope', 95), ... ('KANGDANIEL', 71), ('Stray Kids', 70)]
    name_pop_list.sort(key=lambda x:x[1], reverse=True)
    
    # 가장 인기도가 높은 아티스트 리턴
    return name_pop_list[0][0]

# 아래의 코드는 수정하지 않습니다.
if __name__ == "__main__":
    artists_json = open("data/artists.json", encoding="utf-8")
    artists_list = json.load(artists_json)

    print(max_polularity(artists_list))

# NewJeans