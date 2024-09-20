# 아래 함수를 수정하시오.
def remove_duplicates(input_lst):
    new_lst = []
    input_lst = list(set(input_lst))

    for i in input_lst:
        new_lst.append(i)

    return new_lst

result = remove_duplicates([1, 2, 2, 3, 4, 4, 5])
print(result)
