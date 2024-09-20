data = {'name': '홍길동'}
# if not data['age']:
#     print(data['age'])
# else:
#     print('data에는 age라는 키가 없습니다.')
#     data['age'] = 30
#     print(data)

# 아래에 코드를 작성하시오.
try:
    print(data['age'])
except KeyError:
    print('data에는 age라는 키가 없습니다.')
    data['age'] = 30
    print(data)

arr = ['반갑', '하세요', '안녕']
# for i in range(4):
#     print(arr.pop())
# print(arr)

# 아래에 코드를 작성하시오.
try:
    for i in range(4):
        print(arr.pop())
except IndexError:
    print(arr)
    print('더 이상 pop 할 수 없습니다.')

word = '3.15'
# print(int(word))

# 아래에 코드를 작성하시오.
try:
    print(int(word))
except ValueError:
    print('정수로 변환 가능한 값을 입력해 주세요.')