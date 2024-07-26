import requests
from pprint import pprint


def get_author_other_books(title):
    # 여기에 코드를 작성합니다.
    URL = 'http://www.aladin.co.kr/ttb/api/ItemSearch.aspx'
    api_key = 'ttbyts02751555001'

    params = {
    'ttbkey': {api_key},
    'Query': {title},
    'QueryType': 'Title',
    'MaxResults': 1,
    'start': 1,
    'SearchTarget': 'Book',
    'output': 'js',
    'Version': '20131101',
    }

    info_response = requests.get(URL, params=params)
    info_response = info_response.json()

    try:
        # 자료의 author 값 '윌리엄 셰익스피어 (지은이), 최종철 (옮긴이) 형식을 '윌리엄 셰익스피어'로 슬라이싱
        authors = info_response['item'][0]['author']
        author = authors.split(', ')[0][:-6]

        # 출력에 사용할 title 변수 할당
        title = info_response['item'][0]['title']

        # 지은이 명으로 도서 재검색, 첫 도서와 중복이 있을 경우에 대비해 6개를 요청
        params_2 = {
            'ttbkey': {api_key},
            'Query': {author},
            'QueryType': 'Author',
            'MaxResults': 6,
            'start': 1,
            'SearchTarget': 'Book',
            'output': 'js',
            'Version': '20131101',
            }
        
        author_response = requests.get(URL, params=params_2)
        author_response = author_response.json()

        # 도서명 리스트에 담기
        research_list = []
        for research_i in range(len(author_response['item'])):
            research_list.append(author_response['item'][research_i]['title'])

        # 6개의 도서 중 title과 중복되는 것이 있다면 제거
        if title in research_list:
            research_list.remove(title)
        final_research_list = research_list[:5]

        # 출력 형식에 맞춰 변환 후 리턴
        result = {f'"{title}"의 저자 "{author}"의 다른 도서 목록': final_research_list}
        
        return result
        
    # 검색된 도서가 없어 IndexError가 발생할 경우에는 None을 반환토록 함
    except IndexError:
        return None


'''
{'item': [{'adult': False,
           'author': '윌리엄 셰익스피어 (지은이), 최종철 (옮긴이)',
           'categoryId': 51212,
           'categoryName': '국내도서>소설/시/희곡>희곡>외국희곡',
           'cover': 'https://image.aladin.co.kr/product/857/94/coversum/8937462621_2.jpg',
           'customerReviewRank': 8,
           'description': "'민음사 세계문학전집' 262권. 셰익스피어가 32세 무렵이던 1596~1597년에 쓴 비교적 초기 작품으로, 주인공인 '베니스의 상인' 외에도 유대인 샤일록과 "
                          '지혜로운 여성 포셔까지 모든 인물들의 개성이 돋보이는 희비극이다. 1605년에 초연된 후 지금까지 수없이 공연되었으며, 각각의 인물의 시건으로 다양한 해석이 '
                          '이루어졌다.',
           'fixedPrice': True,
           'isbn': '8937462621',
           'isbn13': '9788937462627',
           'itemId': 8579428,
           'link': 'http://www.aladin.co.kr/shop/wproduct.aspx?ItemId=8579428&amp;partner=openAPI&amp;start=api',
           'mallType': 'BOOK',
           'mileage': 450,
           'priceSales': 8100,
           'priceStandard': 9000,
           'pubDate': '2010-12-28',
           'publisher': '민음사',
           'salesPoint': 5969,
           'seriesInfo': {'seriesId': 13679,
                          'seriesLink': 'http://www.aladin.co.kr/shop/common/wseriesitem.aspx?SRID=13679&amp;partner=openAPI',
                          'seriesName': '민음사 세계문학전집 262'},
           'stockStatus': '',
           'subInfo': {},
           'title': '베니스의 상인'}],
 'itemsPerPage': 1,
 'link': 'http://www.aladin.co.kr/search/wsearchresult.aspx?KeyTitle=%ba%a3%b4%cf%bd%ba%c0%c7+%bb%f3%c0%ce&amp;SearchTarget=book&amp;partner=openAPI',
 'logo': 'http://image.aladin.co.kr/img/header/2011/aladin_logo_new.gif',
 'pubDate': 'Fri, 26 Jul 2024 15:58:23 GMT',
 'query': '베니스의 상인',
 'searchCategoryId': 0,
 'searchCategoryName': '전체',
 'startIndex': 1,
 'title': '알라딘 검색결과 - 베니스의 상인',
 'totalResults': 135,
 'version': '20131101'}
{'item': [{'adult': False,
           'author': '표도르 도스토옙스키 (지은이), 김연경 (옮긴이)',
           'categoryId': 52650,
           'categoryName': '국내도서>소설/시/희곡>러시아소설',
           'cover': 'https://image.aladin.co.kr/product/1621/17/coversum/8937462842_3.jpg',
           'customerReviewRank': 9,
           'description': "'민음사 세계문학전집' 284~285권. 러시아의 대문호 도스토예프스키가 사형선고에 이은 8년간의 유형 생활 후 두 번째로 발표한 작품이다. 전작 "
                          "&lt;지하로부터의 수기&gt;에서 싹튼 새로운 '인물 유형'과 소설 기법이 바로 이 소설에서 만개하여, 인간의 가장 깊은 곳에 숨겨진 심리가 낱낱이 파헤쳐진다.",
           'fixedPrice': True,
           'isbn': '8937462842',
           'isbn13': '9788937462849',
           'itemId': 16211750,
           'link': 'http://www.aladin.co.kr/shop/wproduct.aspx?ItemId=16211750&amp;partner=openAPI&amp;start=api',
           'mallType': 'BOOK',
           'mileage': 550,
           'priceSales': 9900,
           'priceStandard': 11000,
           'pubDate': '2012-03-30',
           'publisher': '민음사',
           'salesPoint': 17625,
           'seriesInfo': {'seriesId': 13679,
                          'seriesLink': 'http://www.aladin.co.kr/shop/common/wseriesitem.aspx?SRID=13679&amp;partner=openAPI',
                          'seriesName': '민음사 세계문학전집 284'},
           'stockStatus': '',
           'subInfo': {},
           'title': '죄와 벌 1'}],
 'itemsPerPage': 1,
 'link': 'http://www.aladin.co.kr/search/wsearchresult.aspx?KeyTitle=%c1%cb%bf%cd+%b9%fa&amp;SearchTarget=book&amp;partner=openAPI',
 'logo': 'http://image.aladin.co.kr/img/header/2011/aladin_logo_new.gif',
 'pubDate': 'Fri, 26 Jul 2024 15:58:23 GMT',
 'query': '죄와 벌',
 'searchCategoryId': 0,
 'searchCategoryName': '전체',
 'startIndex': 1,
 'title': '알라딘 검색결과 - 죄와 벌',
 'totalResults': 143,
 'version': '20131101'}
{'item': [],
 'itemsPerPage': 1,
 'link': 'http://www.aladin.co.kr/search/wsearchresult.aspx?KeyTitle=*&amp;SearchTarget=book&amp;partner=openAPI',
 'logo': 'http://image.aladin.co.kr/img/header/2011/aladin_logo_new.gif',
 'pubDate': 'Fri, 26 Jul 2024 15:58:23 GMT',
 'query': '*',
 'searchCategoryId': 0,
 'searchCategoryName': '전체',
 'startIndex': 1,
 'title': '알라딘 검색결과 - *',
 'totalResults': 0,
 'version': '20131101'}
 '''


# 아래 코드는 수정하지 않습니다.
if __name__ == '__main__':
    pprint(get_author_other_books('베니스의 상인'), width=120)
    pprint(get_author_other_books('죄와 벌'), width=120)
    pprint(get_author_other_books('*'), width=120)

'''
{'"베니스의 상인"의 저자 "윌리엄 셰익스피어"의 다른 도서 목록': ['햄릿',
                                         '셰익스피어 4대 비극 세트 : 햄릿.오셀로.맥베스.리어 왕 - 전4권',
                                         '맥베스',
                                         '로미오와 줄리엣',
                                         '셰익스피어 4대 비극 에디션 세트 - 전4권 (리커버 특별판) - 햄릿 + 오셀로 + 리어 왕 + 맥베스']}
{'"죄와 벌 1"의 저자 "표도르 도스토옙스키"의 다른 도서 목록': ['가난한 사람들', '카라마조프 가의 형제들 세트 - 전3권', '죄와 벌 2', '죄와 벌 - 상', '죄와 벌 - 하']}
None
'''