import json
from pprint import pprint


def artist_info(artist):
    # 여기에 코드를 작성합니다.
    result = {
        "id": artist["id"],
        "name": artist["name"],
        "genres_ids": artist["genres_ids"],
        "images": artist["images"],
        "type": artist["type"],
    }
    return result


# 아래의 코드는 수정하지 않습니다.
if __name__ == "__main__":
    artist_json = open("data/artist.json", encoding="utf-8")
    artist_dict = json.load(artist_json)

    pprint(artist_info(artist_dict))
