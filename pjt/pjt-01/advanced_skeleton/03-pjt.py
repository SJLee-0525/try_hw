import pprint
import requests

# 응답 중 정기예금 상품들의 옵션 리스트를 출력하도록 구성합니다.
# 이 때, 원하는 데이터만 추출하여 새로운 리스트를 만들어 반환하는 함수를 작성하시오.
# [힌트] 아래와 같은 순서로 데이터를 출력하며 진행합니다.
# 1. 응답을 json 형식으로 변환합니다.
# 2. key 값이 "result" 인 데이터를 출력합니다.
# 3. 위의 결과 중 key 값이 "optionList" 인 데이터를 변수에 저장합니다.
# 4. 3번에서 저장된 값을 반복하며, 원하는 데이터만 추출 및 가공하여 결과 리스트에 저장합니다.

def get_deposit_products():
    # 본인의 API KEY 로 수정합니다.
    api_key = 'c19ae7f523953ee767f19e9217fb618e'

    # 요구사항에 맞도록 이곳의 코드를 수정합니다.
    url = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo=1'

    result = []
    response = requests.get(url).json()
    
    for i in range(len(response['result']['optionList'])):  # optionList가 가진 리스트 값에 대한 인덱스 추출 
        temp_dict = {}

        # for문을 통해 optionList[i]중 조건에 맞는 것들을 temp_dict에 삽입
        temp_dict['금융상품코드'] = response['result']['optionList'][i]['fin_prdt_cd']
        temp_dict['저축 금리'] = response['result']['optionList'][i]['intr_rate']
        temp_dict['저축 기간'] = response['result']['optionList'][i]['save_trm']
        temp_dict['저축금리유형'] = response['result']['optionList'][i]['intr_rate_type']
        temp_dict['저축금리유형명'] = response['result']['optionList'][i]['intr_rate_type_nm']
        temp_dict['최고 우대금리'] = response['result']['optionList'][i]['intr_rate2']

        # result 리스트에 완성된 temp_list를 삽입. temp_list는 다음 반복때 새로 재생성
        result.append(temp_dict)

    return result
    
# 아래 코드는 수정하지 않습니다.
if __name__ == '__main__':
    # json 형태의 데이터 반환
    result = get_deposit_products()
    # prrint.prrint(): json 을 보기 좋은 형식으로 출력
    pprint.pprint(result)

# [{'금융상품코드': 'WR0001B',
#   '저축 금리': 3,
#   '저축 기간': '1',
#   '저축금리유형': 'S',
#   '저축금리유형명': '단리',
#   '최고 우대금리': 3},
#  {'금융상품코드': 'WR0001B',
#   '저축 금리': 3.45,
#   '저축 기간': '3',
#   '저축금리유형': 'S',
#   '저축금리유형명': '단리',
#   '최고 우대금리': 3.45},
#  {'금융상품코드': 'WR0001B',
#   '저축 금리': 3.45,
#   '저축 기간': '6',
#   '저축금리유형': 'S',
#   '저축금리유형명': '단리',
#   '최고 우대금리': 3.45},
#  {'금융상품코드': 'WR0001B',
#   '저축 금리': 3.4,
#   '저축 기간': '12',
#   '저축금리유형': 'S',
#   '저축금리유형명': '단리',
#   '최고 우대금리': 3.4},
#  {'금융상품코드': 'WR0001B',
#   '저축 금리': 2.95,
#   '저축 기간': '24',
#   '저축금리유형': 'S',
#   '저축금리유형명': '단리',
#   '최고 우대금리': 2.95},
#  {'금융상품코드': 'WR0001B',
#   '저축 금리': 2.95,
#   '저축 기간': '36',
#   '저축금리유형': 'S',
#   '저축금리유형명': '단리',
#   '최고 우대금리': 2.95},
#  {'금융상품코드': '00320342',
#   '저축 금리': 3,
#   '저축 기간': '1',
#   '저축금리유형': 'S',
#   '저축금리유형명': '단리',
#   '최고 우대금리': 3.2},
#  {'금융상품코드': '00320342',
#   '저축 금리': 3.4,
#   '저축 기간': '3',
#   '저축금리유형': 'S',
#   '저축금리유형명': '단리',
#   '최고 우대금리': 3.6},
#  {'금융상품코드': '00320342',
#   '저축 금리': 3.3,
#   '저축 기간': '6',
#   '저축금리유형': 'S',
#   '저축금리유형명': '단리',
#   '최고 우대금리': 3.5},
#  {'금융상품코드': '00320342',
#   '저축 금리': 3.2,
#   '저축 기간': '12',
#   '저축금리유형': 'S',
#   '저축금리유형명': '단리',
#   '최고 우대금리': 3.5},
#  {'금융상품코드': '10511008000996000',
#   '저축 금리': 2.42,
#   '저축 기간': '6',
#   '저축금리유형': 'S',
#   '저축금리유형명': '단리',
#   '최고 우대금리': 3.07},
#  {'금융상품코드': '10511008000996000',
#   '저축 금리': 3.16,
#   '저축 기간': '12',
#   '저축금리유형': 'S',
#   '저축금리유형명': '단리',
#   '최고 우대금리': 3.81},
#  {'금융상품코드': '10511008000996000',
#   '저축 금리': 3.18,
#   '저축 기간': '24',
#   '저축금리유형': 'S',
#   '저축금리유형명': '단리',
#   '최고 우대금리': 3.83},
#  {'금융상품코드': '10511008000996000',
#   '저축 금리': 3.2,
#   '저축 기간': '36',
#   '저축금리유형': 'S',
#   '저축금리유형명': '단리',
#   '최고 우대금리': 3.85},
#  {'금융상품코드': '10511008001004000',
#   '저축 금리': 1.92,
#   '저축 기간': '3',
#   '저축금리유형': 'S',
#   '저축금리유형명': '단리',
#   '최고 우대금리': 2.37},
#  {'금융상품코드': '10511008001004000',
#   '저축 금리': 2.42,
#   '저축 기간': '6',
#   '저축금리유형': 'S',
#   '저축금리유형명': '단리',
#   '최고 우대금리': 2.87},
#  {'금융상품코드': '10511008001004000',
#   '저축 금리': 3.16,
#   '저축 기간': '12',
#   '저축금리유형': 'S',
#   '저축금리유형명': '단리',
#   '최고 우대금리': 3.61},
#  {'금융상품코드': '10511008001004000',
#   '저축 금리': 3.18,
#   '저축 기간': '24',
#   '저축금리유형': 'S',
#   '저축금리유형명': '단리',
#   '최고 우대금리': 3.63},
#  {'금융상품코드': '10511008001004000',
#   '저축 금리': 3.2,
#   '저축 기간': '36',
#   '저축금리유형': 'S',
#   '저축금리유형명': '단리',
#   '최고 우대금리': 3.65},
#  {'금융상품코드': '10511008001166004',
#   '저축 금리': 3.2,
#   '저축 기간': '12',
#   '저축금리유형': 'S',
#   '저축금리유형명': '단리',
#   '최고 우대금리': 3.65},
#  {'금융상품코드': '10511008001278000',
#   '저축 금리': 2.2,
#   '저축 기간': '1',
#   '저축금리유형': 'S',
#   '저축금리유형명': '단리',
#   '최고 우대금리': 2.25},
#  {'금융상품코드': '10511008001278000',
#   '저축 금리': 2.4,
#   '저축 기간': '3',
#   '저축금리유형': 'S',
#   '저축금리유형명': '단리',
#   '최고 우대금리': 2.45},
#  {'금융상품코드': '10511008001278000',
#   '저축 금리': 3,
#   '저축 기간': '6',
#   '저축금리유형': 'S',
#   '저축금리유형명': '단리',
#   '최고 우대금리': 3.25},
#  {'금융상품코드': '10511008001278000',
#   '저축 금리': 3.25,
#   '저축 기간': '12',
#   '저축금리유형': 'S',
#   '저축금리유형명': '단리',
#   '최고 우대금리': 3.5},
#  {'금융상품코드': '10511008001278000',
#   '저축 금리': 3.18,
#   '저축 기간': '24',
#   '저축금리유형': 'S',
#   '저축금리유형명': '단리',
#   '최고 우대금리': 3.43},
#  {'금융상품코드': '10511008001278000',
#   '저축 금리': 3.2,
#   '저축 기간': '36',
#   '저축금리유형': 'S',
#   '저축금리유형명': '단리',
#   '최고 우대금리': 3.45},
#  {'금융상품코드': '01030500510002',
#   '저축 금리': 2.25,
#   '저축 기간': '1',
#   '저축금리유형': 'S',
#   '저축금리유형명': '단리',
#   '최고 우대금리': 2.25},
#  {'금융상품코드': '01030500510002',
#   '저축 금리': 2.45,
#   '저축 기간': '3',
#   '저축금리유형': 'S',
#   '저축금리유형명': '단리',
#   '최고 우대금리': 3.3},
#  {'금융상품코드': '01030500510002',
#   '저축 금리': 2.55,
#   '저축 기간': '6',
#   '저축금리유형': 'S',
#   '저축금리유형명': '단리',
#   '최고 우대금리': 3.3},
#  {'금융상품코드': '01030500510002',
#   '저축 금리': 2.75,
#   '저축 기간': '12',
#   '저축금리유형': 'S',
#   '저축금리유형명': '단리',
#   '최고 우대금리': 3.3},
#  {'금융상품코드': '01030500510002',
#   '저축 금리': 2.8,
#   '저축 기간': '24',
#   '저축금리유형': 'S',
#   '저축금리유형명': '단리',
#   '최고 우대금리': 2.8},
#  {'금융상품코드': '01030500510002',
#   '저축 금리': 2.8,
#   '저축 기간': '36',
#   '저축금리유형': 'S',
#   '저축금리유형명': '단리',
#   '최고 우대금리': 2.8},
#  {'금융상품코드': '01030500560002',
#   '저축 금리': 2.2,
#   '저축 기간': '1',
#   '저축금리유형': 'S',
#   '저축금리유형명': '단리',
#   '최고 우대금리': 2.75},
#  {'금융상품코드': '01030500560002',
#   '저축 금리': 2.75,
#   '저축 기간': '3',
#   '저축금리유형': 'S',
#   '저축금리유형명': '단리',
#   '최고 우대금리': 3.3},
#  {'금융상품코드': '01030500560002',
#   '저축 금리': 3,
#   '저축 기간': '6',
#   '저축금리유형': 'S',
#   '저축금리유형명': '단리',
#   '최고 우대금리': 3.55},
#  {'금융상품코드': '01030500560002',
#   '저축 금리': 3,
#   '저축 기간': '12',
#   '저축금리유형': 'S',
#   '저축금리유형명': '단리',
#   '최고 우대금리': 3.55},
#  {'금융상품코드': '01030500560002',
#   '저축 금리': 2.25,
#   '저축 기간': '24',
#   '저축금리유형': 'S',
#   '저축금리유형명': '단리',
#   '최고 우대금리': 2.8},
#  {'금융상품코드': '01030500560002',
#   '저축 금리': 1.95,
#   '저축 기간': '36',
#   '저축금리유형': 'S',
#   '저축금리유형명': '단리',
#   '최고 우대금리': 2.5},
#  {'금융상품코드': '01030500600002',
#   '저축 금리': 3.2,
#   '저축 기간': '6',
#   '저축금리유형': 'S',
#   '저축금리유형명': '단리',
#   '최고 우대금리': 3.4},
#  {'금융상품코드': '01030500600002',
#   '저축 금리': 3.25,
#   '저축 기간': '12',
#   '저축금리유형': 'S',
#   '저축금리유형명': '단리',
#   '최고 우대금리': 3.45},
#  {'금융상품코드': 'TD11300027000',
#   '저축 금리': 3.09,
#   '저축 기간': '12',
#   '저축금리유형': 'M',
#   '저축금리유형명': '복리',
#   '최고 우대금리': 3.29},
#  {'금융상품코드': 'TD11300027000',
#   '저축 금리': 3,
#   '저축 기간': '24',
#   '저축금리유형': 'M',
#   '저축금리유형명': '복리',
#   '최고 우대금리': 3.2},
#  {'금융상품코드': 'TD11300027000',
#   '저축 금리': 2.95,
#   '저축 기간': '36',
#   '저축금리유형': 'M',
#   '저축금리유형명': '복리',
#   '최고 우대금리': 3.15},
#  {'금융상품코드': 'TD11300031000',
#   '저축 금리': 2.99,
#   '저축 기간': '1',
#   '저축금리유형': 'S',
#   '저축금리유형명': '단리',
#   '최고 우대금리': 3.09},
#  {'금융상품코드': 'TD11300031000',
#   '저축 금리': 3,
#   '저축 기간': '3',
#   '저축금리유형': 'S',
#   '저축금리유형명': '단리',
#   '최고 우대금리': 3.1},
#  {'금융상품코드': 'TD11300031000',
#   '저축 금리': 3.03,
#   '저축 기간': '6',
#   '저축금리유형': 'S',
#   '저축금리유형명': '단리',
#   '최고 우대금리': 3.13},
#  {'금융상품코드': 'TD11300031000',
#   '저축 금리': 2.99,
#   '저축 기간': '12',
#   '저축금리유형': 'S',
#   '저축금리유형명': '단리',
#   '최고 우대금리': 3.19},
#  {'금융상품코드': 'TD11300031000',
#   '저축 금리': 2.9,
#   '저축 기간': '24',
#   '저축금리유형': 'S',
#   '저축금리유형명': '단리',
#   '최고 우대금리': 3.1},
#  {'금융상품코드': 'TD11300031000',
#   '저축 금리': 2.85,
#   '저축 기간': '36',
#   '저축금리유형': 'S',
#   '저축금리유형명': '단리',
#   '최고 우대금리': 3.05},
#  {'금융상품코드': 'TD11300035000',
#   '저축 금리': 2.89,
#   '저축 기간': '12',
#   '저축금리유형': 'S',
#   '저축금리유형명': '단리',
#   '최고 우대금리': 3.39},
#  {'금융상품코드': 'TD11300036000',
#   '저축 금리': 3.4,
#   '저축 기간': '3',
#   '저축금리유형': 'S',
#   '저축금리유형명': '단리',
#   '최고 우대금리': 3.4},
#  {'금융상품코드': 'TD11300036000',
#   '저축 금리': 3.4,
#   '저축 기간': '6',
#   '저축금리유형': 'S',
#   '저축금리유형명': '단리',
#   '최고 우대금리': 3.4},
#  {'금융상품코드': 'TD11300036000',
#   '저축 금리': 3.4,
#   '저축 기간': '12',
#   '저축금리유형': 'S',
#   '저축금리유형명': '단리',
#   '최고 우대금리': 3.4},
#  {'금융상품코드': '101272000006',
#   '저축 금리': 2.6,
#   '저축 기간': '1',
#   '저축금리유형': 'S',
#   '저축금리유형명': '단리',
#   '최고 우대금리': 2.7},
#  {'금융상품코드': '101272000006',
#   '저축 금리': 2.7,
#   '저축 기간': '3',
#   '저축금리유형': 'S',
#   '저축금리유형명': '단리',
#   '최고 우대금리': 2.8},
#  {'금융상품코드': '101272000006',
#   '저축 금리': 2.85,
#   '저축 기간': '6',
#   '저축금리유형': 'S',
#   '저축금리유형명': '단리',
#   '최고 우대금리': 2.95},
#  {'금융상품코드': '101272000006',
#   '저축 금리': 3.05,
#   '저축 기간': '12',
#   '저축금리유형': 'S',
#   '저축금리유형명': '단리',
#   '최고 우대금리': 3.15},
#  {'금융상품코드': '101272000006',
#   '저축 금리': 3.15,
#   '저축 기간': '24',
#   '저축금리유형': 'S',
#   '저축금리유형명': '단리',
#   '최고 우대금리': 3.25},
#  {'금융상품코드': '101272000006',
#   '저축 금리': 3.25,
#   '저축 기간': '36',
#   '저축금리유형': 'S',
#   '저축금리유형명': '단리',
#   '최고 우대금리': 3.35},
#  {'금융상품코드': '101272000057',
#   '저축 금리': 2.3,
#   '저축 기간': '1',
#   '저축금리유형': 'S',
#   '저축금리유형명': '단리',
#   '최고 우대금리': 3.2},
#  {'금융상품코드': '101272000057',
#   '저축 금리': 2.6,
#   '저축 기간': '3',
#   '저축금리유형': 'S',
#   '저축금리유형명': '단리',
#   '최고 우대금리': 3.5},
#  {'금융상품코드': '101272000057',
#   '저축 금리': 3,
#   '저축 기간': '6',
#   '저축금리유형': 'S',
#   '저축금리유형명': '단리',
#   '최고 우대금리': 3.7},
#  {'금융상품코드': '101272000057',
#   '저축 금리': 3.1,
#   '저축 기간': '12',
#   '저축금리유형': 'S',
#   '저축금리유형명': '단리',
#   '최고 우대금리': 3.75},
#  {'금융상품코드': '101272000057',
#   '저축 금리': 3,
#   '저축 기간': '24',
#   '저축금리유형': 'S',
#   '저축금리유형명': '단리',
#   '최고 우대금리': 3.5},
#  {'금융상품코드': '101272000057',
#   '저축 금리': 3,
#   '저축 기간': '36',
#   '저축금리유형': 'S',
#   '저축금리유형명': '단리',
#   '최고 우대금리': 3.5},
#  {'금융상품코드': '101272000058',
#   '저축 금리': 2.6,
#   '저축 기간': '3',
#   '저축금리유형': 'S',
#   '저축금리유형명': '단리',
#   '최고 우대금리': 3.35},
#  {'금융상품코드': '101272000058',
#   '저축 금리': 2.75,
#   '저축 기간': '6',
#   '저축금리유형': 'S',
#   '저축금리유형명': '단리',
#   '최고 우대금리': 3.5},
#  {'금융상품코드': '101272000058',
#   '저축 금리': 2.95,
#   '저축 기간': '12',
#   '저축금리유형': 'S',
#   '저축금리유형명': '단리',
#   '최고 우대금리': 3.7},
#  {'금융상품코드': '10-01-20-024-0046-0000',
#   '저축 금리': 3.5,
#   '저축 기간': '3',
#   '저축금리유형': 'S',
#   '저축금리유형명': '단리',
#   '최고 우대금리': 3.5},
#  {'금융상품코드': '10-01-20-024-0046-0000',
#   '저축 금리': 3.55,
#   '저축 기간': '6',
#   '저축금리유형': 'S',
#   '저축금리유형명': '단리',
#   '최고 우대금리': 3.55},
#  {'금융상품코드': '10-01-20-024-0046-0000',
#   '저축 금리': 3.4,
#   '저축 기간': '12',
#   '저축금리유형': 'S',
#   '저축금리유형명': '단리',
#   '최고 우대금리': 3.4},
#  {'금융상품코드': '10-01-20-024-0059-0000',
#   '저축 금리': 3.4,
#   '저축 기간': '12',
#   '저축금리유형': 'S',
#   '저축금리유형명': '단리',
#   '최고 우대금리': 3.75},
#  {'금융상품코드': '10-01-20-024-0059-0000',
#   '저축 금리': 3.4,
#   '저축 기간': '24',
#   '저축금리유형': 'S',
#   '저축금리유형명': '단리',
#   '최고 우대금리': 3.6},
#  {'금융상품코드': '10-01-20-024-0059-0000',
#   '저축 금리': 3.4,
#   '저축 기간': '36',
#   '저축금리유형': 'S',
#   '저축금리유형명': '단리',
#   '최고 우대금리': 3.7},
#  {'금융상품코드': '21001115',
#   '저축 금리': 2.45,
#   '저축 기간': '3',
#   '저축금리유형': 'S',
#   '저축금리유형명': '단리',
#   '최고 우대금리': 2.95},
#  {'금융상품코드': '21001115',
#   '저축 금리': 2.6,
#   '저축 기간': '6',
#   '저축금리유형': 'S',
#   '저축금리유형명': '단리',
#   '최고 우대금리': 3.1},
#  {'금융상품코드': '21001115',
#   '저축 금리': 2.95,
#   '저축 기간': '12',
#   '저축금리유형': 'S',
#   '저축금리유형명': '단리',
#   '최고 우대금리': 3.45},
#  {'금융상품코드': '21001115',
#   '저축 금리': 3.05,
#   '저축 기간': '24',
#   '저축금리유형': 'S',
#   '저축금리유형명': '단리',
#   '최고 우대금리': 3.55},
#  {'금융상품코드': '21001203',
#   '저축 금리': 3.05,
#   '저축 기간': '6',
#   '저축금리유형': 'S',
#   '저축금리유형명': '단리',
#   '최고 우대금리': 3.35},
#  {'금융상품코드': '21001203',
#   '저축 금리': 3.3,
#   '저축 기간': '12',
#   '저축금리유형': 'S',
#   '저축금리유형명': '단리',
#   '최고 우대금리': 3.6},
#  {'금융상품코드': '21001203',
#   '저축 금리': 3.35,
#   '저축 기간': '24',
#   '저축금리유형': 'S',
#   '저축금리유형명': '단리',
#   '최고 우대금리': 3.65},
#  {'금융상품코드': '21001265',
#   '저축 금리': 2.4,
#   '저축 기간': '3',
#   '저축금리유형': 'S',
#   '저축금리유형명': '단리',
#   '최고 우대금리': 3.4},
#  {'금융상품코드': '21001265',
#   '저축 금리': 2.4,
#   '저축 기간': '6',
#   '저축금리유형': 'S',
#   '저축금리유형명': '단리',
#   '최고 우대금리': 3.4},
#  {'금융상품코드': '21001265',
#   '저축 금리': 2.4,
#   '저축 기간': '12',
#   '저축금리유형': 'S',
#   '저축금리유형명': '단리',
#   '최고 우대금리': 3.4},
#  {'금융상품코드': '21001266',
#   '저축 금리': 2.4,
#   '저축 기간': '3',
#   '저축금리유형': 'S',
#   '저축금리유형명': '단리',
#   '최고 우대금리': 3.45},
#  {'금융상품코드': '21001266',
#   '저축 금리': 2.4,
#   '저축 기간': '6',
#   '저축금리유형': 'S',
#   '저축금리유형명': '단리',
#   '최고 우대금리': 3.45},
#  {'금융상품코드': '21001266',
#   '저축 금리': 2.4,
#   '저축 기간': '12',
#   '저축금리유형': 'S',
#   '저축금리유형명': '단리',
#   '최고 우대금리': 3.6},
#  {'금융상품코드': '01211310121',
#   '저축 금리': 3.15,
#   '저축 기간': '12',
#   '저축금리유형': 'S',
#   '저축금리유형명': '단리',
#   '최고 우대금리': 3.35},
#  {'금융상품코드': '01211310121',
#   '저축 금리': 3.2,
#   '저축 기간': '24',
#   '저축금리유형': 'S',
#   '저축금리유형명': '단리',
#   '최고 우대금리': 3.4},
#  {'금융상품코드': '01211310121',
#   '저축 금리': 3.3,
#   '저축 기간': '36',
#   '저축금리유형': 'S',
#   '저축금리유형명': '단리',
#   '최고 우대금리': 3.5},
#  {'금융상품코드': '01211310130',
#   '저축 금리': 3.12,
#   '저축 기간': '6',
#   '저축금리유형': 'S',
#   '저축금리유형명': '단리',
#   '최고 우대금리': 3.12},
#  {'금융상품코드': '01211310130',
#   '저축 금리': 3,
#   '저축 기간': '12',
#   '저축금리유형': 'S',
#   '저축금리유형명': '단리',
#   '최고 우대금리': 3},
#  {'금융상품코드': '01211310130',
#   '저축 금리': 2.96,
#   '저축 기간': '24',
#   '저축금리유형': 'S',
#   '저축금리유형명': '단리',
#   '최고 우대금리': 2.96},
#  {'금융상품코드': '01211310130',
#   '저축 금리': 2.95,
#   '저축 기간': '36',
#   '저축금리유형': 'S',
#   '저축금리유형명': '단리',
#   '최고 우대금리': 2.95},
#  {'금융상품코드': '06492',
#   '저축 금리': 3,
#   '저축 기간': '1',
#   '저축금리유형': 'S',
#   '저축금리유형명': '단리',
#   '최고 우대금리': 3},
#  {'금융상품코드': '06492',
#   '저축 금리': 3.1,
#   '저축 기간': '3',
#   '저축금리유형': 'S',
#   '저축금리유형명': '단리',
#   '최고 우대금리': 3.1},
#  {'금융상품코드': '06492',
#   '저축 금리': 3.4,
#   '저축 기간': '6',
#   '저축금리유형': 'S',
#   '저축금리유형명': '단리',
#   '최고 우대금리': 3.4},
#  {'금융상품코드': '06492',
#   '저축 금리': 3.5,
#   '저축 기간': '12',
#   '저축금리유형': 'S',
#   '저축금리유형명': '단리',
#   '최고 우대금리': 3.5},
#  {'금융상품코드': '06492',
#   '저축 금리': 3.35,
#   '저축 기간': '24',
#   '저축금리유형': 'S',
#   '저축금리유형명': '단리',
#   '최고 우대금리': 3.35},
#  {'금융상품코드': '06492',
#   '저축 금리': 3.35,
#   '저축 기간': '36',
#   '저축금리유형': 'S',
#   '저축금리유형명': '단리',
#   '최고 우대금리': 3.35},
#  {'금융상품코드': '010300100335',
#   '저축 금리': 1.8,
#   '저축 기간': '1',
#   '저축금리유형': 'S',
#   '저축금리유형명': '단리',
#   '최고 우대금리': 3},
#  {'금융상품코드': '010300100335',
#   '저축 금리': 2.2,
#   '저축 기간': '3',
#   '저축금리유형': 'S',
#   '저축금리유형명': '단리',
#   '최고 우대금리': 3.4},
#  {'금융상품코드': '010300100335',
#   '저축 금리': 2.3,
#   '저축 기간': '6',
#   '저축금리유형': 'S',
#   '저축금리유형명': '단리',
#   '최고 우대금리': 3.4},
#  {'금융상품코드': '010300100335',
#   '저축 금리': 2.5,
#   '저축 기간': '12',
#   '저축금리유형': 'S',
#   '저축금리유형명': '단리',
#   '최고 우대금리': 3.4},
#  {'금융상품코드': '010300100335',
#   '저축 금리': 2.6,
#   '저축 기간': '24',
#   '저축금리유형': 'S',
#   '저축금리유형명': '단리',
#   '최고 우대금리': 2.7},
#  {'금융상품코드': '010300100335',
#   '저축 금리': 2.6,
#   '저축 기간': '36',
#   '저축금리유형': 'S',
#   '저축금리유형명': '단리',
#   '최고 우대금리': 2.7},
#  {'금융상품코드': '200-0135-12',
#   '저축 금리': 2.15,
#   '저축 기간': '1',
#   '저축금리유형': 'S',
#   '저축금리유형명': '단리',
#   '최고 우대금리': 3},
#  {'금융상품코드': '200-0135-12',
#   '저축 금리': 2.45,
#   '저축 기간': '3',
#   '저축금리유형': 'S',
#   '저축금리유형명': '단리',
#   '최고 우대금리': 3.4},
#  {'금융상품코드': '200-0135-12',
#   '저축 금리': 2.75,
#   '저축 기간': '6',
#   '저축금리유형': 'S',
#   '저축금리유형명': '단리',
#   '최고 우대금리': 3.4},
#  {'금융상품코드': '200-0135-12',
#   '저축 금리': 2.9,
#   '저축 기간': '12',
#   '저축금리유형': 'S',
#   '저축금리유형명': '단리',
#   '최고 우대금리': 3.35},
#  {'금융상품코드': '200-0135-12',
#   '저축 금리': 2.95,
#   '저축 기간': '24',
#   '저축금리유형': 'S',
#   '저축금리유형명': '단리',
#   '최고 우대금리': 3},
#  {'금융상품코드': '200-0135-12',
#   '저축 금리': 3,
#   '저축 기간': '36',
#   '저축금리유형': 'S',
#   '저축금리유형명': '단리',
#   '최고 우대금리': 3},
#  {'금융상품코드': '10-003-1225-0001',
#   '저축 금리': 2.95,
#   '저축 기간': '1',
#   '저축금리유형': 'S',
#   '저축금리유형명': '단리',
#   '최고 우대금리': 3.05},
#  {'금융상품코드': '10-003-1225-0001',
#   '저축 금리': 3.3,
#   '저축 기간': '3',
#   '저축금리유형': 'S',
#   '저축금리유형명': '단리',
#   '최고 우대금리': 3.4},
#  {'금융상품코드': '10-003-1225-0001',
#   '저축 금리': 3.33,
#   '저축 기간': '6',
#   '저축금리유형': 'S',
#   '저축금리유형명': '단리',
#   '최고 우대금리': 3.43},
#  {'금융상품코드': '10-003-1225-0001',
#   '저축 금리': 3.35,
#   '저축 기간': '12',
#   '저축금리유형': 'S',
#   '저축금리유형명': '단리',
#   '최고 우대금리': 3.45},
#  {'금융상품코드': '10-003-1381-0001',
#   '저축 금리': 3.1,
#   '저축 기간': '12',
#   '저축금리유형': 'S',
#   '저축금리유형명': '단리',
#   '최고 우대금리': 3.5},
#  {'금융상품코드': '10-003-1381-0001',
#   '저축 금리': 3.15,
#   '저축 기간': '24',
#   '저축금리유형': 'S',
#   '저축금리유형명': '단리',
#   '최고 우대금리': 3.55},
#  {'금융상품코드': '10-003-1381-0001',
#   '저축 금리': 3.4,
#   '저축 기간': '36',
#   '저축금리유형': 'S',
#   '저축금리유형명': '단리',
#   '최고 우대금리': 3.8},
#  {'금융상품코드': '10-003-1384-0001',
#   '저축 금리': 3,
#   '저축 기간': '1',
#   '저축금리유형': 'S',
#   '저축금리유형명': '단리',
#   '최고 우대금리': 3},
#  {'금융상품코드': '10-003-1384-0001',
#   '저축 금리': 3.4,
#   '저축 기간': '3',
#   '저축금리유형': 'S',
#   '저축금리유형명': '단리',
#   '최고 우대금리': 3.4},
#  {'금융상품코드': '10-003-1384-0001',
#   '저축 금리': 3.43,
#   '저축 기간': '6',
#   '저축금리유형': 'S',
#   '저축금리유형명': '단리',
#   '최고 우대금리': 3.43},
#  {'금융상품코드': '10-003-1384-0001',
#   '저축 금리': 3.45,
#   '저축 기간': '12',
#   '저축금리유형': 'S',
#   '저축금리유형명': '단리',
#   '최고 우대금리': 3.45},
#  {'금융상품코드': '10-003-1384-0001',
#   '저축 금리': 3.23,
#   '저축 기간': '24',
#   '저축금리유형': 'S',
#   '저축금리유형명': '단리',
#   '최고 우대금리': 3.23},
#  {'금융상품코드': '10-003-1384-0001',
#   '저축 금리': 3.4,
#   '저축 기간': '36',
#   '저축금리유형': 'S',
#   '저축금리유형명': '단리',
#   '최고 우대금리': 3.4},
#  {'금융상품코드': '10-003-1387-0001',
#   '저축 금리': 3.1,
#   '저축 기간': '12',
#   '저축금리유형': 'S',
#   '저축금리유형명': '단리',
#   '최고 우대금리': 3.9},
#  {'금융상품코드': '4',
#   '저축 금리': 2,
#   '저축 기간': '1',
#   '저축금리유형': 'S',
#   '저축금리유형명': '단리',
#   '최고 우대금리': 3},
#  {'금융상품코드': '4',
#   '저축 금리': 2.2,
#   '저축 기간': '3',
#   '저축금리유형': 'S',
#   '저축금리유형명': '단리',
#   '최고 우대금리': 3.4},
#  {'금융상품코드': '4',
#   '저축 금리': 2.3,
#   '저축 기간': '6',
#   '저축금리유형': 'S',
#   '저축금리유형명': '단리',
#   '최고 우대금리': 3.4},
#  {'금융상품코드': '4',
#   '저축 금리': 2.6,
#   '저축 기간': '12',
#   '저축금리유형': 'S',
#   '저축금리유형명': '단리',
#   '최고 우대금리': 3.4},
#  {'금융상품코드': '4',
#   '저축 금리': 2.7,
#   '저축 기간': '24',
#   '저축금리유형': 'S',
#   '저축금리유형명': '단리',
#   '최고 우대금리': 3},
#  {'금융상품코드': '4',
#   '저축 금리': 2.8,
#   '저축 기간': '36',
#   '저축금리유형': 'S',
#   '저축금리유형명': '단리',
#   '최고 우대금리': 3},
#  {'금융상품코드': '01013000110000000001',
#   '저축 금리': 3,
#   '저축 기간': '1',
#   '저축금리유형': 'S',
#   '저축금리유형명': '단리',
#   '최고 우대금리': 3},
#  {'금융상품코드': '01013000110000000001',
#   '저축 금리': 3.4,
#   '저축 기간': '3',
#   '저축금리유형': 'S',
#   '저축금리유형명': '단리',
#   '최고 우대금리': 3.4},
#  {'금융상품코드': '01013000110000000001',
#   '저축 금리': 3.4,
#   '저축 기간': '6',
#   '저축금리유형': 'S',
#   '저축금리유형명': '단리',
#   '최고 우대금리': 3.4},
#  {'금융상품코드': '01013000110000000001',
#   '저축 금리': 3.35,
#   '저축 기간': '12',
#   '저축금리유형': 'S',
#   '저축금리유형명': '단리',
#   '최고 우대금리': 3.35},
#  {'금융상품코드': '01013000110000000001',
#   '저축 금리': 3.2,
#   '저축 기간': '24',
#   '저축금리유형': 'S',
#   '저축금리유형명': '단리',
#   '최고 우대금리': 3.2},
#  {'금융상품코드': '01013000110000000001',
#   '저축 금리': 3.2,
#   '저축 기간': '36',
#   '저축금리유형': 'S',
#   '저축금리유형명': '단리',
#   '최고 우대금리': 3.2},
#  {'금융상품코드': '10120110400011',
#   '저축 금리': 2.4,
#   '저축 기간': '12',
#   '저축금리유형': 'S',
#   '저축금리유형명': '단리',
#   '최고 우대금리': 2.8},
#  {'금융상품코드': '10120114300011',
#   '저축 금리': 3.2,
#   '저축 기간': '6',
#   '저축금리유형': 'S',
#   '저축금리유형명': '단리',
#   '최고 우대금리': 3.55},
#  {'금융상품코드': '10120114300011',
#   '저축 금리': 3.25,
#   '저축 기간': '12',
#   '저축금리유형': 'S',
#   '저축금리유형명': '단리',
#   '최고 우대금리': 3.6},
#  {'금융상품코드': '10120114700011',
#   '저축 금리': 3.55,
#   '저축 기간': '3',
#   '저축금리유형': 'S',
#   '저축금리유형명': '단리',
#   '최고 우대금리': 3.55},
#  {'금융상품코드': '10120114700011',
#   '저축 금리': 3.55,
#   '저축 기간': '6',
#   '저축금리유형': 'S',
#   '저축금리유형명': '단리',
#   '최고 우대금리': 3.55},
#  {'금융상품코드': '10120114700011',
#   '저축 금리': 3.6,
#   '저축 기간': '12',
#   '저축금리유형': 'S',
#   '저축금리유형명': '단리',
#   '최고 우대금리': 3.6},
#  {'금융상품코드': '10120116100011',
#   '저축 금리': 2.7,
#   '저축 기간': '12',
#   '저축금리유형': 'S',
#   '저축금리유형명': '단리',
#   '최고 우대금리': 3.75},
#  {'금융상품코드': '10-01-20-388-0002',
#   '저축 금리': 2.7,
#   '저축 기간': '1',
#   '저축금리유형': 'S',
#   '저축금리유형명': '단리',
#   '최고 우대금리': 2.7},
#  {'금융상품코드': '10-01-20-388-0002',
#   '저축 금리': 3.2,
#   '저축 기간': '3',
#   '저축금리유형': 'S',
#   '저축금리유형명': '단리',
#   '최고 우대금리': 3.2},
#  {'금융상품코드': '10-01-20-388-0002',
#   '저축 금리': 3.3,
#   '저축 기간': '6',
#   '저축금리유형': 'S',
#   '저축금리유형명': '단리',
#   '최고 우대금리': 3.3},
#  {'금융상품코드': '10-01-20-388-0002',
#   '저축 금리': 3.3,
#   '저축 기간': '12',
#   '저축금리유형': 'S',
#   '저축금리유형명': '단리',
#   '최고 우대금리': 3.3},
#  {'금융상품코드': '10-01-20-388-0002',
#   '저축 금리': 3,
#   '저축 기간': '24',
#   '저축금리유형': 'S',
#   '저축금리유형명': '단리',
#   '최고 우대금리': 3},
#  {'금융상품코드': '10-01-20-388-0002',
#   '저축 금리': 3,
#   '저축 기간': '36',
#   '저축금리유형': 'S',
#   '저축금리유형명': '단리',
#   '최고 우대금리': 3},
#  {'금융상품코드': '1001202000002',
#   '저축 금리': 3,
#   '저축 기간': '3',
#   '저축금리유형': 'S',
#   '저축금리유형명': '단리',
#   '최고 우대금리': 3},
#  {'금융상품코드': '1001202000002',
#   '저축 금리': 3,
#   '저축 기간': '6',
#   '저축금리유형': 'S',
#   '저축금리유형명': '단리',
#   '최고 우대금리': 3}]