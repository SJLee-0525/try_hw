matrix = [
        ['0, 1', '0, 2', '0, 3'], 
        ['1, 0', '1, 1', '1, 2', '1, 3'], 
        ['2, 0', '2, 1', '2, 2', '2, 3', '2, 4'], 
        ['3, 0', '3, 1'], 
        ['4, 0', '4, 1', '4, 2'], 
        ['5, 0']
    ]
# 아래애 코드를 작성하시오.
matrix_len = 0
for inner_matrix in matrix:
    matrix_len += 1
print(matrix_len)


for inner_matrix in matrix:
    temporary_len = 0
    for inner_inner_matrix in inner_matrix:
        temporary_len += 1
    if temporary_len <= 4:
        print(f'{inner_matrix} 리스트는 {temporary_len}개 만큼 요소를 가지고 있습니다.')

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(f'matrix의 {i}, {j}번째 요소의 값은 {matrix[i][j]}입니다.')