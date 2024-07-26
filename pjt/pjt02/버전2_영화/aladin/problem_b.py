import requests
from pprint import pprint


def get_best_review_books(api_key):
    # 여기에 코드를 작성합니다.
    URL = 'http://www.aladin.co.kr/ttb/api/ItemSearch.aspx'

    params = {
    'ttbkey': {api_key},
    'Query': '파울로 코엘료',
    'QueryType': 'Author',
    'MaxResults': 20,
    'start': 1,
    'SearchTarget': 'Book',
    'output': 'js',
    'Version': '20131101',
    }

    response = requests.get(URL, params=params)
    response = response.json()
    
    # 리스트 내의 dict를 순회하면서 리뷰 점수가 9점 이상인 dict를 새 리스트에 추가
    Good_review_list = []
    for response_i in range(len(response['item'])):
        if response['item'][response_i]['customerReviewRank'] >= 9:
            Good_review_list.append(response['item'][response_i])

    return Good_review_list


# 아래 코드는 수정하지 않습니다.
if __name__ == '__main__':
    api_key = 'ttbyts02751555001'
    pprint(get_best_review_books(api_key))

'''
[{'adult': False,
  'author': '파울로 코엘료 (지은이), 최정수 (옮긴이)',
  'categoryId': 50920,
  'categoryName': '국내도서>소설/시/희곡>스페인/중남미소설',
  'cover': 'https://image.aladin.co.kr/product/30/73/coversum/8982814477_3.jpg',
  'customerReviewRank': 9,
  'description': "세상을 두루두루 여행하기 위해 양치기가 된 청년 산티아고의 '자아의 신화' 찾기 여행담. 자칫 딱딱하게 보일 "
                 '수 있는 제목과는 달리 간결하고 경쾌한 언어들로 쓰여 있어서, 물이 흘러가듯 수월하게 읽히는 작품이다.',
  'fixedPrice': True,
  'isbn': '8982814477',
  'isbn13': '9788982814471',
  'itemId': 307361,
  'link': 'http://www.aladin.co.kr/shop/wproduct.aspx?ItemId=307361&amp;partner=openAPI&amp;start=api',
  'mallType': 'BOOK',
  'mileage': 600,
  'priceSales': 10800,
  'priceStandard': 12000,
  'pubDate': '2001-12-01',
  'publisher': '문학동네',
  'salesPoint': 82999,
  'stockStatus': '',
  'subInfo': {},
  'title': '연금술사'},
 {'adult': False,
  'author': '파울로 코엘료 (지은이), 황중환 (그림), 김미나 (옮긴이)',
  'categoryId': 51373,
  'categoryName': '국내도서>에세이>외국에세이',
  'cover': 'https://image.aladin.co.kr/product/24074/94/coversum/k522639032_1.jpg',
  'customerReviewRank': 9,
  'description': '전 세계 7백30만 명의 팔로어를 열광시킨 노(老)작가의 지혜. 국경을 초월하고 광속으로 퍼져나가는 파울로 '
                 '코엘료의 트윗 글에 여운이 남은 독자들을 위해, 한국의 그림 작가와 손을 잡고 한권의 책으로 태어났다.',
  'fixedPrice': True,
  'isbn': '8954429904',
  'isbn13': '9788954429900',
  'itemId': 240749444,
  'link': 'http://www.aladin.co.kr/shop/wproduct.aspx?ItemId=240749444&amp;partner=openAPI&amp;start=api',
  'mallType': 'BOOK',
  'mileage': 850,
  'priceSales': 15300,
  'priceStandard': 17000,
  'pubDate': '2013-05-07',
  'publisher': '자음과모음',
  'salesPoint': 7152,
  'stockStatus': '',
  'subInfo': {},
  'title': '마법의 순간 (리커버)'},
 {'adult': False,
  'author': '파울로 코엘료 (지은이), 박명숙 (옮긴이)',
  'categoryId': 51373,
  'categoryName': '국내도서>에세이>외국에세이',
  'cover': 'https://image.aladin.co.kr/product/1328/67/coversum/8954616003_2.jpg',
  'customerReviewRank': 9,
  'description': '2006년 국내에 소개된 파울로 코엘료의 &lt;순례자&gt;(1987)가 신작 &lt;알레프&gt;의 '
                 '출간과 함께 새 옷을 입고 독자들에게 선보인다. &lt;순례자&gt;는 파울로 코엘료의 데뷔작이자 그를 '
                 '세계적인 작가의 반열에 올린 &lt;연금술사&gt;의 모태가 되는 작품이다. 방황하던 한 사람이 기적과도 '
                 '같은 변화의 과정을 거쳐 깨달음에 이르는 여정을 담고 있다.',
  'fixedPrice': True,
  'isbn': '8954616003',
  'isbn13': '9788954616003',
  'itemId': 13286743,
  'link': 'http://www.aladin.co.kr/shop/wproduct.aspx?ItemId=13286743&amp;partner=openAPI&amp;start=api',
  'mallType': 'BOOK',
  'mileage': 600,
  'priceSales': 10800,
  'priceStandard': 12000,
  'pubDate': '2011-10-05',
  'publisher': '문학동네',
  'salesPoint': 4859,
  'stockStatus': '',
  'subInfo': {},
  'title': '순례자 - 개정판'},
 {'adult': False,
  'author': '파울로 코엘료 (지은이), 윤예지 (그림), 박태옥 (옮긴이)',
  'categoryId': 51376,
  'categoryName': '국내도서>에세이>사진/그림 에세이',
  'cover': 'https://image.aladin.co.kr/product/24074/93/coversum/895444248x_1.jpg',
  'customerReviewRank': 10,
  'description': '빠르게 변화하는 세상에서 사람들은 자신의 가치와 의미를 잃어버리기 쉽다. 너무 많은 비교 대상과 넘어야 할 '
                 "산을 보며 때로는 우울하고 불안하기만 하다. 전 세계에서 가장 많이 번역된 작가, 파울로 코엘료가 '나'를 "
                 '사랑하는 일에 서툰 사람들을 위한 신작 에세이를 출간했다.',
  'fixedPrice': True,
  'isbn': '895444248X',
  'isbn13': '9788954442480',
  'itemId': 240749317,
  'link': 'http://www.aladin.co.kr/shop/wproduct.aspx?ItemId=240749317&amp;partner=openAPI&amp;start=api',
  'mallType': 'BOOK',
  'mileage': 670,
  'priceSales': 12150,
  'priceStandard': 13500,
  'pubDate': '2020-05-28',
  'publisher': '자음과모음',
  'salesPoint': 3559,
  'stockStatus': '',
  'subInfo': {},
  'title': '내가 빛나는 순간'},
 {'adult': False,
  'author': '파울로 코엘료 (지은이), 뫼비우스 (그림), 최정수 (옮긴이)',
  'categoryId': 50920,
  'categoryName': '국내도서>소설/시/희곡>스페인/중남미소설',
  'cover': 'https://image.aladin.co.kr/product/60/41/coversum/8954600565_2.jpg',
  'customerReviewRank': 9,
  'description': "세상을 두루 여행하기 위해 양치기가 된 청년 산티아고의 '자아의 신화' 찾기 여행담, 파울로 코엘료의 "
                 '장편소설 <연금술사>의 일러스트레이션판이 출간되었다. 삽화를 담당한 뫼비우스는 <연금술사>의 표지 그림을 '
                 '그렸던 일러스트레이터. 소설의 주요 장면들을 솜씨 좋게 포착한 컬러 삽화가, 각각 독립된 페이지에 실려 '
                 '있다.',
  'fixedPrice': True,
  'isbn': '8954600565',
  'isbn13': '9788954600569',
  'itemId': 604158,
  'link': 'http://www.aladin.co.kr/shop/wproduct.aspx?ItemId=604158&amp;partner=openAPI&amp;start=api',
  'mallType': 'BOOK',
  'mileage': 600,
  'priceSales': 10800,
  'priceStandard': 12000,
  'pubDate': '2005-12-01',
  'publisher': '문학동네',
  'salesPoint': 3436,
  'stockStatus': '',
  'subInfo': {},
  'title': '일러스트 연금술사'},
 {'adult': False,
  'author': '파울로 코엘료 (지은이), 오진영 (옮긴이)',
  'categoryId': 50920,
  'categoryName': '국내도서>소설/시/희곡>스페인/중남미소설',
  'cover': 'https://image.aladin.co.kr/product/1303/6/coversum/8954616127_3.jpg',
  'customerReviewRank': 9,
  'description': '&lt;연금술사&gt; &lt;브리다&gt;의 작가 파울로 코엘료의 2011년 신작. 작가의 길에 들어선 지 '
                 '20여 년이 훌쩍 넘은 파울로 코엘료의 세계를 아우르는 동시에, 자신의 근본으로 회귀함으로써 새로운 출발을 '
                 '알리는 작품이다. 코엘료의 고국인 브라질을 시작으로, 포르투갈, 헝가리 등 20여 국에서 출간되어 출간 첫날 '
                 '즉시 베스트셀러 1위에 올라 변함없이 코엘료 신드롬을 일으켰다.',
  'fixedPrice': True,
  'isbn': '8954616127',
  'isbn13': '9788954616126',
  'itemId': 13030616,
  'link': 'http://www.aladin.co.kr/shop/wproduct.aspx?ItemId=13030616&amp;partner=openAPI&amp;start=api',
  'mallType': 'BOOK',
  'mileage': 670,
  'priceSales': 12150,
  'priceStandard': 13500,
  'pubDate': '2011-09-23',
  'publisher': '문학동네',
  'salesPoint': 3036,
  'stockStatus': '',
  'subInfo': {},
  'title': '알레프'},
 {'adult': False,
  'author': '파울로 코엘료 (지은이), 오진영 (옮긴이)',
  'categoryId': 50920,
  'categoryName': '국내도서>소설/시/희곡>스페인/중남미소설',
  'cover': 'https://image.aladin.co.kr/product/29733/11/coversum/8954687482_1.jpg',
  'customerReviewRank': 9,
  'description': '긴 터널 같은 시기를 견디고 자신의 진정한 꿈을 향해 나아가 결국 세계적인 작가로 거듭난 그는, 자신의 '
                 '삶에서 영감을 얻어 써내려간 이 소설 속에 “피할 수 없는 시련은 인생의 형벌이 아닌 도전”이라는 살아 있는 '
                 '메시지를 담아냈다.',
  'fixedPrice': True,
  'isbn': '8954687482',
  'isbn13': '9788954687485',
  'itemId': 297331113,
  'link': 'http://www.aladin.co.kr/shop/wproduct.aspx?ItemId=297331113&amp;partner=openAPI&amp;start=api',
  'mallType': 'BOOK',
  'mileage': 750,
  'priceSales': 13500,
  'priceStandard': 15000,
  'pubDate': '2022-07-12',
  'publisher': '문학동네',
  'salesPoint': 2905,
  'stockStatus': '',
  'subInfo': {},
  'title': '다섯번째 산'}]
'''