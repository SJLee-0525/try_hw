import json
from pprint import pprint


def books_info(books, categories):
    # 카테고리 id를 key로, name을 value로 하는 dict 생성
    categories_info = {}
    for category in categories:
        categories_info[category['id']] = category['name']
    # {31916: '과학', 31908: '에세이 / 수필', 151138: '자기계발', ... 51449: '윤리학', 2721: '컴퓨터 공학'}

    new_books_info_list = []
    for book in books:  
        # categoryId의 id 값을 name 값으로 바꾸기
        for i in range(len(book['categoryId'])):
            book['categoryId'][i] = categories_info[book['categoryId'][i]]

        new_book_info = {
            'id': book.get('id'),
            'title': book.get('title'),
            'author': book.get('author'),
            'priceSales':  book.get('priceSales'),
            'description': book.get('description'),
            'cover': book.get('cover'),
            'categoryName': book.get('categoryId'),
            }

        new_books_info_list.append(new_book_info)
    
    return new_books_info_list


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    books_json = open('data/books.json', encoding='utf-8')
    books = json.load(books_json)

    categories_json = open('data/categories.json', encoding='utf-8')
    categories_list = json.load(categories_json)

    pprint(books_info(books, categories_list))

# [{'author': '제인 오스틴 (지은이), 윤지관, 전승희 (옮긴이)',
#   'categoryName': ['문학', '영미소설'],
#   'cover': 'https://image.aladin.co.kr/product/43/68/coversum/8937460882_3.jpg',
#   'description': '제인 오스틴의 대표작 <오만과 편견>이 보다 정확하고 말끔한 번역으로 재출간됐다. 역자인 윤지관과 전승희는 '
#                  '10여 년에 걸친 기간 동안 철저한 원문대조를 통해, 본래의 의미와 문체를 생생하게 되살려내기 위해 '
#                  '노력했다고.',
#   'id': 436838,
#   'priceSales': 11700,
#   'title': '오만과 편견'},
#  {'author': '어니스트 헤밍웨이 (지은이), 김욱동 (옮긴이)',
#   'categoryName': ['문학', '영미소설'],
#   'cover': 'https://image.aladin.co.kr/product/1452/24/coversum/8937462788_2.jpg',
#   'description': '노벨 문학상, 퓰리처상 수상 작가, 20세기 미국 문학을 개척한 작가 어니스트 헤밍웨이의 대표작. 미국 현대 '
#                  "문학의 개척자라 불리는 헤밍웨이는 제1차 세계대전 후 삶의 좌표를 잃어버린 '길 잃은 세대'를 대표하는 "
#                  "작가이다. '민음사 세계문학전집' 278권으로 출간된 &lt;노인과 바다&gt;는 헤밍웨이의 마지막 소설로, "
#                  '작가 고유의 소설 수법과 실존 철학이 짧은 분량 안에 집약되어 있다.',
#   'id': 14522431,
#   'priceSales': 7200,
#   'title': '노인과 바다'},
#  {'author': '서머싯 몸 (지은이), 송무 (옮긴이)',
#   'categoryName': ['문학', '영미소설'],
#   'cover': 'https://image.aladin.co.kr/product/23/77/coversum/s692639624_1.jpg',
#   'description': '<달과 6펜스>는 15종에 이르는 번역본이 이미 소개되어 있을 만큼 국내에서 크게 환영받는 작품이다. 이 '
#                  '작품은 서머싯 몸을 전세계에 널리 알린 결정적인 작품으로 제1차 세계대전이 끝난 이듬해인 1919년에 '
#                  '출판되어 대단한 인기를 끌었다.',
#   'id': 237763,
#   'priceSales': 9000,
#   'title': '달과 6펜스'},
#  {'author': '올더스 헉슬리 (지은이), 안정효 (옮긴이)',
#   'categoryName': ['문학', '외국 과학소설'],
#   'cover': 'https://image.aladin.co.kr/product/6083/61/coversum/8973814729_2.jpg',
#   'description': '올더스 헉슬리는 명문 집안 출신의 영국 작가로서 광범위한 지식뿐 아니라 예리한 지성과 우아한 문체, 그리고 '
#                  '때로는 냉소적인 유머 감각으로 유명하다. 그가 1932년에 발표한 작품 &lt;멋진 신세계&gt;는 금세기에 '
#                  '미래를 가장 깊이 있고 날카롭게 파헤친 작품 중의 하나로 평가받는다.',
#   'id': 60836103,
#   'priceSales': 12420,
#   'title': '멋진 신세계'},
#  {'author': '헤르만 헤세 (지은이), 박지희 (옮긴이), 김선형 (해설)',
#   'categoryName': ['문학', '독일소설'],
#   'cover': 'https://image.aladin.co.kr/product/9870/83/coversum/k822535559_2.jpg',
#   'description': '성적 위주의 교육 속에서 경쟁에 지쳐 자신을 잃어버린 모든 이들에게 공감과 위로를 전하는 &lt;수레바퀴 '
#                  '아래서&gt;는 헤르만 헤세 자신의 청소년기를 반영한 자전적 소설이다. 이제 &lt;수레바퀴 아래서&gt;를 '
#                  '1906년 오리지널 초판본 표지로 만나 보자.',
#   'id': 98708362,
#   'priceSales': 2970,
#   'title': '수레바퀴 아래서'},
#  {'author': '론다 번 (지은이), 김우열 (옮긴이)',
#   'categoryName': ['자기계발', '성공학'],
#   'cover': 'https://image.aladin.co.kr/product/92/71/coversum/8952206509_2.jpg',
#   'description': "2007년 '아마존' 최고의 화제작. 출간하자마자 아마존 베스트셀러 목록에 올랐고, <오프라 윈프리 쇼>에서 "
#                  "소개되었다. 방송 후 시청자들의 폭발적인 반응에 오프라 홈페이지마저 마비되었고, 결국 책은 미국에서 '가장 "
#                  "짧은 시간에 가장 많이 팔린 책'이 되어버렸다.",
#   'id': 927185,
#   'priceSales': 15120,
#   'title': '시크릿 - 수 세기 동안 단 1%만이 알았던 부와 성공의 비밀'},
#  {'author': '켈리 최 (지은이)',
#   'categoryName': ['자기계발', '성공학'],
#   'cover': 'https://image.aladin.co.kr/product/28273/37/coversum/s242836112_3.jpg',
#   'description': '부를 창조한 사람들이 갖고 있는 생각의 뿌리를 이해하고 체득하기 위해 ‘풍요의 생각’을 이야기하는 책이다. '
#                  '풍요의 생각은 결핍의 생각과 반대되는 개념이다. 풍요의 생각이나 결핍의 생각이나 모두 에너지이지만, 그 '
#                  '방향성은 정반대다.',
#   'id': 282733777,
#   'priceSales': 14400,
#   'title': '웰씽킹 WEALTHINKING (양장) - 부를 창조하는 생각의 뿌리'},
#  {'author': '황농문 (지은이)',
#   'categoryName': ['자기계발', '성공학'],
#   'cover': 'https://image.aladin.co.kr/product/102/9/coversum/s552832633_2.jpg',
#   'description': "'몰입'은 잠재된 우리의 두뇌 능력을 일깨워 능력을 극대화하고 삶의 만족도를 최고로 끌어올리는 방법이다. "
#                  "책은 '왜 우리가 몰입적 사고를 해야 하는지', '어떻게 몰입으로 천재성을 끄집어낼 수 있는지'에 대해 "
#                  '구체적인 해답을 제시한다.',
#   'id': 1020939,
#   'priceSales': 16200,
#   'title': '몰입 : 인생을 바꾸는 자기 혁명 - Think Hard!'},
#  {'author': '지니 킴 (지은이)',
#   'categoryName': ['자기계발', '육아 일반'],
#   'cover': 'https://image.aladin.co.kr/product/31744/45/coversum/k862833807_1.jpg',
#   'description': '아동발달 전문가이자 교육자인 지니 킴(Jeanie Kim) 박사는 회복탄력성은 모두 갖고 태어나고, '
#                  '어려서부터 반복과 연습을 통해 누구나 기를 수 있다고 강조하며, 긍정성, 자기 신뢰, 자기조절능력 같은 '
#                  '회복탄력성의 자원을 아이의 삶에 뿌리내리게 하는 방법들을 구체적으로 안내한다.',
#   'id': 317444541,
#   'priceSales': 16020,
#   'title': '회복탄력성의 힘 - 쉽게 포기하지 않고 결국 해내는 아이의 비밀'},
#  {'author': '서현 (지은이)',
#   'categoryName': ['에세이 / 수필', '건축'],
#   'cover': 'https://image.aladin.co.kr/product/3808/42/coversum/895872126x_1.jpg',
#   'description': '1998년 출간된 &lt;건축, 음악처럼 듣고 미술처럼 보다&gt;의 재개정판이다. 서울대학교 미술관, '
#                  'ECCEhwa Culture Complex, 쌈지길 세 곳은 그 훌륭한 가치와 의미를 전달해야 했기에 기꺼이 '
#                  '새로 추가해 서현 특유의 해석법으로 풀어나갔다.',
#   'id': 38084277,
#   'priceSales': 16200,
#   'title': '건축, 음악처럼 듣고 미술처럼 보다 - 인문적 건축이야기'},
#  {'author': '유현준 (지은이)',
#   'categoryName': ['에세이 / 수필', '건축'],
#   'cover': 'https://image.aladin.co.kr/product/5518/24/coversum/8932472955_1.jpg',
#   'description': '도시는 단순히 건축물이나 공간들을 모아 놓은 곳이 아니다. 도시는 인간의 삶이 반영되기 때문에 인간이 '
#                  '추구하는 것과 욕망이 드러난다. 이 책은 자신들이 만든 도시에 인간의 삶이 어떻게 영향을 받는지, 과연 더 '
#                  '행복해지는지 아니면 피폐해지고 있는지 도시의 답변을 들려준다.',
#   'id': 55182423,
#   'priceSales': 13500,
#   'title': '도시는 무엇으로 사는가 - 도시를 보는 열다섯 가지 인문적 시선'},
#  {'author': '사뮈엘 베케트 (지은이), 오증자 (옮긴이)',
#   'categoryName': ['문학', '프랑스 문학'],
#   'cover': 'https://image.aladin.co.kr/product/25/65/coversum/8937460432_3.jpg',
#   'description': "'고도'의 의미는 이 작품을 읽고자 하는 사람들의 상황과 처지에 따라 자유롭게 해석될 수 있는 것으로, 이 "
#                  '점에서 <고도를 기다리며>는 철저하게 관객을 향해 열려있는 작품이라고 할 수 있겠다. 이 때문에 <고도를 '
#                  '기다리며>는 지금까지도 학인들의 연구대상이 될 수 있었으며, 또한 삶의 질곡으로 고통받는 이들에게는 생의 '
#                  '비밀을 깨닫게 하는 계기가 되었던 것이다.',
#   'id': 256532,
#   'priceSales': 8100,
#   'title': '고도를 기다리며'},
#  {'author': '에른스트 H. 곰브리치 (지은이), 백승길, 이종숭 (옮긴이)',
#   'categoryName': ['에세이 / 수필', '미술사'],
#   'cover': 'https://image.aladin.co.kr/product/7/57/coversum/8970840656_2.jpg',
#   'description': '지금까지 출간된 미술에 관한 가장 유명한 책 중의 하나. 1950년 영국에서 초판이 간행된 이래 전세계에서 '
#                  '서양미술사 개론의 필독서로 자리잡고 있다. 미술의 역사란 과거와의 연관 속에서 미래를 암시하는 각 작품들로 '
#                  '끊임없이 구성되고 변화하는 전통의 역사라는 것이 지은이의 믿음이다. 우리가 살고 있는 이 시대와 이집트에 '
#                  '피라미드가 건설되었던 그 시대가 생생하게 연결되어 있음을 이 책은 보여준다.',
#   'id': 75760,
#   'priceSales': 34200,
#   'title': '서양미술사'},
#  {'author': '유발 하라리 (지은이), 조현욱 (옮긴이), 이태수 (감수)',
#   'categoryName': ['에세이 / 수필', '인류학'],
#   'cover': 'https://image.aladin.co.kr/product/31424/4/coversum/k482832219_1.jpg',
#   'description': '2011년 원서 출간 이후 10년을 돌아보고 위기 상황을 맞은 인류에게 건네는 제언이 특별 서문으로 '
#                  '수록되었다. 현재 인류는 그 어느 때보다 어려운 상황을 맞고 있다. 난국을 헤쳐나가기 위해 무엇을 해야 '
#                  '할까? 저자는 더 나은 세상을 위한 키워드로 ‘인간 이해’를 강조한다.',
#   'id': 314240466,
#   'priceSales': 24120,
#   'title': '사피엔스 - 유인원에서 사이보그까지, 인간 역사의 대담하고 위대한 질문'},
#  {'author': '리처드 도킨스 (지은이), 홍영남, 이상임 (옮긴이)',
#   'categoryName': ['인류학', '생명과학'],
#   'cover': 'https://image.aladin.co.kr/product/17048/25/coversum/8932473900_1.jpg',
#   'description': '과학을 넘어선 우리 시대의 고전, 『이기적 유전자』 40주년 기념판. 진화론의 새로운 패러다임을 제시한 이 '
#                  '책은 다윈의 ‘적자생존과 자연선택’이라는 개념을 유전자 단위로 끌어내려 진화를 설명한다.',
#   'id': 170482558,
#   'priceSales': 18000,
#   'title': '이기적 유전자'},
#  {'author': '칼 세이건 (지은이), 홍승수 (옮긴이)',
#   'categoryName': ['에세이 / 수필', '우주과학'],
#   'cover': 'https://image.aladin.co.kr/product/87/9/coversum/s922637499_3.jpg',
#   'description': '칼 세이건의 <코스모스> 특별판이 세이건의 서거 10주기를 기념하여 출간되었다. 이 특별판은 지난 2004년 '
#                  '12월에 출간된 <코스모스>(양장본)의 텍스트 전문과 도판 일부를 사용하고 판형을 휴대하기 쉬운 신국판으로 '
#                  '바꿔 출간한 책으로, 독자들이 좀 더 쉽게 칼 세이건의 메시지를 만날 수 있도록 배려한 책이다.',
#   'id': 870950,
#   'priceSales': 17910,
#   'title': '코스모스'},
#  {'author': '알베르 카뮈 (지은이), 김화영 (옮긴이)',
#   'categoryName': ['문학', '철학'],
#   'cover': 'https://image.aladin.co.kr/product/21224/66/coversum/8937443848_1.jpg',
#   'description': "'민음사 세계문학전집' 266권. 20세기의 지성이자 실존주의 문학의 대표 작가, 알베르 카뮈의 대표작. "
#                  '1942년 &lt;이방인&gt;이 처음 발표되었을 때, 카뮈는 젊은 무명작가에 불과했다. 낯선 인물과 '
#                  '독창적인 형식으로 현대 프랑스 문단에 이방인처럼 나타난 이 소설은 출간 이후 한순간도 프랑스 베스트셀러 '
#                  '목록에서 빠진 적이 없는 걸작이 되었다.',
#   'id': 212246612,
#   'priceSales': 9000,
#   'title': '이방인'},
#  {'author': '마이클 샌델 (지은이), 김명철 (옮긴이), 김선욱 (감수)',
#   'categoryName': ['서양철학', '윤리학'],
#   'cover': 'https://image.aladin.co.kr/product/31517/61/coversum/k102832536_1.jpg',
#   'description': '마이클 샌델은 구제 금융, 대리 출산, 동성 결혼, 과거사 공개 사과 등 현대 사회에서 우리가 흔히 부딪히는 '
#                  '문제를 통해 ‘무엇이 정의로운가’에 대한 해답을 탐구했다. 이 책은 탁월한 정치 철학자들이 남긴 시대를 '
#                  '초월한 철학적인 질문을 알기 쉽게 소개한다.',
#   'id': 315176143,
#   'priceSales': 13500,
#   'title': '정의란 무엇인가'},
#  {'author': '조너선 스타인하트 (지은이), 오현석 (옮긴이)',
#   'categoryName': ['과학', '컴퓨터 공학'],
#   'cover': 'https://image.aladin.co.kr/product/26844/45/coversum/k942730395_1.jpg',
#   'description': '하드웨어의 토대가 되는 기초 전자회로, 게이트 등을 설명하고, 그 위에서 소프트웨어를 작성하는 방법을 웹과 '
#                  'C 프로그램으로 직접 만들어보며, 개발자라면 반드시 알아야 할 커튼 뒤에 감춰진 컴퓨터 구조와 프로그래밍에 '
#                  '대한 거의 모든 것을 다루는 컴퓨터공학 개론서다.',
#   'id': 268444562,
#   'priceSales': 31500,
#   'title': '한 권으로 읽는 컴퓨터 구조와 프로그래밍 - 더 나은 소프트웨어 개발을 위한 하드웨어, 자료구조, 필수 알고리즘 등 '
#            '프로그래머의 비밀 노트'},
#  {'author': '로버트 C. 마틴 (지은이), 이해영, 박재호 (옮긴이)',
#   'categoryName': ['과학', '컴퓨터 공학'],
#   'cover': 'https://image.aladin.co.kr/product/3408/36/coversum/8966260950_2.jpg',
#   'description': '로버트 마틴은 이 책에서 혁명적인 패러다임을 제시한다. 그는 오브젝트 멘토(Object Mentor)의 '
#                  '동료들과 힘을 모아 ‘개발하며’ 클린 코드를 만드는 최상의 애자일 기법을 정제해 책 한 권에 담았다.',
#   'id': 34083680,
#   'priceSales': 29700,
#   'title': '클린 코드 Clean Code - 애자일 소프트웨어 장인 정신'}]