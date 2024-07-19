"""
    장르에 acoustic이 포함된 아티스트 이름 목록 출력하기
"""

import json
from pprint import pprint


def acoustic_artists():
    # 여기에 코드를 작성합니다.
    # 1. 장르 아이디 가져오기
    acousticId = -1
    genres = json.load(open(f"data/genres.json", encoding="utf-8"))
    for genre in genres:
        if genre["name"] == "acoustic":
            acousticId = genre["id"]
            break

    # 2. 장르가 acoustic인 아티스트 리스트 출력하기
    artists_json = open("data/artists.json", encoding="utf-8")
    artists_list = json.load(artists_json)

    result = []
    for artist in artists_list:
        genres_ids = artist["genres_ids"]
        for g_id in genres_ids:
            if g_id == acousticId:
                result.append(artist["name"])

    return result


# 아래의 코드는 수정하지 않습니다.
if __name__ == "__main__":
    pprint(acoustic_artists())
