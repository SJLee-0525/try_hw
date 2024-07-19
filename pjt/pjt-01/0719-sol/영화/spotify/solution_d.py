import json


def max_popularity(artists):
    # 여기에 코드를 작성합니다.
    result = ""
    popularity = 0
    for artist in artists:
        artists_detail = json.load(
            open(f'data/artists/{artist["id"]}.json', encoding="utf-8")
        )
        if popularity <= artists_detail["popularity"]:
            popularity = artists_detail["popularity"]
            result = artists_detail["name"]

    return result


# 아래의 코드는 수정하지 않습니다.
if __name__ == "__main__":
    artists_json = open("data/artists.json", encoding="utf-8")
    artists_list = json.load(artists_json)

    print(max_popularity(artists_list))
