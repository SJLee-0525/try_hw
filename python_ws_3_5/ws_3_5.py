name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']

number_of_people = 0
number_of_book = 100

# 이거 안 써도 되는 듯
def increase_user():
    global number_of_people
    number_of_people += 1

# name, age, address를 묶어서 회원 정보 (user_info)를 만들어주는 함수
def create_user(f_name, f_age, f_address):

    print(f'{f_name}님 환영합니다!')

    user_info = {}
    user_info['name'] = f_name
    user_info['age'] = f_age
    user_info['address'] = f_address
    
    return user_info

# 기존 회원 정보에서 이름과 몇 권 빌릴지 계산해서 새로운 회원 정보 딕셔너리를 반환하는 함수
def get_user(user): 
    user_dict = {
        'name': user['name'],
        'number_of_rental_books': user['age'] // 10
    }
    return user_dict

# 람다로 풀어쓰면 이런 형식
# lambda user: {'name': user['name'], 'number_of_rental_books': user['age'] // 10}

# 누가 몇 권 빌리는지 확인해서 책 수치를 감소시키는 함수를 호출 후 누가 몇 권 가져갔는지 출력해주는 함수
def rental_book(info):
    decrease_book(info['number_of_rental_books'])
    print(f'{info["name"]}님이 {info["number_of_rental_books"]}권의 책을 대여하였습니다.')

# 몇 권 빌려가는지 입력 받고 실제 그 수치만큼 전체 책의 수는 감소시키고 출력하는 함수
def decrease_book(borrow_book):
    global number_of_book
    number_of_book -= borrow_book
    print(f'남은 책의 수 : {number_of_book}')


# name, age, address를 묶어서 회원 정보 (user_info)를 만들어 many_user에 할당
many_user = list(map(create_user, name, age, address))

# 기존 회원 정보에서 이름과 몇 권 빌릴지 계산해서 새로운 회원 정보를 만들도록 호출
list(map(get_user, many_user))

# 누가 몇 권 빌리는지 확인해서 책 수치를 감소시키는 함수를 호출 후 누가 몇 권 가져갔는지 출력해주는 함수 호출
# 람다 O 버전
list(
    map(
        rental_book, 
        list(map(lambda user: {'name': user['name'], 'number_of_rental_books': user['age'] // 10}, many_user))))

# 람다 X 버전
# list(map(rental_book, list(map(get_user, many_user))))
