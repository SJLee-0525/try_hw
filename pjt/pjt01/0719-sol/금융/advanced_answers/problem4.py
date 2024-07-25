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
    api_key = 'c19ae7f523953ee767f19e9217fb618e'

    url = 'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json'
    params = {
        'auth': api_key,
        # 금융회사 코드 020000(은행), 030200(여신전문), 030300(저축은행), 050000(보험), 060000(금융투자)
        'topFinGrpNo': '020000',
        'pageNo': 1,
    }
    response = requests.get(url, params=params).json()['result']
    base_list = response['baseList']
    option_list = response['optionList']

    result = []
    for product in base_list:
        new_product = {}
        options = []
        for option in option_list:
            new_option = {}
            if option['fin_prdt_cd'] == product['fin_prdt_cd']:
                new_option['저축금리유형'] = option['intr_rate_type']
                new_option['저축금리유형명'] = option['intr_rate_type_nm']
                new_option['저축 기간'] = option['save_trm']
                new_option['저축 금리'] = option['intr_rate']
                new_option['최고 우대금리'] = option['intr_rate2']
                options.append(new_option)
        new_product['금융회사명'] = product['kor_co_nm']
        new_product['금융상품명'] = product['fin_prdt_nm']
        new_product['금리정보'] = options
        result.append(new_product)

    return result


if __name__ == '__main__':
    # json 형태의 데이터 반환
    result = get_deposit_products()
    # prrint.prrint(): json 을 보기 좋은 형식으로 출력
    pprint.pprint(result)
    print(len(result))
