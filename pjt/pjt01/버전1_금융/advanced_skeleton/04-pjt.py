import pprint
import requests

# 상품과 옵션 정보들을 담고 있는 새로운 객체를 만들어 반환하시오.
# [힌트] 상품 리스트와 옵션 리스트를 금융상품 코드를 기준으로 매칭할 수 있습니다.
# [힌트] 아래와 같은 순서로 데이터를 출력하며 진행합니다.
# 1. 응답을 json 형식으로 변환합니다.
# 2. key 값이 "result" 인 데이터를 변수에 저장합니다.
# 3. 2번의 결과 중 key 값이 "baseList" 인 데이터를 변수에 저장합니다.
# 4. 2번의 결과 중 key 값이 "optionList" 인 데이터를 변수에 저장합니다.
# 5. 3번에서 저장된 변수를 순회하며, 4번에서 저장된 값들에서 금융 상품 코드가 
#     같은 모든 데이터들을 가져와 새로운 딕셔너리로 저장합니다.
#     저장 시, 명세서에 맞게 출력되도록 저장합니다.
# 6. 5번에서 만든 딕셔너리를 결과 리스트에 추가합니다.


def get_deposit_products():
    # 본인의 API KEY 로 수정합니다.
    api_key = '입력하세요'

    # 요구사항에 맞도록 이곳의 코드를 수정합니다.
    url = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo=1'

    result = []
    response = requests.get(url).json()

    fin_cd_list = []
    # 금융상품 코드들을 추출해서 fin_cd_list에 담음
    for i in range(len(response['result']['baseList'])):
        fin_cd_list.append(response['result']['baseList'][i]['fin_prdt_cd'])
    # ['WR0001B', '00320342', '10511008000996000', '10511008001004000', ... 10-01-20-388-0002', '1001202000002']

    temp_list_dict = {}
    # fin_cd_list에 들은 금융상품 코드들을 하나씩 가져옴
    for fin_cd in fin_cd_list:
        # baseList에 들은 리스트 요소들의 인덱스 추출
        for i in range(len(response['result']['baseList'])):
            # 만약 해당 인덱스 dict의 fin_prdt_cd value에 해당 금융상품 코드가 있다면?
            if fin_cd in response['result']['baseList'][i]['fin_prdt_cd']:
                company, product = response['result']['baseList'][i]['kor_co_nm'], response['result']['baseList'][i]['fin_prdt_nm']
                company, product = company.replace("\n", ""), product.replace("\n", "") # \n *엔터) 제거
                temp_list_dict[fin_cd] = company, product
                # key는 해당 금융상품 코드로, value는 tuple(회사명, 상품명)으로 할당
                # {'10511008001166004': ('아이엠뱅크', 'iM함께예금'), '06492': ('한국산업은행', 'KDB 정기예금'), ...}

    final_list = []
    # fin_cd_list에 들은 금융상품 코드들을 하나씩 가져옴
    for fin_cd in fin_cd_list:
        temp_dict = {}
        mini_temp_dict_list = []
        for i in range(len(response['result']['optionList'])):
            if fin_cd == response['result']['optionList'][i]['fin_prdt_cd']:
                # for문을 통해 optionList[i]중 조건에 맞는 것들을 mini_temp_dict에 삽입 (금융상품 코드가 맞다면)
                mini_temp_dict = {}
                mini_temp_dict['저축 금리'] = response['result']['optionList'][i]['intr_rate']
                mini_temp_dict['저축 기간'] = response['result']['optionList'][i]['save_trm']
                mini_temp_dict['저축금리유형'] = response['result']['optionList'][i]['intr_rate_type']
                mini_temp_dict['저축금리유형명'] = response['result']['optionList'][i]['intr_rate_type_nm']
                mini_temp_dict['최고 우대금리'] = response['result']['optionList'][i]['intr_rate2']

                # mini_temp_dict_list에 mini_temp_dict를 담음
                mini_temp_dict_list.append(mini_temp_dict)

        # mini_temp_dict_list에 여러개의 mini_temp_dict가 담길 수 있으므로, 해당되는 ['optionList'][i] 반복이 끝난 후 완성된 정보를 삽입
        temp_dict['금리정보'] = mini_temp_dict_list
        temp_dict['금융상품명'] = temp_list_dict[fin_cd][1]
        temp_dict['금융회사명'] = temp_list_dict[fin_cd][0]

        #최종 리스트에 temp_list 삽입
        final_list.append(temp_dict)
    
    result = final_list
    return result

# 아래 코드는 수정하지 않습니다.  
if __name__ == '__main__':
    # json 형태의 데이터 반환
    result = get_deposit_products()
    # prrint.prrint(): json 을 보기 좋은 형식으로 출력
    pprint.pprint(result)


# [{'금리정보': [{'저축 금리': 3,
#             '저축 기간': '1',
#             '저축금리유형': 'S',
#             '저축금리유형명': '단리',
#             '최고 우대금리': 3},
#            {'저축 금리': 3.45,
#             '저축 기간': '3',
#             '저축금리유형': 'S',
#             '저축금리유형명': '단리',
#             '최고 우대금리': 3.45},
#            {'저축 금리': 3.45,
#             '저축 기간': '6',
#             '저축금리유형': 'S',
#             '저축금리유형명': '단리',
#             '최고 우대금리': 3.45},
#            {'저축 금리': 3.4,
#             '저축 기간': '12',
#             '저축금리유형': 'S',
#             '저축금리유형명': '단리',
#             '최고 우대금리': 3.4},
#            {'저축 금리': 2.95,
#             '저축 기간': '24',
#             '저축금리유형': 'S',
#             '저축금리유형명': '단리',
#             '최고 우대금리': 2.95},
#            {'저축 금리': 2.95,
#             '저축 기간': '36',
#             '저축금리유형': 'S',
#             '저축금리유형명': '단리',
#             '최고 우대금리': 2.95}],
#   '금융상품명': 'WON플러스예금',
#   '금융회사명': '우리은행'},
#  {'금리정보': [{'저축 금리': 3,
#             '저축 기간': '1',
#             '저축금리유형': 'S',
#             '저축금리유형명': '단리',
#             '최고 우대금리': 3.2},
#            {'저축 금리': 3.4,
#             '저축 기간': '3',
#             '저축금리유형': 'S',
#             '저축금리유형명': '단리',
#             '최고 우대금리': 3.6},
#            {'저축 금리': 3.3,
#             '저축 기간': '6',
#             '저축금리유형': 'S',
#             '저축금리유형명': '단리',
#             '최고 우대금리': 3.5},
#            {'저축 금리': 3.2,
#             '저축 기간': '12',
#             '저축금리유형': 'S',
#             '저축금리유형명': '단리',
#             '최고 우대금리': 3.5}],
#   '금융상품명': 'e-그린세이브예금',
#   '금융회사명': '한국스탠다드차타드은행'},
#  {'금리정보': [{'저축 금리': 2.42,
#             '저축 기간': '6',
#             '저축금리유형': 'S',
#             '저축금리유형명': '단리',
#             '최고 우대금리': 3.07},
#            {'저축 금리': 3.16,
#             '저축 기간': '12',
#             '저축금리유형': 'S',
#             '저축금리유형명': '단리',
#             '최고 우대금리': 3.81},
#            {'저축 금리': 3.18,
#             '저축 기간': '24',
#             '저축금리유형': 'S',
#             '저축금리유형명': '단리',
#             '최고 우대금리': 3.83},
#            {'저축 금리': 3.2,
#             '저축 기간': '36',
#             '저축금리유형': 'S',
#             '저축금리유형명': '단리',
#             '최고 우대금리': 3.85}],
#   '금융상품명': 'iM주거래우대예금(첫만남고객형)',
#   '금융회사명': '아이엠뱅크'},
#  {'금리정보': [{'저축 금리': 1.92,
#             '저축 기간': '3',
#             '저축금리유형': 'S',
#             '저축금리유형명': '단리',
#             '최고 우대금리': 2.37},
#            {'저축 금리': 2.42,
#             '저축 기간': '6',
#             '저축금리유형': 'S',
#             '저축금리유형명': '단리',
#             '최고 우대금리': 2.87},
#            {'저축 금리': 3.16,
#             '저축 기간': '12',
#             '저축금리유형': 'S',
#             '저축금리유형명': '단리',
#             '최고 우대금리': 3.61},
#            {'저축 금리': 3.18,
#             '저축 기간': '24',
#             '저축금리유형': 'S',
#             '저축금리유형명': '단리',
#             '최고 우대금리': 3.63},
#            {'저축 금리': 3.2,
#             '저축 기간': '36',
#             '저축금리유형': 'S',
#             '저축금리유형명': '단리',
#             '최고 우대금리': 3.65}],
#   '금융상품명': 'iM행복파트너예금(일반형)',
#   '금융회사명': '아이엠뱅크'},
#  {'금리정보': [{'저축 금리': 3.2,
#             '저축 기간': '12',
#             '저축금리유형': 'S',
#             '저축금리유형명': '단리',
#             '최고 우대금리': 3.65}],
#   '금융상품명': 'iM함께예금',
#   '금융회사명': '아이엠뱅크'},
#  {'금리정보': [{'저축 금리': 2.2,
#             '저축 기간': '1',
#             '저축금리유형': 'S',
#             '저축금리유형명': '단리',
#             '최고 우대금리': 2.25},
#            {'저축 금리': 2.4,
#             '저축 기간': '3',
#             '저축금리유형': 'S',
#             '저축금리유형명': '단리',
#             '최고 우대금리': 2.45},
#            {'저축 금리': 3,
#             '저축 기간': '6',
#             '저축금리유형': 'S',
#             '저축금리유형명': '단리',
#             '최고 우대금리': 3.25},
#            {'저축 금리': 3.25,
#             '저축 기간': '12',
#             '저축금리유형': 'S',
#             '저축금리유형명': '단리',
#             '최고 우대금리': 3.5},
#            {'저축 금리': 3.18,
#             '저축 기간': '24',
#             '저축금리유형': 'S',
#             '저축금리유형명': '단리',
#             '최고 우대금리': 3.43},
#            {'저축 금리': 3.2,
#             '저축 기간': '36',
#             '저축금리유형': 'S',
#             '저축금리유형명': '단리',
#             '최고 우대금리': 3.45}],
#   '금융상품명': 'iM스마트예금',
#   '금융회사명': '아이엠뱅크'},
#  {'금리정보': [{'저축 금리': 2.25,
#             '저축 기간': '1',
#             '저축금리유형': 'S',
#             '저축금리유형명': '단리',
#             '최고 우대금리': 2.25},
#            {'저축 금리': 2.45,
#             '저축 기간': '3',
#             '저축금리유형': 'S',
#             '저축금리유형명': '단리',
#             '최고 우대금리': 3.3},
#            {'저축 금리': 2.55,
#             '저축 기간': '6',
#             '저축금리유형': 'S',
#             '저축금리유형명': '단리',
#             '최고 우대금리': 3.3},
#            {'저축 금리': 2.75,
#             '저축 기간': '12',
#             '저축금리유형': 'S',
#             '저축금리유형명': '단리',
#             '최고 우대금리': 3.3},
#            {'저축 금리': 2.8,
#             '저축 기간': '24',
#             '저축금리유형': 'S',
#             '저축금리유형명': '단리',
#             '최고 우대금리': 2.8},
#            {'저축 금리': 2.8,
#             '저축 기간': '36',
#             '저축금리유형': 'S',
#             '저축금리유형명': '단리',
#             '최고 우대금리': 2.8}],
#   '금융상품명': 'LIVE정기예금',
#   '금융회사명': '부산은행'},
#  {'금리정보': [{'저축 금리': 2.2,
#             '저축 기간': '1',
#             '저축금리유형': 'S',
#             '저축금리유형명': '단리',
#             '최고 우대금리': 2.75},
#            {'저축 금리': 2.75,
#             '저축 기간': '3',
#             '저축금리유형': 'S',
#             '저축금리유형명': '단리',
#             '최고 우대금리': 3.3},
#            {'저축 금리': 3,
#             '저축 기간': '6',
#             '저축금리유형': 'S',
#             '저축금리유형명': '단리',
#             '최고 우대금리': 3.55},
#            {'저축 금리': 3,
#             '저축 기간': '12',
#             '저축금리유형': 'S',
#             '저축금리유형명': '단리',
#             '최고 우대금리': 3.55},
#            {'저축 금리': 2.25,
#             '저축 기간': '24',
#             '저축금리유형': 'S',
#             '저축금리유형명': '단리',
#             '최고 우대금리': 2.8},
#            {'저축 금리': 1.95,
#             '저축 기간': '36',
#             '저축금리유형': 'S',
#             '저축금리유형명': '단리',
#             '최고 우대금리': 2.5}],
#   '금융상품명': '더(The) 특판 정기예금',
#   '금융회사명': '부산은행'},
#  {'금리정보': [{'저축 금리': 3.2,
#             '저축 기간': '6',
#             '저축금리유형': 'S',
#             '저축금리유형명': '단리',
#             '최고 우대금리': 3.4},
#            {'저축 금리': 3.25,
#             '저축 기간': '12',
#             '저축금리유형': 'S',
#             '저축금리유형명': '단리',
#             '최고 우대금리': 3.45}],
#   '금융상품명': '더(The) 레벨업 정기예금',
#   '금융회사명': '부산은행'},
#  {'금리정보': [{'저축 금리': 3.09,
#             '저축 기간': '12',
#             '저축금리유형': 'M',
#             '저축금리유형명': '복리',
#             '최고 우대금리': 3.29},
#            {'저축 금리': 3,
#             '저축 기간': '24',
#             '저축금리유형': 'M',
#             '저축금리유형명': '복리',
#             '최고 우대금리': 3.2},
#            {'저축 금리': 2.95,
#             '저축 기간': '36',
#             '저축금리유형': 'M',
#             '저축금리유형명': '복리',
#             '최고 우대금리': 3.15}],
#   '금융상품명': '미즈월복리정기예금',
#   '금융회사명': '광주은행'},
#  {'금리정보': [{'저축 금리': 2.99,
#             '저축 기간': '1',
#             '저축금리유형': 'S',
#             '저축금리유형명': '단리',
#             '최고 우대금리': 3.09},
#            {'저축 금리': 3,
#             '저축 기간': '3',
#             '저축금리유형': 'S',
#             '저축금리유형명': '단리',
#             '최고 우대금리': 3.1},
#            {'저축 금리': 3.03,
#             '저축 기간': '6',
#             '저축금리유형': 'S',
#             '저축금리유형명': '단리',
#             '최고 우대금리': 3.13},
#            {'저축 금리': 2.99,
#             '저축 기간': '12',
#             '저축금리유형': 'S',
#             '저축금리유형명': '단리',
#             '최고 우대금리': 3.19},
#            {'저축 금리': 2.9,
#             '저축 기간': '24',
#             '저축금리유형': 'S',
#             '저축금리유형명': '단리',
#             '최고 우대금리': 3.1},
#            {'저축 금리': 2.85,
#             '저축 기간': '36',
#             '저축금리유형': 'S',
#             '저축금리유형명': '단리',
#             '최고 우대금리': 3.05}],
#   '금융상품명': '스마트모아Dream정기예금',
#   '금융회사명': '광주은행'},
#  {'금리정보': [{'저축 금리': 2.89,
#             '저축 기간': '12',
#             '저축금리유형': 'S',
#             '저축금리유형명': '단리',
#             '최고 우대금리': 3.39}],
#   '금융상품명': '굿스타트예금',
#   '금융회사명': '광주은행'},
#  {'금리정보': [{'저축 금리': 3.4,
#             '저축 기간': '3',
#             '저축금리유형': 'S',
#             '저축금리유형명': '단리',
#             '최고 우대금리': 3.4},
#            {'저축 금리': 3.4,
#             '저축 기간': '6',
#             '저축금리유형': 'S',
#             '저축금리유형명': '단리',
#             '최고 우대금리': 3.4},
#            {'저축 금리': 3.4,
#             '저축 기간': '12',
#             '저축금리유형': 'S',
#             '저축금리유형명': '단리',
#             '최고 우대금리': 3.4}],
#   '금융상품명': 'The플러스예금',
#   '금융회사명': '광주은행'},
#  {'금리정보': [{'저축 금리': 2.6,
#             '저축 기간': '1',
#             '저축금리유형': 'S',
#             '저축금리유형명': '단리',
#             '최고 우대금리': 2.7},
#            {'저축 금리': 2.7,
#             '저축 기간': '3',
#             '저축금리유형': 'S',
#             '저축금리유형명': '단리',
#             '최고 우대금리': 2.8},
#            {'저축 금리': 2.85,
#             '저축 기간': '6',
#             '저축금리유형': 'S',
#             '저축금리유형명': '단리',
#             '최고 우대금리': 2.95},
#            {'저축 금리': 3.05,
#             '저축 기간': '12',
#             '저축금리유형': 'S',
#             '저축금리유형명': '단리',
#             '최고 우대금리': 3.15},
#            {'저축 금리': 3.15,
#             '저축 기간': '24',
#             '저축금리유형': 'S',
#             '저축금리유형명': '단리',
#             '최고 우대금리': 3.25},
#            {'저축 금리': 3.25,
#             '저축 기간': '36',
#             '저축금리유형': 'S',
#             '저축금리유형명': '단리',
#             '최고 우대금리': 3.35}],
#   '금융상품명': '제주Dream정기예금(개인/만기지급식)',
#   '금융회사명': '제주은행'},
#  {'금리정보': [{'저축 금리': 2.3,
#             '저축 기간': '1',
#             '저축금리유형': 'S',
#             '저축금리유형명': '단리',
#             '최고 우대금리': 3.2},
#            {'저축 금리': 2.6,
#             '저축 기간': '3',
#             '저축금리유형': 'S',
#             '저축금리유형명': '단리',
#             '최고 우대금리': 3.5},
#            {'저축 금리': 3,
#             '저축 기간': '6',
#             '저축금리유형': 'S',
#             '저축금리유형명': '단리',
#             '최고 우대금리': 3.7},
#            {'저축 금리': 3.1,
#             '저축 기간': '12',
#             '저축금리유형': 'S',
#             '저축금리유형명': '단리',
#             '최고 우대금리': 3.75},
#            {'저축 금리': 3,
#             '저축 기간': '24',
#             '저축금리유형': 'S',
#             '저축금리유형명': '단리',
#             '최고 우대금리': 3.5},
#            {'저축 금리': 3,
#             '저축 기간': '36',
#             '저축금리유형': 'S',
#             '저축금리유형명': '단리',
#             '최고 우대금리': 3.5}],
#   '금융상품명': 'J정기예금(만기지급식)',
#   '금융회사명': '제주은행'},
#  {'금리정보': [{'저축 금리': 2.6,
#             '저축 기간': '3',
#             '저축금리유형': 'S',
#             '저축금리유형명': '단리',
#             '최고 우대금리': 3.35},
#            {'저축 금리': 2.75,
#             '저축 기간': '6',
#             '저축금리유형': 'S',
#             '저축금리유형명': '단리',
#             '최고 우대금리': 3.5},
#            {'저축 금리': 2.95,
#             '저축 기간': '12',
#             '저축금리유형': 'S',
#             '저축금리유형명': '단리',
#             '최고 우대금리': 3.7}],
#   '금융상품명': '스마일드림 정기예금(개인/만기지급식)',
#   '금융회사명': '제주은행'},
#  {'금리정보': [{'저축 금리': 3.5,
#             '저축 기간': '3',
#             '저축금리유형': 'S',
#             '저축금리유형명': '단리',
#             '최고 우대금리': 3.5},
#            {'저축 금리': 3.55,
#             '저축 기간': '6',
#             '저축금리유형': 'S',
#             '저축금리유형명': '단리',
#             '최고 우대금리': 3.55},
#            {'저축 금리': 3.4,
#             '저축 기간': '12',
#             '저축금리유형': 'S',
#             '저축금리유형명': '단리',
#             '최고 우대금리': 3.4}],
#   '금융상품명': 'JB 다이렉트예금통장(만기일시지급식)',
#   '금융회사명': '전북은행'},
#  {'금리정보': [{'저축 금리': 3.4,
#             '저축 기간': '12',
#             '저축금리유형': 'S',
#             '저축금리유형명': '단리',
#             '최고 우대금리': 3.75},
#            {'저축 금리': 3.4,
#             '저축 기간': '24',
#             '저축금리유형': 'S',
#             '저축금리유형명': '단리',
#             '최고 우대금리': 3.6},
#            {'저축 금리': 3.4,
#             '저축 기간': '36',
#             '저축금리유형': 'S',
#             '저축금리유형명': '단리',
#             '최고 우대금리': 3.7}],
#   '금융상품명': 'JB 123 정기예금 (만기일시지급식)',
#   '금융회사명': '전북은행'},
#  {'금리정보': [{'저축 금리': 2.45,
#             '저축 기간': '3',
#             '저축금리유형': 'S',
#             '저축금리유형명': '단리',
#             '최고 우대금리': 2.95},
#            {'저축 금리': 2.6,
#             '저축 기간': '6',
#             '저축금리유형': 'S',
#             '저축금리유형명': '단리',
#             '최고 우대금리': 3.1},
#            {'저축 금리': 2.95,
#             '저축 기간': '12',
#             '저축금리유형': 'S',
#             '저축금리유형명': '단리',
#             '최고 우대금리': 3.45},
#            {'저축 금리': 3.05,
#             '저축 기간': '24',
#             '저축금리유형': 'S',
#             '저축금리유형명': '단리',
#             '최고 우대금리': 3.55}],
#   '금융상품명': 'BNK더조은정기예금',
#   '금융회사명': '경남은행'},
#  {'금리정보': [{'저축 금리': 3.05,
#             '저축 기간': '6',
#             '저축금리유형': 'S',
#             '저축금리유형명': '단리',
#             '최고 우대금리': 3.35},
#            {'저축 금리': 3.3,
#             '저축 기간': '12',
#             '저축금리유형': 'S',
#             '저축금리유형명': '단리',
#             '최고 우대금리': 3.6},
#            {'저축 금리': 3.35,
#             '저축 기간': '24',
#             '저축금리유형': 'S',
#             '저축금리유형명': '단리',
#             '최고 우대금리': 3.65}],
#   '금융상품명': 'BNK주거래우대정기예금',
#   '금융회사명': '경남은행'},
#  {'금리정보': [{'저축 금리': 2.4,
#             '저축 기간': '3',
#             '저축금리유형': 'S',
#             '저축금리유형명': '단리',
#             '최고 우대금리': 3.4},
#            {'저축 금리': 2.4,
#             '저축 기간': '6',
#             '저축금리유형': 'S',
#             '저축금리유형명': '단리',
#             '최고 우대금리': 3.4},
#            {'저축 금리': 2.4,
#             '저축 기간': '12',
#             '저축금리유형': 'S',
#             '저축금리유형명': '단리',
#             '최고 우대금리': 3.4}],
#   '금융상품명': 'BNK MY 원픽 정기예금',
#   '금융회사명': '경남은행'},
#  {'금리정보': [{'저축 금리': 2.4,
#             '저축 기간': '3',
#             '저축금리유형': 'S',
#             '저축금리유형명': '단리',
#             '최고 우대금리': 3.45},
#            {'저축 금리': 2.4,
#             '저축 기간': '6',
#             '저축금리유형': 'S',
#             '저축금리유형명': '단리',
#             '최고 우대금리': 3.45},
#            {'저축 금리': 2.4,
#             '저축 기간': '12',
#             '저축금리유형': 'S',
#             '저축금리유형명': '단리',
#             '최고 우대금리': 3.6}],
#   '금융상품명': 'The 든든 예금',
#   '금융회사명': '경남은행'},
#  {'금리정보': [{'저축 금리': 3.15,
#             '저축 기간': '12',
#             '저축금리유형': 'S',
#             '저축금리유형명': '단리',
#             '최고 우대금리': 3.35},
#            {'저축 금리': 3.2,
#             '저축 기간': '24',
#             '저축금리유형': 'S',
#             '저축금리유형명': '단리',
#             '최고 우대금리': 3.4},
#            {'저축 금리': 3.3,
#             '저축 기간': '36',
#             '저축금리유형': 'S',
#             '저축금리유형명': '단리',
#             '최고 우대금리': 3.5}],
#   '금융상품명': 'IBK평생한가족통장(실세금리정기예금)',
#   '금융회사명': '중소기업은행'},
#  {'금리정보': [{'저축 금리': 3.12,
#             '저축 기간': '6',
#             '저축금리유형': 'S',
#             '저축금리유형명': '단리',
#             '최고 우대금리': 3.12},
#            {'저축 금리': 3,
#             '저축 기간': '12',
#             '저축금리유형': 'S',
#             '저축금리유형명': '단리',
#             '최고 우대금리': 3},
#            {'저축 금리': 2.96,
#             '저축 기간': '24',
#             '저축금리유형': 'S',
#             '저축금리유형명': '단리',
#             '최고 우대금리': 2.96},
#            {'저축 금리': 2.95,
#             '저축 기간': '36',
#             '저축금리유형': 'S',
#             '저축금리유형명': '단리',
#             '최고 우대금리': 2.95}],
#   '금융상품명': '1석7조통장(정기예금)',
#   '금융회사명': '중소기업은행'},
#  {'금리정보': [{'저축 금리': 3,
#             '저축 기간': '1',
#             '저축금리유형': 'S',
#             '저축금리유형명': '단리',
#             '최고 우대금리': 3},
#            {'저축 금리': 3.1,
#             '저축 기간': '3',
#             '저축금리유형': 'S',
#             '저축금리유형명': '단리',
#             '최고 우대금리': 3.1},
#            {'저축 금리': 3.4,
#             '저축 기간': '6',
#             '저축금리유형': 'S',
#             '저축금리유형명': '단리',
#             '최고 우대금리': 3.4},
#            {'저축 금리': 3.5,
#             '저축 기간': '12',
#             '저축금리유형': 'S',
#             '저축금리유형명': '단리',
#             '최고 우대금리': 3.5},
#            {'저축 금리': 3.35,
#             '저축 기간': '24',
#             '저축금리유형': 'S',
#             '저축금리유형명': '단리',
#             '최고 우대금리': 3.35},
#            {'저축 금리': 3.35,
#             '저축 기간': '36',
#             '저축금리유형': 'S',
#             '저축금리유형명': '단리',
#             '최고 우대금리': 3.35}],
#   '금융상품명': 'KDB 정기예금',
#   '금융회사명': '한국산업은행'},
#  {'금리정보': [{'저축 금리': 1.8,
#             '저축 기간': '1',
#             '저축금리유형': 'S',
#             '저축금리유형명': '단리',
#             '최고 우대금리': 3},
#            {'저축 금리': 2.2,
#             '저축 기간': '3',
#             '저축금리유형': 'S',
#             '저축금리유형명': '단리',
#             '최고 우대금리': 3.4},
#            {'저축 금리': 2.3,
#             '저축 기간': '6',
#             '저축금리유형': 'S',
#             '저축금리유형명': '단리',
#             '최고 우대금리': 3.4},
#            {'저축 금리': 2.5,
#             '저축 기간': '12',
#             '저축금리유형': 'S',
#             '저축금리유형명': '단리',
#             '최고 우대금리': 3.4},
#            {'저축 금리': 2.6,
#             '저축 기간': '24',
#             '저축금리유형': 'S',
#             '저축금리유형명': '단리',
#             '최고 우대금리': 2.7},
#            {'저축 금리': 2.6,
#             '저축 기간': '36',
#             '저축금리유형': 'S',
#             '저축금리유형명': '단리',
#             '최고 우대금리': 2.7}],
#   '금융상품명': 'KB Star 정기예금',
#   '금융회사명': '국민은행'},
#  {'금리정보': [{'저축 금리': 2.15,
#             '저축 기간': '1',
#             '저축금리유형': 'S',
#             '저축금리유형명': '단리',
#             '최고 우대금리': 3},
#            {'저축 금리': 2.45,
#             '저축 기간': '3',
#             '저축금리유형': 'S',
#             '저축금리유형명': '단리',
#             '최고 우대금리': 3.4},
#            {'저축 금리': 2.75,
#             '저축 기간': '6',
#             '저축금리유형': 'S',
#             '저축금리유형명': '단리',
#             '최고 우대금리': 3.4},
#            {'저축 금리': 2.9,
#             '저축 기간': '12',
#             '저축금리유형': 'S',
#             '저축금리유형명': '단리',
#             '최고 우대금리': 3.35},
#            {'저축 금리': 2.95,
#             '저축 기간': '24',
#             '저축금리유형': 'S',
#             '저축금리유형명': '단리',
#             '최고 우대금리': 3},
#            {'저축 금리': 3,
#             '저축 기간': '36',
#             '저축금리유형': 'S',
#             '저축금리유형명': '단리',
#             '최고 우대금리': 3}],
#   '금융상품명': '쏠편한 정기예금',
#   '금융회사명': '신한은행'},
#  {'금리정보': [{'저축 금리': 2.95,
#             '저축 기간': '1',
#             '저축금리유형': 'S',
#             '저축금리유형명': '단리',
#             '최고 우대금리': 3.05},
#            {'저축 금리': 3.3,
#             '저축 기간': '3',
#             '저축금리유형': 'S',
#             '저축금리유형명': '단리',
#             '최고 우대금리': 3.4},
#            {'저축 금리': 3.33,
#             '저축 기간': '6',
#             '저축금리유형': 'S',
#             '저축금리유형명': '단리',
#             '최고 우대금리': 3.43},
#            {'저축 금리': 3.35,
#             '저축 기간': '12',
#             '저축금리유형': 'S',
#             '저축금리유형명': '단리',
#             '최고 우대금리': 3.45}],
#   '금융상품명': 'NH왈츠회전예금 II',
#   '금융회사명': '농협은행주식회사'},
#  {'금리정보': [{'저축 금리': 3.1,
#             '저축 기간': '12',
#             '저축금리유형': 'S',
#             '저축금리유형명': '단리',
#             '최고 우대금리': 3.5},
#            {'저축 금리': 3.15,
#             '저축 기간': '24',
#             '저축금리유형': 'S',
#             '저축금리유형명': '단리',
#             '최고 우대금리': 3.55},
#            {'저축 금리': 3.4,
#             '저축 기간': '36',
#             '저축금리유형': 'S',
#             '저축금리유형명': '단리',
#             '최고 우대금리': 3.8}],
#   '금융상품명': 'NH내가Green초록세상예금',
#   '금융회사명': '농협은행주식회사'},
#  {'금리정보': [{'저축 금리': 3,
#             '저축 기간': '1',
#             '저축금리유형': 'S',
#             '저축금리유형명': '단리',
#             '최고 우대금리': 3},
#            {'저축 금리': 3.4,
#             '저축 기간': '3',
#             '저축금리유형': 'S',
#             '저축금리유형명': '단리',
#             '최고 우대금리': 3.4},
#            {'저축 금리': 3.43,
#             '저축 기간': '6',
#             '저축금리유형': 'S',
#             '저축금리유형명': '단리',
#             '최고 우대금리': 3.43},
#            {'저축 금리': 3.45,
#             '저축 기간': '12',
#             '저축금리유형': 'S',
#             '저축금리유형명': '단리',
#             '최고 우대금리': 3.45},
#            {'저축 금리': 3.23,
#             '저축 기간': '24',
#             '저축금리유형': 'S',
#             '저축금리유형명': '단리',
#             '최고 우대금리': 3.23},
#            {'저축 금리': 3.4,
#             '저축 기간': '36',
#             '저축금리유형': 'S',
#             '저축금리유형명': '단리',
#             '최고 우대금리': 3.4}],
#   '금융상품명': 'NH올원e예금',
#   '금융회사명': '농협은행주식회사'},
#  {'금리정보': [{'저축 금리': 3.1,
#             '저축 기간': '12',
#             '저축금리유형': 'S',
#             '저축금리유형명': '단리',
#             '최고 우대금리': 3.9}],
#   '금융상품명': 'NH고향사랑기부예금',
#   '금융회사명': '농협은행주식회사'},
#  {'금리정보': [{'저축 금리': 2,
#             '저축 기간': '1',
#             '저축금리유형': 'S',
#             '저축금리유형명': '단리',
#             '최고 우대금리': 3},
#            {'저축 금리': 2.2,
#             '저축 기간': '3',
#             '저축금리유형': 'S',
#             '저축금리유형명': '단리',
#             '최고 우대금리': 3.4},
#            {'저축 금리': 2.3,
#             '저축 기간': '6',
#             '저축금리유형': 'S',
#             '저축금리유형명': '단리',
#             '최고 우대금리': 3.4},
#            {'저축 금리': 2.6,
#             '저축 기간': '12',
#             '저축금리유형': 'S',
#             '저축금리유형명': '단리',
#             '최고 우대금리': 3.4},
#            {'저축 금리': 2.7,
#             '저축 기간': '24',
#             '저축금리유형': 'S',
#             '저축금리유형명': '단리',
#             '최고 우대금리': 3},
#            {'저축 금리': 2.8,
#             '저축 기간': '36',
#             '저축금리유형': 'S',
#             '저축금리유형명': '단리',
#             '최고 우대금리': 3}],
#   '금융상품명': '헤이(Hey)정기예금',
#   '금융회사명': '수협은행'},
#  {'금리정보': [{'저축 금리': 3,
#             '저축 기간': '1',
#             '저축금리유형': 'S',
#             '저축금리유형명': '단리',
#             '최고 우대금리': 3},
#            {'저축 금리': 3.4,
#             '저축 기간': '3',
#             '저축금리유형': 'S',
#             '저축금리유형명': '단리',
#             '최고 우대금리': 3.4},
#            {'저축 금리': 3.4,
#             '저축 기간': '6',
#             '저축금리유형': 'S',
#             '저축금리유형명': '단리',
#             '최고 우대금리': 3.4},
#            {'저축 금리': 3.35,
#             '저축 기간': '12',
#             '저축금리유형': 'S',
#             '저축금리유형명': '단리',
#             '최고 우대금리': 3.35},
#            {'저축 금리': 3.2,
#             '저축 기간': '24',
#             '저축금리유형': 'S',
#             '저축금리유형명': '단리',
#             '최고 우대금리': 3.2},
#            {'저축 금리': 3.2,
#             '저축 기간': '36',
#             '저축금리유형': 'S',
#             '저축금리유형명': '단리',
#             '최고 우대금리': 3.2}],
#   '금융상품명': '코드K 정기예금',
#   '금융회사명': '주식회사 케이뱅크'},
#  {'금리정보': [{'저축 금리': 2.4,
#             '저축 기간': '12',
#             '저축금리유형': 'S',
#             '저축금리유형명': '단리',
#             '최고 우대금리': 2.8}],
#   '금융상품명': 'Sh평생주거래우대예금(만기일시지급식)',
#   '금융회사명': '수협은행'},
#  {'금리정보': [{'저축 금리': 3.2,
#             '저축 기간': '6',
#             '저축금리유형': 'S',
#             '저축금리유형명': '단리',
#             '최고 우대금리': 3.55},
#            {'저축 금리': 3.25,
#             '저축 기간': '12',
#             '저축금리유형': 'S',
#             '저축금리유형명': '단리',
#             '최고 우대금리': 3.6}],
#   '금융상품명': 'Sh해양플라스틱Zero!예금(만기일시지급식)',
#   '금융회사명': '수협은행'},
#  {'금리정보': [{'저축 금리': 3.55,
#             '저축 기간': '3',
#             '저축금리유형': 'S',
#             '저축금리유형명': '단리',
#             '최고 우대금리': 3.55},
#            {'저축 금리': 3.55,
#             '저축 기간': '6',
#             '저축금리유형': 'S',
#             '저축금리유형명': '단리',
#             '최고 우대금리': 3.55},
#            {'저축 금리': 3.6,
#             '저축 기간': '12',
#             '저축금리유형': 'S',
#             '저축금리유형명': '단리',
#             '최고 우대금리': 3.6}],
#   '금융상품명': '헤이(Hey)정기예금',
#   '금융회사명': '수협은행'},
#  {'금리정보': [{'저축 금리': 2.7,
#             '저축 기간': '12',
#             '저축금리유형': 'S',
#             '저축금리유형명': '단리',
#             '최고 우대금리': 3.75}],
#   '금융상품명': 'Sh첫만남우대예금',
#   '금융회사명': '수협은행'},
#  {'금리정보': [{'저축 금리': 2.7,
#             '저축 기간': '1',
#             '저축금리유형': 'S',
#             '저축금리유형명': '단리',
#             '최고 우대금리': 2.7},
#            {'저축 금리': 3.2,
#             '저축 기간': '3',
#             '저축금리유형': 'S',
#             '저축금리유형명': '단리',
#             '최고 우대금리': 3.2},
#            {'저축 금리': 3.3,
#             '저축 기간': '6',
#             '저축금리유형': 'S',
#             '저축금리유형명': '단리',
#             '최고 우대금리': 3.3},
#            {'저축 금리': 3.3,
#             '저축 기간': '12',
#             '저축금리유형': 'S',
#             '저축금리유형명': '단리',
#             '최고 우대금리': 3.3},
#            {'저축 금리': 3,
#             '저축 기간': '24',
#             '저축금리유형': 'S',
#             '저축금리유형명': '단리',
#             '최고 우대금리': 3},
#            {'저축 금리': 3,
#             '저축 기간': '36',
#             '저축금리유형': 'S',
#             '저축금리유형명': '단리',
#             '최고 우대금리': 3}],
#   '금융상품명': '카카오뱅크 정기예금',
#   '금융회사명': '주식회사 카카오뱅크'},
#  {'금리정보': [{'저축 금리': 3,
#             '저축 기간': '3',
#             '저축금리유형': 'S',
#             '저축금리유형명': '단리',
#             '최고 우대금리': 3},
#            {'저축 금리': 3,
#             '저축 기간': '6',
#             '저축금리유형': 'S',
#             '저축금리유형명': '단리',
#             '최고 우대금리': 3}],
#   '금융상품명': '토스뱅크 먼저 이자 받는 정기예금',
#   '금융회사명': '토스뱅크 주식회사'}]