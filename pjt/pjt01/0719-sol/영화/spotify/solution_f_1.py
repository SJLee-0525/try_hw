"""
    팔로워가 5,000,000이상, 10,000,000미만인 아티스트들을 
    아티스트 이름과 팔로워를 목록으로 출력하기
"""

import json
from pprint import pprint


def get_popular():
    # 여기에 코드를 작성합니다.
    artists_json = open("data/artists.json", encoding="utf-8")
    artists_list = json.load(artists_json)

    result = []
    for artist in artists_list:
        artists_detail = json.load(
            open(f'data/artists/{artist["id"]}.json', encoding="utf-8")
        )
        if (
            artists_detail["followers"]["total"] >= 5_000_000
            and artists_detail["followers"]["total"] < 10_000_000
        ):
            result.append(
                {
                    "name": artists_detail["name"],
                    "followers": artists_detail["followers"]["total"],
                }
            )

    return result


# 아래의 코드는 수정하지 않습니다.
if __name__ == "__main__":
    pprint(get_popular())
