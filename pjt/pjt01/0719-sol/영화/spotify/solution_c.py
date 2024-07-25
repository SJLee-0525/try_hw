import json
from pprint import pprint


def artist_info(artists, genres):
    # 여기에 코드를 작성합니다.
    result = []
    for artist in artists[1:3]:
        genres_names = []
        gerne_ids = artist["genres_ids"]
        for genre_id in gerne_ids:
            for genre in genres:
                if genre["id"] == genre_id:
                    genres_names.append(genre["name"])

        tmp = {
            "id": artist["id"],
            "name": artist["name"],
            "images": artist["images"],
            "type": artist["type"],
            "genres_names": genres_names,
        }
        result.append(tmp)
    return result


# 아래의 코드는 수정하지 않습니다.
if __name__ == "__main__":
    artists_json = open("data/artists.json", encoding="utf-8")
    artists_list = json.load(artists_json)

    genres_json = open("data/genres.json", encoding="utf-8")
    genres_list = json.load(genres_json)

    pprint(artist_info(artists_list, genres_list))
