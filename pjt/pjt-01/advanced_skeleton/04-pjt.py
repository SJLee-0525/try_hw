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
    api_key = 'c19ae7f523953ee767f19e9217fb618e'

    # 요구사항에 맞도록 이곳의 코드를 수정합니다.
    url = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo=1'

    result = []
    response = requests.get(url).json()

    fin_cd_list = []
    for i in range(len(response['result']['optionList'])):
        fin_cd_list.append(response['result']['optionList'][i]['fin_prdt_cd'])

    fin_cd_list = list(set(fin_cd_list))

    temp_list_dict = {}
    for fin_cd in fin_cd_list:
        for i in range(len(response['result']['baseList'])):
            if fin_cd in response['result']['baseList'][i]['fin_prdt_cd']:
                a, b = response['result']['baseList'][i]['kor_co_nm'], response['result']['baseList'][i]['fin_prdt_nm']
                a, b = a.replace("\n", ""), b.replace("\n", "")
                temp_list_dict[fin_cd] = [a, b]
            
    # print(temp_list_dict)

    final_list = []
    for fin_cd in fin_cd_list:
        temp_dict = {}
        
        mini_temp_dict_list = []
        for i in range(len(response['result']['optionList'])):
            if fin_cd == response['result']['optionList'][i]['fin_prdt_cd']:
                mini_temp_dict = {}
                mini_temp_dict['저축 금리'] = response['result']['optionList'][i]['intr_rate']
                mini_temp_dict['저축 기간'] = response['result']['optionList'][i]['save_trm']
                mini_temp_dict['저축금리유형'] = response['result']['optionList'][i]['intr_rate_type']
                mini_temp_dict['저축금리유형명'] = response['result']['optionList'][i]['intr_rate_type_nm']
                mini_temp_dict['최고 우대금리'] = response['result']['optionList'][i]['intr_rate2']
                code = i
                mini_temp_dict_list.append(mini_temp_dict)
                temp_dict['금융상품명'] = temp_list_dict[fin_cd][1]
                temp_dict['금융회사명'] = temp_list_dict[fin_cd][0]

        temp_dict['금리정보'] = mini_temp_dict_list
        

        final_list.append(temp_dict)
    
    result = final_list

    return result
  

if __name__ == '__main__':
    # json 형태의 데이터 반환
    result = get_deposit_products()
    # prrint.prrint(): json 을 보기 좋은 형식으로 출력
    pprint.pprint(result)
    print(len(result))