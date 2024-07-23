# 아래 함수를 수정하시오.
def even_elements(input_list):
    for _ in range(len(input_list)):
        i = input_list.pop(0)
        if i % 2 == 0:
            input_list.extend([i])

    return input_list

# def even_elements(input_list):


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = even_elements(my_list)
print(result)
