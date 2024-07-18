number_of_people = 0

def increase_user():
    global number_of_people
    number_of_people += 1

def create_user(f_name, f_age, f_address):

    increase_user()

    print(f'{f_name}님 환영합니다!')
    global user_list

    user_info = {}
    user_info['name'] = f_name
    user_info['age'] = f_age
    user_info['address'] = f_address
    
    return user_info
    # user_list.append(user_info)
    # if len(user_list) == len(name):
    #     print(user_list)
    
name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']

user_list = [] 

result = list(map(create_user, name, age, address))
print(result)






