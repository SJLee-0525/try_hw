data_1 = 'qweqwYadnOyjnsaU4trwg asjnaAn245krRmkfE 42grTasdnHasdnvEasdn asdevadnBasdanEsdkqefqefvaSasdqaeeqqvedwt5hfbsdT24tewfd'
'''
예시코드
arr = [1, 2, 3, 4, 5]
for num in arr:
    print(num, end='')
출력결과 : 12345
'''
# 아래에 코드를 작성하시오.
data_1_list = list(data_1)

for data in data_1_list:
    if data.isupper() == True:
        print(data, end = '')
    elif data == ' ':
        print(data, end = '')
print()

data_2 = '걉파반샤팝다푸거맥파바자들퍼바배들밥샵파누타히매니배사바파힘다브사부힙헤베내테치대내'
arr = []
# 아래에 코드를 작성하시오.
data_2_list = list(data_2)
target_list = list('내힘들다')

for target in target_list:
    arr.append(data_2_list.index(target))

print(arr)

arr.sort()

print(arr)

for index in arr:
    print(data_2_list[index], end = '')