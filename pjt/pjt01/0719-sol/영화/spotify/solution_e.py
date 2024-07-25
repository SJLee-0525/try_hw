import json
from pprint import pprint


def dec_artists(artists):
    # 여기에 코드를 작성합니다.
    result = []
    for artist in artists:
        artists_detail = json.load(
            open(f'data/artists/{artist["id"]}.json', encoding="utf-8")
        )
        if artists_detail["followers"]["total"] >= 10_000_000:
            uri_id = artists_detail["uri"].split(":")[-1]
            result.append({"name": artists_detail["name"], "uri-id": uri_id})
    return result


# 아래의 코드는 수정하지 않습니다.
if __name__ == "__main__":
    artists_json = open("data/artists.json", encoding="utf-8")
    artists_list = json.load(artists_json)

    pprint(dec_artists(artists_list))
