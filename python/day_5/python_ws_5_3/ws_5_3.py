# 아래 함수를 수정하시오.
def sort_tuple(input_tuple):
    new_tuple = ()
    input_list = list(input_tuple)
    input_list.sort()

    new_list = list(new_tuple)
    new_list.extend(input_list)
    new_tuple = tuple(new_list)
    
    return new_tuple


result = sort_tuple((5, 2, 8, 1, 3))
print(result)
