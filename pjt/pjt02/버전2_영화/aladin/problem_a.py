import requests
from pprint import pprint


def get_author_books(api_key):
    # 여기에 코드를 작성합니다.
    # 이건 상품 검색 API임
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

    title_list = []
    for response_i in range(len(response['item'])):
        title_list.append(response['item'][response_i]['title'])

    return title_list

def get_author_books_2(api_key):

    ttbkey = api_key
    query = '파울로 코엘료'
    query_type = 'Author'
    max_results = 20
    start = 1
    search_target = 'Book'
    output = 'js'
    version = 20131101

    URL = f'http://www.aladin.co.kr/ttb/api/ItemSearch.aspx?ttbkey={ttbkey}&Query={query}&QueryType={query_type}&MaxResults={max_results}&start={start}&SearchTarget={search_target}&output={output}&Version={version}'
    # 위와 같은 방법으로 표시할 때는 url과 params 사이 구분은 '?'로, params과 params 사이는 &으로 구분
    
    response = requests.get(URL)
    response = response.json()

    title_list = []
    for response_i in range(len(response['item'])):
        title_list.append(response['item'][response_i]['title'])

    return title_list

# 아래 코드는 수정하지 않습니다.
if __name__ == '__main__':
    api_key = '알라딘 api 키 입력'
    pprint(get_author_books(api_key))
    print('---------------------------------------')
    pprint(get_author_books_2(api_key))

'''
['연금술사',
 '11분',
 '흐르는 강물처럼',
 '브리다',
 '포르토벨로의 마녀',
 '마법의 순간 (리커버)',
 '오 자히르',
 '불륜',
 '순례자 - 개정판',
 '내가 빛나는 순간',
 '아처',
 '스파이',
 '일러스트 연금술사',
 '피에트라 강가에서 나는 울었네',
 '알레프',
 '아크라 문서',
 '승자는 혼자다 1',
 '다섯번째 산',
 '악마와 미스 프랭',
 '연금술사 (문학동네 30주년 기념 특별판)']
 '''

'''
{'item': [{'adult': False,
           'author': '파울로 코엘료 (지은이), 최정수 (옮긴이)',
           'categoryId': 50920,
           'categoryName': '국내도서>소설/시/희곡>스페인/중남미소설',
           'cover': 'https://image.aladin.co.kr/product/30/73/coversum/8982814477_3.jpg',
           'customerReviewRank': 9,
           'description': "세상을 두루두루 여행하기 위해 양치기가 된 청년 산티아고의 '자아의 신화' 찾기 여행담. "
                          '자칫 딱딱하게 보일 수 있는 제목과는 달리 간결하고 경쾌한 언어들로 쓰여 있어서, 물이 '
                          '흘러가듯 수월하게 읽히는 작품이다.',
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
           'salesPoint': 83158,
           'stockStatus': '',
           'subInfo': {},
           'title': '연금술사'},
          {'adult': False,
           'author': '파울로 코엘료 (지은이), 이상해 (옮긴이)',
           'categoryId': 50920,
           'categoryName': '국내도서>소설/시/희곡>스페인/중남미소설',
           'cover': 'https://image.aladin.co.kr/product/48/92/coversum/8982818227_2.jpg',
           'customerReviewRank': 8,
           'description': '<연금술사>, <베로니카, 죽기로 결심하다> 등으로 많은 독자들의 사랑을 받은 파울로 '
                          '코엘료의 최신 화제작. 2003년 유럽과 남미 등지에서 <해리 포터와 불사조 기사단>을 '
                          '누르고 베스트셀러 1위에 오른바 있다. 제목 <11분>은 성행위의 평균 지속시간을 의미한다.',
           'fixedPrice': True,
           'isbn': '8982818227',
           'isbn13': '9788982818226',
           'itemId': 489254,
           'link': 'http://www.aladin.co.kr/shop/wproduct.aspx?ItemId=489254&amp;partner=openAPI&amp;start=api',
           'mallType': 'BOOK',
           'mileage': 750,
           'priceSales': 13500,
           'priceStandard': 15000,
           'pubDate': '2004-05-11',
           'publisher': '문학동네',
           'salesPoint': 10434,
           'stockStatus': '',
           'subInfo': {},
           'title': '11분'},
          {'adult': False,
           'author': '파울로 코엘료 (지은이), 박경희 (옮긴이)',
           'categoryId': 51373,
           'categoryName': '국내도서>에세이>외국에세이',
           'cover': 'https://image.aladin.co.kr/product/261/0/coversum/8954606830_1.jpg',
           'customerReviewRank': 8,
           'description': '&lt;연금술사&gt; &lt;베로니카, 죽기로 결심하다&gt;의 작가 파울로 코엘료 첫 '
                          '산문집. 세계 각국의 신화와 종교를 두루 섭렵한 작가가 인간 영혼 깊은 곳에서 건져올린 '
                          '아름다운 우화, 작가 자신의 일상과 코엘료 문학의 비밀을 엿볼 수 있는 열쇠 같은 글들, '
                          '길에서 만난 사람들과의 감동적인 일화들을 담았다.',
           'fixedPrice': True,
           'isbn': '8954606830',
           'isbn13': '9788954606837',
           'itemId': 2610076,
           'link': 'http://www.aladin.co.kr/shop/wproduct.aspx?ItemId=2610076&amp;partner=openAPI&amp;start=api',
           'mallType': 'BOOK',
           'mileage': 700,
           'priceSales': 12600,
           'priceStandard': 14000,
           'pubDate': '2008-10-14',
           'publisher': '문학동네',
           'salesPoint': 10107,
           'stockStatus': '',
           'subInfo': {},
           'title': '흐르는 강물처럼'},
          {'adult': False,
           'author': '파울로 코엘료 (지은이), 권미선 (옮긴이)',
           'categoryId': 50920,
           'categoryName': '국내도서>소설/시/희곡>스페인/중남미소설',
           'cover': 'https://image.aladin.co.kr/product/788/4/coversum/8954612997_1.jpg',
           'customerReviewRank': 8,
           'description': '&lt;연금술사&gt;, &lt;베로니카, 죽기로 결심하다&gt;의 작가 파울로 코엘료가 '
                          '들려주는 운명과 사랑에 관한 이야기. &lt;브리다&gt;는 운명을 찾아나선 스무 살 '
                          '브리다가 사랑을 찾고 더 나아가 자아를 발견하면서 변모해가는 가슴 뭉클한 여정의 기록이다. '
                          '1990년 출간되어 지금까지 전세계 독자들에게 큰 사랑을 받고 있다.',
           'fixedPrice': True,
           'isbn': '8954612997',
           'isbn13': '9788954612999',
           'itemId': 7880484,
           'link': 'http://www.aladin.co.kr/shop/wproduct.aspx?ItemId=7880484&amp;partner=openAPI&amp;start=api',
           'mallType': 'BOOK',
           'mileage': 750,
           'priceSales': 13500,
           'priceStandard': 15000,
           'pubDate': '2010-10-20',
           'publisher': '문학동네',
           'salesPoint': 10072,
           'stockStatus': '',
           'subInfo': {},
           'title': '브리다'},
          {'adult': False,
           'author': '파울로 코엘료 (지은이), 임두빈 (옮긴이)',
           'categoryId': 50920,
           'categoryName': '국내도서>소설/시/희곡>스페인/중남미소설',
           'cover': 'https://image.aladin.co.kr/product/98/35/coversum/8954603904_1.jpg',
           'customerReviewRank': 8,
           'description': '&lt;연금술사&gt;의 작가 파울로 코엘료의 2007년 신작. 런던 중심가인 포르토벨로에 '
                          "'마녀' 붐을 일으키는, '아테나'라는 이름의 한 비범한 여자가 소설의 중심에 놓이며, 여러 "
                          "화자가 뒤섞여 그녀의 행적을 쫓는다. 브라질의 한 언론은 '지금까지 코엘료의 다른 모든 "
                          "작품보다 훨씬 더 멀리 나아간 첨단의 작품'이란 평을 내놓았다.",
           'fixedPrice': True,
           'isbn': '8954603904',
           'isbn13': '9788954603904',
           'itemId': 983581,
           'link': 'http://www.aladin.co.kr/shop/wproduct.aspx?ItemId=983581&amp;partner=openAPI&amp;start=api',
           'mallType': 'BOOK',
           'mileage': 650,
           'priceSales': 11700,
           'priceStandard': 13000,
           'pubDate': '2007-10-11',
           'publisher': '문학동네',
           'salesPoint': 8404,
           'stockStatus': '',
           'subInfo': {},
           'title': '포르토벨로의 마녀'},
          {'adult': False,
           'author': '파울로 코엘료 (지은이), 황중환 (그림), 김미나 (옮긴이)',
           'categoryId': 51373,
           'categoryName': '국내도서>에세이>외국에세이',
           'cover': 'https://image.aladin.co.kr/product/24074/94/coversum/k522639032_1.jpg',
           'customerReviewRank': 9,
           'description': '전 세계 7백30만 명의 팔로어를 열광시킨 노(老)작가의 지혜. 국경을 초월하고 광속으로 '
                          '퍼져나가는 파울로 코엘료의 트윗 글에 여운이 남은 독자들을 위해, 한국의 그림 작가와 손을 '
                          '잡고 한권의 책으로 태어났다.',
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
           'author': '파울로 코엘료 (지은이), 최정수 (옮긴이)',
           'categoryId': 50920,
           'categoryName': '국내도서>소설/시/희곡>스페인/중남미소설',
           'cover': 'https://image.aladin.co.kr/product/57/26/coversum/8982819991_2.jpg',
           'customerReviewRank': 8,
           'description': '<연금술사>, <베로니카 죽기로 결심하다>의 작가 파울로 코엘료의 2005년 최신작 <오 '
                          '자히르>가 출간됐다. 이란에서 하루에 8만5천 부가 팔려나갔으며, 프랑스에서는 1주일 만에 '
                          '베스트셀러 1위에 올랐고, 이탈리아에서 출간 1개월 만에 42만 부의 판매고를 기록한 '
                          "화제작이다. '소유하고 싶고 자유롭고 싶다'-사랑의 두 얼굴을 빛나는 성찰로 그려낸 소설.",
           'fixedPrice': True,
           'isbn': '8982819991',
           'isbn13': '9788982819995',
           'itemId': 572641,
           'link': 'http://www.aladin.co.kr/shop/wproduct.aspx?ItemId=572641&amp;partner=openAPI&amp;start=api',
           'mallType': 'BOOK',
           'mileage': 800,
           'priceSales': 14400,
           'priceStandard': 16000,
           'pubDate': '2005-07-11',
           'publisher': '문학동네',
           'salesPoint': 5632,
           'stockStatus': '',
           'subInfo': {},
           'title': '오 자히르'},
          {'adult': False,
           'author': '파울로 코엘료 (지은이), 민은영 (옮긴이)',
           'categoryId': 50920,
           'categoryName': '국내도서>소설/시/희곡>스페인/중남미소설',
           'cover': 'https://image.aladin.co.kr/product/4299/41/coversum/8954625177_3.jpg',
           'customerReviewRank': 7,
           'description': '2014년 파울로 코엘료의 신작. 완벽한 삶을 살아가던 삼십대 여성 린다가 위기를 통해 '
                          '진정한 사랑의 의미를 찾아나가는 과정을 담고 있다. 코엘료는 일상의 권태와 사랑의 불안정성 '
                          '앞에 위태로운 여성의 마음을 청진하듯 짚어내며, 우리가 잊고 있던 삶의 의미와 사랑의 '
                          '소중함에 대해 이야기한다.',
           'fixedPrice': True,
           'isbn': '8954625177',
           'isbn13': '9788954625173',
           'itemId': 42994129,
           'link': 'http://www.aladin.co.kr/shop/wproduct.aspx?ItemId=42994129&amp;partner=openAPI&amp;start=api',
           'mallType': 'BOOK',
           'mileage': 690,
           'priceSales': 12420,
           'priceStandard': 13800,
           'pubDate': '2014-07-25',
           'publisher': '문학동네',
           'salesPoint': 5407,
           'stockStatus': '',
           'subInfo': {},
           'title': '불륜'},
          {'adult': False,
           'author': '파울로 코엘료 (지은이), 박명숙 (옮긴이)',
           'categoryId': 51373,
           'categoryName': '국내도서>에세이>외국에세이',
           'cover': 'https://image.aladin.co.kr/product/1328/67/coversum/8954616003_2.jpg',
           'customerReviewRank': 9,
           'description': '2006년 국내에 소개된 파울로 코엘료의 &lt;순례자&gt;(1987)가 신작 '
                          '&lt;알레프&gt;의 출간과 함께 새 옷을 입고 독자들에게 선보인다. '
                          '&lt;순례자&gt;는 파울로 코엘료의 데뷔작이자 그를 세계적인 작가의 반열에 올린 '
                          '&lt;연금술사&gt;의 모태가 되는 작품이다. 방황하던 한 사람이 기적과도 같은 변화의 '
                          '과정을 거쳐 깨달음에 이르는 여정을 담고 있다.',
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
           'description': '빠르게 변화하는 세상에서 사람들은 자신의 가치와 의미를 잃어버리기 쉽다. 너무 많은 비교 '
                          '대상과 넘어야 할 산을 보며 때로는 우울하고 불안하기만 하다. 전 세계에서 가장 많이 번역된 '
                          "작가, 파울로 코엘료가 '나'를 사랑하는 일에 서툰 사람들을 위한 신작 에세이를 출간했다.",
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
           'salesPoint': 3557,
           'stockStatus': '',
           'subInfo': {},
           'title': '내가 빛나는 순간'},
          {'adult': False,
           'author': '파울로 코엘료 (지은이), 김동성 (그림), 민은영 (옮긴이)',
           'categoryId': 50920,
           'categoryName': '국내도서>소설/시/희곡>스페인/중남미소설',
           'cover': 'https://image.aladin.co.kr/product/27652/38/coversum/8954681565_1.jpg',
           'customerReviewRank': 8,
           'description': '활쏘기로 최고의 경지에 오른 이방인이 먼길을 돌아 전설적인 명궁 ‘진’을 찾아오며 이야기는 '
                          '시작된다. 이방인은 진에게 도전해 현재 그의 명성을 자신의 것으로 만들고 싶어한다. 진은 '
                          '이방인의 도전을 받아들이고, 대결을 통해 그에게 단순한 기술보다 중요한 가르침을 전한다.',
           'fixedPrice': True,
           'isbn': '8954681565',
           'isbn13': '9788954681568',
           'itemId': 276523821,
           'link': 'http://www.aladin.co.kr/shop/wproduct.aspx?ItemId=276523821&amp;partner=openAPI&amp;start=api',
           'mallType': 'BOOK',
           'mileage': 700,
           'priceSales': 12600,
           'priceStandard': 14000,
           'pubDate': '2021-08-11',
           'publisher': '문학동네',
           'salesPoint': 3616,
           'stockStatus': '',
           'subInfo': {},
           'title': '아처'},
          {'adult': False,
           'author': '파울로 코엘료 (지은이), 오진영 (옮긴이)',
           'categoryId': 50920,
           'categoryName': '국내도서>소설/시/희곡>스페인/중남미소설',
           'cover': 'https://image.aladin.co.kr/product/9046/99/coversum/8954642012_2.jpg',
           'customerReviewRank': 8,
           'description': "삶의 지혜가 가득한 문장으로 전 세계 2억 독자들에게 따뜻한 위로와 감동을 전해온 '영혼의 "
                          "연금술사' 파울로 코엘료의 장편소설. 1차세계대전 당시 이중 스파이 혐의로 비극적인 최후를 "
                          "맞은 전설의 무희 '마타 하리'의 삶을 다룬 작품이다.",
           'fixedPrice': True,
           'isbn': '8954642012',
           'isbn13': '9788954642019',
           'itemId': 90469999,
           'link': 'http://www.aladin.co.kr/shop/wproduct.aspx?ItemId=90469999&amp;partner=openAPI&amp;start=api',
           'mallType': 'BOOK',
           'mileage': 620,
           'priceSales': 11250,
           'priceStandard': 12500,
           'pubDate': '2016-09-23',
           'publisher': '문학동네',
           'salesPoint': 3494,
           'stockStatus': '',
           'subInfo': {},
           'title': '스파이'},
          {'adult': False,
           'author': '파울로 코엘료 (지은이), 뫼비우스 (그림), 최정수 (옮긴이)',
           'categoryId': 50920,
           'categoryName': '국내도서>소설/시/희곡>스페인/중남미소설',
           'cover': 'https://image.aladin.co.kr/product/60/41/coversum/8954600565_2.jpg',
           'customerReviewRank': 9,
           'description': "세상을 두루 여행하기 위해 양치기가 된 청년 산티아고의 '자아의 신화' 찾기 여행담, 파울로 "
                          '코엘료의 장편소설 <연금술사>의 일러스트레이션판이 출간되었다. 삽화를 담당한 뫼비우스는 '
                          '<연금술사>의 표지 그림을 그렸던 일러스트레이터. 소설의 주요 장면들을 솜씨 좋게 포착한 '
                          '컬러 삽화가, 각각 독립된 페이지에 실려 있다.',
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
           'author': '파울로 코엘료 (지은이), 이수은 (옮긴이)',
           'categoryId': 50920,
           'categoryName': '국내도서>소설/시/희곡>스페인/중남미소설',
           'cover': 'https://image.aladin.co.kr/product/41/31/coversum/8982816593_1.gif',
           'customerReviewRank': 7,
           'description': '<연금술사>로 세계적인 베스트셀러 작가가 된 파울로 코엘료의 1994년 작. 스페인 '
                          '마드리드에서 출발, 피레네 산맥을 넘어 프랑스의 생사뱅과 루르드를 거쳐 피에트라 강가에서 '
                          "끝나는 이 '순례기'는 일주일의 기간 동안 한 여자와 한 남자에게 일어나는 '삶의 기적'에 "
                          '관한 이야기이다.',
           'fixedPrice': True,
           'isbn': '8982816593',
           'isbn13': '9788982816598',
           'itemId': 413188,
           'link': 'http://www.aladin.co.kr/shop/wproduct.aspx?ItemId=413188&amp;partner=openAPI&amp;start=api',
           'mallType': 'BOOK',
           'mileage': 570,
           'priceSales': 10350,
           'priceStandard': 11500,
           'pubDate': '2003-05-03',
           'publisher': '문학동네',
           'salesPoint': 3177,
           'stockStatus': '',
           'subInfo': {},
           'title': '피에트라 강가에서 나는 울었네'},
          {'adult': False,
           'author': '파울로 코엘료 (지은이), 오진영 (옮긴이)',
           'categoryId': 50920,
           'categoryName': '국내도서>소설/시/희곡>스페인/중남미소설',
           'cover': 'https://image.aladin.co.kr/product/1303/6/coversum/8954616127_3.jpg',
           'customerReviewRank': 9,
           'description': '&lt;연금술사&gt; &lt;브리다&gt;의 작가 파울로 코엘료의 2011년 신작. 작가의 '
                          '길에 들어선 지 20여 년이 훌쩍 넘은 파울로 코엘료의 세계를 아우르는 동시에, 자신의 '
                          '근본으로 회귀함으로써 새로운 출발을 알리는 작품이다. 코엘료의 고국인 브라질을 시작으로, '
                          '포르투갈, 헝가리 등 20여 국에서 출간되어 출간 첫날 즉시 베스트셀러 1위에 올라 변함없이 '
                          '코엘료 신드롬을 일으켰다.',
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
           'author': '파울로 코엘료 (지은이), 공보경 (옮긴이)',
           'categoryId': 50920,
           'categoryName': '국내도서>소설/시/희곡>스페인/중남미소설',
           'cover': 'https://image.aladin.co.kr/product/3025/29/coversum/8954620973_1.jpg',
           'customerReviewRank': 8,
           'description': '파울로 코엘료 소설. 2010년 발표한 &lt;알레프&gt;가 코엘료 자신을 시베리아 횡단 '
                          '열차에 오르게 했던 정체성의 위기에 관해 다루고 있다면, &lt;아크라 문서&gt;는 그 '
                          '위기를 극복하는 과정에서 얻은 소중한 결론들을 집대성한 작품이라고 볼 수 있다.',
           'fixedPrice': True,
           'isbn': '8954620973',
           'isbn13': '9788954620970',
           'itemId': 30252913,
           'link': 'http://www.aladin.co.kr/shop/wproduct.aspx?ItemId=30252913&amp;partner=openAPI&amp;start=api',
           'mallType': 'BOOK',
           'mileage': 640,
           'priceSales': 11520,
           'priceStandard': 12800,
           'pubDate': '2013-09-05',
           'publisher': '문학동네',
           'salesPoint': 3026,
           'stockStatus': '',
           'subInfo': {},
           'title': '아크라 문서'},
          {'adult': False,
           'author': '파울로 코엘료 (지은이), 임호경 (옮긴이)',
           'categoryId': 50920,
           'categoryName': '국내도서>소설/시/희곡>스페인/중남미소설',
           'cover': 'https://image.aladin.co.kr/product/418/76/coversum/8954608485_2.jpg',
           'customerReviewRank': 8,
           'description': '"꿈을 이루기 위해 당신은 어디까지 갈 수 있습니까?" <연금술사>의 작가, 마법적 이야기꾼 '
                          '파울로 코엘료의 2009년 신작! 칸 영화제를 배경으로 24시간 동안 펼쳐지는 숨가쁜 '
                          '이야기를 그린 작품. 명성의 정상에 서 있는 사람들과 그들의 자리에 오르기 위해 발버둥치는 '
                          "사람들의 이야기가 담겨 있다. 프랑스 DNA는 '위대한 고전 비극을 연상시키는 작품'이라 "
                          '평하기도 했다.',
           'fixedPrice': True,
           'isbn': '8954608485',
           'isbn13': '9788954608480',
           'itemId': 4187698,
           'link': 'http://www.aladin.co.kr/shop/wproduct.aspx?ItemId=4187698&amp;partner=openAPI&amp;start=api',
           'mallType': 'BOOK',
           'mileage': 600,
           'priceSales': 10800,
           'priceStandard': 12000,
           'pubDate': '2009-07-25',
           'publisher': '문학동네',
           'salesPoint': 3003,
           'stockStatus': '',
           'subInfo': {},
           'title': '승자는 혼자다 1'},
          {'adult': False,
           'author': '파울로 코엘료 (지은이), 오진영 (옮긴이)',
           'categoryId': 50920,
           'categoryName': '국내도서>소설/시/희곡>스페인/중남미소설',
           'cover': 'https://image.aladin.co.kr/product/29733/11/coversum/8954687482_1.jpg',
           'customerReviewRank': 9,
           'description': '긴 터널 같은 시기를 견디고 자신의 진정한 꿈을 향해 나아가 결국 세계적인 작가로 거듭난 '
                          '그는, 자신의 삶에서 영감을 얻어 써내려간 이 소설 속에 “피할 수 없는 시련은 인생의 '
                          '형벌이 아닌 도전”이라는 살아 있는 메시지를 담아냈다.',
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
           'title': '다섯번째 산'},
          {'adult': False,
           'author': '파울로 코엘료 (지은이), 이상해 (옮긴이)',
           'categoryId': 50920,
           'categoryName': '국내도서>소설/시/희곡>스페인/중남미소설',
           'cover': 'https://image.aladin.co.kr/product/43/58/coversum/8982816860_1.gif',
           'customerReviewRank': 8,
           'description': '이 소설의 무대는 프랑스의 산골마을 베스코스. 그곳에 낯선 이방인이 찾아오면서 이야기가 '
                          '시작된다. 이방인은 마을 호텔의 여종업원인 미스 프랭에게 막대한 양의 금괴를 보여주며, 마을 '
                          '사람들의 목숨을 담보로 한 제안을 하고, 순박한 베스코스 주민들은 선악에 관한 악마의 시험을 '
                          '치르게 되는데...',
           'fixedPrice': True,
           'isbn': '8982816860',
           'isbn13': '9788982816864',
           'itemId': 435867,
           'link': 'http://www.aladin.co.kr/shop/wproduct.aspx?ItemId=435867&amp;partner=openAPI&amp;start=api',
           'mallType': 'BOOK',
           'mileage': 750,
           'priceSales': 13500,
           'priceStandard': 15000,
           'pubDate': '2003-10-10',
           'publisher': '문학동네',
           'salesPoint': 2790,
           'stockStatus': '',
           'subInfo': {},
           'title': '악마와 미스 프랭'},
          {'adult': False,
           'author': '파울로 코엘료 (지은이), 최정수 (옮긴이)',
           'categoryId': 50920,
           'categoryName': '국내도서>소설/시/희곡>스페인/중남미소설',
           'cover': 'https://image.aladin.co.kr/product/31892/47/coversum/8954692796_1.jpg',
           'customerReviewRank': 0,
           'description': '전 세계 8천 5백만 독자의 사랑을 받은 베스트셀러이자 파울로 코엘료를 세계적인 작가의 '
                          '반열에 오르게 한 기념비적 작품. 마음의 목소리에 귀기울이는 것이 얼마나 중요한지 증언하는 '
                          '성서와도 같은 이 책은 진정 자기 자신의 꿈과 대면하고자 하는 모든 이를 축복하는 희망과 '
                          '환희의 메시지를 전한다.',
           'fixedPrice': True,
           'isbn': '8954692796',
           'isbn13': '9788954692793',
           'itemId': 318924713,
           'link': 'http://www.aladin.co.kr/shop/wproduct.aspx?ItemId=318924713&amp;partner=openAPI&amp;start=api',
           'mallType': 'BOOK',
           'mileage': 600,
           'priceSales': 10800,
           'priceStandard': 12000,
           'pubDate': '2023-06-14',
           'publisher': '문학동네',
           'salesPoint': 2676,
           'seriesInfo': {'seriesId': 1124477,
                          'seriesLink': 'http://www.aladin.co.kr/shop/common/wseriesitem.aspx?SRID=1124477&amp;partner=openAPI',
                          'seriesName': '문학동네 30주년 기념 특별판 '},
           'stockStatus': '',
           'subInfo': {},
           'title': '연금술사 (문학동네 30주년 기념 특별판)'}],
 'itemsPerPage': 20,
 'link': 'http://www.aladin.co.kr/search/wsearchresult.aspx?KeyAuthor=%c6%c4%bf%ef%b7%ce+%c4%da%bf%a4%b7%e1&amp;SearchTarget=book&amp;partner=openAPI',
 'logo': 'http://image.aladin.co.kr/img/header/2011/aladin_logo_new.gif',
 'pubDate': 'Fri, 26 Jul 2024 15:05:09 GMT',
 'query': '파울로 코엘료',
 'searchCategoryId': 0,
 'searchCategoryName': '전체',
 'startIndex': 1,
 'title': '알라딘 검색결과 - 파울로 코엘료',
 'totalResults': 44,
 'version': '20131101'}
 '''