import json
from pprint import pprint


def artist_info(artist, genres):
    # 여기에 코드를 작성합니다.
    genres_names = []
    genres_ids = artist["genres_ids"]

    for genre_id in genres_ids:
        for genre in genres:
            id = genre["id"]
            if id == genre_id:
                genres_names.append(genre["name"])

    result = {
        "id": artist["id"],
        "name": artist["name"],
        "images": artist["images"],
        "type": artist["type"],
        "genres_names": genres_names,
    }
    return result


# 아래의 코드는 수정하지 않습니다.
if __name__ == "__main__":
    artist_json = open("data/artist.json", encoding="utf-8")
    artist_dict = json.load(artist_json)

    genres_json = open("data/genres.json", encoding="utf-8")
    genres_list = json.load(genres_json)

    pprint(artist_info(artist_dict, genres_list))
